'''
Dowload San Francisco health inspector data.
Relevant web sites:
  https://data.sfgov.org/Public-Health/Restaurant-Scores/stya-26eb
  https://204.68.210.15/food/File%20Specifications.pdf

There are two zip packages:
  SFBusinesses.zip: contains businesses, inspections, violations
  SFFoodProgram_Complete_Data.zip: contains _plus.csv files
The _plus files contain business owner data and inspections without scores, but
has fewer businesses.

From data.SFgov.org:
The difference between the two files is that the "Complete" file include all
establishments that are regulated by the DPH Food Safety program, which may
include businesses that have no food preparation on premises. The other data
set, with the "_plus" files, are those establishments with food preparation,
which is what YELP uses to integrate into their site. If there is an inspection
done on a business but you do not see that business_id within the
"business_plus.csv", it may be due to the fact that the permit status for that
establishment is currently inactive, which may occur for several reasons.

Files are encoded as ISO-8859-15

Violations can fall into:
* high risk: records specific violations that directly relate to the transmission of food borne illnesses, the adulteration of food products and the contamination of food-contact surfaces.
* moderate risk: records specific violations that are of a moderate risk to the public health and safety.
* low risk: records violations that are low risk or have no immediate risk to the public health and safety.

Scores:
* 0-70   "Poor"
* 71-85  "Needs Improvement"
* 86-90  "Adequate"
* 91-100 "Good"
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

import sys
import csv
import os.path, time
import urllib2


#TODO Detect most recent previous downloaded file
#TODO Fix file layout: if __name__ == "__main__":

last_zip_file = "" # Insert path here

## check whether we need to update the file
time_ori=os.path.getmtime(last_zip_file)

sf_food=urlib2.request.urlopen("https://204.68.210.15/food/SFFoodProgram_Complete_Data.zip")
time_now = sf_food.info().getdate('last-modified')

if time_now > time_ori
   sf_data=open("SFFoodProgram_Complete_Data.zip","w")
   sf_data.write(sf_food.read())
   sf_data.close()


#vim tabstop=8 expandtab shiftwidth=4 softtabstop=4
