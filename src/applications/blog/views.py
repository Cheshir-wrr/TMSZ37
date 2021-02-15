from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic import UpdateView

from applications.blog.forms import CommentForm
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
    template_name = "blog/post_detail.html"
    model = Post
    success_url = "/b/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class AddComment(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = post
            form.save()
        return redirect(post.get_absolute_url())


class UpdatePostView(UpdateView):
    template_name = "blog/update.html"
    model = Post
    fields = ["title", "content"]
    success_url = "/b/"


class LikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        payload = {"ok": False, "nr_likes": 0, "reason": "unknown reason"}

        pk = self.kwargs.get("pk", 0)
        post = Post.objects.filter(pk=pk).first()

        if not post:
            payload.update({"reason": "post not found"})
        elif post.author == self.request.user:
            payload.update({"reason": "ne laikai svoi posty"})
        else:
            if post.is_liked_by(user):
                post.likers.remove(user)
            else:
                post.likers.add(user)
            post.save()

            post = Post.objects.get(pk=pk)
            payload.update({"ok": True, "nr_likes": post.nr_likes, "reason": None})

        return JsonResponse(payload)


class Search(ListView):
    template_name = "blog/blog.html"

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        context.update(
            {"search_field": context["q"].replace("q=", "").replace("&", "")}
        )

        return context
