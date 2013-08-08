import os
import csv
from django.core.management.base import BaseCommand
from foodcheck_app.models import Restaurant, Score, Violation

class Command(BaseCommand):
#    args = '<city_name city_name ...>' #Don't know what this does yet
    help = 'Imports the city data from a CSV into the database'

    
    def __load_csv_to_dict(self, csv_filepath):
        # TODO Current error: new-line character seen in unquoted field - do you need to open the file in universal-newline mode?
        csvfile = open(csv_filepath)
        dialect = csv.Sniffer().sniff(csvfile.read(4098))
        csvfile.seek(0)
        return csv.DictReader(csvfile, dialect=dialect)
 

    def __load_sf_dict_to_db(self):
        # Read in Restaurant data
        # TODO Find the latest data dump instead of hardcoding the name
        restaurant_dict_array = self.__load_csv_to_dict(os.path.join(os.environ['OPENSHIFT_REPO_DIR'],
                                             "data", "data_dumps",
                                             "20130805_businesses_plus.csv"))
        for row in restaurant_dict_array:
            
            restaurant_object = Restaurant(business_id=row['business_id'],name=row['name'], 
                                            address=row['address'] ,city=row['city'],
                                             state=row['state'], post_code=row['post_code'] ,
                                              latitude=row['latitude'], longitude=row['longitude'],
                                              phone_no=row['phone_no'])
            restaurant_object.save()
            self.stdout.write('Successfully loaded row')
            
         ##Read the Score data   
        score_dict_array = self.__load_csv_to_dict(os.path.join(
                                             os.environ['OPENSHIFT_REPO_DIR'],
                                             "data", "data_dumps",
                                             "20130805_inspections_plus.csv"))
        for row in score_dict_array:
            
            score_object =Score(business_id=row['business_id'], score=row['Score'],
                                date=row['data'], type=row['type'])                       
            score_object.save()
            self.stdout.write('Successfully loaded row')    
            
        ##Read the Score data   
        violation_dict_array = self.__load_csv_to_dict(os.path.join(
                                             os.environ['OPENSHIFT_REPO_DIR'],
                                             "data", "data_dumps",
                                             "20130805_violations_plus.csv"))
        for row in violation_dict_array:
            
            violation_object =Violation(business_id=row['business_id'], date=row['date'],
                                vi_type=row['violation_type'], vi_severe=row['ViolationSeverity'],
                                vi_description=row['description'])                       
            violation_object.save()
            self.stdout.write('Successfully loaded row')        
            
            
        pass
        


    def handle(self, *args, **options):
        self.__load_sf_dict_to_db()


# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
