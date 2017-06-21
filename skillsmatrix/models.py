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
    difficulty = models.IntegerField(blank=True, null=True)
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
    phone = models.CharField(max_length=512, default="(###) ###-####", blank=True, null=True)
    is_manager = models.BooleanField(default=False)
    extra_credit_tokens = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


# DeveloperSkill model
class DeveloperSkill(models.Model):
    developer = models.ForeignKey('Developer', on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)
    proficiency = models.IntegerField(choices=PROFICIENCY_CHOICES, blank=True, null=True)
    years_of_experience = models.IntegerField(blank=True, null=True)
    has_skill = models.BooleanField(default=False)

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

    # def validate_unique(self, exclude=None):
    #     '''
    #     Check if the developer has already added this skill.
    #     '''
    #     qs = DeveloperSkill.objects.filter(developer=self.developer, skill=self.skill)
    #     if qs:
    #         raise ValidationError('You already added this skill.')
    #
    # def save(self, *args, **kwargs):
    #     self.validate_unique()
    #
    #     super(DeveloperSkill, self).save(*args, **kwargs)


# ExtraCredit model
class ExtraCredit(models.Model):
    recipient = models.ForeignKey(Developer, related_name='extracredit_recipient')
    sender = models.ForeignKey(Developer, related_name='extracredit_sender')
    skill = models.ForeignKey(Skill, related_name='extracredit_skill')
    description = models.TextField(blank=True, null=True)
    date_credited = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s -> %s %s - %s' % (self.sender.user.first_name, self.sender.user.last_name, self.recipient.user.first_name, self.recipient.user.last_name, self.skill.name)


