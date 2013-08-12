'''
Facade class to expose Inspections in a more pythonic way
Will probably only be accessed as components of the Business class
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
from violation import load_violations


logger = logging.getLogger('foodcheck_app.facade.Inspections')

def load_inspections(business):
    '''
    Return a list of inspections for the given business object.
    Returns None if there are no previous inspections.
    '''
    biz_db_id = business.db_id
    logger.info('Creating a list of inspections related to business. DB ID: %s'
                %(biz_db_id))
    inspections_match = models.Inspection.objects.filter(business_id=biz_db_id)
    if len(inspections_match) == 0:
        logger.warning("No inspections exist for this business! DB ID: %s" 
                     %(biz_db_id))
        return None
    inspections_list = []
    for i in inspections_match:
        inspections_list.append(Inspection(business_obj=business, orm_obj=i))
    return inspections_list


class Inspection():
    '''
    A class for accessing information about an inspection, including violations.
    An inspection has to be related to a business.
    '''
    db_id = None
    score = None
    date = None # datetime object
    reason = None
    # References to associated classes, will normally be set at object creation
    business = None # Parent object back-reference
    violations = None # A list of violation objects


    def __repr__(self):
        return "Inspection (business ID: %s), Date: %s" \
                %(self.business.db_id, self.date)


    def __init__(self, business_obj, db_id=None, orm_obj=None):
        '''
        Populate the class with information about the inspection that matches
        the database id.
        If have an orm_obj, use that instead of hitting the DB again.
        If both the db_id and orm_obj are populated, ignore the db_id
        If none is provided, create an empty inspection.
        '''
        self.business = business_obj

        # If no existing inspection, return an empty object
        if db_id == None and orm_obj == None:
            return
        elif orm_obj == None:
            # Look up the inspection in the DB
            self.db_id = db_id
            inspections_match = models.Inspection.objects.filter(id=db_id)
            if len(inspections_match) != 1:
                logger.error("Should be exactly one entry for this ID! %s" 
                             %(db_id))
                return None
            orm_obj = inspections_match[0]
 
        logger.info('Initializing inspection with content from db_row %s'
                    %(self.db_id))

        self.score = orm_obj.score
        self.date = orm_obj.date
        self.reason = orm_obj.reason

        self.violations = load_violations(self)


# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
