from django.urls import path

from applications.blog import views
from applications.blog.apps import BlogConfig

app_name = BlogConfig.label

urlpatterns = [
    path("", views.AllPostsView.as_view(), name="index"),
    path("new/", views.NewPostView.as_view()),
    path("reset/", views.AllPostDelete.as_view()),
    path("post/<int:pk>/", views.SinglePostView.as_view()),
    path("delete/<int:pk>/", views.PostDelete.as_view()),
    path("update/<int:pk>/", views.UpdatePostView.as_view()),
]
