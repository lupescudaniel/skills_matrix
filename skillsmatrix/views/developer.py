# View file for developer pages

from django.views.generic import *
from skillsmatrix.models import *

class DeveloperList(ListView):
    model = Developer
    template_name = "developer_list.html"


class DeveloperListByManager(DeveloperList):
    def get_queryset(self):
        return super(DeveloperListByManager, self).get_queryset().filter(manager=self.kwargs['manager'])


class DeveloperDetail(DetailView):
    model = Developer
    template_name = "developer_detail.html"

    def get_context_data(self, **kwargs):
        c = super(DeveloperDetail, self).get_context_data()
        c['skills'] = DeveloperSkill.objects.filter(developer=self.object).order_by('-years_of_experience')
        return c



