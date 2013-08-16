'''
Django View functions for foodcheck_app
'''
# Copyright (C) 2013 Timothy James Austen, Eileen Qiuhua Lin,
# Richard Esplin <richard-oss@esplins.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import os
from django.shortcuts import render
from django.http import HttpResponse
import facade


def home(request):
    return render(request, 'home.html',
                  {},
                 )


def search(request):
    error_message = False
    if 'q' in request.GET:
        try:
            # GET['q'] contains a search string for the business
            businesses = facade.load_businesses_by_name(request.GET['q'],
                                    no_details=True)
        except Exception as error:
            error_message = "%s" %(error)
    else:
        error_message = 'You submitted an empty form.'

    if error_message:
        return render(request, 'home.html',
                      {'error': True,
                       'message': message}
                     )
    else:
        return render(request, 'home.html',
                      {'businesses': businesses,})


def selected_business(request, db_id):
    try:
        business = facade.Business(request.GET['q'])
    except Exception as error:
        return render(request, 'home.html',
                      {'error': True,
                       'message': "%s" %(error)}
                     )

    return render(request, 'home.html',
                  {'business': business,})


def about(request):
	return render(request, 'about.html',)


# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
