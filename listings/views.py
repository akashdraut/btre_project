from django.shortcuts import render, get_object_or_404

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
    return render(request, 'listings/search.html')
