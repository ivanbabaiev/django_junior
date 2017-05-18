# -*- coding: utf-8 -*-
from django.conf.urls import url

from html_test.views import questions_detail_view


urlpatterns = [

    url(r'results/$', questions_detail_view, name='profile'),

]
