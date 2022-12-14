from . import views
from django.urls import path


urlpatterns = [
    path('', views.ThreadList.as_view(), name='home'),
    path('add_thread/', views.AddThreadView.as_view(), name='add_thread'),
    path('update_thread/<slug:slug>', views.UpdateThreadView.as_view(),
         name='update_thread'),
    path('<slug:slug>/delete', views.DeleteThreadView.as_view(),
         name='delete_thread'),
    path('post/<int:pk>/delete', views.DeletePostView.as_view(),
         name='delete_post'),
    path('post/<int:pk>/update', views.UpdatePostView.as_view(),
         name='update_post'),
    path('<slug:slug>/', views.ThreadDetail.as_view(), name='thread_detail'),
    path('upvote/<slug:slug>', views.ThreadUpvote.as_view(),
         name='thread_upvote'),
    path('downvote/<slug:slug>', views.ThreadDownvote.as_view(),
         name='thread_downvote'),
]
