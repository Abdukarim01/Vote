from django.urls import path
from .views import home

app_name = "vote"

urlpatterns = [
    path('',home,name="home")
]