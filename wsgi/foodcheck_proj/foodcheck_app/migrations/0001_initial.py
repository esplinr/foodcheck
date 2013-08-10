# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Restaurant'
        db.create_table('foodcheck_app_restaurant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city_business_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('postal_code', self.gf('django.db.models.fields.IntegerField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('foodcheck_app', ['Restaurant'])

        # Adding model 'Inspection'
        db.create_table('foodcheck_app_inspection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city_business_id', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('foodcheck_app', ['Inspection'])

        # Adding model 'Violation'
        db.create_table('foodcheck_app_violation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city_business_id', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('vi_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('severity', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('foodcheck_app', ['Violation'])


    def backwards(self, orm):
        # Deleting model 'Restaurant'
        db.delete_table('foodcheck_app_restaurant')

        # Deleting model 'Inspection'
        db.delete_table('foodcheck_app_inspection')

        # Deleting model 'Violation'
        db.delete_table('foodcheck_app_violation')


    models = {
        'foodcheck_app.inspection': {
            'Meta': {'object_name': 'Inspection'},
            'city_business_id': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'score': ('django.db.models.fields.IntegerField', [], {})
        },
        'foodcheck_app.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city_business_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'postal_code': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'foodcheck_app.violation': {
            'Meta': {'object_name': 'Violation'},
            'city_business_id': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'vi_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['foodcheck_app']

