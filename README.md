# Employee web applications

This project is a web application for managing employees. It includes frontend components built with Vue.js and backend components built with Django.

## Setup Instructions

### Frontend (Vue.js)

1. **Install Vue CLI**: If you haven't already, install Vue CLI globally using npm:

   ```bash
   npm install -g @vue/cli
Setup Vue Project: Create a new Vue project:

bash
Copy code
vue create employee_frontend
Install Dependencies: Navigate to the employee_frontend directory and install additional dependencies:

bash
Copy code
cd employee_frontend
npm install axios
Run Development Server: Start the Vue.js development server:

bash
Copy code
npm run serve
Access the Vue.js application at http://localhost:8080/.

Backend (Django)
Install Django: Ensure Django is installed in your Python environment:

bash
Copy code
pip install django
Navigate to Backend Directory: Navigate to the directory containing the Django project (employee_backend).

Run Django Server: Start the Django development server:

bash
Copy code
python manage.py runserver
Access the Django API at http://localhost:8000/.

Troubleshooting
If you encounter any issues during setup or while running the application, here are some common solutions:

ModuleNotFoundError: No module named 'django': Ensure Django is installed in your Python environment. You can install it using pip install django.

Permission Denied: If you encounter permission issues during installation or running commands, try using the --user option with pip (pip install --user django) or running commands with administrative privileges.

File Not Found Errors: Make sure you are in the correct directory and that the file paths specified in commands are correct.

Python Version Compatibility: Ensure that your Python environment is compatible with the versions of Django and other dependencies used in the project.
