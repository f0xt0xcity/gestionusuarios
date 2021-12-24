from django.urls import path
from .views import PageCreateView, PagesDetailView, PagesListView

app_name = 'pages_app'

urlpatterns = [
    path(
        '', 
        PagesListView.as_view(), 
        name='pages'),
    path(
        '<int:pk>/<slug:slug>/', 
        PagesDetailView.as_view(), 
        name='page'
        ),
    path(
        'create/', 
        PageCreateView.as_view(), 
        name='page_create'
        ),
]