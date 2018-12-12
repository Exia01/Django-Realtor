from django.shortcuts import get_object_or_404, render
from .models import Listing
from .choices import (price_choices, bedroom_choices, state_choices)

#import paginator
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)

""" req is short for request """


def index(req):
    # this shows the dates in decending order because of "-"
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # ADD PAGINATOR based on listing count
    paginator = Paginator(listings, 2)
    # here be dragons
    page = req.GET.get('page')
    paged_listings = paginator.get_page(page)

    # creates a dictionary to pass a parameter
    context = {
        'listings': listings,
        # passing dictionaries
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
    }

    return render(req, 'listings/listings.html', context)


def listing(req, listing_id):
    # This is a built in page "404"

    # listing takes primary key pass through url and the model
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(req, 'listings/listing.html', context)


def search(req):
    # first we pull all of them we will filter them out first
    queryset_list = Listing.objects.order_by('-list_date')
    listings = Listing.objects.all()

    # Keywords
    # this test checks for the keywords in the form
    if 'keywords' in req.GET:
        # if it does exist, assign it
        keywords = req.GET['keywords'] #looking for a field name in the html
        # print(keywords)
        # we don't want to pass empty strings
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
            # not exact match but it contains

     # City
    if 'city' in req.GET:
        city = req.GET['city']
        print(city)
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)  # exact but not case sensitive

    # State
    if 'state' in req.GET:
        state = req.GET['state']
        # print(state)
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)

    # Bedrooms
    if 'bedrooms' in req.GET:
        bedrooms = req.GET['bedrooms']
        # print(bedrooms)
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)  # up to number bedrooms

    # Price
    if 'price' in req.GET:
        price = req.GET['price']
        # print(price)
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)  # price up to

    context = {
        'listings': queryset_list,
        'values': req.GET, # obtaining all queries as values 
        'state_choices': state_choices,
        # 'cityValues': cityValues,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
    }
    return render(req, 'listings/search.html', context)
