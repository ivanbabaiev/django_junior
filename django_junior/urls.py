from django.conf.urls import url, include
from django.contrib import admin

from django_junior.views import index


handler404 = 'django_junior.views.custom_404_server_error'
handler500 = 'django_junior.views.custom_500_server_error'


urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^html_test/', include('html_test.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profile/', include('profile.urls')),

    url(r'^admin/', include(admin.site.urls), name="admin"),
]
