from django import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic import UpdateView

from applications.blog.models import Post


class AllPostsView(ListView):
    template_name = "blog/blog.html"
    model = Post


class NewPostView(CreateView):
    model = Post
    fields = ["title", "content"]
    success_url = "/b/"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)


class AllPostDelete(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        Post.objects.all().delete()
        return reverse_lazy("blog:main")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content"]
        widgets = {"content": forms.Textarea(attrs={"rows": 2})}


class PostDelete(DeleteView):
    http_method_names = ["post"]
    model = Post
    success_url = reverse_lazy("blog:main")


class SinglePostView(DetailView):
    template_name = "blog/post.html"
    model = Post
    success_url = "/b/"


class UpdatePostView(UpdateView):
    template_name = "blog/update.html"
    model = Post
    fields = ["title", "content"]
    success_url = "/b/"
