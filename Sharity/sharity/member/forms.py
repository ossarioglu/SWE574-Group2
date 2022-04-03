
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyRegisterForm(UserCreationForm):
    # emain, first_name, and last_name fields are shown at this form as additional to UserCreationForm
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
    def save(self, commit=True):
        user = super(MyRegisterForm,self).save(commit=False)
        if commit:
            user.save()
        return user