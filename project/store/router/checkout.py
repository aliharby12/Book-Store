from django.urls import path

from project.store.views import checkout, pay


urlpatterns = [
    path('', checkout, name='checkout'),
    path('pay', pay, name='pay'),
]