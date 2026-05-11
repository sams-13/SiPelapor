from django.contrib import admin
from .models import Kategori, Lokasi, Laporan, UpdateLaporan, Profile

@admin.register(Laporan)
class LaporanAdmin(admin.ModelAdmin):
    list_display = ['id', 'pelapor', 'kategori', 'status', 'prioritas', 'tanggal_dibuat']
    list_filter = ['status', 'prioritas', 'kategori']
    search_fields = ['pelapor__username', 'deskripsi']
    list_editable = ['status', 'prioritas']

    def has_module_perms(self, request, app_label):
        return request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    def has_add_permission(self, request):
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # hanya superuser yang bisa hapus

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return request.user.is_staff
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
    def has_add_permission(self, request):
        return request.user.is_superuser
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

@admin.register(Lokasi)
class LokasiAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return request.user.is_staff
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
    def has_add_permission(self, request):
        return request.user.is_superuser
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

@admin.register(UpdateLaporan)
class UpdateLaporanAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return request.user.is_staff
    def has_change_permission(self, request, obj=None):
        return request.user.is_staff
    def has_add_permission(self, request):
        return request.user.is_staff
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser