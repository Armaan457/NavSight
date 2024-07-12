from django.urls import path
from NavSight.user.views import yolo, blip, voice_control

urlpatterns = [
    path('yolo/',yolo,name='yolo'),
    path('blip/',blip,name='blip'),
    path('voice_control/',voice_control,name='voice_control'),
]