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


    def __init__(self, db_id = None):
        '''
        Populate the class with information about the business that matches
        the database id.
        If none is provided, create an empty business.
        '''
        if db_id = None:
            return

        logger.info('Initializing business object from existing data. ID: %s'
                    %(db_id))
        business_match = models.Business.objects.filter(
                                    city_business_id=city_business_id)
        if len(business_match) <> 1:
            logger.error("Should be exactly one entry for this ID! %s" 
                           %(db_id))
            return None

        db_business = business_match[0]
        self.db_id = db_business.id
        self.city_business_id = db_business.city_business_id
        self.name = db_business.name
        self.address = db_business.address
        self.city = db_business.city
        self.state = db_business.state
        self.postal_code = db_business.postal_code
        self.latitude = db_business.latitude
        self.longitude = db_business.longitude
        self.phone = db_business.phone


    def load_inspections(self):
       self.inspections=load_inspections(self) 


# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
