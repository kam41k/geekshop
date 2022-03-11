from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.contrib import messages
from users.models import User
from products.models import ProductCategory, Product
from geekshop_admin.forms import GeekshopAdminUserCreationForm, GeekshopAdminUserProfileForm, \
    GeekshopAdminProductCategoryForm, GeekshopAdminProductForm


# Create your views here.
@user_passes_test(lambda user: user.is_staff)
def admin(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'geekshop_admin/admin.html', context)


@user_passes_test(lambda user: user.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        form = GeekshopAdminUserCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно создан.')
            return HttpResponseRedirect(reverse('geekshop-admin:admin-users-read'))
    else:
        form = GeekshopAdminUserCreationForm()
    context = {'title': 'GeekShop - Admin', 'form': form}
    return render(request, 'geekshop_admin/admin-users-create.html', context)


@user_passes_test(lambda user: user.is_staff)
def admin_users_read(request):
    context = {'title': 'GeekShop - Admin', 'Users': User.objects.all()}
    return render(request, 'geekshop_admin/admin-users-read.html', context)


@user_passes_test(lambda user: user.is_staff)
def admin_users_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = GeekshopAdminUserProfileForm(instance=user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('geekshop-admin:admin-users-read'))
    else:
        form = GeekshopAdminUserProfileForm(instance=user)
    context = {'title': 'GeekShop - Admin', 'User': user, 'form': form}
    return render(request, 'geekshop_admin/admin-users-update-delete.html', context)


@user_passes_test(lambda user: user.is_staff)
def admin_users_delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.self_delete()
    return HttpResponseRedirect(reverse('geekshop_admin:admin-users-read'))


@user_passes_test(lambda user: user.is_staff)
def admin_product_category_read(request):
    context = {'title': 'GeekShop - Admin', 'ProductCategories': ProductCategory.objects.all()}
    return render(request, 'geekshop_admin/admin-product-category-read.html', context)


@user_passes_test(lambda user: user.is_staff)
def admin_product_category_create(request):
    if request.method == 'POST':
        form = GeekshopAdminProductCategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно создана.')
            return HttpResponseRedirect(reverse('geekshop-admin:admin-product-category-read'))
    else:
        form = GeekshopAdminProductCategoryForm()
    context = {'title': 'GeekShop - Admin', 'form': form}
    return render(request, 'geekshop_admin/admin-product-category-create.html', context)


@user_passes_test(lambda user: user.is_staff)
def admin_product_category_update(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    if request.method == 'POST':
        form = GeekshopAdminProductCategoryForm(instance=category, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('geekshop-admin:admin-product-category-read'))
    else:
        form = GeekshopAdminProductCategoryForm(instance=category)
    context = {'title': 'GeekShop - Admin', 'Category': category, 'form': form}
    return render(request, 'geekshop_admin/admin-product-category-update-delete.html', context)


@user_passes_test(lambda user: user.is_staff)
def admin_product_category_delete(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    category.delete()
    return HttpResponseRedirect(reverse('geekshop-admin:admin-product-category-read'))


@user_passes_test(lambda user: user.is_staff)
def admin_product_create(request):
    if request.method == 'POST':
        form = GeekshopAdminProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно создан.')
            return HttpResponseRedirect(reverse('geekshop-admin:admin-product-read'))
    else:
        form = GeekshopAdminProductForm()
    context = {'title': 'GeekShop - Admin', 'form': form}
    return render(request, 'geekshop_admin/admin-product-create.html', context)


@user_passes_test(lambda user: user.is_staff)
def admin_product_read(request):
    context = {'title': 'GeekShop - Admin', 'Products': Product.objects.all()}
    return render(request, 'geekshop_admin/admin-product-read.html', context)


@user_passes_test(lambda user: user.is_staff)
def admin_product_update(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = GeekshopAdminProductForm(instance=product, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('geekshop-admin:admin-product-read'))
    else:
        form = GeekshopAdminProductForm(instance=product)
    context = {'title': 'GeekShop - Admin', 'Product': product, 'form': form}
    return render(request, 'geekshop_admin/admin-product-update-delete.html', context)


@user_passes_test(lambda user: user.is_staff)
def admin_product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('geekshop_admin:admin-product-read'))
