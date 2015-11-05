from swampdragon.serializers.model_serializer import ModelSerializer


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = 'photos.Photo'
        publish_fields = ('title', 'image', 'audio', 'movie', 'date', 'age', 'comment', 'owner', 'stamp', 'footer', 'motion')
        update_fields = ('title', 'image', 'audio', 'movie', 'date', 'age', 'comment', 'owner', 'stamp', 'footer', 'motion')

    def serialize_image(self, obj):
        return obj.image.url if obj.image else ''

    def serialize_audio(self, obj):
        return 'media/' + obj.audio.url if obj.audio else ''
    
    def serialize_movie(self, obj):
        return obj.movie.url if obj.movie else ''
    
    def serialize_stamp(self, obj):
        return obj.stamp.image.url if obj.stamp and obj.stamp.image else ''
    
    def serialize_date(self, obj):
        return obj.date.strftime('%Y/%m/%d %H:%M:%S')
