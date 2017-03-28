from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^content/$', 'cms.views.barra'),
    url(r'^content/create/(.*)/(.*)', 'cms.views.createPage'),
    url(r'^content/(.*)', 'cms.views.searchContent'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'(.*)', 'cms.views.error'),
)
