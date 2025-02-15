from django.shortcuts import render
from utils.utils import get_pickup_line
# import time
def home_view(request):
    context = {}
    if request.method == 'POST':
        # context = {"pickupline" : get_pickup_line()}
        # time.sleep(5)
        context = {"pickupline": "HEY"}
        
    return render(request, 'index.html', context)