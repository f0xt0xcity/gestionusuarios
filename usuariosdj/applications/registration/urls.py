from django.urls import path
from .views import SignUpView

app_name = 'register_app'

urlpatterns = [
    #aplicaciones
    path(
        'signup/',
        SignUpView.as_view(),
        name='signup',
    )
]
