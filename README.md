# Curzr - Simple E-commerce Store (CodeAlpha Internship Task 1)

Welcome to Curzr, a simple e-commerce store developed as Task 1 for the CodeAlpha Full Stack Development Internship. This project demonstrates core e-commerce functionalities built with Python (Django) for the backend and HTML, CSS, and JavaScript for the frontend.

## Live Demo

*   **Deployed Site:** [Demo Link](http://curzr.pythonanywhere.com) 

## Project Overview

Curzr is a web application designed to simulate a basic online store experience, allowing users to browse products, add items to a shopping cart, and proceed through a simulated checkout process.

## Features Implemented

*   **Product Listings:** Display of available products with images, names, and prices.
*   **Product Detail Pages:** Individual pages for each product showing more details and an "Add to Cart" option.
*   **User Authentication:**
    *   User Registration
    *   User Login & Logout
*   **Shopping Cart:**
    *   Add items to the cart.
    *   View cart contents.
    *   Update item quantities in the cart.
    *   Remove items from the cart.
    *   Cart total calculation.
*   **Order Processing (Simulated):**
    *   Checkout form for shipping information.
    *   Order creation and storage in the database.
    *   (Payment is simulated for this demo).
*   **Order History:** Logged-in users can view their past orders.
*   **Responsive Design:** Basic responsiveness for usability on different screen sizes.
*   **Admin Panel:** Django admin interface for managing products, orders, and users.

## Technologies Used

*   **Backend:**
    *   Python 3.x
    *   Django Framework
    *   Django REST framework (if used for APIs, otherwise remove)
*   **Frontend:**
    *   HTML5
    *   CSS3 (with custom styling)
    *   JavaScript (for cart interactions, dynamic updates)
*   **Database:**
    *   SQLite (for development and this demo)
*   **Version Control:**
    *   Git & GitHub
*   **Deployment (Example):**
    *   PythonAnywhere (or specify if different)
*   **Others:**
    *   `Pillow` (for image handling)
    *   `python-decouple` (for environment variable management)

## Setup and Installation (For Local Development)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/CodeAlpha_SimpleEcommerceStore.git
    cd CodeAlpha_SimpleEcommerceStore
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Create a `.env` file** in the project root based on `.env.example` (if you provide one) and add your `SECRET_KEY` and set `DEBUG=True`.
    Example `.env` content:
    ```
    SECRET_KEY=your_strong_secret_key_here
    DEBUG=True
    ```
5.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
6.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
8.  Open your browser and navigate to `http://127.0.0.1:8000/`.

## Project Structure

A brief overview of the main directories:
*   `ecommerce_project/`: Contains the main Django project settings and configurations.
*   `store/`: The Django app containing models, views, templates, and URLs for the e-commerce functionality.
*   `static/`: Project-wide static files (CSS, JavaScript, images).
*   `mediafiles/`: (Typically for user-uploaded content like product images, usually in `.gitignore` for development db.sqlite3 but structure is relevant).
*   `templates/`: Project-level base templates and registration templates.
*   `manage.py`: Django's command-line utility.
*   `requirements.txt`: List of Python dependencies.
*   `.env`: (Not committed) For environment variables.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.

## Screenshots

![1](https://github.com/user-attachments/assets/34795750-e1bc-4274-b09f-687a105d20c8)

![2](https://github.com/user-attachments/assets/89d07e89-3aa4-4fa0-98af-89068f426341)

![3](https://github.com/user-attachments/assets/495691d5-c000-4711-b7e9-e3943231bfc3)

![4](https://github.com/user-attachments/assets/ad0e0527-4716-43ee-a7e1-f8d49a5343a9)

![5](https://github.com/user-attachments/assets/1c7e4017-5622-45fc-afa3-d6c62773421c)

![6](https://github.com/user-attachments/assets/53da3ad2-564b-46bf-804a-11dba4dfd03a)


## Internship Task Requirements Fulfilled

This project fulfills the requirements for Task 1 of the CodeAlpha Full Stack Development Internship:
*   Basic e-commerce site with product listings.
*   Frontend: HTML, CSS, JavaScript.
*   Backend: Django.
*   Features: Shopping cart, Product details page, Order processing, User registration/login.
*   Database for storing products, users, and orders.