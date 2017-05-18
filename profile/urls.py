# -*- coding: utf-8 -*-
from django.conf.urls import url

from profile import views


urlpatterns = [

    url(r'^profile/$', views.profile_detail_view, name='profile'),

]
