from django import forms

from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User
from products.models import ProductCategory, Product


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


class GeekshopAdminProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Название товара'}))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Описание'}), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    # price = forms.DecimalField(widget=forms.DecimalField(attrs={
    #     'class': 'form-control py-4', 'placeholder': 'Цена'}), required=False)
    # quantity = forms.IntegerField(widget=forms.IntegerField(attrs={
    #     'class': 'form-control py-4', 'placeholder': 'Количество'}), required=False)
    # category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(),
    #                                   widget=forms.ModelChoiceField(queryset=ProductCategory.objects.all(),
    #                                                                 attrs={'class': 'custom-file-input'}),
    #                                   required=False),

    class Meta:
        model = Product
        fields = '__all__'#('name', 'description', 'image', 'price', 'quantity', 'category')
