from django.shortcuts import render
# from django.http import HttpResponse
from ..listings.models import Listing
from ..realtors.models import Realtor

""" req is short for request """

# Create your views here.


def index(request):
    # Get 3 Latest Listings
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
        # only published pages will show along with 3 because of split [0:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get Realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # descending order because of the minus sign

    # Get MVP Realtor quering all in case of more than one 
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor
    }
    return render(request, 'pages/about.html', context)
