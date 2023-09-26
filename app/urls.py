from django.urls import path

from .views import AdvertView

urlpatterns = [
    path(
        'advert-list/',
        AdvertView.as_view({'get': 'list'}),
        name='advert-list',
    ),
    path(
        'advert/<int:pk>/',
        AdvertView.as_view({'get': 'retrieve'}),
        name='advert-detail',
    ),
]
