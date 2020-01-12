"""test file from xav class"""

from django import forms
# from .models import Movies
# class MoviesForm(forms.ModelForm):
#     class Meta:
#         model = Movies
#         fields = ('name', 'description', 'time', 'authors', 'realisator')


class UserLoginForm(forms.Form):
    """ Form to be used to log users in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)