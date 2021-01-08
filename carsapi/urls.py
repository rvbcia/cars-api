from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers

from . import views

# router = routers.DefaultRouter()
# router.register(r'cars', views.car_list)

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls',
    #                           namespace='rest_framework')),
    url(r'^cars/$', views.CarList.as_view()),
    url(r'^rates/$', views.RateView.as_view())
]
