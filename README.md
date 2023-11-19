# food_delivery
Food Delivery System
Overview
This project is a simple food delivery system built using Django, with Django Rest Framework (DRF) for API development.
The system consists of three user roles: Admin, Delivery Agent, and Customer, each with specific responsibilities.
project include the soft delete user bulk, bulk uploads(as a background task) of products using celery,Email Notifications, and OTP Verification etc..

Project Structure
The project is structured as follows:

user_management: Django app for users related functionalities (admin,delivery aget,coustomer).
product_management: Django app for product management functionalities.
order_management: Django app for order related functionalities.
bulk_upload_management: Django app for bulk_upload related functionalities.

Installation
Clone the repository:

https://github.com/sreerangk/food_delivery.git
cd FoodDeliverySystem

Create a virtual environment:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Create a superuser for admin access:
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Access the admin panel at http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
Usage
Admin
Product Management:

CRUD operations on food products.
Delivery Agent Management:

Add, update, and view delivery agents.
Customer Management:

Block or unblock customers.
View the list and details of customers, including total orders and amounts.
Order Management:

View, update order statuses (PENDING, ASSIGNED, DELIVERED, CANCELLED).
Assign delivery agents to orders.
Trigger email notifications for order events.
Email Notifications:

Email notifications for order cancellations and assignments.
Bulk Product Upload:

Background task for bulk product uploads .
Delivery Agent
Order Management:
View and manage assigned orders.
Change order statuses.
OTP Verification:
Verify OTP during order delivery.
Customer
Product Section:

View a list of available food products with details.
Order Section:

Explore our API endpoints and test requests using [Postman Documentation]
( https://www.postman.com/winter-meadow-5288/workspace/my-workspace/folder/24868897-260a2636-45ed-4c98-a947-c52dd9085ae8?action=share&creator=24868897&ctx=documentation ).


Create orders with multiple products and Cash on Delivery option.
View and manage their own orders.
Cancel orders within 30 minutes of creation.
Profile Management:

Delete (soft delete) their profile if no pending orders.
