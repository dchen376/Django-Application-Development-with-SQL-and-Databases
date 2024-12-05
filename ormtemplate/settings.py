# Purpose: The central configuration file for your Django project.

# Contains all project-specific settings like:
# Database configurations.
# Installed apps.
# Middleware.
# Templates.
# Static and media files handling.
# Security settings (e.g., SECRET_KEY, DEBUG, ALLOWED_HOSTS).

# Acts as a bridge between Django's framework and the project's requirements.


# PostgreSQL (database config)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'Place with your password generated in Step 1',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

# Installed apps.
INSTALLED_APPS = (
    'standalone',
)

# Security settings (e.g., SECRET_KEY, DEBUG, ALLOWED_HOSTS).
SECRET_KEY = 'SECRET KEY for this Django Project'