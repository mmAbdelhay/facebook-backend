from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("", views.index),
    path("myPosts", views.getMyPosts),
    path("profile/posts/<name>", views.gitPostsByName),
    path('create', views.create),
    path('addComment', views.addComment),
    path('like', views.like),
    path('delete/<int:id>', views.delete),
    path('delete/comment/<int:id>', views.deleteComment),
    path('unlike/<int:id>', views.unlike),
    path('update/<int:id>', views.update),
]
