from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView
from applications.blog.models import Post


class AllPostsView(ListView):
    template_name = "blog/blog.html"
    model = Post


class NewPostView(CreateView):
    model = Post
    fields = ["title", "content"]
    success_url = "/b/"


def blog_reset(request: HttpRequest) -> HttpResponse:
    Post.objects.all().delete()
    return redirect("/b/")
