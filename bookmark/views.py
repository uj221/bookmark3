from django.shortcuts import render


# 어떤 기능을 만들어 주는 곳
# urls.py 내가 views.py 만든 기능이 어떤 url로 접속했을 때 동작하게 할 것이냐?
# Create your views here.

from django.views.generic.base import TemplateView

class IndexPage(TemplateView):
    template_name = 'index.html'

from django.views.generic.list import ListView
from .models import Bookmark
class BookmarkListView(ListView):
    model = Bookmark