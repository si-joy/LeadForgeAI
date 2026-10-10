from django.urls import path

from . import views


app_name = "searches"


urlpatterns = [
    path(
        "",
        views.search_list,
        name="list",
    ),
    path(
        "new/",
        views.create_search,
        name="create",
    ),
    path(
        "<int:pk>/",
        views.search_detail,
        name="detail",
    ),
    path(
        "<int:pk>/start/",
        views.start_discovery,
        name="start",
    ),
]