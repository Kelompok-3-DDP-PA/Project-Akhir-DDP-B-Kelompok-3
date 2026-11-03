# Projek Akhir Kelompok 3 Dasar Dasar Pemrograman

# Sistem Pembayaran dan Administrasi Klinik

# 1. Anggota Kelompok dan peran
1.Muhammad Atha Andhika | Project Leader, memastikan semua anggota berkontribusi dan berkerja sama satu dengan lainnya, merancang alur dan struktur program, membuat programnya serta melakukan pengawasan dan testing.

2.Nabilah Rahmadhani | Anggota, membuat flowchart untuk menggambarkan alur kerja program secara sistematis, menyusun laporan, dan file README yang berisi penjelasan dan fitur-fitur program.

3.Annisa Maulida Rizky | Anggota, membantu pembuatan flowchart, menyusun laporan, dan file readme fitur setiap role dan output penjelasan bagian menu user

4.Mario Bawa Welan | Anggota, membantu pembuatan code dan testing code, menyusun laporan

# 2. Deskripsi dan Tujuan

Sistem Pembayaran dan Administrasi Klinik merupakan program berbasis Python yang dirancang untuk membantu proses pengelolaan administrasi dan transaksi pembayaran layanan klinik. Program ini menyediakan beberapa fitur, seperti registrasi dan login pengguna, pengelolaan data layanan klinik, top-up saldo, pembayaran layanan, serta pencatatan riwayat transaksi. Program juga menerapkan dua hak akses pengguna, yaitu admin dan user, dengan kewenangan yang berbeda. Admin memiliki akses untuk mengelola data layanan dan pengguna serta melihat laporan transaksi, sedangkan user dapat melakukan top-up saldo, pembayaran layanan, dan melihat riwayat transaksinya.

Pembuatan program ini bertujuan untuk menerapkan konsep dasar pemrograman Python yang telah dipelajari, meliputi penggunaan variabel, tipe data, percabangan, perulangan, fungsi, pengolahan file CSV, validasi input, serta penggunaan library tambahan. Selain itu, program ini dibuat untuk memberikan gambaran sederhana mengenai penerapan sistem informasi dalam proses administrasi dan pembayaran layanan klinik, khususnya dalam pengelolaan data pengguna, layanan, saldo, dan transaksi secara terstruktur.

Program ini juga disusun sebagai salah satu syarat untuk menyelesaikan Final Project Praktikum Dasar-Dasar Pemrograman, Program Studi Sistem Informasi, Fakultas Teknik, Universitas Mulawarman. Melalui pengerjaan proyek ini, diharapkan kemampuan dalam memahami logika pemrograman, mengintegrasikan berbagai materi yang telah dipelajari, serta mengembangkan program yang fungsional dan terstruktur dapat semakin meningkat.

# 3. Flowchart Program

## 1. menu utama
<img width="1146" height="1607" alt="FLOWCHART PA DDP 3 -menu utama" src="https://github.com/user-attachments/assets/6429593f-13fc-428e-a432-29451dc4800f" />

Menu utama merupakan bagian awal program Administrasi Transaksi Klinik yang berfungsi sebagai pintu masuk bagi pengguna untuk mengakses fitur yang tersedia. Pada bagian ini, program menampilkan tiga pilihan, yaitu login, registrasi, dan keluar program.

a. Menampilkan Menu Utama

Program menampilkan pilihan login, registrasi, dan keluar program. Pengguna memasukkan pilihan sesuai kebutuhan. Jika pilihan tidak tersedia, program menampilkan pesan kesalahan dan mengarahkan pengguna kembali ke menu utama.

b. Proses Login

Jika pengguna memilih login, program meminta username dan password. Setiap input diperiksa untuk memastikan tidak kosong. Jika input kosong, program menampilkan pesan kesalahan dan meminta pengguna memasukkan data kembali.

Setelah username dan password diisi, program memeriksa kecocokan data dengan database pengguna. Jika data benar, program menampilkan pesan login berhasil. Jika data salah, program menampilkan pesan bahwa username atau password salah dan mencatat percobaan login. Pengguna dapat mencoba kembali selama kesempatan login belum habis. Jika kesempatan habis, program mengarahkan pengguna kembali ke menu utama.

Setelah login berhasil, program memeriksa peran atau role pengguna. Jika pengguna berperan sebagai admin, program mengarahkannya ke menu admin. Jika pengguna bukan admin, program mengarahkannya ke menu user.

c. Proses Registrasi

Jika pengguna memilih registrasi, program meminta username, password, dan nama lengkap. Setiap input diperiksa untuk memastikan tidak kosong.

Username harus terdiri dari minimal 4 karakter, sedangkan password harus terdiri dari minimal 8 karakter. Jika input tidak memenuhi ketentuan, program menampilkan pesan kesalahan dan meminta pengguna memasukkan data kembali.

Jika seluruh data memenuhi ketentuan, program menyimpan data pengguna ke database. Selanjutnya, program menampilkan informasi bahwa data pengguna telah dibuat dan mengarahkan pengguna kembali ke menu utama.

d. Keluar Program

Jika pengguna memilih opsi keluar program, program mengakhiri proses. Dengan demikian, pengguna dapat keluar tanpa melanjutkan ke proses login atau registrasi.

## 2. menu admin 
<img width="4108" height="3059" alt="FLOWCHART PA DDP 3 -Menu admin " src="https://github.com/user-attachments/assets/6cabeca1-79d7-4a98-a9da-021fa10d9f7f" />

Menu admin merupakan bagian program yang digunakan oleh administrator untuk mengelola data dalam sistem Administrasi Transaksi Klinik. Setelah berhasil login sebagai admin, program mengarahkan pengguna ke menu admin untuk mengakses fitur sesuai dengan hak aksesnya.

a. Menampilkan Menu Admin

Program menampilkan pilihan menu yang dapat digunakan oleh admin. Admin memilih fitur yang ingin dijalankan. Jika pilihan sesuai dengan menu yang tersedia, program menjalankan proses berdasarkan pilihan tersebut. Jika pilihan tidak tersedia, program menampilkan pesan kesalahan dan meminta admin memilih kembali.

b. Menampilkan Data

Ketika admin memilih menu untuk melihat data, program mengambil data dari database yang sesuai. Data tersebut kemudian diproses dan ditampilkan agar admin dapat memeriksa informasi yang tersimpan dalam sistem.

c. Pengelolaan Data Layanan

Menu pengelolaan data layanan digunakan untuk mengatur informasi layanan klinik yang tersimpan dalam sistem. Program mengambil data dari file CSV dan menampilkannya kepada admin agar dapat diperiksa serta dikelola sesuai kebutuhan.

Di dalam menu ini, admin dapat melihat daftar layanan, menambahkan layanan baru, mengubah nama dan harga layanan, serta menghapus layanan yang sudah tidak diperlukan. Setiap tindakan dilengkapi validasi untuk memastikan data yang dimasukkan sesuai dengan ketentuan program.

d. Pengelolaan Data Pengguna

Menu pengelolaan data pengguna digunakan untuk mengatur informasi akun yang telah terdaftar dalam sistem. Program mengambil data pengguna dari file CSV dan menampilkannya dalam bentuk tabel agar admin dapat memeriksa informasi setiap akun.

Melalui menu ini, admin dapat mengubah hak akses pengguna antara admin dan user serta menghapus akun tertentu. Program juga menerapkan pembatasan agar akun admin utama tidak dapat diubah maupun dihapus.

e. Pengelolaan Seluruh Transaksi

Menu pengelolaan seluruh transaksi digunakan untuk memantau seluruh aktivitas transaksi yang dilakukan oleh pengguna. Program mengambil data dari file transaksi CSV, kemudian mengolah dan menampilkannya dalam bentuk tabel.

Informasi yang ditampilkan meliputi ID transaksi, waktu transaksi, username, jenis transaksi, nama layanan, nominal pembayaran, dan status transaksi. Dengan demikian, admin dapat memeriksa aktivitas top-up saldo maupun pembayaran layanan yang tercatat dalam sistem.

f. Laporan Transakasi

Menu laporan transaksi digunakan untuk menyajikan ringkasan aktivitas transaksi secara keseluruhan. Program mengolah data transaksi yang tersimpan untuk menghasilkan informasi mengenai jumlah dan nominal transaksi.

Laporan ini mencakup total transaksi, jumlah transaksi berhasil, total nominal top-up, total pembayaran layanan, serta riwayat transaksi seluruh pengguna. Informasi tersebut membantu admin memantau aktivitas pembayaran dan melihat rekapitulasi transaksi dalam sistem.

g. Validasi Input

Validasi input dilakukan untuk memastikan bahwa data yang dimasukkan admin memenuhi ketentuan program. Validasi ini dapat mencakup pemeriksaan input kosong dan kesesuaian data dengan persyaratan yang ditetapkan. Jika terjadi kesalahan, program menampilkan pesan dan meminta admin memasukkan data kembali.

h. Penyimpanan dan Penampilan Hasil

Setelah input dinyatakan valid, program memproses data sesuai dengan pilihan admin. Jika terdapat perubahan data, program menyimpan perubahan tersebut ke database yang berkaitan. Program kemudian menampilkan hasil pemrosesan agar admin dapat mengetahui hasil dari tindakan yang dilakukan.

i. Logout dan Keluar Program

Jika admin memilih logout, program mengakhiri sesi admin dan mengarahkan pengguna kembali ke menu utama. Jika admin memilih keluar program, program mengakhiri proses secara keseluruhan.

## 3. menu user
<img width="1511" height="1608" alt="FLOWCHART PA DDP 3 -menu user" src="https://github.com/user-attachments/assets/a9bdb1f5-6a1e-4621-bfd2-01e0aeebafda" />

Menu user merupakan bagian program yang digunakan oleh pengguna biasa untuk mengakses layanan klinik dan melakukan transaksi. Setelah berhasil login sebagai user, program mengambil dan menampilkan data pengguna dari database, kemudian menampilkan menu yang tersedia.

a. Menampilkan Menu User

Program menampilkan lima pilihan menu, yaitu melihat layanan, top up saldo, membayar layanan, melihat riwayat transaksi, dan logout. Pengguna dapat memilih fitur sesuai kebutuhan. Jika pilihan tidak tersedia, program menampilkan pesan kesalahan dan meminta pengguna memilih kembali.

b. Menu Lihat Layanan

Ketika pengguna memilih menu lihat layanan, program mengambil data layanan dari database layanan. Data tersebut kemudian diproses dan ditampilkan dalam bentuk daftar layanan yang tersedia. Setelah daftar layanan ditampilkan, pengguna diarahkan kembali ke menu user.

c. Menu Top Up Saldo

Pada menu top up, program meminta pengguna memasukkan nominal saldo yang ingin ditambahkan. Program memeriksa apakah input kosong dan apakah nominal berupa bilangan bulat. Jika input tidak sesuai, program menampilkan pesan kesalahan dan meminta pengguna memasukkan nominal kembali.

Nominal top up harus berada dalam rentang Rp1.000 hingga Rp10.000.000. Jika nominal berada di luar batas tersebut, program menampilkan informasi mengenai batas nominal yang diperbolehkan.

Jika nominal memenuhi ketentuan, program meminta konfirmasi kepada pengguna. Jika pengguna menyetujui top up, data transaksi disimpan ke database transaksi dan program menampilkan invoice. Jika pengguna membatalkan, program menampilkan informasi bahwa top up dibatalkan.

d. Menu Bayar Layanan

Ketika pengguna memilih menu bayar layanan, program meminta pengguna memasukkan ID layanan. Jika input kosong, program menampilkan pesan kesalahan dan meminta ID layanan dimasukkan kembali.

Selanjutnya, program memeriksa apakah layanan dengan ID tersebut tersedia. Jika layanan ditemukan, program akan memeriksa apakah saldo mencukupi untuk membayar layanan, Jika cukup maka program akan menampilkan informasi pembayaran dan meminta konfirmasi. Jika layanan tidak ditemukan dan saldo tidak mencukupi, program menampilkan pesan bahwa layanan tidak tersedia dan saldo tidak mencukupi.

Jika pengguna menyetujui pembayaran, data transaksi disimpan ke database transaksi dan program menampilkan invoice. Jika pengguna membatalkan pembayaran, program menampilkan informasi bahwa pembayaran dibatalkan.

e. Menu Riwayat Transaksi

Menu riwayat transaksi digunakan untuk melihat transaksi yang telah tercatat. Program mengambil data dari database transaksi, memprosesnya, kemudian menampilkan riwayat transaksi kepada pengguna. Setelah proses selesai, pengguna dapat kembali ke menu user.

f. Logout dan Keluar Program

Jika pengguna memilih logout, program mengakhiri sesi akun dan mengarahkan pengguna kembali ke menu utama. Jika pengguna memilih keluar program, program mengakhiri proses secara keseluruhan.

# 4. Fitur Setiap Role
## 1. User
   User memiliki menu untuk melihat layanan yang tersedia, menu top-up dengan minimal top-up Rp 1000 dan akan menampilkan       invoice jika top-up berhasil dilakukan, menu untuk membayar layanan yang tersedia dan akan menampilkan invoice jika          pembayaran berhasil, menu untuk melihat riyawat transaksi yang telah dilakukan, dan menu untuk logout dari akun, serta       menu untuk keluar dari programnya.
## 2. Admin
   Admin memiliki menu untuk mengelola layanan mulai dari melihat layanan, menambah layanan, mengubah layanan, dan              menghapus layanan. Lalu admin memiliki menu untuk mengelola data user mulai dari mengubah role user hingga menghapus         akun user. Selanjutnya menu untuk melihat riwayat transaksi yang ada/telah dilakukan. Lalu menu untuk melihat laporan        transaksi, seperti transaksi apa yang dilakukan, total transaksi yang berhasil, total top-up dan total layanan yang          dibayar. Menu logout dan menu untuk keluar dari program. 

# 5. Output dan penjelasan 

## 1. Tampilan Awal(Menu Utama)

<img width="318" height="130" alt="Screenshot 2026-10-29 142201" src="https://github.com/user-attachments/assets/1e15801b-c2c2-4cf9-a5e8-87653b305c69" />


Pada Tampilan awal berisi menu login, registrasi akun, dan menu keluar dari program. Jika anda admin, silahkan langsung login. Namun jika anda adalah user dan belum memiliki akun, silahkan melakukan registrasi terlebih dahulu sebelum login. Untuk menu keluar program juga tersedia pada pilihan menu user dan admin, dimana jika memilih menu tersebut maka program selesai. 

### 1.1. Menu Registrasi Akun

<img width="381" height="190" alt="Screenshot 2026-10-29 142504" src="https://github.com/user-attachments/assets/813739e7-fd6c-4c5a-b3bf-9c62a739fc72" />

Pada menu ini, silahkan buat username dan memasukkannya ke dalam program. Setelah itu silahkan masukkan password dan konfismasi password yang telah dibuat, lalu masukkan nama pengguna, maka registrasi akun telah berhasil dan silahkan  lakukan login dengan akun yang baru dibuat.

### 1.2. Menu Login

<img width="323" height="326" alt="Screenshot 2026-10-29 144930" src="https://github.com/user-attachments/assets/fcd71ae0-f14f-4613-a741-9c980219d809" />


Pada menu ini, silahkan login dengan memasukkan username dan password, pengguna akan memiliki 3 kali kesempatan login dimana jika pengguna salah memasukkan username atau password, maka kesempatan login akan berkurang 1. Jika login berhasil maka akan masuk ke tampilan menu sesuai dengan role nya. 

## 2. Menu User

<img width="358" height="235" alt="Screenshot 2026-10-29 142537" src="https://github.com/user-attachments/assets/3d2b06a6-1e17-4797-a32f-8f85be97b767" />

Menu user merupakan tampilan utama yang diberikan kepada pengguna dengan hak akses sebagai user. Pada bagian ini, program menampilkan informasi akun berupa nama pengguna, username, dan jumlah saldo yang dimiliki. Selain itu, terdapat beberapa pilihan fitur, yaitu melihat layanan, melakukan top-up saldo, membayar layanan, melihat riwayat transaksi, logout, dan keluar program. Pengguna dapat memilih fitur sesuai kebutuhan, kemudian program akan menjalankan proses berdasarkan pilihan tersebut.

### 2.1. Menu daftar layanan klinik 

<img width="393" height="272" alt="Screenshot 2026-10-29 142553" src="https://github.com/user-attachments/assets/7f71102b-0573-45a5-b640-6f01dce21d94" />

Berikut adalah tampilan dari menu 1 user, yaitu melihat layanan yang tersedia. 

### 2.2. Menu top up

<img width="353" height="447" alt="Screenshot 2026-10-29 142629" src="https://github.com/user-attachments/assets/400cd993-57b5-49a0-aec5-838c805c0c6d" />

Berikut adalah tampilan dari menu 2 user, yaitu top-up saldo. Pengguna akan diminta untuk memasukkan nominal top-up dengan minimal top-up adalah Rp 1000 dan mengkonfirmasi pembayarannya. Setelah berhasil maka akan muncul sebuah Invoice yang berisi informasi transaksi dan rincian saldo.

### 2.3. Menu bayar layanan 

<img width="406" height="446" alt="Screenshot 2026-10-29 142746" src="https://github.com/user-attachments/assets/040e449f-faba-40c2-af27-5a9354773738" />

<img width="371" height="452" alt="Screenshot 2026-10-29 142803" src="https://github.com/user-attachments/assets/c55de0ee-a474-4e57-a36c-ce4a603c51b2" />


Berikut adalah tampilan dari menu 3 user, yaitu pembayaran layanan. Pertama akan muncul layanan apa saja yang tersedia lalu pengguna akan diminta untuk memasukkan id layanan yang ingin dibayar dan akan muncul rincian dari transaksi dan pengguna diminta untuk konfirmasi pembayaran. Jika pengguna memilih tidak maka pembayaran dibatlakan. Jika pengguna memilih ya, maka pembayaran berhasil dan akan menampilkan invoice dengan informasi transaksi, rincian layanan, dan rincian saldo. Saldo dari pengguna akan otomatis terpotong jika mengkonfirmasi pembayaran. 

### 2.4. Menu lihat riwayat transaksi

<img width="846" height="178" alt="Screenshot 2026-10-29 142823" src="https://github.com/user-attachments/assets/e807437e-fa90-4384-8b6e-945dd83463b7" />

Berikut adalah tampilan dari menu 4 user, yaitu melihat riwayat transaksi yang sudah dilakukan(top-up atau membayar layanan).

### 2.5. Menu logout

<img width="340" height="285" alt="Screenshot 2026-10-29 142839" src="https://github.com/user-attachments/assets/424882ba-bc67-4e96-9163-f868122c8c93" />

Menu 5 adalah menu untuk logout dari akun yang digunakan, setelah logout berhasil maka akan kembali ke menu tampilan awal. 

## 3. Menu Admin

<img width="336" height="217" alt="Screenshot 2026-11-02 232023" src="https://github.com/user-attachments/assets/886dbe20-1b38-477f-942d-3160d6081112" />

Ini adalah tampilan dan pilihan menu jika role pengguna adalah admin. 

### 3.1. Menu kelola layanan

<img width="455" height="177" alt="Screenshot 2026-11-02 232638" src="https://github.com/user-attachments/assets/961786e7-8c30-4c74-bdef-2233640fd780" />

Menu kelola layanan digunakan admin untuk mengatur data layanan klinik. Terdapat fitur melihat, menambah, mengubah, dan menghapus layanan.

#### 3.1.1 Menu Melihat Layanan

<img width="394" height="242" alt="Screenshot 2026-11-03 145843" src="https://github.com/user-attachments/assets/5870165b-2e09-406e-8a08-35c859fbe93e" />

Menu melihat layanan digunakan oleh admin untuk menampilkan seluruh data layanan klinik yang tersedia di dalam sistem. Program mengambil data dari database layanan, kemudian memproses dan menampilkannya dalam bentuk tabel yang memuat ID layanan, nama layanan, serta harga masing-masing layanan. Melalui menu ini, admin dapat mengetahui daftar layanan yang sedang tersedia beserta biaya yang dikenakan. Informasi tersebut juga dapat digunakan sebagai acuan dalam melakukan pengelolaan layanan, seperti penambahan, perubahan, maupun penghapusan data layanan.

#### 3.1.2 Menu Menambah Layanan

<img width="327" height="187" alt="Screenshot 2026-11-03 181125" src="https://github.com/user-attachments/assets/e8992b1b-a91a-4068-9748-8c887e02f06e" />

Menu Tambah Layanan digunakan oleh admin untuk menambahkan layanan klinik baru. Admin diminta memasukkan ID layanan, nama layanan, dan harga. Sistem akan memvalidasi data agar ID dan nama layanan tidak duplikat serta harga yang dimasukkan harus berupa angka lebih dari nol.

#### 3.1.3 Menu Mengubah Layanan

<img width="300" height="219" alt="Screenshot 2026-11-03 181346" src="https://github.com/user-attachments/assets/24d4bc11-b84e-44fe-954d-f17551ecca84" />

Menu Ubah Layanan digunakan untuk memperbarui data layanan klinik yang sudah terdaftar. Admin dapat mengubah nama dan harga layanan berdasarkan ID layanan yang dipilih. Sistem akan memeriksa ID layanan terlebih dahulu sebelum menyimpan perubahan.

#### 3.1.4 Menu Menghapus Layanan

<img width="429" height="209" alt="Screenshot 2026-11-03 181434" src="https://github.com/user-attachments/assets/e38166ce-dc57-4f3b-a050-501f4774e417" />

Menu Hapus Layanan digunakan untuk menghapus layanan yang sudah tidak diperlukan dari daftar layanan klinik. Admin memasukkan ID layanan yang ingin dihapus, kemudian melakukan konfirmasi sebelum sistem menghapus data tersebut.

### 3.2. menu kelola pengguna

<img width="415" height="202" alt="Screenshot 2026-11-02 233130" src="https://github.com/user-attachments/assets/146b35dc-955b-46b7-936d-318959e1a6a9" />

Menu kelola pengguna digunakan untuk melihat daftar akun pengguna yg terdaftar, mengubah role pengguna menjadi admin atau user, serta menghapus akun pengguna.

#### 3.2.1 Menu Mengubah Role Pengguna

<img width="284" height="193" alt="Screenshot 2026-11-03 181806" src="https://github.com/user-attachments/assets/5b15f2e9-de04-4805-8507-1e3c86ffec6d" />

Menu Mengubah Role Pengguna digunakan oleh admin untuk mengubah hak akses akun pengguna. Role pengguna dapat diubah menjadi Admin atau User sesuai kebutuhan. Sistem juga melakukan validasi agar role yang dimasukkan sesuai dengan pilihan yang tersedia.

#### 3.2.2 Menu Menghapus Pengguna

<img width="314" height="169" alt="Screenshot 2026-11-03 181831" src="https://github.com/user-attachments/assets/b1b3eec2-1362-4998-b4da-366e8fe54d04" />

Menu Menghapus Pengguna digunakan oleh admin untuk menghapus akun pengguna yang sudah tidak diperlukan. Admin memasukkan username akun yang ingin dihapus dan melakukan konfirmasi sebelum penghapusan dilakukan. Akun admin utama tidak dapat dihapus melalui fitur ini.

### 3.3. menu lihat seluruh transaksi

<img width="778" height="303" alt="Screenshot 2026-11-03 183821" src="https://github.com/user-attachments/assets/4cb2fbc3-dbcd-4f58-b767-4c04f5d514a1" />

Menu lihat seluruh transaksi digunakan oleh admin untuk menampilkan seluruh riwayat transaksi yang dilakukan oleh semua pengguna. Program mengambil data dari database transaksi dan menampilkannya dalam bentuk tabel yang berisi ID transaksi, waktu transaksi, username, jenis transaksi, nama layanan, nominal, serta status transaksi. Informasi tersebut mencakup transaksi pengisian saldo (top-up) maupun pembayaran layanan klinik. Melalui menu ini, admin dapat memantau aktivitas transaksi seluruh pengguna serta memeriksa detail dan status setiap transaksi yang telah tercatat di dalam sistem.

### 3.4. menu laporan transaksi

<img width="770" height="531" alt="Screenshot 2026-11-03 183833" src="https://github.com/user-attachments/assets/20b2a892-d0a7-4347-b9c2-39c5d2bfc351" />

Menu laporan transaksi digunakan oleh admin untuk melihat ringkasan keseluruhan aktivitas transaksi yang tercatat di dalam sistem. Program mengambil dan mengolah data dari database transaksi untuk menampilkan beberapa informasi, yaitu total transaksi, jumlah transaksi berhasil, total pengisian saldo (top-up), serta total pembayaran layanan. Seluruh informasi tersebut ditampilkan dalam bentuk tabel ringkasan sehingga admin dapat memantau aktivitas transaksi dan mengetahui gambaran umum keuangan yang terjadi di dalam sistem.

### 3.5. Menu logout

<img width="288" height="203" alt="Screenshot 2026-11-02 235520" src="https://github.com/user-attachments/assets/4db92e49-8f74-431f-9b7d-8de411205964" />

Menu logout digunakan untuk mengakhiri sesi login admin dan mengembalikan pengguna ke tampilan awal program. Ketika admin memilih menu ini, program akan menampilkan pesan bahwa proses logout berhasil dan meminta pengguna menekan tombol Enter untuk melanjutkan. Setelah itu, sesi akun admin akan berakhir, tetapi program tetap berjalan sehingga pengguna dapat melakukan login kembali menggunakan akun yang terdaftar.










