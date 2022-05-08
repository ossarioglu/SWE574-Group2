import random
from django.shortcuts import render
from offers.models import Offer

    
def home(request):
    result = list(Offer.objects.all())

    # Number of unread notification is send to main page
    if request.user.is_authenticated:
        unreadNote = request.user.receiverID.filter(status='Unread').count
    else:
        unreadNote = ""

    if len(result) >= 3:
        return render(request, 'home.html', {'offers': random.sample(result, 3), 'notes':unreadNote})
    return render(request, 'home.html', {'offers': result, 'notes':unreadNote})


