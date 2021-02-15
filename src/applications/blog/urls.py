from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from applications.blog import views
from applications.blog.apps import BlogConfig

app_name = BlogConfig.label

urlpatterns = [
    path("", views.AllPostsView.as_view(), name="main"),
    path("new/", views.NewPostView.as_view(), name="new_post"),
    path("reset/", views.AllPostDelete.as_view(), name="reset_all"),
    path("search/", views.Search.as_view(), name="search"),
    path("post/<int:pk>/", views.SinglePostView.as_view(), name="post"),
    path("delete/<int:pk>/", views.PostDelete.as_view(), name="post_delete"),
    path("update/<int:pk>/", views.UpdatePostView.as_view(), name="post_update"),
    path("post/<int:pk>/like/", csrf_exempt(views.LikeView.as_view()), name="like"),
    path("post/<int:pk>/comment/", views.AddComment.as_view(), name="add_comment"),
]
