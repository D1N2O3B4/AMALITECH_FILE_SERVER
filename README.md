# LIZZY'S FILE SERVER

    This project is a file server application built with Django. It allows users to upload, download, and email files of various formats. The application also includes custom user authentication via email and a custom login view.

# Deployed link and admin credentials
* email: admin@admin.com
* password: password
* [Deployed link](http://d1n2o3b4.pythonanywhere.com/)

# ER diagram of database design
![ER diagram of database](https://github.com/D1N2O3B4/AMALITECH_FILE_SERVER/blob/main/media/files/ER.png)


# Email Authentication
###  Backend (backends.py)
    EmailBackend: A custom authentication backend that allows users to log in using their email address instead of their username. It extends ModelBackend and overrides the authenticate method to authenticate users based on their email and password.
###  Forms (forms.py)
    CustomUserCreationForm: A custom user creation form that includes an email field. It validates that the email is unique and uses the email as the username.
    EmailAuthenticationForm: A custom authentication form that replaces the username field with an email field.
###  Views (views.py)
    signup: Handles user registration. Validates the email provider, creates a new user, sends a confirmation email, and displays appropriate messages based on the success or failure of the operation.
    CustomLoginView: A custom login view that uses the EmailAuthenticationForm for user authentication.
    confirm_email: Confirms the user's email address by validating the token sent in the confirmation email.
###  Templates
    registration/signup.html: The signup page where users can create a new account.
    registration/login.html: The login page for user authentication.
    registration/password_reset_form.html: The password reset form.
    registration/password_reset_done.html: The password reset done page.
    registration/password_reset_confirm.html: The password reset confirmation page.
    registration/password_reset_complete.html: The password reset complete page.
# File Management
###  Models (models.py)
    File: Represents a file uploaded by the user. Includes fields for the title, description, file format, file, upload date, download count, email count, and the user who uploaded the file. It validates the file format and overrides the __str__ method to provide a readable string representation of the file.
### Filters (filters.py)
    FileFilter: A filter set for filtering files based on their title. It allows partial matches by splitting the search query into words and checking if the file titles start with any of the words.
### Forms (forms.py)
    EmailForm: A form for sending an email with a file attachment. Includes fields for the recipient's email and a message.
### Middleware (middleware.py)
    AuthMiddleware: Middleware that restricts access to certain views for unauthenticated users. It allows access to login, signup, and password reset views.
### Views (views.py)
    HomeView: A template view for the home page. Redirects authenticated users to the file list view.
    file_list: A function view that displays a list of all files and applies any filters provided in the request.
    FileDetailView: A detail view that displays the details of a specific file.
    FileEmailView: A form view that handles sending an email with a file attachment. Increments the email count of the file upon successful email sending.
    FileDownloadView: A view that handles file downloads. Increments the download count of the file upon each download.
### Admin (admin.py)
    UserAdmin: A custom user admin class that modifies the list display and fieldsets of the User model in the admin interface. It also makes the email field read-only for existing users.
    File: Registers the File model with the admin interface.
### URL Configuration (urls.py)
    config/urls.py: Defines the URL patterns for the project, including paths for admin, home, dashboard, file detail, file email, file download, login, signup, email confirmation, and password reset views.
    file_app/urls.py: Defines the URL patterns specific to the file app, including paths for home, dashboard, file detail, file email, and file download views.
### Settings (settings.py)
    INSTALLED_APPS: Lists the installed applications, including third-party apps such as jazzmin, django_filters, crispy_forms, and crispy_tailwind.
    MIDDLEWARE: Lists the middleware used in the project, including custom middleware for authentication.
    TEMPLATES: Configures the template settings, including directories and context processors.
    DATABASES: Configures the database settings.
    MEDIA_URL, MEDIA_ROOT: Configures the URL and root directory for serving media files.
    LOGIN_REDIRECT_URL: Configures the URL to redirect to after a successful login.
    CRISPY_ALLOWED_TEMPLATE_PACKS, CRISPY_TEMPLATE_PACK: Configures the Crispy Forms settings.
    EMAIL_BACKEND, EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS, DEFAULT_FROM_EMAIL, SERVER_EMAIL: Configures the email settings for sending confirmation and password reset emails.
    PASSWORD_RESET_TIMEOUT: Configures the timeout for password reset tokens.
    AUTHENTICATION_BACKENDS: Lists the authentication backends used, including the custom email backend.

