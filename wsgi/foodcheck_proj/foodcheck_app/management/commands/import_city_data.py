from django.core.management.base import BaseCommand
from foodcheck_app.models import Restaurant, Score, Violation

class Command(BaseCommand):
    args = '<city_name city_name ...>'
    help = 'Imports the city data from a CSV into the database'

    def handle(self, *args, **options):
        self.stdout.write('Successfully ran the function')

# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
