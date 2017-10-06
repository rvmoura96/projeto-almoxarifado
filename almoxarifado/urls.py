from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.equip_list, name='equip_list'),
    url(r'^equip/(?P<pk>\d+)$', views.equip_detail, name='equip_detail'),
    url(r'^equip/new/$', views.item_new, name='item_new'),
    url(r'^equip/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
]