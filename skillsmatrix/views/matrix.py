from django.views.generic import *
from skillsmatrix.models import *


# View file for the homepage
class Matrix(TemplateView):
    template_name = "materialize/matrix_materialize.html"

    def get_context_data(self, **kwargs):
        context = super(Matrix, self).get_context_data()

        context['developer_count'] = Developer.objects.count()
        context['developerskills_count'] = DeveloperSkill.objects.count()

        return context
