from django.urls import path

from geekshop_admin.views import admin, admin_users_create, admin_users_read, admin_users_update, admin_users_delete

app_name = 'geekshop_admin'

urlpatterns = [
    path('', admin, name='admin'),
    path('admin-users-create/', admin_users_create, name='admin-users-create'),
    path('admin-users-read/', admin_users_read, name='admin-users-read'),
    path('admin-users-update/<int:user_id>/', admin_users_update, name='admin-users-update'),
    path('admin-users-delete/<int:user_id>/', admin_users_delete, name='admin-users-delete'),
]
