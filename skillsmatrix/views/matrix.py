from django.views.generic import *
from skillsmatrix.models import *
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import json


# View file for the homepage
class Matrix(TemplateView):
    template_name = "materialize/matrix_materialize.html"

    def get_context_data(self, **kwargs):
        context = super(Matrix, self).get_context_data()

        dev_list = Developer.objects.filter().values('id', 'user__first_name', 'user__last_name')
        skill_list = Skill.objects.filter().values('id', 'name')

        # Get list of dev names for x categories
        devs = []
        dev_filter_list = []
        for dev in dev_list:
            d = str(dev['user__first_name']) + ' ' + str(dev['user__last_name'])
            devs.append(d)
            str_dev = {
                'first_name': str(dev['user__first_name']),
                'last_name': str(dev['user__last_name']),
                'id': dev['id']
            }
            dev_filter_list.append(str_dev)
        devs.sort()
        dev_filter_list = sorted(dev_filter_list, key=lambda k: k['first_name'])

        # Get list of skills for y categories
        skills = []
        for skill in skill_list:
            s = str(skill['name'])
            skills.append(s)
        skills.sort()

        # Get list of each developer skill -
        # must be format [index of dev in devs, index of skill in skills, proficiency]
        devskills = []

        # Loop through each developer
        for dev in dev_list:
            # Loop through each skill
            for skill in skill_list:
                dev_name = str(dev['user__first_name']) + " " + str(dev['user__last_name'])
                dev_index = devs.index(dev_name)

                # Get skill index
                skill_name = str(skill['name'])
                skill_index = skills.index(skill_name)

                try:
                    devskill = DeveloperSkill.objects.get(developer=dev['id'], skill=skill['id'])

                    if devskill.has_skill:
                        if devskill.proficiency == None:
                            devskill.proficiency = 0
                        dskill = [dev_index, skill_index, devskill.proficiency]

                    else:
                        dskill = [dev_index, skill_index, 0]
                    devskills.append(dskill)
                except:
                    pass

        devskills.sort()

        managers = Developer.objects.filter(is_manager=True)

        context = {
            'dev_filter_list': dev_filter_list,
            'developers': devs,
            'skills': skills,
            'devskills': devskills,
            'managers': managers
        }

        return context


def FilterMatrix(request):
    dev_ids = request.GET.getlist('devs[]') # IDs of the selected developers
    skill_names = request.GET.getlist('skills[]')# Names of the selected skills

    dev_list = Developer.objects.filter(id__in=dev_ids).values('id', 'user__first_name', 'user__last_name')
    skill_list = Skill.objects.filter(name__in=skill_names).values('id', 'name')

    # Get a list of the full names of the developers and sort alphabetically
    dev_names = []
    for dev in dev_list:
        d = str(dev['user__first_name']) + " " + str(dev['user__last_name'])
        dev_names.append(d)
    dev_names.sort()

    # Get a list of the names of the skills and sort alphabetically
    skill_names = []
    for s in skill_list:
        skill_names.append(str(s['name']))
    skill_names.sort()

    # Get list of each developer skill -
    # must be format [index of dev in devs, index of skill in skills, proficiency]
    devskills = []

    for dev in dev_list:
        # Loop through each skill
        for skill in skill_list:
            dev_name = str(dev['user__first_name']) + " " + str(dev['user__last_name'])
            dev_index = dev_names.index(dev_name)

            # Get skill index
            skill_name = str(skill['name'])
            skill_index = skill_names.index(skill_name)

            try:
                devskill = DeveloperSkill.objects.get(developer=dev['id'], skill=skill['id'])
                if devskill.has_skill:
                    dskill = [dev_index, skill_index, devskill.proficiency]

                else:
                    dskill = [dev_index, skill_index, 0]
                devskills.append(dskill)

            except:
                pass

        devskills.sort()

    data = {
        "dev_names": dev_names,
        "skill_names": skill_names,
        "dev_skills": devskills
    }

    return HttpResponse(json.dumps(data), content_type='application/json')
