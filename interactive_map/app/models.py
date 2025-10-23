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

    class Meta:
        ordering = ["id"]


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="imgs")
    image = models.ImageField(upload_to=place_image_path, verbose_name="Картинки места")
    the_order = models.PositiveIntegerField(
        default=0, editable=True, db_index=True, verbose_name="Порядок"
    )

    class Meta:
        verbose_name = "Картинка места"
        verbose_name_plural = "Картинки места"
        ordering = ["the_order"]

    def __str__(self):
        return f"Картинка для {self.place.title}"
