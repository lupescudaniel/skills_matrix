from django.contrib import admin
from skillsmatrix.models import Skill, Developer, DeveloperSkill

# Skill admin configuration
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'family', )
    list_filter = ('difficulty', 'family', )

class DeveloperSkillAdmin(admin.ModelAdmin):
    list_display = ('developer', 'skill', 'proficiency', 'years_of_experience')
    list_filter = ('skill', 'proficiency', 'years_of_experience')

    def get_developer_name(self, obj):
        return obj.developer.

admin.site.register(Skill, SkillAdmin)

# Developer admin configuration
admin.site.register(Developer)

# DeveloperSkills admin configuration


# ExtraCredit admin configuration


admin.site.register(DeveloperSkill, DeveloperSkillAdmin)