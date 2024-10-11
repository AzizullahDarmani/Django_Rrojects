from django.urls import path
from .views import post_create, post_list, post_delete, post_edit

urlpatterns = [
    path('post/list/', post_list, name='post_list'),
    # path('post/<int:id>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),

    path('post/edit/<int:id>/', post_edit, name='post_edit'),  # Edit URL
    path('post/delete/<int:id>/', post_delete, name='post_delete'), 
]
