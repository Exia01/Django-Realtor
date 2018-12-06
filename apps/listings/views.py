from django.shortcuts import render
from .models import Listing

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
        'listings': paged_listings
    }

    return render(req, 'listings/listings.html', context)


def listing(req, listing_id):
    # listing = get_object_or_404(Listing, pk=listing_id)
    # context = {
    #     'listing': listing
    # }
    return render(req, 'listings/listing.html')


def search(req):
    queryset_list = Listing.objects.order_by('-list_date')
    # queryset_list = Listing.objects.all()

    # Keywords
    if 'keywords' in req.GET:
        keywords = req.GET['keywords']
        print(keywords)
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # City
    if 'city' in req.GET:
        city = req.GET['city']
        print(city)
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)

    # State
    if 'state' in req.GET:
        state = req.GET['state']
        print(state)
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)

    # Bedrooms
    if 'bedrooms' in req.GET:
        bedrooms = req.GET['bedrooms']
        print(bedrooms)
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)

    # Price
    if 'price' in req.GET:
        price = req.GET['price']
        print(price)
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    context = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset_list,
        'values': req.GET
    }
    return render(req, 'listings/search.html', context)
