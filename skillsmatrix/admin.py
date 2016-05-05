from django.contrib import admin
from skillsmatrix.models import Skill, Developer, DeveloperSkill, ExtraCredit


# Skill admin configuration
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'family')
    list_filter = ('difficulty', 'family')

admin.site.register(Skill, SkillAdmin)

# Developer admin configuration
admin.site.register(Developer)


# DeveloperSkills admin configuration
class DeveloperSkillAdmin(admin.ModelAdmin):
    list_display = ('get_developer_user', 'get_skill_name', 'proficiency', 'years_of_experience')
    list_filter = ('skill', 'proficiency', 'years_of_experience')

    def get_developer_user(self, obj):
        return obj.developer.user

    def get_skill_name(self, obj):
        return obj.skill.name

admin.site.register(DeveloperSkill, DeveloperSkillAdmin)

admin.site.register(ExtraCredit)


# ExtraCredit admin configuration