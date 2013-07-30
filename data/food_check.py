import sys
import csv
import os.path, time
import urllib2



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



