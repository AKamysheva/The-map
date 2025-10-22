from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path("admin/", admin.site.urls),
    re_path(
        r"^(?P<path>.*)$", serve, {"document_root": settings.BASE_DIR / "frontend"}
    ),
]
