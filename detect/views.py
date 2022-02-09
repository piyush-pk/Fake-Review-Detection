from genericpath import exists
from django.shortcuts import render
from .models import Review
from django.contrib import messages
# Create your views here.


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def Home(request):
    context = {
        'UserAgent': request.headers['User-Agent'],
        'ip': get_client_ip(request)

    }
    return render(request,  'index.html', context)


def reviews(request):
    if request.method == "POST":
        data = dict(request.POST)
        ip = get_client_ip(request)
        userAgent = request.headers['User-Agent']
        try:
            Review(name=data['name'][0], desc=data['desc']
                   [0], ip=ip, userAgent=userAgent).save()
        except:
            messages.error(request, 'Fake Review Detected .')
    return render(request, 'review.html')
