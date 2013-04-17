# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Package.installed'
        db.add_column('marketplace_package', 'installed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Package.installed'
        db.delete_column('marketplace_package', 'installed')


    models = {
        'marketplace.package': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Package'},
            'developer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'download_status': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.FilePathField', [], {'max_length': '100'}),
            'pid': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['marketplace']