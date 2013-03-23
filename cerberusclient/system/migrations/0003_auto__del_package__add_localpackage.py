# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Package'
        db.delete_table('system_package')

        # Adding model 'LocalPackage'
        db.create_table('system_localpackage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pid', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('developer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.FilePathField')(max_length=100)),
            ('download_status', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('status', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('system', ['LocalPackage'])


    def backwards(self, orm):
        # Adding model 'Package'
        db.create_table('system_package', (
            ('status', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('download_status', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('location', self.gf('django.db.models.fields.FilePathField')(max_length=100)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pid', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('developer', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('system', ['Package'])

        # Deleting model 'LocalPackage'
        db.delete_table('system_localpackage')


    models = {
        'system.localpackage': {
            'Meta': {'object_name': 'LocalPackage'},
            'developer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'download_status': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.FilePathField', [], {'max_length': '100'}),
            'pid': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'system.message': {
            'Meta': {'object_name': 'Message'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['system']