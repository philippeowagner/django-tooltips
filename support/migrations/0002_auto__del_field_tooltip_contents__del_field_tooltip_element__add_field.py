# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Tooltip.contents'
        db.delete_column(u'help_tooltip', 'contents')

        # Deleting field 'Tooltip.element'
        db.delete_column(u'help_tooltip', 'element')

        # Adding field 'Tooltip.selector'
        db.add_column(u'help_tooltip', 'selector',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Tooltip.contents'
        raise RuntimeError("Cannot reverse this migration. 'Tooltip.contents' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Tooltip.contents'
        db.add_column(u'help_tooltip', 'contents',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)

        # Adding field 'Tooltip.element'
        db.add_column(u'help_tooltip', 'element',
                      self.gf('django.db.models.fields.CharField')(default='span', max_length=50),
                      keep_default=False)

        # Deleting field 'Tooltip.selector'
        db.delete_column(u'help_tooltip', 'selector')


    models = {
        u'help.tooltip': {
            'Meta': {'object_name': 'Tooltip'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'selector': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['help']