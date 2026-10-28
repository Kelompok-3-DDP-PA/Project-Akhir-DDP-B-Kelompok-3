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

