#!/usr/bin/python

import psycopg2
import sys

dbname_1= 'business'
dbname_2 ='inspection'
dbname_3='violation'


try:
  con1=psycopg2_connect(database=dbname_1 user='food' host='localhost' password='check')
  cur1=con1.cursor()
  cur1.execute("CREATE TABLE Restaurant (business_id INT, name VARCHAR, address VARCHAR, city VARCHAR, state CHAR(2), postal_code INT, latitude FLOAT, longtitude FLOAT, phone_no VCHAR)")
  business_id=os.path+"business_id.cvs"
  cur1.execute("COPY Restaurant FROM  business_id DELIMITER ' ' csv")
  con1.commit()

  con2=psycopg2_connect(database=dbname_2 user='food' host='localhost' password='check')
  cur2=con2.cursor()
  cur2.execute("CREATE TABLE Score (business_id INT, date DATE, score INT, type VARCHAR)")
  inspection_id=os.path+"inspection_id.cvs"
  cur2.execute("COPY Score FROM  inspection_id DELIMITER ' ' csv")
  con2.commit()  

  con3=psycopg2_connect(database=dbname_3 user='food' host='localhost' password='check')
  cur3=con3.cursor()
  cur3.execute("CREATE TABLE Violation (business_id INT, date DATE, vi_type VARCHAR, vi_severe VARCHAR, vi_description VARCHAR)")
  violation_id=os.path+"violation_id.cvs"
  cur3.execute("COPY Violation FROM  violation_id DELIMITER ' ' csv")
  con3.commit()


expect:
  print " database connection error"


con1.close()
con2.close()
con3.close()

