from django.urls import path
from .views import (
    Landing_page,
)
urlpatterns = [
    path('home', Landing_page.as_view(), name = "landing_page"),
]
