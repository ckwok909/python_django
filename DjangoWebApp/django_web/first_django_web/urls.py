from django.urls import path
from first_django_web import views

urlpatterns = [
    path('', views.user, name='user'),
]
