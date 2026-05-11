from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Kategori, Lokasi, Laporan
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def home(request):
    laporan_terbaru = Laporan.objects.all().order_by('-tanggal_dibuat')[:5]
    total_laporan = Laporan.objects.count()
    pending_laporan = Laporan.objects.filter(status='pending').count()
    proses_laporan = Laporan.objects.filter(status='processed').count()
    selesai_laporan = Laporan.objects.filter(status='completed').count()
    context = {
        'laporan_terbaru': laporan_terbaru,
        'total_laporan': total_laporan,
        'pending_laporan': pending_laporan,
        'proses_laporan': proses_laporan,
        'selesai_laporan': selesai_laporan,
    }
    return render(request, 'reports/home.html', context)

@login_required
def buat_laporan(request):
    if request.method == 'POST':
        kategori_id = request.POST.get('kategori')
        lokasi_id = request.POST.get('lokasi')
        deskripsi = request.POST.get('deskripsi')
        laporan = Laporan(
            pelapor=request.user,
            kategori_id=kategori_id,
            lokasi_id=lokasi_id,
            deskripsi=deskripsi,
        )
        if request.FILES.get('foto'):
            laporan.foto = request.FILES['foto']
        laporan.save()
        messages.success(request, 'Laporan berhasil dikirim!')
        return redirect('laporan_saya')
    kategori_list = Kategori.objects.all()
    lokasi_list = Lokasi.objects.all()
    context = {
        'kategori_list': kategori_list,
        'lokasi_list': lokasi_list,
    }
    return render(request, 'reports/buat_laporan.html', context)

@login_required
def laporan_saya(request):
    laporan_list = Laporan.objects.filter(pelapor=request.user)
    context = {'laporan_list': laporan_list}
    return render(request, 'reports/laporan_saya.html', context)

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        messages.error(request, 'Anda tidak memiliki akses ke halaman ini!')
        return redirect('home')
    total_reports = Laporan.objects.count()
    pending_reports = Laporan.objects.filter(status='pending').count()
    processed_reports = Laporan.objects.filter(status='processed').count()
    completed_reports = Laporan.objects.filter(status='completed').count()
    last_week = timezone.now() - timedelta(days=7)
    reports_last_week = Laporan.objects.filter(tanggal_dibuat__gte=last_week).count()
    completed = Laporan.objects.filter(status='completed', tanggal_selesai__isnull=False)
    avg_completion = 0
    if completed.exists():
        total_hours = sum((c.tanggal_selesai - c.tanggal_dibuat).total_seconds() / 3600 for c in completed)
        avg_completion = round(total_hours / completed.count(), 1)
    all_reports = Laporan.objects.all().order_by('-tanggal_dibuat')[:10]
    context = {
        'total_reports': total_reports,
        'pending_reports': pending_reports,
        'processed_reports': processed_reports,
        'completed_reports': completed_reports,
        'reports_last_week': reports_last_week,
        'avg_completion': avg_completion,
        'all_reports': all_reports,
    }
    return render(request, 'reports/admin_dashboard.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role = request.POST.get('role')

        if not username or not email or not password1:
            messages.error(request, 'Semua field harus diisi!')
            return redirect('register')
        if password1 != password2:
            messages.error(request, 'Password tidak cocok!')
            return redirect('register')
        if len(password1) < 4:
            messages.error(request, 'Password minimal 4 karakter!')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username sudah dipakai!')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email sudah terdaftar!')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        # Hanya teknisi yang dapat akses admin panel
        if role == 'technician':
            user.is_staff = True
        else:
            user.is_staff = False

        user.save()

        # Simpan role ke Profile
        from .models import Profile
        profile, created = Profile.objects.get_or_create(user=user)
        profile.role = role if role else 'student'
        profile.save()

        messages.success(request, 'Registrasi berhasil! Silakan login.')
        return redirect('login')
    return render(request, 'reports/register.html')

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Selamat datang kembali, {user.username}!')
            # Teknisi dan superuser diarahkan ke admin dashboard
            if user.is_staff or user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Username atau password salah!')
            return redirect('login')
    return render(request, 'reports/login.html')

def custom_logout(request):
    auth_logout(request)
    messages.info(request, 'Anda telah logout.')
    return redirect('login')