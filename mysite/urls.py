from django.contrib import admin
from django.urls import path, include





urlpatterns = [

    path("", include("gift.urls")),
    path('admin/', admin.site.urls),
    path("ref/", include("gift_ref.urls")),

]
