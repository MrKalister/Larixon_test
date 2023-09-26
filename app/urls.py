from django.urls import path

from app.views import AdvertDetailView, AdvertListView

urlpatterns = [
    path(
        'advert-list/',
        AdvertListView.as_view(),
        name='advert-list',
    ),
    path(
        'advert/<int:pk>/',
        AdvertDetailView.as_view(),
        name='advert-detail',
    ),
]
