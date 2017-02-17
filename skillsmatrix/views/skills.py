# View file for Skills pages
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.views.generic import *
from django.forms import modelformset_factory

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

    def get_context_data(self, **kwargs):
        context = super(AddSkill, self).get_context_data()
        context['skill_action'] = "Add"
        context['skill_name'] = "Skill"
        return context


class EditSkill(UpdateView):
    model = DeveloperSkill
    template_name = 'materialize/skill_add_materialize.html'
    success_url = '/my_developer_details'
    fields = '__all__'

    def get_form(self, form_class=None):
        form = super(EditSkill, self).get_form()
        form.fields['developer'].widget = forms.HiddenInput()
        form.fields['skill'].widget = forms.HiddenInput()

        return form

    def get_object(self, queryset=None):
        try:
            obj = DeveloperSkill.objects.get(id=self.kwargs['skill_id'])
            return obj
        except ObjectDoesNotExist:
            raise Http404("No object found matching this query")

    def get_context_data(self, **kwargs):
        context = super(EditSkill, self).get_context_data()
        context['skill_action'] = "Edit"
        context['skill_name'] = str(DeveloperSkill.objects.get(id=self.kwargs['skill_id']).skill.name) + " Skill"

        return context


class BulkAddSkills(TemplateView):
    template_name = 'materialize/bulk_add_skills.html'

    def get_context_data(self, **kwargs):
        context = super(BulkAddSkills, self).get_context_data()

        DevSkillFormSet = modelformset_factory(DeveloperSkill, fields=('skill', 'has_skill', 'proficiency', 'developer'))
        formset = DevSkillFormSet(queryset=DeveloperSkill.objects.filter(developer__user=self.request.user))

        print(formset)

        context['formset'] = formset
        context['skill_action'] = "Add"
        context['skill_name'] = "Skill"
        return context

    # def get_queryset(self):
    #     return super(BulkAddSkills, self).get_queryset().filter(developer__user=self.request.user)
