from django.urls import path
from chat_room.views import Dialog,Rooms

urlpatterns = [
    path('room/',Rooms.as_view()),
    path('dialog/',Dialog.as_view()),

]
