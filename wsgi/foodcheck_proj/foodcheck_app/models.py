from django.db import models


class Restaurant(models.Model):
    city_business_id=models.IntegerField(
        verbose_name="business ID for city"
        help_text="The ID the city uses for this business")
    name=models.CharField(max_length=40)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    postal_code=models.IntegerField()
    latitude=models.FloatField()
    longitude=models.FloatField()
    phone=models.CharField(verbose_name="phone number", max_length=15)


class Inspection(models.Model):
    restaurant = models.ForeignKey(Restaurant,
        verbose_name="related restaurant", on_delete=models.CASCADE
        help_text="Connect to the restaurant by the city_business_id")
    city_business_id=models.IntegerField(
        help_text="City business ID, used to match to Restaurant")
    date=models.DateField()
    score=models.IntegerField()
    reason=models.CharField(verbose_name="Reason for Inspection",
        max_length=50
        help_text="The reason for the inspection is given in the inspection type")


class Violation(models.Model):
    inspection = models.ForeignKey(Inspection,
        verbose_name="inspection during which violation was found",
        on_delete=models.CASCADE,
        help_text="Connect to the inspection by the city_business_id + date")
    # TODO -- should foreign key be Inspection or Restaruant?
    city_business_id=models.IntegerField(
        help_text="City business ID, used to match to Restaurant")
    date=models.DateField(verbose_name="date of violation")
    vi_type=models.CharField(verbose_name="violation type", max_length=20)
    severity=models.CharField(verbose_name="violation severity", max_length=20)
    description=models.CharField(verbose_name="description of violation",
        max_length=50)


# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
