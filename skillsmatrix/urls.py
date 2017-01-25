"""skillsmatrix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from skillsmatrix.views.home import *
from skillsmatrix.views.developer import *
from skillsmatrix.views.matrix import *
from skillsmatrix.views.skills import *

urlpatterns = [
    url(r'^$', Home.as_view(), name='home_page'),
    url(r'^developers/$', DeveloperList.as_view(), name="developer_list"),
    url(r'^developers/(?P<manager>\w+)/$', DeveloperListByManager.as_view()),
    url(r'^developer_detail/(?P<pk>\d+)/$', DeveloperDetail.as_view(), name="developer_detail"),
    url(r'^my_developer_details/$', DeveloperDetailMe.as_view(), name="my_developer_details"),
    url(r'^developer/(?P<pk>\d+)/update/$', DeveloperUpdate.as_view(), name="developer_update"),
    url(r'^skills/$', SkillsList.as_view(), name="skills_list"),
    url(r'^skills/(?P<skill_id>\d+)/$', DeveloperListBySkill.as_view(), name='developer_list_by_skill'),
    url(r'^skills/add/$', AddSkill.as_view(), name='add_skill'),
    url(r'^matrix/$', Matrix.as_view(), name='matrix'),
    url(r'^matrix/filter-matrix/$', FilterMatrix, name='filter_matrix')
]
