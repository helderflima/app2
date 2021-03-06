from django.conf.urls import include, url
from django.contrib import admin
from artigos.feeds import ArtigosRss
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'app2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'artigos.views.index'),
    url(r'^paginacao/(?P<pagina>[^\.]+)', 'artigos.views.index'),
    url(r'^artigo/(?P<url>[^\.]+)', 'artigos.views.artigo'),
    url(r'^form-pesquisa/$', 'artigos.views.form_pesquisa'),
    url(r'^pesquisa/$', 'artigos.views.pesquisa'),
    url(r'^contato', 'artigos.views.contato'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rss/(?P<url>.*)', ArtigosRss()),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^comments/', include('django_comments.urls')),
]
