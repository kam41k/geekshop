from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from users.models import User
from products.models import ProductCategory, Product
from geekshop_admin.forms import GeekshopAdminUserCreationForm, GeekshopAdminUserProfileForm, \
    GeekshopAdminProductCategoryForm, GeekshopAdminProductForm


# Create your views here.
@user_passes_test(lambda user: user.is_staff)
def admin(request):
    context = {'title': 'GeekShop - Админка'}
    return render(request, 'geekshop_admin/admin.html', context)


class CommonMixin(SuccessMessageMixin):
    title = 'GeekShop - Админка'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CommonMixin, self).get_context_data(object_list=None, **kwargs)
        context['title'] = self.title
        return context


class AdminUsersListView(CommonMixin, ListView):
    model = User
    template_name = 'geekshop_admin/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminUsersListView, self).dispatch(request, *args, **kwargs)


class AdminUserCreateView(CommonMixin, CreateView):
    model = User
    form_class = GeekshopAdminUserCreationForm
    template_name = 'geekshop_admin/admin-users-create.html'
    success_url = reverse_lazy('geekshop-admin:admin-users-read')
    success_message = 'Пользователь успешно создан.'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminUserCreateView, self).dispatch(request, *args, **kwargs)


class AdminUserUpdateView(CommonMixin, UpdateView):
    model = User
    form_class = GeekshopAdminUserProfileForm
    template_name = 'geekshop_admin/admin-users-update-delete.html'
    success_url = reverse_lazy('geekshop-admin:admin-users-read')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminUserUpdateView, self).dispatch(request, *args, **kwargs)


class AdminUserDeleteView(DeleteView):
    model = User
    template_name = 'geekshop_admin/admin-users-update-delete.html'
    success_url = reverse_lazy('geekshop-admin:admin-users-read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.self_delete()
        return HttpResponseRedirect(self.success_url)

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminUserDeleteView, self).dispatch(request, *args, **kwargs)


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
    return HttpResponseRedirect(reverse('geekshop-admin:admin-product-read'))
