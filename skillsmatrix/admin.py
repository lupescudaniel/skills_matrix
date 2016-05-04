from django.contrib import admin
from skillsmatrix.models import Skill, Developer


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'family', )
    list_filter = ('difficulty', 'family', )

admin.site.register(Skill, SkillAdmin)

admin.site.register(Developer)