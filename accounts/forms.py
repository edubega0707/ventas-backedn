from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class FormUsuario(forms.Form):
    username = forms.CharField(label='Ingresa nombre de usuario', min_length=4, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    first_name = forms.CharField(label='Ingresa Nombre', min_length=4, max_length=250,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre '}))
    last_name = forms.CharField(label='Ingresa Apellido', min_length=4, max_length=250,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
    #email = forms.EmailField(label='Ingresa Correo Electronico', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}))
    password1 = forms.CharField(label='Ingresa Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label='Conforma Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}))
    #is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'placeholder': 'Usuario activo'}))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("El usuario ya existe")
        return username


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['username'],
            self.cleaned_data['password1']
        )
        user.first_name = self.cleaned_data['first_name'].upper()
        user.last_name = self.cleaned_data['last_name'].upper()
        user.save()

        return


