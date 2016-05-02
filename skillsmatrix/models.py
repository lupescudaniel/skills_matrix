from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Extend user model
    title = models.CharField(max_length=100) #Associate Research Programmer, etc.
    manager = models.CharField(max_length=100) #Dave, Alex, Caleb
    extra_credit_tokens = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username

class Skill(models.Model):
    name = models.CharField(max_length=100) #AngularJS, Django, PostgreSQL, Apache 2.4, Nginx, etc
    family = models.CharField(max_length=100) #Frontend, backend, server admin, database
    difficulty = models.IntegerField(default=0) #0 = Easy, 1 = Moderate, 2 = Difficult, 3 = Good Luck

    def __unicode__(self):
        return self.name

class DeveloperSkill(models.Model):
    developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='+')
    years_of_experience = models.IntegerField(default=0)
    proficiency = models.CharField(max_length=100)

    def __unicode__(self):
        return self.developer.username + ' : ' + self.skill.name

class ExtraCredit(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='+')
    description = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.sender.username + ' --> ' + self.recipient.username + ' (' + self.skill.name + ')'






