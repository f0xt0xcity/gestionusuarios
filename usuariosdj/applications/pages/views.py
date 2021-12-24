from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import Page

# Create your views here.
class PagesListView(ListView):
    model = Page
    template_name = 'pages/pages.html'
    context_object_name = 'pages'


class PagesDetailView(DetailView):
    model = Page
    template_name = 'pages/page.html'
    context_object_name = 'page'


class PageCreateView(CreateView):
    model = Page
    template_name = 'pages/add.html'
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages_app:pages')


class PageUpdateView(UpdateView):
    model = Page
    template_name = 'pages/update.html'
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages_app:pages')
    

class PageDeleteView(DeleteView):
    model = Page
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('pages_app:pages')