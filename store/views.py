from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Product, Order, OrderItem
from django.contrib.auth import login

from django.http import JsonResponse
import json

from .forms import CustomUserCreationForm, OrderCreateForm # Add OrderCreateForm
from django.contrib.auth.decorators import login_required

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/product_list.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'store/product_detail.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in
            return redirect('product_list') # Redirect to home or product list
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    # You might also fetch posts by this user, their profile details from a Profile model, etc.
    context = {
        'profile_user': profile_user,
        # 'user_profile_details': profile_user.profile, # If you have a OneToOneField named 'profile'
    }
    return render(request, 'store/profile_page.html', context) # Create this template

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items_detailed = []
    total_cart_price = 0

    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)
    product_map = {str(product.id): product for product in products}

    for product_id, item_data in cart.items():
        product = product_map.get(str(product_id))
        if product:
            item_total_price = item_data['quantity'] * product.price
            cart_items_detailed.append({
                'id': product_id,
                'product': product, # Pass the whole product object
                'quantity': item_data['quantity'],
                'total_price': item_total_price
            })
            total_cart_price += item_total_price

    context = {
        'cart_items': cart_items_detailed,
        'total_cart_price': total_cart_price,
        'is_empty': not bool(cart_items_detailed)
    }
    return render(request, 'store/view_cart.html', context)


def update_cart_item(request):
    data = json.loads(request.body)
    productId_str = str(data['productId']) # Ensure product ID is string for dict keys
    action = data['action']

    cart = request.session.get('cart', {}) # Get cart or empty dict

    if action == 'add':
        if productId_str not in cart:
            cart[productId_str] = {'quantity': 1}
        else:
            cart[productId_str]['quantity'] += 1
    elif action == 'remove':
        if productId_str in cart:
            cart[productId_str]['quantity'] -= 1
            if cart[productId_str]['quantity'] <= 0:
                del cart[productId_str] # Remove item if quantity is zero or less
    elif action == 'delete':
        if productId_str in cart:
            del cart[productId_str]


    request.session['cart'] = cart # Save cart back to session
    request.session.modified = True # Mark session as modified

    total_items = sum(item['quantity'] for item in cart.values())
    return JsonResponse({'message': 'Cart updated', 'total_items': total_items, 'cart': cart})

def get_cart_data_view(request): # Renamed to avoid conflict if you name a URL 'get_cart_data'
    cart = request.session.get('cart', {})
    total_items = sum(item['quantity'] for item in cart.values())
    return JsonResponse({'total_items': total_items, 'cart': cart})

@login_required # Make checkout require login
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('product_list')

    # Calculate cart items for display on checkout page
    cart_items_display = []
    total_cart_price_checkout = 0
    product_ids = cart.keys()
    products_in_cart = Product.objects.filter(id__in=product_ids)
    product_map_checkout = {str(p.id): p for p in products_in_cart}

    for product_id_str, item_data in cart.items():
        product_obj = product_map_checkout.get(product_id_str)
        if product_obj:
            item_total = product_obj.price * item_data['quantity']
            cart_items_display.append({
                'product_name': product_obj.name,
                'quantity': item_data['quantity'],
                'price': product_obj.price,
                'total_price': item_total
            })
            total_cart_price_checkout += item_total


    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user # Assign logged-in user
            order.total_paid = total_cart_price_checkout # Set total based on cart at checkout time
            order.paid = True  # Simulate payment for this demo
            order.save() # Save order to get an ID

            for product_id_str, item_data in cart.items():
                product_obj = product_map_checkout.get(product_id_str)
                if product_obj and product_obj.stock >= item_data['quantity']:
                    OrderItem.objects.create(
                        order=order,
                        product=product_obj,
                        price_at_purchase=product_obj.price, # Price at time of purchase
                        quantity=item_data['quantity']
                    )
                    # Basic stock update
                    product_obj.stock -= item_data['quantity']
                    product_obj.save()
                elif product_obj:
                    # Handle out of stock situation - e.g. add error message, don't complete order
                    print(f"Product {product_obj.name} out of stock for desired quantity.")
                    # For a real app, you'd roll back or prevent order completion
                    pass


            # Clear the cart from session
            request.session['cart'] = {}
            request.session.modified = True

            # Redirect to an order success page
            return render(request, 'store/order_created.html', {'order': order})
    else:
        # Pre-fill form if user has details
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
        form = OrderCreateForm(initial=initial_data)

    context = {
        'form': form,
        'cart_items_display': cart_items_display,
        'total_cart_price_checkout': total_cart_price_checkout
    }
    return render(request, 'store/checkout.html', context)

@login_required # Ensures only logged-in users can see their order history
def order_history_view(request):
    # Fetch orders placed by the currently logged-in user
    # The 'related_name' on Order.user might be 'orders' by default if not specified,
    # or you can filter directly on the user field.
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'orders': orders,
    }
    return render(request, 'store/order_history.html', context)
