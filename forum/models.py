from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

status = ((0, "Draft"), (1, "Published"))


class Thread(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_threads")
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=status, default=1)
    upvotes = models.ManyToManyField(User, related_name='thread_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='thread_downvotes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_upvotes(self):
        return self.upvotes.count()

    def number_of_downvotes(self):
        return self.downvotes.count()


class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="posts")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.name} in section {self.thread} on {self.created_on} "


class Section(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    threads = models.ManyToManyField(Thread, related_name='threads', blank=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"Section: {self.title} contains {self.threads}"
