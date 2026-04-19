from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.job_list,         name='job_list'),
    path('apply/<int:job_id>/',     views.apply_job,        name='apply_job'),
    path('admin-panel/',            views.admin_dashboard,  name='admin_dashboard'),
    path('admin-panel/add/',        views.add_job,          name='add_job'),
    path('admin-panel/edit/<int:job_id>/', views.edit_job,  name='edit_job'),
    path('admin-panel/delete/<int:job_id>/', views.delete_job, name='delete_job'),
]