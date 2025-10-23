from django.contrib import admin
from app.models import Place, PlaceImage
from django.utils.safestring import mark_safe


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    readonly_fields = ("display_image",)
    extra = 1
    fields = ("image", "display_image")

    def display_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=100>")
        return "-"

    display_image.short_description = "Превью картинки"


class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description_short",
        "description_long",
        "longitude",
        "latitude",
    )
    list_display_links = ("title",)
    inlines = [PlaceImageInline]


admin.site.register(Place, PlaceAdmin)
