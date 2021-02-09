from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("applications.landing.urls")),
    path("b/", include("applications.blog.urls")),
    path("h/", include("applications.hello.urls")),
    path("o/", include("applications.onboarding.urls")),
]
