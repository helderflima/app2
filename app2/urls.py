from django.conf.urls import include, url
from django.contrib import admin
from app2.views import ola, data_atual

urlpatterns = [
    # Examples:
    # url(r'^$', 'app2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', ola),
    url(r'^ola/$', ola),
    url(r'^data_atual/$', data_atual),
    url(r'^admin/', include(admin.site.urls)),
]
