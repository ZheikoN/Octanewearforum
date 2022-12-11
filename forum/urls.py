from . import views
from django.urls import path


urlpatterns = [
    path('', views.ThreadList.as_view(), name='home'),
    path('<slug:slug>/', views.ThreadDetail.as_view(), name='thread_detail'),
    path('upvote/<slug:slug>', views.ThreadUpvote.as_view(), name='thread_upvote'),
    path('downvote/<slug:slug>', views.ThreadDownvote.as_view(), name='thread_downvote'),
]