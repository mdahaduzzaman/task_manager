from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import *

class SingupForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=100, required=True, error_messages={'required': 'First Name is required'}, widget=forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter first name", 'autofocus': 'autofocus'}))

    last_name = forms.CharField(label='Last Name', max_length=100, required=True, error_messages={'required': 'Last Name is required'}, widget=forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter last name"}))
    username = forms.CharField(label='Username', max_length=100, required=True, error_messages={'required': 'Username must be set'}, widget=forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter username"}))

    email = forms.EmailField(label='Email', max_length=254, required=True, error_messages={'required': 'Email is required'}, widget=forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter email"}))

    password1 = forms.CharField(label="Password", required=True, error_messages={'required': 'Password must be set'}, widget=forms.PasswordInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter password"}))

    password2 = forms.CharField(label="Confrim Password", required=True, error_messages={'required': 'Confirm password must be set'}, widget=forms.PasswordInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter confirm password"}))

    avatar = forms.ImageField(label="Avatar", required=False, widget=forms.FileInput(attrs={'class': 'shadow-sm block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'avatar']



class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=254, required=True, error_messages={'required': 'Username is required'}, widget=forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter username"}))
    
    password = forms.CharField(label="Password", required=True, error_messages={'required': 'Password must be set'}, widget=forms.PasswordInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter password"}))