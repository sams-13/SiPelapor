from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buat-laporan/', views.buat_laporan, name='buat_laporan'),
    path('laporan-saya/', views.laporan_saya, name='laporan_saya'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('register/', views.register, name='register'),
]