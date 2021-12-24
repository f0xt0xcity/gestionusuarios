from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Campo requerido")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.clean_data.get("email")
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('Este email ya ha sido registrado')
        return email