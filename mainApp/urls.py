from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('createPost',views.createPost),
    path('feed',views.feed),
    path('<username>',views.profile),
    path('deletePost/<int:id>',views.deletePost),
]
