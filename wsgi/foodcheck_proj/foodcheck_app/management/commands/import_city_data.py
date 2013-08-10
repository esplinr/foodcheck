import os
import csv
from django.core.management.base import BaseCommand
from foodcheck_app.models import Restaurant, Inspection, Violation

class Command(BaseCommand):
#    args = '<city_name city_name ...>' #Don't know what this does yet
    help = 'Imports the city data from a CSV into the database'

    
    def __load_csv_to_dict(self, csv_filepath):
        csvfile = open(csv_filepath, 'rU')
        dialect = csv.Sniffer().sniff(csvfile.read(4098))
        csvfile.seek(0)
        return csv.DictReader(csvfile, dialect=dialect)
 

    def __load_sf_dict_to_db(self):
        # TODO Find the latest data dumps instead of hardcoding the name
        # Read in Restaurant data
        restaurant_dict_array = self.__load_csv_to_dict(os.path.join(
                                             os.environ['OPENSHIFT_REPO_DIR'],
                                             "data", "data_dumps",
                                             "20130805_businesses_plus.csv"))
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
                                             "data", "data_dumps",
                                             "20130805_inspections_plus.csv"))
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
                                             "data", "data_dumps",
                                             "20130805_violations_plus.csv"))
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
