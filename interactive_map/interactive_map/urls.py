from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def main_page(request):
    return HttpResponse("<h1>Здесь будет карта</h1>")


urlpatterns = [
    path("", main_page, name="main_page"),
    path("admin/", admin.site.urls),
]
