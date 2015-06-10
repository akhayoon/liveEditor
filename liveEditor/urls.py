from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'liveEditor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^edit$', 'editor.views.displayEditor'),
    url(r'^save$', 'editor.views.saveData'),
    url(r'^render$', 'editor.views.render'),
)
