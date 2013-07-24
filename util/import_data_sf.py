# Copyright (C) 2013 Eileen Lin, Tim Austen, Richard Esplin
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.:
'''
Download health inspector data from San Fransisco
and load into a database.
'''

import sys
import csv


if len(sys.argv) < 2:
    print("Please enter a restaurant name.")
    search_1 = input("Search for:")
else:
    search_1=sys.argv[1]


## read variables for searching
cvsfile=open("business_id.csv","r")
cvsfile.seek
reader=csv.reader(csvfile,dialect='excel', delimiter=",")

## search for the restaurant
for line in reader:
   if search_1 in line:
       business_id=line[1];
       latitude=line[7];
       longitude=line[8];


## read the score
cvsfile=open("business_id.csv","r")
cvsfile.seek
reader=csv.reader(csvfile,dialect='excel', delimiter=",")


## search for the score
for line in reader:
   if business_id in line:
      score=line[2]


csvfile.close()


#vim tabstop=8 expandtab shiftwidth=4 softtabstop=4
