import random
from django.shortcuts import render
from offers.models import Offer
from django.http import JsonResponse
from django.contrib.auth.models import User
from actstream import feeds
from actstream.models import model_stream
import json

def home(request):
    result = list(Offer.objects.all())

    # Number of unread notification is send to main page
    if request.user.is_authenticated:
        unreadNote = request.user.receiverID.filter(status='Unread').count
        stream = model_stream(request.user)
        for i in stream:
            print(vars(i))
        if len(result) >= 3:
            return render(request, 'home_with_activity.html', {'offers': random.sample(result, 3), 'notes': unreadNote,"stream":stream})
        return render(request, 'home_with_activity.html', {'offers': result, 'notes': unreadNote,"stream":stream})
    else:
        unreadNote = ""
        if len(result) >= 3:
            return render(request, 'home.html', {'offers': random.sample(result, 3), 'notes': unreadNote})
        return render(request, 'home.html', {'offers': result, 'notes': unreadNote})


def notificationcount(request):

    if request.user.is_authenticated:
        unreadNoteCount = request.user.receiverID.filter(status='Unread').count()
    else:
        unreadNoteCount = ""

    return JsonResponse({'count':unreadNoteCount})


def activity_feed(request):
    return render(request, 'activity_feed.html')

