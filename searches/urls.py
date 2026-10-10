from django.urls import path

from . import views


app_name = "searches"


urlpatterns = [
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
]