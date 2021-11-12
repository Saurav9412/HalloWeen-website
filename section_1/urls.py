from django.urls import path
from .views import (
    Landing_page,
)
urlpatterns = [
    path('', Landing_page.as_view(), name = "landing_page"),
]
