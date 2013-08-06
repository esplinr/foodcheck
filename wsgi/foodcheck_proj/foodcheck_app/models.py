from django.db import models

# Create your models here.
class Restaurant(models.Model):
  business_id=models.IntegerField()
  name=models.CharField(max_length=40)
  address=models.CharField(max_length=50)
  city=models.CharField(max_length=50)
  state=models.CharField(max_length=50)
  postal_code=models.IntegerField()
  latitude=models.FloatField()
  longitude=models.FloatField()
  phone_no=models.CharField()

class Score(models.Model):
  business_id=models.IntegerField()
  date=models.DateField()
  score=models.IntegerField()
  type=models.CharField(max_length=50)


class Violation(models.Model):
   business_id=models.IntegerField()
   date=models.DateField()
   vi_type=models.CharField(max_length=20)
   vi_severe=models.CharField(max_length=20)
   vi_description=models.CharField(max_length=50)
