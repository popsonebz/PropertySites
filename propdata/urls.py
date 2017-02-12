from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from . import views

urlpatterns = [
                url(r'^$', views.home, name='home'),  # default url to call on visiting the website
                url(r'^search/$', views.search, name='search'),  # Url to be called when performing a search
                url(r'^search/(?P<pk>\d+)/$', views.detail, name='detail'),  # Url to be called on clicking a picture for more details after the search
              ]