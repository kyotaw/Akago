from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter

from sakuya.photos.models import Photo
from sakuya.photos.serializers import PhotoSerializer


class PhotoRouter(ModelRouter):
    route_name = 'photo-router'
    serializer_class = PhotoSerializer
    model = Photo

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.filter(owner__id=kwargs['owner_id'])

route_handler.register(PhotoRouter)
