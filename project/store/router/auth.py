from django.urls import path

from project.store.views import register

urlpatterns = [
    path('register', register, name='register'),
]
