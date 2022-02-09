"""Define the configurations for the app."""

from django.apps import AppConfig


class CuisineConfig(AppConfig):
    """Defines the configurations for 'cuisine'."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cuisine'
