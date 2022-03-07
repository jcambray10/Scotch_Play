from operator import index
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('dashboard', views.golf),
    path('dashboard/newgolf', views.new),
    path('create_golf', views.create_golf),
    path('edit/<int:golf_id>', views.edit),
    path('edit/<int:golf_id>/update', views.update),
    path('view/<int:golf_id>', views.view_golf),
    path('dashboard/user_profile/<int:user_id>', views.profile),
    path('dashboard/user_profile/<int:user_id>/create_profile)', views.create_profile),
    path('dashboard/user_profile/edit/<int:profile_id>', views.edit_profile),
    path('dashboard/user_profile/edit/<int:profile_id>/update', views.update_profile),
    path('dashboard/cancel/<int:golf_id>', views.cancel),
    path('dashboard/done/<int:golf_id>', views.done_with_golf),
    path('dashboard/add_to_my_golf/<int:golf_id>', views.add_to_my_golf),
]