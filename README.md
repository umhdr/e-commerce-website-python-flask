# e-commerce-website-python-flask
This project is an e-commerce website built using Python and Flask. It includes APIs for CRUD operations on customers and products, as well as an endpoint for making a product active/inactive.

**E-commerce Website**
This is an e-commerce website built using Python and Flask. It includes APIs for CRUD operations on customers and products, as well as an endpoint for making a product active/inactive. The project uses a MySQL database to store customer and product information.

**Installation**
To install and run this project on a local machine, follow these steps:

Clone the repository to your local machine.
Run the application using python main.py.

**Usage**
To use this project, you can use tools like Postman to interact with the API endpoints. Here are some examples of how to use the endpoints:

To create a new customer, send a POST request to /customer with the customer details in the request body.
To retrieve all customers, send a GET request to /customer.
To update a customer, send a PUT request to /customer/{customer_id} with the updated customer details in the request body.
To delete a customer, send a DELETE request to /customer/{customer_id}.
To create a new product, send a POST request to /product with the product details in the request body.
To retrieve all products, send a GET request to /product.
To update a product, send a PUT request to /product/{product_id} with the updated product details in the request body.
To delete a product, send a DELETE request to /product/{product_id}.
To make a product active/inactive, send a PUT request to /product/{product_id}/status with the new status in the request body.

**License**
This project is licensed under the MIT License. See LICENSE.md for more information.
