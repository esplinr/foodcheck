import os
from django.shortcuts import render

def home(request):
    return render(request, 'foodcheck/home.html',
                  {},
                 )

# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
