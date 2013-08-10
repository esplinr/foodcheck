# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Restaurant.name'
        db.alter_column('foodcheck_app_restaurant', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Restaurant.phone'
        db.alter_column('foodcheck_app_restaurant', 'phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Restaurant.state'
        db.alter_column('foodcheck_app_restaurant', 'state', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Restaurant.postal_code'
        db.alter_column('foodcheck_app_restaurant', 'postal_code', self.gf('django.db.models.fields.CharField')(max_length=15))

        # Changing field 'Restaurant.address'
        db.alter_column('foodcheck_app_restaurant', 'address', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Violation.description'
        db.alter_column('foodcheck_app_violation', 'description', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Restaurant.name'
        db.alter_column('foodcheck_app_restaurant', 'name', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Restaurant.phone'
        db.alter_column('foodcheck_app_restaurant', 'phone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'Restaurant.state'
        db.alter_column('foodcheck_app_restaurant', 'state', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Restaurant.postal_code'
        db.alter_column('foodcheck_app_restaurant', 'postal_code', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Restaurant.address'
        db.alter_column('foodcheck_app_restaurant', 'address', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Violation.description'
        db.alter_column('foodcheck_app_violation', 'description', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        'foodcheck_app.inspection': {
            'Meta': {'object_name': 'Inspection'},
            'city_business_id': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foodcheck_app.Restaurant']"}),
            'score': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'score_description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        'foodcheck_app.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city_business_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'foodcheck_app.violation': {
            'Meta': {'object_name': 'Violation'},
            'city_business_id': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foodcheck_app.Inspection']"}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'vi_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['foodcheck_app']