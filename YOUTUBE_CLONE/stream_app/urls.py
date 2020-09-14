from django.urls import path
from . import views

app_name = "stream_app"

urlpatterns = [
    path("",views.home,name="home"),
    path('video-detail/<slug:slug>/',views.details,name='video_details'),
    path('upload-video',views.upload_video,name='upload_video'),
    path('edit-video/<slug:slug>',views.edit_video,name="edit_video"),

    
]
