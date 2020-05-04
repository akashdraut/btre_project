from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    """ Contains & manage the data need to show on Featured Listing page """
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    """ Contains and manages the data need to show on About pag """

    # Get all realtors based on hire_date
    realtors = Realtor.objects.order_by('-hired_date')

    # get mvp realtor
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
