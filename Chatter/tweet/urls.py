from . import views
from django.urls import path


urlpatterns = [
    path('' , views.tweet_list, name='tweet_list'),
    path('<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),
    path('create/' , views.create_tweet , name='create_tweet'),
    path('<int:tweet_id>/like/', views.like_tweet, name='like_tweet'),
    path('<int:tweet_id>/comment/', views.add_comment, name='add_comment'),
path(
    '<int:comment_id>/comment/delete/',
    views.delete_comment,
    name='delete_comment'
),
path(
    '<int:comment_id>/comment/edit/',
    views.edit_comment,
    name='edit_comment'
),
    path('<int:tweet_id>/edit/' , views.edit_tweet, name='edit_tweet'),
    path('<int:tweet_id>/delete/' , views.delete_tweet , name='delete_tweet'),
    path('register/', views.register, name='register'),

]


