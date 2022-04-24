from . import views
from django.urls import path

from .views import *

urlpatterns = [
    path('', views.get_list_video, name='home'),
    path('stream/<int:pk>/', views.get_streaming_video, name='stream'),
    path('post/<slug:post_slug>/', get_video.as_view(), name='video'),

    # path('',  Index.as_view(), name='home'),

    path('create/', create.as_view(), name='create'),
    path('category/<slug:cat_slug>/', show_category.as_view(), name='category'),
    path('search/', Search.as_view(), name='search'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.logoutuser, name='logout'),
]
