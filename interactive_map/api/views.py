from rest_framework import generics
from app.models import Place
from .serializers import PlaceSerializer


class PlaceNameView(generics.ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        place_id = self.kwargs["place_id"]
        return Place.objects.filter(id=place_id)
