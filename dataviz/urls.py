from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.upload, name='upload'),
    url(r'^data$', views.data, name='data'),
    url(r'^plot$', views.plot, name='plot'),
]
