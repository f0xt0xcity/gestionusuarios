from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


from applications.pages.forms import PageForm

from .models import Page
from .forms import PageForm

# Create your views here.
class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class PagesListView(ListView):
    model = Page
    template_name = 'pages/pages.html'
    context_object_name = 'pages'


class PagesDetailView(DetailView):
    model = Page
    template_name = 'pages/page.html'
    context_object_name = 'page'


@method_decorator(staff_member_required, name='dispatch')
class PageCreateView(CreateView):
    model = Page
    template_name = 'pages/add.html'
    #fields = ['title', 'content', 'order']
    form_class =PageForm
    success_url = reverse_lazy('pages_app:pages')


@method_decorator(staff_member_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    template_name = 'pages/update.html'
   # fields = ['title', 'content', 'order']
    form_class =PageForm
    success_url = reverse_lazy('pages_app:pages')
    
@method_decorator(staff_member_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('pages_app:pages')