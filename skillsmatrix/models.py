from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import date

LOW = 1
MEDIUM = 2
HIGH = 3
PROFICIENCY_CHOICES = (
    (LOW, 'Low'),
    (MEDIUM, 'Medium'),
    (HIGH, 'High')
)


# Skill model
class Skill(models.Model):
    name = models.CharField(max_length=512)
    difficulty = models.IntegerField()
    family = models.CharField(max_length=256)

    def __str__(self):
        return self.name


# Developer model
class Developer(models.Model):
    user = models.OneToOneField(User)
    extra_credit_tokens = models.IntegerField(default=0)
    manager = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, default="phone")
    start_date = models.DateField(default=date.today())
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


# DeveloperSkill model
class DeveloperSkill(models.Model):
    developer = models.ForeignKey('Developer', on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)
    proficiency = models.IntegerField(choices=PROFICIENCY_CHOICES)
    years_of_experience = models.IntegerField()

    def __unicode__(self):
        return u'%s %s' % (self.developer, self.skill)


# ExtraCredit model
class ExtraCredit(models.Model):
    recipient = models.ForeignKey(Developer, related_name='extracredit_recipient')
    sender = models.ForeignKey(Developer, related_name='extracredit_sender')
    skill = models.ForeignKey(Skill, related_name='extracredit_skill')
    description = models.TextField(blank=True, null=True)
    date_credited = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s -> %s %s - %s' % (self.sender.user.first_name, self.recipient.user.last_name, self.recipient.user.first_name, self.recipient.user.last_name, self.skill.name)


# Project model
class Project(models.Model):
    name = models.CharField(max_length=30)
    project_lead = models.ForeignKey('Developer', on_delete=models.CASCADE)
    pi = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.name)


# ProjectSkill model
class ProjectSkill(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.skill.name)


# ProjectDeveloper model
class ProjectDeveloper(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    developer = models.ForeignKey('Developer', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.developer.user.first_name)


