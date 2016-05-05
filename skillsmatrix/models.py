from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Skill model
class Skill(models.Model):
    name = models.CharField(max_length=512)
    difficulty = models.IntegerField()
    family = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

# Developer model
class Developer(models.Model):
    user = models.OneToOneField(User)
    extra_credit_tokens = models.IntegerField
    manager = models.CharField(max_length=30)
    title = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' %(self.user.first_name, self.user.last_name)
        
# DeveloperSkill model


# ExtraCredit model
