from django.urls import path  # imports path package
from . import views

urlpatterns = [#naming space for easier method 
    path('contact', views.contact, name="contact"),
]

