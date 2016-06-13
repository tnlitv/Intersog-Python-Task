from django.conf.urls import url

from blog.views import PostList, PostDetailView
from . import views

urlpatterns = [
    # url(r'/add', views.add, name='add'),
    # url(r'/edit', views.edit, name='edit'),
    # url(r'/delete', views.delete, name='delete'),
    url(r'post/(?P<pk>\d+)/', PostDetailView.as_view(), name='post_id'),
    url(r'', PostList.as_view(), name='all'),
]
