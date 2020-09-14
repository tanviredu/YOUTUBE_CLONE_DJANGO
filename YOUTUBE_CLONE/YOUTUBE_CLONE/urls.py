from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from stream_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('login_app.urls')),
    path('stream/',include('stream_app.urls')),
    path("",views.home,name="home")
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)