from django.urls import path
from core import views

urlpatterns = [
    path("", views.test, name="test"),
    path("index", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("check-result/<str:task_id>", views.check_result, name="check-result"),
]
