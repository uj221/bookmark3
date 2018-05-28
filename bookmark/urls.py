from django.urls import path, re_path
from .views import BookmarkListView


app_name = 'bookmark'

urlpatterns = [
    # http://localhost:8000/bookmark/
    path('', BookmarkListView.as_view(), name='index'),
]