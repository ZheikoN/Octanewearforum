from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Thread


class ThreadList(generic.ListView):
    model = Thread
    queryset = Thread.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class ThreadDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Thread.objects.filter(status=1)
        thread = get_object_or_404(queryset, slug=slug)
        post = thread.posts.filter(approved=True).order_by('-created_on')

        upvotes = False
        if thread.upvotes.filter(id=self.request.user.id).exists():
            upvotes = True
        downvotes = False
        if thread.downvotes.filter(id=self.request.user.id).exists():
            downvotes = True

        return render(
            request, "post_detail.html",
            {
                "thread": thread,
                "post": post,
                "upvotes": upvotes,
                "downvotes": downvotes
            },
        )