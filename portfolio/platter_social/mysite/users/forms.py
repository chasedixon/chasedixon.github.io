from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=10, required=True)
    city = forms.CharField(max_length=150, required=True)
    state = forms.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "city", "state", "password1", "password2")


    def save(self, commit=True):
        user = super(NewUserForm, self).save()
        profile = Profile.objects.create(user=user)
        profile.email = self.cleaned_data['email']
        profile.phone_number = self.cleaned_data['phone_number']
        profile.city = self.cleaned_data['city']
        profile.state = self.cleaned_data['state']

        profile.save()

        return user


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image', 'email', 'phone_number', 'city', 'state', 'bio']

