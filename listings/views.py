from django.shortcuts import render, get_object_or_404

from .choices import *

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing


def index(request):
    """ Contains all the published listings and pagination logic """
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    """ Contains single property information """
    listing = get_object_or_404(Listing, pk=listing_id)  # if invalid id passed page_not_found error will show

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    """ Contains code for search bar """
    queryset_list = Listing.objects.order_by('-list_date')

    # For search with Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:  # To check keyword is not empty
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # For search with ciy
    if 'city' in request.GET:
        city = request.GET['city']
        if city:  # To check city is not empty
            queryset_list = queryset_list.filter(city__iexact=city)

    # For search with state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:  # To check state is not empty
            queryset_list = queryset_list.filter(state__iexact=state)

    # For search with Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:  # To check bedrooms field is not empty
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # For search with price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:  # To check price field is not empty
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET  # To abvailable values to keep it in search bar
    }

    return render(request, 'listings/search.html', context)
