Sipelapor adalah platform pengaduan dan pelaporan digital berbasis web yang dirancang untuk memudahkan masyarakat dalam menyampaikan laporan atau keluhan secara cepat, terstruktur, dan terdokumentasi dengan baik. Aplikasi ini dibangun menggunakan framework Django untuk menangani logika backend dan database SQLite untuk penyimpanan data.

Tentang Proyek

Sipelapor hadir sebagai solusi modern untuk mengelola berbagai jenis laporan, mulai dari pengaduan layanan publik hingga pelaporan masalah lingkungan, keamanan, atau sosial. Dengan sistem ini, pelapor dapat mengirimkan laporan beserta bukti pendukung, sementara admin atau pengelola dapat memverifikasi, memproses, dan menindaklanjuti setiap laporan secara terpusat.

Proyek ini dikembangkan dengan pendekatan full-stack sederhana namun skalabel, sehingga cocok digunakan oleh instansi pemerintah, sekolah, kampus, komunitas, atau organisasi mana pun yang membutuhkan sistem pengelolaan pengaduan yang efisien.

Fitur Utama

Berikut adalah fitur-fitur utama yang tersedia dalam aplikasi SiPelapor:

-Formulir pengaduan online dengan input teks, kategori laporan, dan unggahan file (gambar/dokumen)

-Panel admin untuk mengelola, memverifikasi, dan menindaklanjuti laporan

-Database SQLite yang ringan dan mudah dipindahkan

-Tampilan antarmuka berbasis HTML dan CSS yang responsif

-Server pengembangan bawaan Django untuk proses development dan pengujian

-Dukungan ngrok untuk akses sementara ke aplikasi dari jaringan luar

Teknologi yang Digunakan

-Python 3.x: Bahasa pemrograman utama untuk logika backend

-Django: Web framework yang digunakan untuk membangun aplikasi

-SQLite: Basis data ringan untuk menyimpan data laporan dan pengguna

-HTML, CSS, JavaScript: Untuk antarmuka pengguna sisi depan

-ngrok: Alat untuk membuka tunnel lokal ke internet (untuk pengujian eksternal)

Cara Menjalankan Proyek Secara Lokal

Ikuti langkah-langkah berikut untuk menjalankan proyek SiPelapor di komputer Anda:

1.Clone repositori ini:
git clone https://github.com/sams-13/SiPelapor.git

2.Masuk ke direktori proyek:
cd SiPelapor

3.(Opsional) Buat virtual environment dan aktifkan:
python -m venv venv
(Di Windows) venv\Scripts\activate
(Di macOS/Linux) source venv/bin/activate

4.Instal dependensi yang diperlukan:
pip install django

5.Jalankan migrasi database (django akan membuat file db.sqlite3 secara otomatis):
python manage.py migrate

6.Buat akun superuser untuk mengakses panel admin:
python manage.py createsuperuser

7.Jalankan server pengembangan Django:
python manage.py runserver

8.Buka browser dan akses alamat:
http://127.0.0.1:8000
Panel admin dapat diakses di http://127.0.0.1:8000/admin

Catatan: Aplikasi ini sudah menyertakan file db.sqlite3 dan ngrok.exe untuk kebutuhan pengujian. Pastikan Anda memiliki Python yang terinstal di sistem.

Demo Langsung

Lihat langsung hasil akhir proyek ini dalam aksi di sini:
https://sams-13.github.io/SiPelapor/

(Catatan: Jika halaman tidak dapat diakses, kemungkinan aplikasi sedang dalam tahap pengembangan atau belum di-deploy secara publik. Silakan clone repositori ini dan jalankan secara lokal.)

Kontribusi

Kami sangat terbuka terhadap kontribusi dari siapa pun. Jika Anda ingin menambahkan fitur baru, memperbaiki bug, atau meningkatkan antarmuka pengguna, silakan lakukan langkah-langkah berikut:

1.Fork repositori ini.

2.Buat branch baru untuk fitur atau perbaikan Anda:
git checkout -b fitur-baru

3.Lakukan commit pada perubahan Anda:
git commit -m 'Menambahkan fitur baru'

4.Push ke branch Anda:
git push origin fitur-baru

5.Buka Pull Request dan jelaskan perubahan Anda secara rinci.

Lisensi

Proyek ini dilisensikan di bawah MIT License. Anda bebas menggunakan, menyalin, memodifikasi, dan mendistribusikan kode ini, selama menyertakan lisensi asli. Silakan lihat file LICENSE untuk informasi lebih lanjut.

Kontak

Jika ada pertanyaan, saran, atau sekadar ingin berkenalan, hubungi melalui:

Email: alqassamamuhammad@gmail.com

GitHub: sams-13

Jangan lupa untuk memberi bintang (star) pada repositori ini jika Anda merasa proyek ini bermanfaat.
