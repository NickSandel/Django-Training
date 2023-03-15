from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blogpost-detail'),
    path('<int:pk>/create', views.BlogCommentCreateView.as_view(), name='blogpost-create'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
]