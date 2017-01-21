# View file for Skills pages
from django import forms
from django.views.generic import *
from skillsmatrix.models import Skill, DeveloperSkill, Developer

from django.views.generic.edit import CreateView


# ListView that lists all of the skills using the skills_list_materialize.html template
class SkillsList(ListView):

    model = Skill
    template_name = 'materialize/skill_list_materialize.html'

    def get_queryset(self):
        q = super(SkillsList, self).get_queryset()
        return q.order_by('name')


class AddSkill(CreateView):
    model = DeveloperSkill
    template_name = 'materialize/skill_add_materialize.html'
    success_url = '/my_developer_details'
    fields = '__all__'

    def get_form(self, form_class=None):
        form = super(AddSkill, self).get_form()
        form.fields['developer'].widget = forms.HiddenInput()

        return form

    def get_initial(self):
        initial = super(AddSkill, self).get_initial()
        initial['developer'] = Developer.objects.get(user=self.request.user)
        print(self.request.user)
        return initial
