#/usr/bin/python
import sys
import csv
import os.path, time
import urllib2
import psycopg2

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

dbname_1= 'business'
dbname_2 ='inspection'
dbname_3='violation'

con1=psycopg2_connect(database=dbname_1, user='food', host='localhost', password='check')
cur1=con1.cursor()

## search for the restaurant
cur1.execute("SELECT "+search_1+"  FROM Restaurant")
rows=cur1.fetchall()
id=rows[1]
latitude=rows[7]
longitude=rows[8]



## read the score
con2=psycopg2_connect(database=dbname_2, user='food', host='localhost', password='check')
cur2=con2.cursor()
cur2.execute("SELECT "+id+" FROM Score")
rows=cur2.fetchall()
  if row in rows
     time=row[2]
     score=row[3]
 

## search for the violation

con3=psycopg2_connect(database=dbname_3 user='food' host='localhost' password='check')
cur3=con3.cursor()
cur3.execute("SELECT "+id+" FROM Violation")
rows=cur3.fetchall()  
if row in rows
     date=row[2]
     vi_type=row[3]
     vi_severe=row[4]
     vi_description=row[5]


con1.close()
con2.close()
con3.close()

     
 



