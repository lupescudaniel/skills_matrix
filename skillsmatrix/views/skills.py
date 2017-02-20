# View file for Skills pages
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic import *
from django.views.decorators.http import require_http_methods

from skillsmatrix.models import Skill, DeveloperSkill, Developer

from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
import json

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

        skill_families = Skill.objects.filter().values_list('family')
        skill_families_list = []
        for s in skill_families:
            skill_families_list.append(str(s[0]))
        skill_family_unique = list(set(skill_families_list))

        all_dev_skills = DeveloperSkill.objects.filter(developer__user=self.request.user)

        context['my_skills'] = all_dev_skills
        context['skill_family_list'] = skill_family_unique
        context['skill_action'] = "Add"
        context['skill_name'] = "Skill"
        return context


@login_required
@require_http_methods(["POST"])
def bulk_update_skill_view(request):
    response_data = {}
    for skill in json.loads(request.POST.get('skills_list', [])):
        devskill = DeveloperSkill.objects.get(id=skill[u'id'], developer__user=request.user)
        devskill.has_skill = skill[u'has_skill']
        if not devskill.has_skill:
            devskill.proficiency = None
            devskill.years_of_experience = 0
        else:
            devskill.proficiency = skill[u'proficiency']
            devskill.years_of_experience = skill[u'years_of_experience']
        devskill.save()
    response_data['success'] = True
    return HttpResponse(json.dumps(response_data), content_type='application/json')
