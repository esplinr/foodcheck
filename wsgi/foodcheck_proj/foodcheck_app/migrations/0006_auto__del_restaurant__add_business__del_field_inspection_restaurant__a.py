# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Restaurant'
        db.delete_table('foodcheck_app_restaurant')

        # Adding model 'Business'
        db.create_table('foodcheck_app_business', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city_business_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
        ))
        db.send_create_signal('foodcheck_app', ['Business'])

        # Deleting field 'Inspection.restaurant'
        db.delete_column('foodcheck_app_inspection', 'restaurant_id')

        # Adding field 'Inspection.business'
        db.add_column('foodcheck_app_inspection', 'business',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['foodcheck_app.Business']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Restaurant'
        db.create_table('foodcheck_app_restaurant', (
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city_business_id', self.gf('django.db.models.fields.IntegerField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal('foodcheck_app', ['Restaurant'])

        # Deleting model 'Business'
        db.delete_table('foodcheck_app_business')

        # Adding field 'Inspection.restaurant'
        db.add_column('foodcheck_app_inspection', 'restaurant',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['foodcheck_app.Restaurant']),
                      keep_default=False)

        # Deleting field 'Inspection.business'
        db.delete_column('foodcheck_app_inspection', 'business_id')


    models = {
        'foodcheck_app.business': {
            'Meta': {'object_name': 'Business'},
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
        'foodcheck_app.inspection': {
            'Meta': {'object_name': 'Inspection'},
            'business': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foodcheck_app.Business']"}),
            'city_business_id': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'score': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'score_description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
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