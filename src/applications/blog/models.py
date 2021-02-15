import delorean
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Manager
from django.urls import reverse_lazy

User = get_user_model()


def _now():
    return delorean.utcnow().datetime


class PostManager(Manager):
    pass


class Post(models.Model):
    objects = PostManager()
    title = models.TextField(null=True, blank=True, unique=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=_now)
    nr_views = models.IntegerField(default=0)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likers = models.ManyToManyField(User, related_name="liked_posts", blank=True)

    @property
    def nr_likes(self):
        return self.likers.count()

    def is_liked_by(self, user: User) -> bool:
        liked = Post.objects.filter(pk=self.pk, likers=user).exists()
        return liked

    class Meta:
        ordering = ["-created_at"]

    def get_absolute_url(self):
        kwargs = {"pk": self.pk}
        url = reverse_lazy("blog:post", kwargs=kwargs)
        return url


class Comments(models.Model):

    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    post = models.ForeignKey(Post, verbose_name="Пост", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.post}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
