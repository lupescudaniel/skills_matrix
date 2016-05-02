from django.contrib import admin

# Register your models here.
from .models import Developer, DeveloperSkill, Skill, ExtraCredit

admin.site.register(Developer)
admin.site.register(DeveloperSkill)
admin.site.register(Skill)
admin.site.register(ExtraCredit)
