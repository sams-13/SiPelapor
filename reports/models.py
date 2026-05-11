from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

# ==================== MODEL PROFILE ====================
class Profile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Mahasiswa'),
        ('lecturer', 'Dosen'),
        ('technician', 'Teknisi'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(user_signed_up)
def handle_user_signup(request, user, **kwargs):
    role = request.POST.get('role', 'student')
    profile, created = Profile.objects.get_or_create(user=user)
    profile.role = role
    profile.save()
    if role == 'technician':
        user.is_staff = True
    else:
        user.is_staff = False
    user.save()

# ==================== MODEL KATEGORI ====================
class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural = "Kategori"

# ==================== MODEL LOKASI ====================
class Lokasi(models.Model):
    gedung = models.CharField(max_length=100)
    lantai = models.CharField(max_length=50, blank=True, null=True)
    ruangan = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return f"{self.gedung} - {self.ruangan}"
    class Meta:
        verbose_name_plural = "Lokasi"

# ==================== MODEL LAPORAN ====================
class Laporan(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Menunggu'),
        ('processed', 'Diproses'),
        ('completed', 'Selesai'),
        ('rejected', 'Ditolak'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Rendah'),
        ('medium', 'Sedang'),
        ('high', 'Tinggi'),
    ]
    pelapor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='laporan_dibuat')
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True)
    lokasi = models.ForeignKey(Lokasi, on_delete=models.SET_NULL, null=True, blank=True)
    deskripsi = models.TextField()
    foto = models.ImageField(upload_to='laporan_foto/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    prioritas = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    teknisi = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='laporan_ditangani')
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    tanggal_diproses = models.DateTimeField(blank=True, null=True)
    tanggal_selesai = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"Laporan #{self.id} - {self.kategori}"
    class Meta:
        ordering = ['-tanggal_dibuat']
        verbose_name_plural = "Laporan"

# ==================== MODEL UPDATE LAPORAN ====================
class UpdateLaporan(models.Model):
    laporan = models.ForeignKey(Laporan, on_delete=models.CASCADE, related_name='updates')
    status = models.CharField(max_length=20)
    catatan = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='update_foto/', blank=True, null=True)
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Update {self.laporan.id} - {self.status}"
    class Meta:
        verbose_name_plural = "Update Laporan"