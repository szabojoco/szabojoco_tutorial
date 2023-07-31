from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


# Custom user registration form
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize widget attributes
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your first name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your last name'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your email address'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please re-enter your password'})


# Custom authentication form with username and password fields
class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize widget attributes
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})


# Custom password change form
class PasswordChangeNewForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize widget attributes
        self.fields['old_password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your new password'})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your new password confirmation'})
