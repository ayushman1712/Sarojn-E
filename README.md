# Sarojn-E Application

Starter repository for the course CSE202 - Fundamentals of Database Management System (Winter 2024), IIIT Delhi.

## Collaborators

Ayushman Pandey [@ayushman1712](https://www.github.com/ayushman1712/)<br />
Aditya Moza [@m0za_rt](https://www.linkedin.com/in/aditya-moza-09bb9521b/)<br />
Shaurya Parashar [@parashar01](https://www.linkedin.com/in/shaurya-parashar-847673284/)<br />
Vijval Ekbote [@ekbotevijval](https://www.linkedin.com/in/vijval-ekbote-55454b280/)

## Overview

Sarojn-E is an online affordable retail application designed to facilitate the purchase and delivery of everyday products to customers. This repository contains the database schema and the initial application code for managing orders, customer information, product inventory.

## Database Configuration

### Tables

1. **Account**
   - Stores information about customers including their personal details, contact information, and loyalty points.

2. **Category**
   - Contains details about different product categories available in the store.

3. **Product**
   - Holds information about the products available for purchase, including their descriptions, prices, and supplier details.

4. **Membership**
   - Maintains details of customers who are part of the membership program, including their membership level and benefits.

5. **Discount**
   - Records information about discounts available, including discount codes, percentage off, and applicable conditions.

6. **Cart**
   - Tracks items added to the cart by customers before they place an order.

7. **Purchase History**
   - Archives past orders, including details about the customer, product, quantity, price, delivery address, and order status.

8. **User**
   - Stores user credentials and profile details for customers and employees using the system.

9. **Session**
   - Tracks user sessions, including login times, session durations, and activities performed during the session.

10. **Employee**
    - Contains details of employees, including their personal information, job roles, and contact information.

11. **CartItem**
    - Represents individual items within a shopping cart, including product ID, quantity, and price.

12. **Reviews**
    - Contains customer reviews and ratings for products and delivery personnel.

13. **Employee_UPDATES_category**
    - Tracks updates made by employees to product categories, including timestamps and details of changes.

14. **Employee_UPDATES_Product**
    - Tracks updates made by employees to product details, including timestamps and specifics of modifications.

15. **Membership_has_Discount**
    - Links membership levels with applicable discounts, detailing which discounts are available to which membership levels.

## Application Code

The application is built using Python and StreamLit for the GUI and connects to a MySQL database for data storage and retrieval. The key features of the application include:

- Placing orders
- Viewing product statistics
- Viewing and managing customer orders

### Requirements

- Python3
- MySQL Server
- Streamlit
- MySQL Connector for Python

### Running the Application

1. Ensure MySQL server is running and accessible.
2. Clone this repository.
3. Set up the database using the provided SQL schema.
4. Update the database configuration in the application code if necessary.
5. Run the application using the following command:
   ```bash
   python connection.py
   ```
