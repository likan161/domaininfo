from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.get_form, name='get_form'),
            url('answer', views.get_form, name='get_form '),
            #url('email', views.get_form, name='email '),
            ]
