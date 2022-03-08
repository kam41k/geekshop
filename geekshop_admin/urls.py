from django.urls import path

from geekshop_admin.views import admin, AdminUserCreateView, AdminUsersListView, AdminUserUpdateView, AdminUserDeleteView, AdminProductCategoriesListView, \
    AdminProductCategoryCreateView, AdminProductCategoryUpdateView, AdminProductCategoryDeleteView, AdminProductsListView, AdminProductCreateView, AdminProductUpdateView, \
    AdminProductDeleteView

app_name = 'geekshop_admin'

urlpatterns = [
    path('', admin, name='admin'),
    path('admin-users-read/', AdminUsersListView.as_view(), name='admin-users-read'),
    path('admin-users-create/', AdminUserCreateView.as_view(), name='admin-users-create'),
    path('admin-users-update/<int:pk>/', AdminUserUpdateView.as_view(), name='admin-users-update'),
    path('admin-users-delete/<int:pk>/', AdminUserDeleteView.as_view(), name='admin-users-delete'),
    path('admin-product-category-read/', AdminProductCategoriesListView.as_view(), name='admin-product-category-read'),
    path('admin-product-category-create/', AdminProductCategoryCreateView.as_view(), name='admin-product-category-create'),
    path('admin-product-category-update/<int:pk>', AdminProductCategoryUpdateView.as_view(), name='admin-product-category-update'),
    path('admin-product-category-delete/<int:pk>', AdminProductCategoryDeleteView.as_view(), name='admin-product-category-delete'),
    path('admin-product-read/', AdminProductsListView.as_view(), name='admin-product-read'),
    path('admin-product-create/', AdminProductCreateView.as_view(), name='admin-product-create'),
    path('admin-product-update/<int:pk>', AdminProductUpdateView.as_view(), name='admin-product-update'),
    path('admin-product-delete/<int:pk>', AdminProductDeleteView.as_view(), name='admin-product-delete'),
]
