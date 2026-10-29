# Project-Akhir-DDP-B-Kelompok-3

# Sistem Pembayaran dan Administrasi Klinik

# 1.Anggota Kelompok dan peran
1.Muhammad Atha Andhika | Project Leader, memastikan semua anggota berkontribusi dan berkerja sama satu dengan lainnya, merancang alur dan struktur program serta membuat programnya.

2.Nabilah Rahmadhani | Anggota, 

3.Annisa Maulida Rizky | Anggota, 

4.Mario Bawa Welan | Anggota,

# 2 Deskripsi dan Tujuan

Sistem Pembayaran dan Administrasi Klinik merupakan program berbasis Python yang digunakan untuk membantu pengelolaan layanan klinik dan transaksi pembayaran. Program ini menyediakan fitur registrasi dan login pengguna, pengelolaan data layanan, top-up saldo, serta pembayaran layanan klinik.

Tujuan pembuatan program ini adalah untuk menerapkan materi dasar pemrograman Python, seperti fungsi, percabangan, perulangan, pengolahan file CSV, validasi input, dan penanganan kesalahan. Data pengguna, layanan, dan transaksi disimpan menggunakan file CSV.

# 3 Flowchart Program
<img width="3219" height="2531" alt="DDP_kel 3" src="https://github.com/user-attachments/assets/2f375a62-258a-448a-8577-1d46284e8fc6" />

Flowchart menggambarkan alur sebuah program manajemen layanan klinik yang memiliki dua peran, yaitu admin dan user, lengkap dengan sistem login, registrasi, serta pengelolaan transaksi.

Program dimulai dari start, lalu menampilkan menu utama dengan tiga pilihan: 1. Login, 2. Registrasi, dan 0. Keluar program. Jika pengguna memilih angka selain ketiganya, program menampilkan pesan "pilihan tidak tersedia" dan kembali ke menu utama. Jika memilih 0, program langsung menuju End.Pada jalur registrasi, pengguna diminta memasukkan username baru, password baru, dan nama lengkap. Setelah itu program menampilkan data user yang telah dibuat, lalu kembali ke menu utama.

Pada jalur login, pengguna memasukkan username dan password, kemudian sistem memeriksa kebenarannya. Jika salah, sistem menampilkan pesan "username atau password salah", mengurangi jumlah percobaan login sebanyak satu, lalu memeriksa apakah kesempatan sudah habis. Bila belum habis, pengguna diminta mengisi username lagi. Bila sudah habis, program kembali ke menu utama. Jika benar, sistem menampilkan "login berhasil" dan memeriksa peran (role) pengguna. Jika role adalah admin, program menampilkan menu admin. Jika bukan, program menampilkan menu user.

Alur menu admin memiliki beberapa pilihan. Pilihan pertama adalah kelola layanan, yang membuka menu kelola layanan dengan empat fitur. Fitur lihat layanan menampilkan daftar layanan klinik. Fitur tambah layanan meminta id, nama, dan harga layanan baru, lalu menyimpannya ke database layanan dan menampilkan pesan berhasil ditambahkan. Fitur ubah layanan menampilkan daftar layanan, meminta id layanan, menampilkan data layanan tersebut, lalu meminta nama, harga, dan status baru (aktif atau nonaktif). Bila status yang dimasukkan tidak valid, sistem meminta input ulang. Bila valid, data disimpan ke database dan muncul pesan berhasil diubah. Fitur hapus layanan menampilkan daftar layanan, meminta id, lalu menanyakan konfirmasi. Jika yakin, data dihapus dari database; jika tidak, penghapusan dibatalkan. Pilihan 0 pada menu ini akan kembali ke menu admin, sedangkan input lain menampilkan pesan pilihan tidak valid dan kembali ke menu kelola layanan.

Pilihan kedua admin adalah kelola pengguna, yaitu menampilkan data pengguna dan memungkinkan admin mengubah saldo pengguna. Admin memasukkan username, melihat saldo sekarang, memasukkan saldo baru, lalu mengonfirmasi perubahan. Jika yakin, data disimpan ke database pengguna dan muncul pesan berhasil; jika tidak, perubahan dibatalkan. Pilihan ketiga adalah lihat seluruh transaksi, yang menampilkan riwayat transaksi seluruh pengguna. Pilihan keempat adalah laporan transaksi, yang menampilkan laporan untuk admin. Pilihan kelima adalah logout, yang membawa program kembali ke menu utama, dan pilihan 0 adalah keluar program menuju End.

Alur menu user terdiri dari beberapa pilihan. Pilihan lihat layanan memproses dan menampilkan daftar layanan. Pilihan top up meminta nominal, menyimpan data ke database transaksi, lalu menampilkan invoice. Pilihan bayar layanan meminta id layanan, lalu memeriksa validitasnya. Jika id tidak valid, sistem menampilkan "layanan tidak ada". Jika valid, sistem menampilkan rincian pembayaran dan menanyakan konfirmasi. Bila pengguna yakin, data disimpan ke database transaksi dan invoice ditampilkan; bila tidak, pembayaran dibatalkan. Pilihan lihat riwayat transaksi menampilkan riwayat transaksi milik user tersebut. Pilihan logout mengembalikan pengguna ke menu utama, sedangkan pilihan 0 mengakhiri program. Setelah setiap proses selesai, alur kembali ke menu user sehingga pengguna dapat memilih fitur lain hingga logout atau keluar.
Secara keseluruhan, program berjalan dalam perulangan menu: setiap fitur yang selesai dijalankan akan mengembalikan pengguna ke menu asalnya, dan program baru berhenti ketika pengguna memilih keluar program, yang mengarah ke End.

# Fitur Setiap Role
## 1. User
   User memiliki menu untuk melihat layanan yang tersedia, menu top-up dengan minimal top-up Rp 1000 dan akan menampilkan       invoice jika top-up berhasil dilakukan, menu untuk membayar layanan yang tersedia dan akan menampilkan invoice jika          pembayaran berhasil, menu untuk melihat riyawat transaksi yang telah dilakukan, dan menu untuk logout dari akun, serta       menu untuk keluar dari programnya.
## 2. Admin
   Admin memiliki menu untuk mengelola layanan mulai dari melihat layanan, menambah layanan, mengubah layanan, dan              menghapus layanan. Lalu admin memiliki menu untuk mengelola data user mulai dari mengubah role user hingga menghapus         akun user. Selanjutnya menu untuk melihat riwayat transaksi yang ada/telah dilakukan. Lalu menu untuk melihat laporan        transaksi, seperti transaksi apa yang dilakukan, total transaksi yang berhasil, total top-up dan total layanan yang          dibayar. Menu logout dan menu untuk keluar dari program. 

# Output dan penjelasan 

## 1. Tampilan Awal

<img width="318" height="130" alt="Screenshot 2026-10-29 142201" src="https://github.com/user-attachments/assets/1e15801b-c2c2-4cf9-a5e8-87653b305c69" />


Pada Tampilan awal berisi menu login, registrasi akun, dan menu keluar dari program. Jika anda admin, silahkan langsung login. Namun jika anda adalah user dan belum memiliki akun, silahkan melakukan registrasi terlebih dahulu sebelum login. Untuk menu keluar program juga tersedia pada pilihan menu user dan admin, dimana jika memilih menu tersebut maka program selesai. 

### 1. Menu Registrasi Akun

<img width="381" height="190" alt="Screenshot 2026-10-29 142504" src="https://github.com/user-attachments/assets/813739e7-fd6c-4c5a-b3bf-9c62a739fc72" />

Pada menu ini, silahkan buat username dan memasukkannya ke dalam program. Setelah itu silahkan masukkan password dan konfismasi password yang telah dibuat, lalu masukkan nama pengguna, maka registrasi akun telah berhasil dan silahkan  lakukan login dengan akun yang baru dibuat.

### 2. Menu Login

<img width="323" height="326" alt="Screenshot 2026-10-29 144930" src="https://github.com/user-attachments/assets/fcd71ae0-f14f-4613-a741-9c980219d809" />


Pada menu ini, silahkan login dengan memasukkan username dan password, pengguna akan memiliki 3 kali kesempatan login dimana jika pengguna salah memasukkan username atau password, maka kesempatan login akan berkurang 1. Jika login berhasil maka akan masuk ke tampilan menu sesuai dengan role nya. 

### 3. Menu User

<img width="358" height="235" alt="Screenshot 2026-10-29 142537" src="https://github.com/user-attachments/assets/3d2b06a6-1e17-4797-a32f-8f85be97b767" />

Ini adalah tampilan dan pilihan menu jika role pengguna adalah user dan bukan admin.

#### 3.1. Menu 1 User 

<img width="393" height="272" alt="Screenshot 2026-10-29 142553" src="https://github.com/user-attachments/assets/7f71102b-0573-45a5-b640-6f01dce21d94" />

Berikut adalah tampilan dari menu 1 user, yaitu melihat layanan yang tersedia. 

#### 3.2. Menu 2 User 

<img width="353" height="447" alt="Screenshot 2026-10-29 142629" src="https://github.com/user-attachments/assets/400cd993-57b5-49a0-aec5-838c805c0c6d" />

Berikut adalah tampilan dari menu 2 user, yaitu top-up saldo. Pengguna akan diminta untuk memasukkan nominal top-up dengan minimal top-up adalah Rp 1000 dan mengkonfirmasi pembayarannya. Setelah berhasil maka akan muncul sebuah Invoice yang berisi informasi transaksi dan rincian saldo.

#### 3.3. Menu 3 User 

<img width="406" height="446" alt="Screenshot 2026-10-29 142746" src="https://github.com/user-attachments/assets/040e449f-faba-40c2-af27-5a9354773738" />

<img width="371" height="452" alt="Screenshot 2026-10-29 142803" src="https://github.com/user-attachments/assets/c55de0ee-a474-4e57-a36c-ce4a603c51b2" />


Berikut adalah tampilan dari menu 3 user, yaitu pembayaran layanan. Pertama akan muncul layanan apa saja yang tersedia lalu pengguna akan diminta untuk memasukkan id layanan yang ingin dibayar dan akan muncul rincian dari transaksi dan pengguna diminta untuk konfirmasi pembayaran. Jika berhasil, maka akan menampilkan invoice dengan informasi transaksi, rincian layanan, dan rincian saldo. Saldo dari pengguna akan otomatis terpotong jika mengkonfirmasi pembayaran.

#### 3.4. Menu 4 User

<img width="846" height="178" alt="Screenshot 2026-10-29 142823" src="https://github.com/user-attachments/assets/e807437e-fa90-4384-8b6e-945dd83463b7" />

Berikut adalah tampilan dari menu 4 user, yaitu melihat riwayat transaksi yang sudah dilakukan(top-up atau membayar layanan).

#### 3.5. Menu 5 User

<img width="340" height="285" alt="Screenshot 2026-10-29 142839" src="https://github.com/user-attachments/assets/424882ba-bc67-4e96-9163-f868122c8c93" />

Menu 5 adalah menu untuk logout dari akun yang digunakan, setelah logout berhasil maka akan kembali ke menu tampilan awal. 
