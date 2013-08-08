import os
import csv
from django.core.management.base import BaseCommand
from foodcheck_app.models import Restaurant, Score, Violation

class Command(BaseCommand):
#    args = '<city_name city_name ...>' #Don't know what this does yet
    help = 'Imports the city data from a CSV into the database'

    
    def __load_csv_to_dict(self, csv_filepath):
        csvfile = open(csv_filepath)
        dialect = csv.Sniffer().sniff(csvfile.read(4098))
        csvfile.seek(0)
        return csv.DictReader(csvfile, dialect=dialect)
 

    def __load_sf_dict_to_db(self):
        # Read in Restaurant data
        # TODO Find the latest data dump instead of hardcoding the name
        restaurant_dict_array = self.__load_csv_to_dict(os.path.join(
                                             os.environ['OPENSHIFT_REPO_DIR'],
                                             "data", "data_dumps",
                                             "20130805_businesses_plus.csv"))
        for row in restaurant_dict_array:
            self.stdout.write(row)
#            restaurant_object = Restaurant(name=row['name'], address=row['address'] . . . )
#            restaurant_object.save()
            self.stdout.write('Successfully loaded row')
        pass
        # Read in Score data
        # Read in Violation data


    def handle(self, *args, **options):
        self.__load_sf_dict_to_db()


# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
