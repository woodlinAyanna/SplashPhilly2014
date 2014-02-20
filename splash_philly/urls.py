from django.conf.urls import patterns, include, url
from splash_philly import views,settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'splash_philly.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^map$', views.MapView.as_view(),name='map'),
)
