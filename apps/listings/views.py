from django.shortcuts import render


def index(req):
    return render(req, 'listings/listings.html')


def listing(req):
    return render(req, 'listings/listing.html')


def search(req):
   return render(req, 'listings/search.html')
