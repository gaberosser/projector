# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Videos'
        db.create_table(u'projector_videos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=256)),
            ('series_no', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('episode_no', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('media_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projector.FileType'], null=True, blank=True)),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projector.Genre'], null=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'projector', ['Videos'])

        # Adding model 'FileType'
        db.create_table(u'projector_filetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'projector', ['FileType'])

        # Adding model 'Genre'
        db.create_table(u'projector_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'projector', ['Genre'])


    def backwards(self, orm):
        # Deleting model 'Videos'
        db.delete_table(u'projector_videos')

        # Deleting model 'FileType'
        db.delete_table(u'projector_filetype')

        # Deleting model 'Genre'
        db.delete_table(u'projector_genre')


    models = {
        u'projector.filetype': {
            'Meta': {'object_name': 'FileType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'projector.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'projector.videos': {
            'Meta': {'object_name': 'Videos'},
            'episode_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projector.Genre']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projector.FileType']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'}),
            'series_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['projector']