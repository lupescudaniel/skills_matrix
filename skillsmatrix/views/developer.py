# View file for developer pages
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic import *

from skillsmatrix.models import Developer, DeveloperSkill, Skill, ExtraCredit


# ListView that lists all of the developers by using the developer_list.html template
class DeveloperList(ListView):
    model = Developer
    template_name = 'materialize/developer_list_materialize.html'

    def get_queryset(self):
        q = super(DeveloperList, self).get_queryset()
        return q.order_by('user__last_name')


# ListView that inherits from DeveloperList but uses a url parameter to only show the list of developers that have the
# manager passed in on the url
class DeveloperListByManager(DeveloperList):
    def get_queryset(self):
        q = super(DeveloperListByManager, self).get_queryset()
        return q.filter(manager=self.kwargs['manager'])


# DetailView of a single developer
class DeveloperDetail(DetailView):
    model = Developer
    template_name = 'materialize/developer_detail_materialize.html'

    def get_context_data(self, **kwargs):
        context = super(DeveloperDetail, self).get_context_data(**kwargs)
        devskill_list = DeveloperSkill.objects.filter(developer=self.object, has_skill=True).order_by('-years_of_experience')
        extracredit_list = ExtraCredit.objects.filter(recipient=self.object).order_by('date_credited')
        context['extracredits'] = extracredit_list
        context['skills'] = devskill_list
        context['isCurrentUser'] = False
        return context


# DetailView of current logged in user
class DeveloperDetailMe(LoginRequiredMixin, UserPassesTestMixin, DeveloperDetail):
    def test_func(self):
        dev = Developer.objects.filter(user=self.request.user)
        if dev:
            return True
        else:
            raise PermissionDenied

    def get_object(self):
        return Developer.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(DeveloperDetail, self).get_context_data()
        devskill_list = DeveloperSkill.objects.filter(developer=self.object, has_skill=True).order_by('-years_of_experience')
        context['skills'] = devskill_list
        context['isCurrentUser'] = True
        return context


# UpdateView that uses the developer_update.html template to update a developer's title
class DeveloperUpdate(UpdateView):
    model = Developer
    template_name = 'developer_update.html'
    fields = ['title']

    def form_valid(self, form):
        return super(DeveloperUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('developer_detail', kwargs={'pk': self.object.id})


# ListView that inherits from DeveloperList but uses a url parameter to only show the list of developers that have
# the skill passed in on the url
class DeveloperListBySkill(ListView):
    model = DeveloperSkill
    template_name = 'materialize/developer_list_by_skill_materialize.html'

    def get_queryset(self):
        q = super(DeveloperListBySkill, self).get_queryset()
        return q.filter(skill_id=self.kwargs['skill_id'], has_skill=True)

    def get_context_data(self, **kwargs):
        context = super(DeveloperListBySkill, self).get_context_data()
        skill_id = self.kwargs['skill_id']
        skill_obj = Skill.objects.get(id=skill_id)
        context['skill_name'] = skill_obj.name
        context['skill_object'] = skill_obj
        return context


class CreateExtraCredit(CreateView):
    model = ExtraCredit
    template_name = "materialize/extracredit_create_materialize.html"
    success_url = '/extracredit_sent'
    fields = '__all__'

    def get_form(self, form_class=None):
        form = super(CreateExtraCredit, self).get_form()
        form.fields['recipient'].queryset = Developer.objects.exclude(user=self.request.user)
        form.fields['sender'].widget = forms.HiddenInput()
        return form

    def get_initial(self):
        initial = super(CreateExtraCredit, self).get_initial()
        initial['sender'] = Developer.objects.get(user=self.request.user)

        return initial

    def get_context_data(self, **kwargs):
        context = super(CreateExtraCredit, self).get_context_data(**kwargs)
        me = Developer.objects.get(user=self.request.user)
        context['my_tokens'] = me.extra_credit_tokens
        return context

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        # Check that the user has tokens available to send extra credit
        me = Developer.objects.get(user=self.request.user)
        if me.extra_credit_tokens <= 0:
            form.add_error(None, "You do not have any extra credit tokens!")
            return self.form_invalid(form=form)

        # Save the form
        self.object = form.save()

        # Decrement the sender's tokens
        me = Developer.objects.get(user=self.request.user)
        me.extra_credit_tokens -= 1
        me.save()
        # if object successfully saved
        return HttpResponseRedirect(self.get_success_url())


class ExtraCreditSent(TemplateView):
    template_name = "materialize/extracredit_sent.html"

    def get_context_data(self, **kwargs):
        context = super(ExtraCreditSent, self).get_context_data()
        me = Developer.objects.get(user=self.request.user)
        context['my_tokens'] = me.extra_credit_tokens
        return context
