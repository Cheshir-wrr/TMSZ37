from django.urls import path

from applications.blog import views
from applications.blog.apps import BlogConfig

app_name = BlogConfig.label

urlpatterns = [
    path("", views.AllPostsView.as_view(), name="main"),
    path("new/", views.NewPostView.as_view(), name="new_post"),
    path("reset/", views.AllPostDelete.as_view(), name="reset_all"),
    path("post/<int:pk>/", views.SinglePostView.as_view()),
    path("delete/<int:pk>/", views.PostDelete.as_view(), name="post_delete"),
    path("update/<int:pk>/", views.UpdatePostView.as_view(), name="post_update"),
]
