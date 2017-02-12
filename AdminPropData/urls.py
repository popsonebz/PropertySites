from django.conf.urls import url, include
from django.conf.urls.static import static

from PropertySite import settings
from propdata import views

urlpatterns = [
                url(r'^$', views.admin, name='admin'),
                url(r'^agent/$', views.agent, name='agent'),
                url(r'^showallagents/$', views.showallagents, name='showallagents'),
                url(r'^addlisting/$', views.addlisting, name='addlisting'),
                url(r'^showlisting/$', views.showlisting, name='showlisting'),
                url(r'^showleads/$', views.showleads, name='showleads'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)