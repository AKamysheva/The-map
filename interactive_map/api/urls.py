from django.urls import path
from .views import PlaceNameView


urlpatterns = [path("<int:place_id>/", PlaceNameView.as_view(), name="place-name")]
