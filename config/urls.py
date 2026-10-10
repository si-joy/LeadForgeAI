from django.contrib import admin
from django.urls import include, path

from searches.views import dashboard


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "",
        dashboard,
        name="dashboard",
    ),

    path(
        "searches/",
        include("searches.urls"),
    ),
]