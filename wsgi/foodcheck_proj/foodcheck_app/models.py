'''
Django Model definition for foodcheck_app
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

from django.db import models


class Restaurant(models.Model):
    city_business_id=models.IntegerField(
        verbose_name="business ID for city",
        help_text="The ID the city uses for this business")
    name=models.CharField(max_length=40)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    postal_code=models.IntegerField()
    latitude=models.FloatField(null=True)
    longitude=models.FloatField(null=True)
    phone=models.CharField(verbose_name="phone number", max_length=15,
                           null=True)


class Inspection(models.Model):
    restaurant = models.ForeignKey(Restaurant,
        verbose_name="related restaurant", on_delete=models.CASCADE,
        help_text="Connect to the restaurant by the city_business_id")
    city_business_id=models.IntegerField(
        help_text="City business ID, used to match to Restaurant")
    date=models.DateField()
    score=models.IntegerField(null=True,
        help_text="<70=Poor, 71-85=Needs Improvement, 86-90=Adequate, >91=Good")
    score_description=models.CharField(verbose_name="description of score",
        help_text="A description to help people interprete the score.",
        max_length=50, null=True)
    reason=models.CharField(verbose_name="reason for Inspection",
        max_length=50,
        help_text="The reason for the inspection is given in the inspection type")


class Violation(models.Model):
    inspection = models.ForeignKey(Inspection,
        verbose_name="inspection during which violation was found",
        on_delete=models.CASCADE,
        help_text="Connect to the inspection by the city_business_id + date")
    city_business_id=models.IntegerField(
        help_text="City business ID, used to match to Restaurant")
    date=models.DateField(verbose_name="date of violation")
    vi_type=models.CharField(verbose_name="violation type", max_length=20)
    severity=models.CharField(verbose_name="violation severity", max_length=20)
    description=models.CharField(verbose_name="description of violation",
        max_length=50)


# vim:expandtab tabstop=8 shiftwidth=4 ts=8 sw=4 softtabstop=4
