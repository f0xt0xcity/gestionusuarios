from django.urls import path
from .views import SampleView, HomeView
app_name = 'home_app'

urlpatterns = [
    path(
        '', 
        HomeView.as_view(),
        name = "home"),
    path(
        'sample/', 
        SampleView.as_view(),
        name = "sample"),
]
