from django.urls import path

from geekshop_admin.views import admin, admin_users_create, admin_users_read, admin_users_update, admin_users_delete, \
    admin_product_category_read, admin_product_category_create, admin_product_category_update, \
    admin_product_category_delete, admin_product_read, admin_product_create, admin_product_update, admin_product_delete

app_name = 'geekshop_admin'

urlpatterns = [
    path('', admin, name='admin'),
    path('admin-users-create/', admin_users_create, name='admin-users-create'),
    path('admin-users-read/', admin_users_read, name='admin-users-read'),
    path('admin-users-update/<int:user_id>/', admin_users_update, name='admin-users-update'),
    path('admin-users-delete/<int:user_id>/', admin_users_delete, name='admin-users-delete'),
    path('admin-product-category-read/', admin_product_category_read, name='admin-product-category-read'),
    path('admin-product-category-create/', admin_product_category_create, name='admin-product-category-create'),
    path('admin-product-category-update/<int:category_id>', admin_product_category_update,
         name='admin-product-category-update'),
    path('admin-product-category-delete/<int:category_id>', admin_product_category_delete,
         name='admin-product-category-delete'),
    path('admin-product-read/', admin_product_read, name='admin-product-read'),
    path('admin-product-create/', admin_product_create, name='admin-product-create'),
    path('admin-product-update/<int:product_id>', admin_product_update,
         name='admin-product-update'),
    path('admin-product-delete/<int:product_id>', admin_product_delete,
         name='admin-product-delete'),
]
