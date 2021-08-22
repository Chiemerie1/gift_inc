from django.contrib import admin
from django.urls import path

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from . import views as V



app_name ="gift"

urlpatterns = [

    path("", V.home, name="home"),
    path("register/", V.register, name="register"),
    path("dashboard/", V.dashboard, name="dashboard"),
    path("tree/",V.tree, name="tree"),
    path("logout/", V.logout_request, name="logout"),
    path("profile/", V.profile, name="profile"),
    path("change_password/", V.change_password, name="change_password"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
