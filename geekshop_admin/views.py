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


class AdminProductCategoriesListView(CommonMixin, ListView):
    model = ProductCategory
    template_name = 'geekshop_admin/admin-product-category-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductCategoriesListView, self).dispatch(request, *args, **kwargs)


class AdminProductCategoryCreateView(CommonMixin, CreateView):
    model = ProductCategory
    form_class = GeekshopAdminProductCategoryForm
    template_name = 'geekshop_admin/admin-product-category-create.html'
    success_url = reverse_lazy('geekshop-admin:admin-product-category-read')
    success_message = 'Категория успешно создана.'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductCategoryCreateView, self).dispatch(request, *args, **kwargs)


class AdminProductCategoryUpdateView(CommonMixin, UpdateView):
    model = ProductCategory
    form_class = GeekshopAdminProductCategoryForm
    template_name = 'geekshop_admin/admin-product-category-update-delete.html'
    success_url = reverse_lazy('geekshop-admin:admin-product-category-read')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductCategoryUpdateView, self).dispatch(request, *args, **kwargs)


class AdminProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'geekshop_admin/admin-product-category-update-delete.html'
    success_url = reverse_lazy('geekshop-admin:admin-product-category-read')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductCategoryDeleteView, self).dispatch(request, *args, **kwargs)


class AdminProductsListView(CommonMixin, ListView):
    model = Product
    template_name = 'geekshop_admin/admin-product-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductsListView, self).dispatch(request, *args, **kwargs)


class AdminProductCreateView(CommonMixin, CreateView):
    model = Product
    form_class = GeekshopAdminProductForm
    template_name = 'geekshop_admin/admin-product-create.html'
    success_url = reverse_lazy('geekshop-admin:admin-product-read')
    success_message = 'Продукт успешно создан.'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductCreateView, self).dispatch(request, *args, **kwargs)


class AdminProductUpdateView(CommonMixin, UpdateView):
    model = Product
    form_class = GeekshopAdminProductForm
    template_name = 'geekshop_admin/admin-product-update-delete.html'
    success_url = reverse_lazy('geekshop-admin:admin-product-read')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductUpdateView, self).dispatch(request, *args, **kwargs)


class AdminProductDeleteView(DeleteView):
    model = Product
    template_name = 'geekshop_admin/admin-product-update-delete.html'
    success_url = reverse_lazy('geekshop-admin:admin-product-read')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductDeleteView, self).dispatch(request, *args, **kwargs)
