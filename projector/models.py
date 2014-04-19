__author__ = 'gabriel'
from django.db import models

class Drive(models.Model):
    name = models.CharField(max_length=256)
    path = models.CharField(max_length=256, unique=True)
    series_no = models.IntegerField(null=True, blank=True)
    episode_no = models.IntegerField(null=True, blank=True)
    media_type = models.ForeignKey('FileType', null=True, blank=True)
    genre = models.ForeignKey('Genre', null=True, blank=True)


class FileType(models.Model):
    name = models.CharField(max_length=128)


class Genre(models.Model):
    name = models.CharField(max_length=128)