import os
from django.shortcuts import render

def home(request):
    return render(request, 'home.html',
                  {},
                 )

# Search_form example
# def search_form(request):
    # return render(request, 'search_form.html')
    
# def search(request):
    # if 'q' in request.GET:
    #    message = 'You searched for: %r' % request.GET['q']
    # else:
    #    message = 'You submitted an empty form.'
    # return HttpResponse(message)
# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
