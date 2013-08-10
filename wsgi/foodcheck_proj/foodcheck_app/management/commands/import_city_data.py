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
import codecs
import datetime
from django.core.management.base import BaseCommand
from foodcheck_app.models import Business, Inspection, Violation


class Command(BaseCommand):
#    args = '<city_name city_name ...>' #Don't know what this does yet
    help = 'Imports the city data from a CSV into the database'


    # Need to explicitly handle UTF-8 data (adapted example from docs)
    def __utf8_encoder(self, unicode_csv_data):
        for line in unicode_csv_data:
            yield line.encode('utf-8')

    def __utf8_dict_decoder(self, utf8_dict):
        unicode_dict = {}
        for key, value in utf8_dict.iteritems():
            unicode_dict[unicode(key,'utf-8')] = unicode(value,'utf-8')
        return unicode_dict

    def __unicode_csv_reader(self, unicode_csv_data, dialect=csv.excel, **kwargs):
        # csv.py doesn't do Unicode; encode temporarily as UTF-8:
        csv_dictreader = csv.DictReader(self.__utf8_encoder(unicode_csv_data),
                                        dialect=dialect, **kwargs)
        for row in csv_dictreader:
            yield self.__utf8_dict_decoder(row)

    def __load_csv_to_dict(self, csv_filepath):
        # Warning: Reads entire file into memory!
        # Sniff file as ascii, so we don't stop mid-utf-8 char
        csvfile = open(csv_filepath, 'rb')
        dialect = csv.Sniffer().sniff(csvfile.read(4098))
        csvfile.close()
        csvfile = codecs.open(csv_filepath, 'rb', 'iso-8859-15')
        return self.__unicode_csv_reader(csvfile, dialect)


    def __empty_to_none(self, value):
        ''' The DB does not like getting an empty string where it expects null,
            So we detect empty strings, and return None.
        '''
        if value == '':
            return None
        else:
            return value


    def __date_string_to_object(self, string_date):
        ''' Convert from YYYYMMDD to a python object
        '''
        # There is probably a better way to do this with a constructor that 
        # takes a string and a format specifier, but I didn't see it.
        year = int(string_date[:4])
        month = int(string_date[4:6])
        day = int(string_date[6:8])
        return datetime.date(year, month, day)
 
    def __load_sf_dict_to_db(self):
        # TODO Find the latest data dumps instead of hardcoding the name
        # Read in Business data
        business_dict_array = self.__load_csv_to_dict(os.path.join(
                                             os.environ['OPENSHIFT_REPO_DIR'],
                                             "data", "data_dump_sf_20130810",
                                             "businesses_plus.csv"))
        for row in business_dict_array:
            business_object = Business(city_business_id=row['business_id'],
                                       name=row['name'],
                                       address=row['address'] ,
                                       city=row['city'],
                                       state=row['state'],
                                       postal_code=row['postal_code'],
                                       latitude=self.__empty_to_none(row['latitude']),
                                       longitude=self.__empty_to_none(row['longitude']),
                                       phone=self.__empty_to_none(row['phone_no'])
                                      )
            business_object.save()
        #    self.stdout.write('Successfully loaded business\n')
            
        # Read the Inspection data   
        inspection_dict_array = self.__load_csv_to_dict(os.path.join(
                                             os.environ['OPENSHIFT_REPO_DIR'],
                                             "data", "data_dump_sf_20130810",
                                             "inspections_plus.csv"))
        for row in inspection_dict_array:
            # Look up foreign key in Business table
            business_match = Business.objects.filter(city_business_id=row['business_id'])
            if len(business_match) == 0:
                self.stdout.write("WARNING: No businesses match this inspection! Skipping\n")
                self.stdout.write(str(row) + "\n")
                continue
            elif len(business_match) > 1:
                self.stdout.write("Multiple businesses match this ID! Using first.\n")
                self.stdout.write(str(row) + "\n")

            date = self.__date_string_to_object(row['date'])
            inspection_object = Inspection(business_id=business_match[0].id,
                                    city_business_id=row['business_id'],
                                    score=self.__empty_to_none(row['Score']),
                                    date=date,
                                    reason=row['type'])
            inspection_object.save()
            self.stdout.write('Successfully loaded inspection\n')    
            
        # Read the Violation data   
        violation_dict_array = self.__load_csv_to_dict(os.path.join(
                                             os.environ['OPENSHIFT_REPO_DIR'],
                                             "data", "data_dump_sf_20130810",
                                             "violations_plus.csv"))
        for row in violation_dict_array:
            date = self.__date_string_to_object(row['date'])
            # Look up foreign key in Inspection table
            inspection_match = Inspection.objects.filter(
                                            city_business_id=row['business_id'],
                                            date=date)
            if len(inspection_match) == 0:
                self.stdout.write("WARNING: No inspections match this violation! Skipping\n")
                self.stdout.write(str(row) + "\n")
                continue
            elif len(inspection_match) > 1:
                self.stdout.write("Multiple inspections match this violation! Using first.\n")
                self.stdout.write(str(row) + "\n")

            violation_object =Violation(inspection_id=inspection_match[0].id,
                                        city_business_id=row['business_id'], 
                                        date=date,
                                        vi_type=row['violation_type_id'],
                                        severity=row['ViolationSeverity'],
                                        description=row['description'])
            violation_object.save()
            self.stdout.write('Successfully loaded violation')        


    def handle(self, *args, **options):
        self.__load_sf_dict_to_db()


# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
