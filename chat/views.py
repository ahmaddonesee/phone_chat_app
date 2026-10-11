from django.shortcuts import render


def main_view(request):
    return render(request, "chat/main.html")

# for chat room
def room_view(request, room_name):
    room_name=None
    return render(request, "chat/room.html", {"room_name": room_name})