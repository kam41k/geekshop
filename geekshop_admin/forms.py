from django import forms

from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User


class GeekshopAdminCreationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'city', 'username', 'email', 'password1', 'password2')


class GeekshopAdminProfileForm(UserProfileForm):
    pass
