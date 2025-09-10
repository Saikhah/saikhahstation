1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Jawab: 
   pada tahap awal, saya membuat repositori baru di github dengan nama saikhahstation untuk menyimpan seluruh kode proyek. setelah itu, saya menyiapkan lingkungan kerja dengan menginstal django serta beberapa dependensi lain yang dibutuhkan. selanjutnya, saya membuat proyek django bernama saikhahstation sekaligus menambahkan aplikasi utama bernama main. di aplikasi tersebut, saya mulai mendefinisikan model yang relevan dengan kebutuhan proyek, seperti model produk yang memuat atribut nama, harga, deskripsi, kategori, dan lain-lain.

   setelah model selesai dibuat, saya menghubungkannya dengan view agar data dapat diproses dan kemudian ditampilkan melalui template. saya juga menyusun konfigurasi routing dengan menambahkan path pada urls.py, sehingga setiap permintaan dari pengguna dapat diarahkan ke view yang sesuai. untuk memastikan aplikasi berjalan dengan baik, saya melakukan migrasi basis data dan menjalankan server secara lokal, lalu memverifikasi bahwa halaman dapat diakses melalui browser.

   tahap berikutnya adalah pengaturan variabel lingkungan. saya membuat berkas .env untuk kebutuhan pengembangan lokal dan menyiapkan konfigurasi berbeda untuk mode produksi. dengan cara ini, proyek tetap aman dan fleksibel, baik saat dijalankan di komputer pribadi maupun ketika dideploy ke server. setelah semuanya selesai, saya melakukan commit perubahan, mendorongnya ke github, dan menyiapkan proses deployment agar aplikasi saikhahstation dapat diakses melalui alamat publik.

   sebagai rangkuman, langkah-langkah yang saya lakukan dapat diuraikan sebagai berikut:
        1.	membuat repositori baru di github dengan nama saikhahstation.
        2.	menginstal django.
        3.	membuat proyek django bernama saikhahstation.
        4.	menambahkan aplikasi utama bernama main.
        5.	mendefinisikan model produk pada models.py.
        6.	menghubungkan model dengan view dan template.
        7.	mengatur routing di urls.py agar request terhubung ke view.
        8.	menjalankan migrasi basis data.
        9.	menguji aplikasi dengan server lokal melalui browser.
        10.	menyiapkan variabel lingkungan untuk konfigurasi lokal dan produksi.
        11.	melakukan commit dan push ke github.
        12.	menyiapkan deployment agar aplikasi dapat diakses secara publik.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   Jawab:
   ![alt text](image-1.png)
   
   Penjelasannya:
   - urls.py berfungsi sebagai pemetaan (routing) yang menghubungkan permintaan dari client ke fungsi yang sesuai pada views.py.
   - views.py bertugas memproses logika aplikasi sesuai permintaan, misalnya mengambil data dari basis data atau memanggil fungsi tertentu.
   - models.py berisi definisi struktur basis data dalam bentuk kelas. View dapat memanfaatkan model untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada basis data.
   - Template HTML digunakan untuk merender data yang diproses view sehingga dapat ditampilkan kembali ke pengguna.
   - Hasil akhirnya adalah response berupa halaman web yang dikembalikan ke client.


3. Jelaskan peran settings.py dalam proyek Django!
   Jawab:
   dalam proyek django, berkas settings.py berperan sebagai pusat konfigurasi utama yang menentukan bagaimana aplikasi dijalankan, baik pada lingkungan pengembangan maupun produksi. file ini memuat berbagai pengaturan penting, seperti daftar aplikasi yang digunakan (installed apps), middleware, konfigurasi basis data, direktori template, hingga pengaturan keamanan seperti secret key dan allowed hosts. dengan kata lain, settings.py menjadi fondasi yang mengatur interaksi antar-komponen dalam proyek django.

   pada proyek saikhahstation, saya memanfaatkan settings.py untuk menghubungkan aplikasi dengan database, menambahkan aplikasi main ke dalam INSTALLED_APPS, serta mengatur template dan routing agar dapat berjalan dengan benar. selain itu, saya juga menambahkan logika pemilihan konfigurasi berdasarkan environment variables sehingga proyek dapat membedakan mode pengembangan dan produksi. hal ini menjadikan settings.py tidak hanya sebagai file konfigurasi standar, tetapi juga sebagai sarana untuk menjaga fleksibilitas dan keamanan aplikasi.

4. Bagaimana cara kerja migrasi database di Django?
   Jawab:
   migrasi merupakan mekanisme untuk menyesuaikan struktur basis data dengan model yang didefinisikan pada models.py. proses ini dilakukan dalam dua tahap:
	1.	perintah python manage.py makemigrations menghasilkan berkas migrasi berdasarkan perubahan model.
	2.	perintah python manage.py migrate mengeksekusi migrasi tersebut sehingga struktur basis data diperbarui sesuai model.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
   Jawab:
   menurut saya alasan Django dipilih sebagai framework awal dalam pembelajaran pengembangan perangkat lunak karena menggunakan bahasa Python yang relatif mudah dipelajari. selain itu, Django menyediakan berbagai fitur bawaan seperti ORM, autentikasi, dan admin panel sehingga mahasiswa dapat lebih cepat memahami alur pengembangan aplikasi web secara menyeluruh. dokumentasi Django yang lengkap dan komunitas yang luas juga memudahkan proses pembelajaran. framework ini menerapkan konsep MVT yang melatih mahasiswa berpikir terstruktur dalam membangun aplikasi.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
   Jawab:
   tidak ada. 