from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.general_list, name='general_list'),
    url(r'^equips/$', views.equip_list, name='equip_list'),
    url(r'^itens/$', views.item_list, name='item_list'),
    url(r'^manufacturer/$', views.fab_list, name='fab_list'),
    url(r'^item/(?P<pk>\d+)$', views.item_detail, name='item_detail'),
    url(r'^equip/(?P<pk>\d+)$', views.equip_detail, name='equip_detail'),
    url(r'^manufacturer/(?P<pk>\d+)$', views.fab_detail, name='fab_detail'),
    url(r'^item/new/$', views.item_new, name='item_new'),
    url(r'^equip/new/$', views.equip_new, name='equip_new'),
    url(r'^manufacturer/new/$', views.fab_new, name='fab_new'),
    url(r'^tipo/new/$', views.tipo_equip_new, name='tipo_equip_new'),
    url(r'^tipo/(?P<pk>\d+)$', views.tipo_equip_detail, name='tipo_equip_detail'),
    url(r'^tipo/item/new/$',views.tipo_item_new, name='tipo_item_new'),
    url(r'tipo/item/(?P<pk>\d+)$', views.tipo_item_detail, name='tipo_item_detail'),
    url(r'tipo/item/(?P<pk>\d+)/edit/$', views.tipo_item_edit, name='tipo_item_edit'),
    url(r'^equip/(?P<pk>\d+)/edit/$', views.equip_edit, name='equip_edit'),
    url(r'^manufacturer/(?P<pk>\d+)/edit/$', views.fab_edit, name='fab_edit'),
    url(r'^item/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
    url(r'^tipo/(?P<pk>\d+)/edit/$', views.tipo_equip_edit, name='tipo_equip_edit'),
]