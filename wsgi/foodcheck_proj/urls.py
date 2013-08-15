'''
URL definitions for foodcheck project
'''
#    Copyright (C) 2013 Timothy James Austen, Eileen Qiuhua Lin,
#                       Richard Esplin <richard-oss@esplins.org>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import patterns, include, url 


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'foodcheck_app.views.home', name='home'),
    url(r'^about/', 'foodcheck_app.views.about', name='about'),
#	url(r'^$', 'foodcheck_app.views.resources', name='resources')
    
    
    # url(r'^search/$', 'foodcheck_app.views.search', name='search'),
    # url(r'^search-form/$', views.search_form),
	# url(r'^$', 'foodcheck_app.views.search_form', name='search_form'),
    # url(r'^$', 'foodcheck_app.views.search', name='search'),
    # url(r'^foodcheck/', include('foodcheck.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
