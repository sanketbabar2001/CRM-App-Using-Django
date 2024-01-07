# Customer Relationship Management (CRM) using Django

## Project Overview
This project is a Customer Relationship Management (CRM) application built using Django, a powerful web framework for building web applications. The CRM system allows businesses to manage customer records, including their contact information, such as names, email addresses, phone numbers, and more.

## Getting Started
Follow these steps to set up and run the CRM application on your local machine.

## 1. Create a Virtual Environment
First, create a virtual environment to isolate your project's dependencies:

python -m venv virt

virt\Scripts\activate

## 2. Install Dependencies
Install the project dependencies:

pip install -r requirements.txt


## 3. Configure Database
Change the database configuration in both the settings.py file and the mydb.py script according to your MySQL database.

In settings.py:
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'YourDatabaseName',
       'USER': 'YourDatabaseUser',
       'PASSWORD': 'YourDatabasePassword',
       'HOST': 'YourDatabaseHost',
       'PORT': 'YourDatabasePort',
   }
}


In mydb.py:
import mysql.connector
dataBase = mysql.connector.connect(
	host='YourDatabaseHost',
	user='YourDatabaseUser',
	password='YourDatabasePassword'
)


## 4. Apply Migrations
Apply the initial database migrations to set up the necessary database tables:

python manage.py makemigrations
python manage.py migrate


## 5. Create a Superuser
To access the Django admin interface, create a superuser with administrative privileges:

python manage.py createsuperuser


## 6. Run the Development Server
Start the Django development server:

python manage.py runserver


## 7. Access the Application
Open your web browser and access the CRM application at http://127.0.0.1:8000.


## Usage

1. Login or Register: If you are a new user, you can register. Otherwise, log in using your credentials.

2. View Customer Records: After logging in, you can view a list of customer records, including their names, email addresses, phone numbers, and more.

3. Add, Update, and Delete Records: You can add new customer records, update existing ones, or delete records as needed.

4. Record Details: Click on a customer's name to view their detailed record, including all available information.

5. Logout: When you are done, you can log out of the application.



## Screenshots

![Register User ](SS/register.png)

![Login User](SS/login.png)

![Home Page](SS/home.png)

![Individual Record](SS/record_view.png)

![Add New Record](SS/add_record.png)

![Update Record](SS/update_record.png)

![Logout](SS/logout.png)
