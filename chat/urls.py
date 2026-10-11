from django.urls import path
from .views import main_view,room_view

app_name="chat"

urlpatterns = [
    path("", main_view, name="main_view"),
    path("<str:room_name>/", room_view, name="room_view"),
]