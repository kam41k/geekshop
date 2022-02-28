from django import forms

from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User
from products.models import ProductCategory


class GeekshopAdminUserCreationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'city', 'username', 'email', 'password1', 'password2')


class GeekshopAdminUserProfileForm(UserProfileForm):
    pass


class GeekshopAdminProductCategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Название категории'}))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Описание'}), required=False)

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')
