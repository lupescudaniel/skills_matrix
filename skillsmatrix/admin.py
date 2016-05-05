from django.contrib import admin
from skillsmatrix.models import Skill, Developer, DeveloperSkill


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'family', )
    list_filter = ('difficulty', 'family', )

class DeveloperSkillAdmin(admin.ModelAdmin):
    list_display = ('developer', 'skill', 'proficiency', 'years_of_experience')
    list_filter = ('skill', 'proficiency', 'years_of_experience')

    def get_developer_name(self, obj):
        return obj.developer.

admin.site.register(Skill, SkillAdmin)

admin.site.register(Developer)

admin.site.register(DeveloperSkill, DeveloperSkillAdmin)