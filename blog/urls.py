from django.urls import path 
from . import views
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static




urlpatterns = [
    
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),

]
