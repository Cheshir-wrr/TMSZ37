from django.urls import path

from applications.hello.views import hello
from applications.hello.views import reset_hello
from applications.hello.views import save_hello

urlpatterns = [
    path("", hello),
    path("save/", save_hello),
    path("reset/", reset_hello),
]
