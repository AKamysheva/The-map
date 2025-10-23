from django.db import models


def place_image_path(instance, filename):
    return f"images/place_{instance.place.id}/{filename}"


class Place(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название места")
    description_short = models.TextField(verbose_name="Короткое описание")
    description_long = models.TextField(verbose_name="Подробное описание")
    longitude = models.FloatField(verbose_name="Долгота")
    latitude = models.FloatField(verbose_name="Широта")
    created_at = models.DateTimeField(auto_now_add=True)


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="imgs")
    image = models.ImageField(upload_to=place_image_path, verbose_name="Картинки места")
