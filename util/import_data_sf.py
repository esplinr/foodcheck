import sys
import csv
import os.path, time
import urllib2
'''
Dowload San Francisco health inspector data.
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


if len(sys.argv) < 2:
    print("Please enter a restaurant name.")
    search_1 = input("Search for:")
else:
    search_1=sys.argv[1]

## check whether we need to update the file
time_ori=os.path.getmtime(file)

sf_food=urlib2.request.urlopen("https://204.68.210.15/food/SFFoodProgram_Complete_Data.zip")
time_now = sf_food.info().getdate('last-modified')

if time_now > time_ori
   sf_data=open("SFFoodProgram_Complete_Data.zip","w")
   sf_data.write(sf_food.read())
   sf_data.close()


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
cvsfile=open("inspection_plus.csv","r")
cvsfile.seek
reader=csv.reader(csvfile,dialect='excel', delimiter=",")


## search for the score
for line in reader:
   if business_id in line:
      score=line[2]
      time=line[3]
      vilation=line[4]


csvfile.close()


#vim tabstop=8 expandtab shiftwidth=4 softtabstop=4
