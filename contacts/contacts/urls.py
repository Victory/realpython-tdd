from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from user_contacts import views as uc_views


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', uc_views.home),
    url(r'^all/$', uc_views.all_contacts),
    url(r'^add/$', uc_views.add_contact),
    url(r'^create$', uc_views.create),
)
