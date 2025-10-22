from django.contrib import admin
from app.models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage


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
