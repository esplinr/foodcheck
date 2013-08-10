'''
Custom django admin command to import data from CSV file into database
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

import os
import csv
from django.core.management.base import BaseCommand
from foodcheck_app.models import Restaurant, Inspection, Violation


class Command(BaseCommand):
#    args = '<city_name city_name ...>' #Don't know what this does yet
    help = 'Imports the city data from a CSV into the database'

    # Need to explicitly handle UTF-8 data (adapted example from docs)
    def __utf8_csv_reader(self, utf8_data, dialect=csv.excel, **kwargs):
        csv_dictreader = csv.DictReader(utf8_data, dialect=dialect, **kwargs)
        dict_array = []
        for row in csv_dictreader:
            data_dict = {}
            print "New Row"
            for key, value in row.iteritems():
                print "%s, %s" %(key, value)
                # TODO it isn't carrying the UTF-8 value through
                data_dict[unicode(key, 'utf-8',errors='replace')]= \
                    unicode(value, 'utf-8',errors='replace')
            dict_array.append(data_dict)
        return dict_array


    def __load_csv_to_dict(self, csv_filepath):
        # Warning: Reads entire file into memory!
        csvfile = open(csv_filepath, 'rb')
        dialect = csv.Sniffer().sniff(csvfile.read(4098))
        csvfile.seek(0)
        data_dict_array = self.__utf8_csv_reader(csvfile, dialect)
        csvfile.close()
        return data_dict_array


    def __load_sf_dict_to_db(self):
        # TODO Find the latest data dumps instead of hardcoding the name
        # Read in Restaurant data
        restaurant_dict_array = self.__load_csv_to_dict(os.path.join(
                                             os.environ['OPENSHIFT_REPO_DIR'],
                                             "data", "data_dump_sf_20130810",
                                             "businesses_plus.csv"))
        for row in restaurant_dict_array:
            restaurant_object = Restaurant(city_business_id=row['business_id'],
                                           name=row['name'],
                                           address=row['address'] ,
                                           city=row['city'],
                                           state=row['state'],
                                           postal_code=row['postal_code'],
                                           latitude=row['latitude'],
                                           longitude=row['longitude'],
                                           phone=row['phone_no'])
            restaurant_object.save()
            self.stdout.write('Successfully loaded row')
            
        # Read the Inspection data   
        inspection_dict_array = self.__load_csv_to_dict(os.path.join(
                                             os.environ['OPENSHIFT_REPO_DIR'],
                                             "data", "data_dump_sf_20130810",
                                             "inspections_plus.csv"))
        for row in inspection_dict_array:
            inspection_object = Inspection(city_business_id=row['business_id'],
                                score=row['Score'],
                                date=row['data'],
                                reason=row['type'])
            inspection_object.save()
            self.stdout.write('Successfully loaded row')    
            
        # Read the Violation data   
        violation_dict_array = self.__load_csv_to_dict(os.path.join(
                                             os.environ['OPENSHIFT_REPO_DIR'],
                                             "data", "data_dump_sf_20130810",
                                             "violations_plus.csv"))
        for row in violation_dict_array:
            
            violation_object =Violation(city_business_id=row['business_id'], 
                                        date=row['date'],
                                        vi_type=row['violation_type'],
                                        vi_severe=row['ViolationSeverity'],
                                        vi_description=row['description'])
            violation_object.save()
            self.stdout.write('Successfully loaded row')        


    def handle(self, *args, **options):
        self.__load_sf_dict_to_db()


# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
