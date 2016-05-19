from django.views.generic import DetailView, ListView
from skillsmatrix.models import *
from django.utils import timezone

class DeveloperList(ListView):
    template_name = 'developer_list.html'
    model = Developer

    def get_queryset(self):
        qs = super(DeveloperList, self).get_queryset()

        if self.kwargs['manager']:
            return qs.filter(manager=self.kwargs['manager'])
        else:
            return qs

class DeveloperDetail(DetailView):
    model = Developer
    template_name = 'developer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DeveloperDetail, self).get_context_data(**kwargs)
        context['skills'] = DeveloperSkill.objects.filter(developer_id=self.kwargs['pk'])
        return context
