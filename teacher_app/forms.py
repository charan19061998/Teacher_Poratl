from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from .models import Student
from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import ValidationError
class Signup_Form(UserCreationForm):
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

class Edituserprofile(UserChangeForm):
    password = None
    class Meta:
         model=User
         fields=['username','first_name','last_name','email','date_joined','last_login']
         labels={'email':'Email'}


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'subject', 'marks']

class UsernamePasswordResetForm(PasswordResetForm):
    def clean_email(self):
        """
        Overriding the method to validate username instead of email.
        """
        username = self.cleaned_data["email"]
        try:
            user = User.objects.get(username=username)  # Find the user by username
        except User.DoesNotExist:
            raise ValidationError("User with this username does not exist.")
        return user.username
