from django.db import models

# Create your models here.
class Restaurant(models.Model):
  city_business_id=models.IntegerField()
  name=models.CharField(max_length=40)
  address=models.CharField(max_length=50)
  city=models.CharField(max_length=50)
  state=models.CharField(max_length=50)
  postal_code=models.IntegerField()
  latitude=models.FloatField()
  longitude=models.FloatField()
  phone_no=models.CharField(max_length=15)

class Inspection(models.Model):
  city_business_id=models.IntegerField()
  date=models.DateField()
  score=models.IntegerField()
  reason=models.CharField(max_length=50)


class Violation(models.Model):
   city_business_id=models.IntegerField()
   date=models.DateField()
   vi_type=models.CharField(max_length=20)
   severity=models.CharField(max_length=20)
   description=models.CharField(max_length=50)
