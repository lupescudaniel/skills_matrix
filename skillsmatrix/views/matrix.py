from django.views.generic import *
from skillsmatrix.models import *
from django.core.exceptions import ObjectDoesNotExist

# View file for the homepage
class Matrix(TemplateView):
    template_name = "materialize/matrix_materialize.html"

    def get_context_data(self, **kwargs):
        context = super(Matrix, self).get_context_data()

        dev_list = Developer.objects.filter().values('id', 'user__first_name', 'user__last_name')
        skill_list = Skill.objects.filter().values('id', 'name')

        # Get list of dev names for x categories
        devs = []
        for dev in dev_list:
            d = str(dev['user__first_name']) + ' ' + str(dev['user__last_name'])
            devs.append(d)
        devs.sort()

        # Get list of skills for y categories
        skills = []
        for skill in skill_list:
            s = str(skill['name'])
            skills.append(s)
        skills.sort()

        # Get list of each developer skill -
        # must be format [index of dev in devs, index of skill in skills, proficiency]
        devskill_list = DeveloperSkill.objects.filter()
        devskills = []

        for ds in devskill_list:
            # Get developer index
            dev_name = str(ds.developer.user.first_name) + " " + str(ds.developer.user.last_name)
            dev_index = devs.index(dev_name)

            # Get skill index
            skill_name = str(ds.skill.name)
            skill_index = skills.index(skill_name)

            # create list
            item = [dev_index, skill_index, ds.proficiency]
            devskills.append(item)

        # Loop through each developer
        for dev in dev_list:
            print(dev)
            # Loop through each skill
            for skill in skill_list:
                print(skill['name'])
                try:
                    DeveloperSkill.objects.get(developer=dev['id'], skill=skill['id'])
                except ObjectDoesNotExist:
                    dev_name = str(dev['user__first_name']) + " " + str(dev['user__last_name'])
                    dev_index = devs.index(dev_name)

                    # Get skill index
                    skill_name = str(skill['name'])
                    skill_index = skills.index(skill_name)

                    no_skill_item = [dev_index, skill_index, 0]
                    devskills.append(no_skill_item)
                    devskills.sort()

        context = {
            'developers': devs,
            'skills': skills,
            'devskills': devskills
        }
        print(context)
        return context
