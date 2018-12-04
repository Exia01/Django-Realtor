from django.urls import path  # imports path package
from . import views


urlpatterns = [#naming space for easier method 
    path('', views.index, name="listings"),
    path('<int:listing_id>', views.listing, name="listing"),
    path('search', views.search, name="search"),
]
