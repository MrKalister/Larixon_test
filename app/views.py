from django.db.models import F
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from app.models import Advert
from app.serializers import AdvertSerializer


class AdvertView(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet
):
    """
    Provides information about ads.
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
        instance.views = F('views') + 1
        instance.save(update_fields=('views',))
