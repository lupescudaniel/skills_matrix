from django.contrib import admin
from skillsmatrix.models import Skill, Developer

# Skill admin configuration
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'family', )
    list_filter = ('difficulty', 'family', )

admin.site.register(Skill, SkillAdmin)

# Developer admin configuration
admin.site.register(Developer)

# DeveloperSkills admin configuration


# ExtraCredit admin configuration
