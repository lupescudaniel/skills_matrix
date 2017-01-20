# View file for Skills pages
from django.views.generic import *
from skillsmatrix.models import Skill, DeveloperSkill
from skillsmatrix.forms.forms import SkillForm
from django.views.generic.edit import FormView


# ListView that lists all of the skills using the skills_list_materialize.html template
class SkillsList(ListView):

    model = Skill
    template_name = 'materialize/skill_list_materialize.html'

    def get_queryset(self):
        q = super(SkillsList, self).get_queryset()
        return q.order_by('name')


class AddSkill(FormView):
    template_name = 'materialize/skill_add_materialize.html'
    form_class = SkillForm
    success_url = '/my_developer_details'

    def form_valid(self, form):
        # Skill.objects.get_or_create()
        print self
        print "============================"
        print form
        Skill.objects.get_or_create(name=form.id_skill.value())

        return super(AddSkill, self).form_valid(form)
