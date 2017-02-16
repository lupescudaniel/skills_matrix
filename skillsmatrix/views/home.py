from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import *
from skillsmatrix.models import *


#View file for the homepage
class Home(LoginRequiredMixin, TemplateView):
    template_name = "materialize/base_materialize.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data()

        context['developer_count'] = Developer.objects.count()
        context['developerskills_count'] = DeveloperSkill.objects.count()

        is_dev = False
        try:
            dev = Developer.objects.filter(user=self.request.user)
            if dev:
                is_dev = True
        except ObjectDoesNotExist:
            is_dev = False

        context['is_developer'] = is_dev

        return context


class ScrumResourcesView(TemplateView):
    template_name = "materialize/scrum_resources.html"
