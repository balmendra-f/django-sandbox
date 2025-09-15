# Django Backend with MariaDB
This project is a backend built with **Django** and connected to **MariaDB**.  
This README is designed for users who want to quickly run the project.

---

## 🚀 Requirements

- Python 3.x  
- pip  
- MariaDB  
- Git  

---

## 1. Clone the Project

```bash
git clone https://github.com/balmendra-f/django-sandbox.git
cd django-sandbox

2. Install Dependencies and Activate Virtual Environment
# Create and activate virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

3. Configure Database and Run the Server
Start MariaDB and create the database:
mysql -u root -p
CREATE DATABASE your_database_name;
Update the connection settings in django-sandbox/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Run migrations and start the development server:

python manage.py migrate
python manage.py runserver

(Optional) Create a Superuser
To access the Django Admin Panel:

python manage.py createsuperuser
Then go to: http://127.0.0.1:8000/admin/

Backend available at:
http://127.0.0.1:8000/
