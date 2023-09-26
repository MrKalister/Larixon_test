from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from app.models import Advert
from app.serializers import AdvertSerializer


class AdvertListView(ListAPIView):
    """
    Provides information about Adverts.
    """

    queryset = Advert.objects.select_related('city', 'category')
    serializer_class = AdvertSerializer


class AdvertDetailView(RetrieveAPIView):
    """
    Provides information about Advert.
    """

    queryset = Advert.objects.select_related('city', 'category')
    serializer_class = AdvertSerializer

    def retrieve(self, request, *args, **kwargs) -> Response:
        # Можно через super(), но так бы пришлось дважды вызывать get_object
        instance = self.get_object()
        self.up_views(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def up_views(self, instance: Advert) -> None:
        instance.views = instance.views + 1
        instance.save(update_fields=('views',))
