'''
Facade class to expose Businesses in a more pythonic way
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

import logging
from foodcheck_app import models
# Other facades
from inspection import load_inspections

logger = logging.getLogger('foodcheck_app.facade.Business')

def load_businesses_by_name(name_search_term, offset=0, page_limit=100,
                            no_details=False):
    '''
    Return a list of businesses that match the given name.
    Returns None if there are no matching businesses.
    Offset and limit helps with paging.
    '''
    businesses_match = models.Business.objects\
                             .filter(name__contains=name_search_term)\
                                     [offset:offset+page_limit]
    if len(businesses_match) == 0:
        return []
    businesses_list = []
    for b in businesses_match:
        businesses_list.append(Business(orm_obj=b, no_details))
    return businesses_list


def load_businesses_by_address(address_search_term, offset=0, page_limit=100
                               no_details=False):
    '''
    Return a list of businesses that match the given address.
    Returns None if there are no matching businesses.
    Offset and limit helps with paging.
    '''
    businesses_match = models.Business.objects\
                             .filter(address__contains=address_search_term)\
                                     [offset:offset+page_limit]
    if len(businesses_match) == 0:
        return []
    businesses_list = []
    for b in businesses_match:
        businesses_list.append(Business(orm_obj=b, no_details))
    return businesses_list


#def load_businesses_by_bounding_box(lat1, long1, lat2, long2):
#    '''
#    Return a list of businesses that are located within the geographic
#    bounding box.
#    Returns None if there are no matching businesses.
#    '''


class Business():
    '''
    A class for accessing information about a business, including inspection
    data and violations.
    '''
    db_id = None
    city_business_id = ""
    name = ""
    address = ""
    city = ""
    state = ""
    postal_code = ""
    latitude = 0.0
    longitude = 0.0
    phone = ""
    # TODO Might be less resource intensive to use a python property decorator
    #      to define a getter that populates these if None at access time.
    #      Then only need to take the hit when the data is needed
    inspections = None # A list of inspection objects
    violations = None # A list of violation objects


    def __repr__(self):
        return "Business object with City ID: %s, Name: %s, Address: %s" \
                %(self.city_business_id, self.name, self.address)


    def __init__(self, db_id=None, orm_obj=None, no_details=False):
        '''
        Populate the class with information about the business that matches
        the database id.
        If have an orm_obj, use that instead of hitting the DB again.
        If both the db_id and orm_obj are populated, ignore the db_id
        If none is provided, create an empty business.
        If no_details is true, skip loading inspections and violations
        This provides a performance improvement
        '''
        if db_id == None and orm_obj == None:
            return
        elif orm_obj == None:
            # Look up the business in the DB
            try:
               orm_obj = models.Business.objects.get(id=db_id)
            except models.Business.DoesNotExist:
                logger.error("No business matches this db_id! %s" %(db_id))
                return None
            except models.Business.MultipleObjectsReturned:
                logger.error("Should be exactly one business with ID! %s"
                        %(db_id))
                return None

        logger.info('Initializing business object from existing data. ID: %s'
                    %(orm_obj.id))

        self.db_id = orm_obj.id
        self.city_business_id = orm_obj.city_business_id
        self.name = orm_obj.name
        self.address = orm_obj.address
        self.city = orm_obj.city
        self.state = orm_obj.state
        self.postal_code = orm_obj.postal_code
        self.latitude = orm_obj.latitude
        self.longitude = orm_obj.longitude
        self.phone = orm_obj.phone

        if !no_details:
            self.load_inspections()
            self.load_violations_from_inspections()


    def load_inspections(self):
        self.inspections=load_inspections(self) 


    def load_violations_from_inspections(self):
        self.violations = []
        for i in self.inspections:
            self.violations.extend(i.violations)


# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
