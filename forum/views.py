from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Thread
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator


class ThreadList(generic.ListView):
    model = Thread
    queryset = Thread.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class ThreadDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Thread.objects.filter(status=1)
        thread = get_object_or_404(queryset, slug=slug)
        posts = thread.posts.filter(approved=True).order_by('created_on')

        upvotes = False
        if thread.upvotes.filter(id=self.request.user.id).exists():
            upvotes = True
        downvotes = False
        if thread.downvotes.filter(id=self.request.user.id).exists():
            downvotes = True

        posts_list = thread.posts.filter(approved=True).order_by('created_on')
        paginator = Paginator(posts_list, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request, "thread_detail.html",
            {
                "thread": thread,
                "posts": posts,
                "upvotes": upvotes,
                "downvotes": downvotes,
                "post_form": PostForm(),
                "page_obj": page_obj,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Thread.objects.filter(status=1)
        thread = get_object_or_404(queryset, slug=slug)
        posts = thread.posts.filter(approved=True).order_by('-created_on')

        upvotes = False
        if thread.upvotes.filter(id=self.request.user.id).exists():
            upvotes = True
            downvotes = False
        if thread.downvotes.filter(id=self.request.user.id).exists():
            downvotes = True

        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post_form.instance.email = request.user.email
            post_form.instance.name = request.user.username
            post = post_form.save(commit=False)
            post.thread = thread
            post.save()
            messages.success(request, "Your post was successful")
        else:
            post_form = PostForm()
            messages.error(request, "Posting to the thread failed, contact administrator")

        posts_list = thread.posts.filter(approved=True).order_by('created_on')
        paginator = Paginator(posts_list, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request, "thread_detail.html",
            {
                "thread": thread,
                "posts": posts,
                "post_form": PostForm,
                "upvotes": upvotes,
                "downvotes": downvotes,
                "page_obj": page_obj,
            },
        )


class ThreadUpvote(View):

    def post(self, request, slug, *args, **kwargs):
        thread = get_object_or_404(Thread, slug=slug)

        if thread.upvotes.filter(id=request.user.id).exists():
            thread.upvotes.remove(request.user)
            messages.warning(request, "Your upvote was removed successfully")
        else:
            thread.upvotes.add(request.user)
            messages.success(request, "Your have upvoted this thread successfully")

        return HttpResponseRedirect(reverse('thread_detail', args=[slug]))


class ThreadDownvote(View):

    def post(self, request, slug, *args, **kwargs):
        thread = get_object_or_404(Thread, slug=slug)

        if thread.downvotes.filter(id=request.user.id).exists():
            thread.downvotes.remove(request.user)
            messages.success(request, "Your downvote was removed successfully")
        else:
            thread.downvotes.add(request.user)
            messages.warning(request, "You have downvoted this thread")

        return HttpResponseRedirect(reverse('thread_detail', args=[slug]))
