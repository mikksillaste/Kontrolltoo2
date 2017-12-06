from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/data$', views.get_soogikohad, name='api-data'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindaeelroad1/$', views.hindaEelroad1, name='hindaeelroad1'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindaeelroad2/$', views.hindaEelroad1, name='hindaeelroad2'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindaeelroad3/$', views.hindaEelroad1, name='hindaeelroad3'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindaeelroad4/$', views.hindaEelroad1, name='hindaeelroad4'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindaeelroad5/$', views.hindaEelroad1, name='hindaeelroad5'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindasupid1/$', views.hindasupid1, name='hindasupid1'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindasupid2/$', views.hindasupid2, name='hindasupid2'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindasupid3/$', views.hindasupid3, name='hindasupid3'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindasupid4/$', views.hindasupid4, name='hindasupid4'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindasupid5/$', views.hindasupid5, name='hindasupid5'),

    url(r'^(?P<soogikoha_id>[0-9]+)/hindapraed1/$', views.hindapraed1, name='hindapraed1'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindapraed2/$', views.hindapraed2, name='hindapraed2'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindapraed3/$', views.hindapraed3, name='hindapraed3'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindapraed4/$', views.hindapraed4, name='hindapraed4'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindapraed5/$', views.hindapraed5, name='hindapraed5'),

    url(r'^(?P<soogikoha_id>[0-9]+)/hindamagus1/$', views.hindamagus1, name='hindamagus1'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindamagus2/$', views.hindamagus2, name='hindamagus2'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindamagus3/$', views.hindamagus3, name='hindamagus3'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindamagus4/$', views.hindamagus4, name='hindamagus4'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindamagus5/$', views.hindamagus5, name='hindamagus5'),

    url(r'^(?P<soogikoha_id>[0-9]+)/hindajoogid1/$', views.hindajoogid1, name='hindajoogid1'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindajoogid2/$', views.hindajoogid2, name='hindajoogid2'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindajoogid3/$', views.hindajoogid3, name='hindajoogid3'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindajoogid4/$', views.hindajoogid4, name='hindajoogid4'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindajoogid5/$', views.hindajoogid5, name='hindajoogid5'),

    url(r'^(?P<soogikoha_id>[0-9]+)/hindakohv1/$', views.hindakohv1, name='hindakohv1'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindakohv2/$', views.hindakohv2, name='hindakohv2'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindakohv3/$', views.hindakohv3, name='hindakohv3'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindakohv4/$', views.hindakohv4, name='hindakohv4'),
    url(r'^(?P<soogikoha_id>[0-9]+)/hindakohv5/$', views.hindakohv5, name='hindakohv5'),
]