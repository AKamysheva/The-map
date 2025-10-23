from rest_framework import serializers
from app.models import Place, PlaceImage


class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ["image"]


class PlaceSerializer(serializers.ModelSerializer):
    imgs = serializers.SerializerMethodField()
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = [
            "title",
            "imgs",
            "description_short",
            "description_long",
            "coordinates",
        ]

    def get_imgs(self, obj):
        return [img.image.url for img in obj.imgs.all()]

    def get_coordinates(self, obj):
        return {"lng": str(obj.longitude), "lat": str(obj.latitude)}
