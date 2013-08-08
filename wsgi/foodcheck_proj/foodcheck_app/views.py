import os
from django.shortcuts import render
from django.http import HttpResponse

# Load home page into skeleton
def home(request):
    return render(request, 'home.html',
                  {},
                 )
    
def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
