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

## menu utama
<img width="1146" height="1607" alt="DDP FLOWCHART PA rev-menu utama" src="https://github.com/user-attachments/assets/77722d1c-84fd-41e4-946f-fc33ebcca8a9" />

## menu admin
<img width="4108" height="3059" alt="DDP FLOWCHART PA rev-Menu admin " src="https://github.com/user-attachments/assets/0dabe2c9-c5cf-44f3-9215-061f4c483599" />

## menu user
<img width="1511" height="1567" alt="DDP FLOWCHART PA rev-menu user" src="https://github.com/user-attachments/assets/84581266-d0cf-49bc-99ed-355b3ce83552" />

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

### 4. Menu Admin

<img width="336" height="217" alt="Screenshot 2026-11-02 232023" src="https://github.com/user-attachments/assets/886dbe20-1b38-477f-942d-3160d6081112" />

Ini adalah tampilan dan pilihan menu jika role pengguna adalah admin. 

#### 4.1. menu 1 admin

<img width="455" height="177" alt="Screenshot 2026-11-02 232638" src="https://github.com/user-attachments/assets/961786e7-8c30-4c74-bdef-2233640fd780" />

menu kelola layanan digunakan admin untuk mengatur data layanan klinik.terdapat fitur melihat,menambah,mengubah,dan menghapus layanan beserta harga yang tersedia.

#### 4.2. menu 2 admin

<img width="415" height="202" alt="Screenshot 2026-11-02 233130" src="https://github.com/user-attachments/assets/146b35dc-955b-46b7-936d-318959e1a6a9" />

Menu kelola pengguna digunakan untuk melihat daftar akun pengguna yg terdaftar,mengubah role pengguna menjadi admin atau user,,serta menghapus akun pengguna.

#### 4.3. menu 3 admin

<img width="882" height="212" alt="image" src="https://github.com/user-attachments/assets/4cb8e43a-2650-436b-b37e-a7c0ceb9188c" />

Digunakan untuk menampilkan seluruh riwayat transaksi yang dilakukan oleh semua pengguna, baik transaksi top-up maupun pembayaran layanan klinik.

#### 4.4. menu 4 admin

<img width="319" height="212" alt="Screenshot 2026-11-02 235228" src="https://github.com/user-attachments/assets/2066cc0d-0ab4-4b77-8d84-8292ce2d2048" />

Digunakan untuk menampilkan ringkasan laporan transaksi, seperti jumlah transaksi, transaksi berhasil, total top-up saldo, dan total pembayaran layanan.

#### 4.5. Menu 5 admin

<img width="288" height="203" alt="Screenshot 2026-11-02 235520" src="https://github.com/user-attachments/assets/4db92e49-8f74-431f-9b7d-8de411205964" />

digunakan untuk mengakhiri sesi login admin dan kembali ke tampilan awal.










