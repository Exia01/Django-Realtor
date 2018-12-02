from django.urls import path  # imports path package
from . import views

urlpatterns = [#naming space for easier method 
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
]
