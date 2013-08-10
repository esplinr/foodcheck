# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Inspection.restaurant'
        db.add_column('foodcheck_app_inspection', 'restaurant',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['foodcheck_app.Restaurant']),
                      keep_default=False)

        # Deleting field 'Restaurant.phone_no'
        db.delete_column('foodcheck_app_restaurant', 'phone_no')

        # Adding field 'Restaurant.phone'
        db.add_column('foodcheck_app_restaurant', 'phone',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True),
                      keep_default=False)


        # Changing field 'Restaurant.longitude'
        db.alter_column('foodcheck_app_restaurant', 'longitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Restaurant.latitude'
        db.alter_column('foodcheck_app_restaurant', 'latitude', self.gf('django.db.models.fields.FloatField')(null=True))
        # Adding field 'Violation.inspection'
        db.add_column('foodcheck_app_violation', 'inspection',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['foodcheck_app.Inspection']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Inspection.restaurant'
        db.delete_column('foodcheck_app_inspection', 'restaurant_id')

        # Adding field 'Restaurant.phone_no'
        db.add_column('foodcheck_app_restaurant', 'phone_no',
                      self.gf('django.db.models.fields.CharField')(default=-1, max_length=15),
                      keep_default=False)

        # Deleting field 'Restaurant.phone'
        db.delete_column('foodcheck_app_restaurant', 'phone')


        # Changing field 'Restaurant.longitude'
        db.alter_column('foodcheck_app_restaurant', 'longitude', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Restaurant.latitude'
        db.alter_column('foodcheck_app_restaurant', 'latitude', self.gf('django.db.models.fields.FloatField')(default=None))
        # Deleting field 'Violation.inspection'
        db.delete_column('foodcheck_app_violation', 'inspection_id')


    models = {
        'foodcheck_app.inspection': {
            'Meta': {'object_name': 'Inspection'},
            'city_business_id': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foodcheck_app.Restaurant']"}),
            'score': ('django.db.models.fields.IntegerField', [], {})
        },
        'foodcheck_app.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city_business_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'postal_code': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'foodcheck_app.violation': {
            'Meta': {'object_name': 'Violation'},
            'city_business_id': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foodcheck_app.Inspection']"}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'vi_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['foodcheck_app']