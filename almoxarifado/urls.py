from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.general_list, name='general_list'),
    url(r'^equips/$', views.equip_list, name='equip_list'),
    url(r'^itens/$', views.item_list, name='item_list'),
    url(r'^item/(?P<pk>\d+)$', views.item_detail, name='item_detail'),
    url(r'^equip/(?P<pk>\d+)$', views.equip_detail, name='equip_detail'),
    url(r'^equip/new/$', views.item_new, name='item_new'),
    url(r'^equip/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
]