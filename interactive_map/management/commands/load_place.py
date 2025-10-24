import requests
from django.core.management.base import BaseCommand
from app.models import Place, PlaceImage
from urllib.request import urlretrieve
from django.core.files import File


def create_place(data_place):
    place = Place.objects.create(
        title=data_place["title"],
        description_short=data_place.get("description_short", ""),
        description_long=data_place.get("description_long", ""),
        longitude=data_place["coordinates"]["lng"],
        latitude=data_place["coordinates"]["lat"],
    )

    for img_url in data_place.get("imgs", []):
        img_name = img_url.split("/")[-1]
        img_path, _ = urlretrieve(img_url)
        with open(img_path, "rb") as img_file:
            PlaceImage.objects.create(place=place, image=File(img_file, name=img_name))


class Command(BaseCommand):
    help = "Load a place from a JSON URL"

    def add_arguments(self, parser):
        parser.add_argument("url", type=str, help="URL of the JSON file")

    def handle(self, *args, **options):
        url = options["url"]
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        for place_data in data:
            create_place(place_data)
        self.stdout.write(self.style.SUCCESS("Places successfully loaded!"))
