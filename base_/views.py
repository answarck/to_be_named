from django.shortcuts import render
from utils.utils import get_pickup_line

def home_view(request):
    context = {}
    if request.method == 'POST':
        context = {"pickupline" : get_pickup_line()}
        
    return render(request, 'index.html', context)