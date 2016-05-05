from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Skill(models.Model):
    name = models.CharField(max_length=512)
    difficulty = models.IntegerField()
    family = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Developer(models.Model):
    user = models.OneToOneField(User)
    extra_credit_tokens = models.IntegerField
    manager = models.CharField(max_length=30)
    title = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' %(self.user.first_name, self.user.last_name)


class DeveloperSkill(models.Model):
    developer = models.ForeignKey('Developer', on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)
    proficiency = models.CharField(max_length=30)
    years_of_experience = models.IntegerField()

    def __unicode__(self):
        return u'%s %s' % (self.developer.user.first_name + ' ' + self.developer.user.last_name, self.skill)
