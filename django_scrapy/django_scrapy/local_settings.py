DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_scrapy_db",
        "USER": "root",
        "PASSWORD": "pengye2901307001",
        "HOST": "0.0.0.0",
        "POST": "5432",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS += ('debug_toolbar', )
