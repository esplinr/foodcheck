'''
Facade class to expose Violations in a more pythonic way
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


logger = logging.getLogger('foodcheck_app.facade.Violation')

def load_violations(inspection):
    '''
    Return a list of violations for the given inspection object.
    Returns None if there are no previous violations.
    '''
    inspection_db_id = inspection.db_id
    logger.info('Creating a list of violations related to inspection. DB ID: %s'
                %(inspection_db_id))
    violations_match = models.Violation.objects.filter(
                                                 inspection_id=inspection_db_id)
    if len(violations_match) == 0:
        logger.warning("No violations exist for this inspection! DB ID: %s" 
                     %(inspection_db_id))
        return None
    violations_list = []
    for v in violations_match:
        violations_list.append(Violation(inspection_obj=inspection, orm_obj=v))
    return inspections_list


class Violation():
    '''
    A class for accessing information about a violation.
    An inspection has to be related to an inspection, which is related to a
    business.
    '''
    db_id = None
    date = None # datetime object
    vi_type = None
    severity = None
    description = None
    # References to associated classes, will normally be set at object creation
    inspection = None # Parent object back-reference


    def __repr__(self):
        return "Violation (inspection ID: %s), Type: %s" \
                %(self.inspection.db_id, self.vi_type)


    def __init__(self, inspection_obj, db_id=None, orm_obj=None):
        '''
        Populate the class with information about the violation that matches
        the database id.
        If have an orm_obj, use that instead of hitting the DB again.
        If both the db_id and orm_obj are populated, ignore the db_id
        If none is provided, create an empty violation.
        '''
        self.inspection = inspection_obj

        # If no existing violation, return an empty object
        if db_id == None and orm_obj == None:
            return
        elif orm_obj == None:
            # Look up the violation in the DB
            self.db_id = db_id
            violations_match = models.Violation.objects.filter(id=db_id)
            if len(violations_match) != 1:
                logger.error("Should be exactly one entry for this ID! %s" 
                             %(db_id))
                return None
            orm_obj = violations_match[0]
 
        logger.info('Initializing violation with content from db_row %s'
                    %(self.db_id))

        self.date = orm_obj.date
        self.vi_type = orm_obj.vi_type
        self.severity = orm_obj.severity
        self.description = orm_obj.description


# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
