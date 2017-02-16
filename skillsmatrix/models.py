from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

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
    description = models.TextField(default="")
    skill_url = models.CharField(max_length=512, default="")

    def __str__(self):
        return self.name


# Developer model
class Developer(models.Model):
    user = models.OneToOneField(User)
    manager = models.CharField(max_length=512)
    title = models.CharField(max_length=512)
    phone = models.CharField(max_length=512, default="phone", blank=True, null=True)
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

    def get_proficiency_string(self):
        proficiency_string = ""
        if self.proficiency == 1:
            proficiency_string = "Low"
        elif self.proficiency == 2:
            proficiency_string = "Medium"
        elif self.proficiency == 3:
            proficiency_string = "High"
        return proficiency_string

    def validate_unique(self, exclude=None):
        '''
        Check if the developer has already added this skill.
        '''
        qs = DeveloperSkill.objects.filter(developer=self.developer, skill=self.skill)
        if qs:
            raise ValidationError('You already added this skill.')

    def save(self, *args, **kwargs):
        self.validate_unique()

        super(DeveloperSkill, self).save(*args, **kwargs)


# Project model
class Project(models.Model):
    name = models.CharField(max_length=512)
    project_lead = models.ForeignKey('Developer', on_delete=models.CASCADE)
    pi = models.CharField(max_length=512)

    def __str__(self):
        return '%s' % self.name


# ProjectSkill model
class ProjectSkill(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.skill.name


# ProjectDeveloper model
class ProjectDeveloper(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    developer = models.ForeignKey('Developer', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % self.developer.user.first_name


