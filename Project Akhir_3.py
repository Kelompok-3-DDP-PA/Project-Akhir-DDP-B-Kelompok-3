import csv
import os
import time
import random
import hashlib
from datetime import datetime
from prettytable import PrettyTable
from pwinput import pwinput
FOLDER_PROGRAM = os.path.dirname(os.path.abspath(__file__))
# Pengaturan lokasi file CSV
def lokasi_csv(nama_file):
    lokasi_program = os.path.join(FOLDER_PROGRAM, nama_file)
    lokasi_terminal = os.path.abspath(nama_file)
    if os.path.isfile(lokasi_program):
        return lokasi_program
    if os.path.isfile(lokasi_terminal):
        return lokasi_terminal
    return lokasi_program
FILE_USERS = lokasi_csv("users.csv")
FILE_LAYANAN = lokasi_csv("layanan.csv")
FILE_TRANSAKSI = lokasi_csv("transaksi.csv")
ROLE_PENGGUNA = ("admin", "user")

KOLOM_USERS = [
    "username",
    "password_hash",
    "role",
    "saldo",
    "nama"
]
KOLOM_LAYANAN = [
    "id_layanan",
    "nama_layanan",
    "harga"
]
KOLOM_TRANSAKSI = [
    "id_transaksi",
    "waktu",
    "username",
    "jenis",
    "id_layanan",
    "nama_layanan",
    "jumlah",
    "nominal",
    "saldo_awal",
    "saldo_akhir",
    "status"
]

def bersihkan_layar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def jeda():
    input("\nTekan enter untuk melanjutkan...")

# Fungsi untuk input dan validasi
def input_teks(pesan):
    while True:
        try:
            nilai = input(pesan).strip()
            if nilai:
                return nilai
            print("Input tidak boleh kosong. Silakan isi terlebih dahulu ⚠️")
        except (ValueError, TypeError):
            print("⚠️ Input tidak valid. Silakan coba lagi. ⚠️")

def input_password(pesan):
    while True:
        try:
            password = pwinput(pesan)
            if password.strip():
                return password
            print("⚠️ Password tidak boleh kosong. ⚠️")
        except (ValueError, TypeError):
            print("⚠️ Input password tidak valid. Silakan coba lagi. ⚠️")

def input_angka(pesan, minimum=None):
    while True:
        try:
            angka = int(input_teks(pesan))
            if minimum is not None and angka < minimum:
                print("⚠️ Input minimal adalah", minimum, "⚠️")
            else:
                return angka
        except ValueError:
            print("Input harus berupa angka bulat ⚠️")

def konfirmasi(pesan):
    while True:
        pilihan = input_teks(pesan + " (y/n): ").lower()
        if pilihan == "y":
            return True
        if pilihan == "n":
            return False
        print("Masukkan y atau n ⚠️")

def format_rupiah(nominal):
    return "Rp" + format(int(nominal), ",").replace(",", ".")

# Tampilan judul dan tabel
def tampilkan_judul(teks, ikon="✨", lebar=44):
    isi = f"{ikon} {teks} {ikon}"
    ruang = lebar - 4
    if len(isi) > ruang:
        ruang = len(isi)
        lebar = ruang + 4
    kiri = (ruang - len(isi)) // 2
    kanan = ruang - len(isi) - kiri
    print("╭" + "─" * (lebar - 2) + "╮")
    print("│ " + " " * kiri + isi + " " * kanan + "")
    print("╰" + "─" * (lebar - 2) + "╯")

def tampilkan_tabel(judul, kolom, data):
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = kolom
    tabel.align = {nama_kolom: "l" for nama_kolom in kolom}
    tabel.header = True
    tabel.hrules = 1
    for indeks, nama_kolom in enumerate(kolom):
        if "harga" in nama_kolom.lower() or "nominal" in nama_kolom.lower() or "saldo" in nama_kolom.lower() or "total" in nama_kolom.lower():
            tabel.align[nama_kolom] = "r"
    for baris in data:
        tabel.add_row(baris)
    print(tabel)

# Membaca dan menyimpan data CSV
def baca_csv(lokasi, kolom):
    try:
        with open(lokasi, "r", newline="", encoding="utf-8-sig") as file:
            pembaca = csv.DictReader(file)
            if pembaca.fieldnames != kolom:
                raise ValueError(
                    "Format kolom file tidak sesuai: " + lokasi
                )
            data = []
            for baris in pembaca:
                if None in baris or any(baris.get(kolom_csv) is None for kolom_csv in kolom):
                    raise ValueError(
                        "Terdapat data dengan format tidak sesuai: " + lokasi
                    )
                data.append(baris)
            return data
    except FileNotFoundError:
        return []

def simpan_csv(lokasi, kolom, data):
    with open(lokasi, "w", newline="", encoding="utf-8") as file:
        penulis = csv.DictWriter(file, fieldnames=kolom)
        penulis.writeheader()
        penulis.writerows(data)

def baca_csv_layanan():
    try:
        with open(FILE_LAYANAN, "r", newline="", encoding="utf-8-sig") as file:
            pembaca = csv.DictReader(file)
            kolom_file = pembaca.fieldnames or []
            if not all(kolom in kolom_file for kolom in ("id_layanan", "nama_layanan", "harga")):
                raise ValueError("Format kolom file layanan.csv tidak sesuai.")
            data_layanan = []
            for baris in pembaca:
                data_layanan.append({
                    "id_layanan": (baris.get("id_layanan") or "").strip(),
                    "nama_layanan": (baris.get("nama_layanan") or "").strip(),
                    "harga": (baris.get("harga") or "").strip()
                })
        return data_layanan
    except FileNotFoundError:
        return []

def simpan_csv_layanan(data_layanan):
    simpan_csv(FILE_LAYANAN, KOLOM_LAYANAN, data_layanan)

def kunci_id_layanan(layanan):
    return layanan["id_layanan"].upper()

# Pengolahan data akun dan data awal
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def inisialisasi_data():
    if not os.path.exists(FILE_USERS):
        data_users = [
            {
                "username": "admin",
                "password_hash": hash_password("Adminklinik2"),
                "role": "admin",
                "saldo": "0",
                "nama": "Administrator Klinik"
            }
        ]
        simpan_csv(FILE_USERS, KOLOM_USERS, data_users)
    else:
        data_users = baca_csv(FILE_USERS, KOLOM_USERS)
        if cari_user("admin", data_users) is None:
            data_users.append({
                "username": "admin",
                "password_hash": hash_password("Adminklinik2"),
                "role": "admin",
                "saldo": "0",
                "nama": "Administrator Klinik"
            })
            simpan_csv(FILE_USERS, KOLOM_USERS, data_users)
    data_layanan_awal = [
        {"id_layanan": "L001", "nama_layanan": "Konsultasi Umum", "harga": "50000"},
        {"id_layanan": "L002", "nama_layanan": "Pemeriksaan Tekanan Darah", "harga": "20000"},
        {"id_layanan": "L003", "nama_layanan": "Pemeriksaan Gula Darah", "harga": "35000"},
        {"id_layanan": "L004", "nama_layanan": "Pemeriksaan Kolesterol", "harga": "45000"},
        {"id_layanan": "L005", "nama_layanan": "Konsultasi Kesehatan", "harga": "40000"}
    ]
    perlu_buat_layanan = not os.path.exists(FILE_LAYANAN)
    if not perlu_buat_layanan:
        try:
            data_layanan_tersimpan = baca_csv_layanan()
            if not data_layanan_tersimpan:
                perlu_buat_layanan = True
            else:
                data_layanan_tersimpan.sort(key=kunci_id_layanan)
                simpan_csv_layanan(data_layanan_tersimpan)
        except (ValueError, csv.Error, OSError):
            perlu_buat_layanan = True
    if perlu_buat_layanan:
        simpan_csv_layanan(data_layanan_awal)

def cari_user(username, data_users):
    for user in data_users:
        if user["username"].lower() == username.lower():
            return user
    return None

def cari_layanan(id_layanan, data_layanan):
    for layanan in data_layanan:
        if layanan["id_layanan"].lower() == id_layanan.lower():
            return layanan
    return None

# Registrasi dan login pengguna
def registrasi():
    bersihkan_layar()
    tampilkan_judul("Registrasi Pengguna", "📝")
    data_users = baca_csv(FILE_USERS, KOLOM_USERS)
    while True:
        username = input_teks("Buat username: ")
        if len(username) < 4:
            print("Username minimal 4 karakter!")
        elif not username.isalnum():
            print("Username hanya boleh menggunakan huruf dan angka!")
        elif cari_user(username, data_users) is not None:
            print("Username sudah digunakan!")
        else:
            break
    while True:
        password = input_password("Buat password (minimal 8 karakter): ")
        if len(password) < 8:
            print("Password minimal 8 karakter.")
        else:
            password_konfirmasi = input_password("Konfirmasi password: ")
            if password != password_konfirmasi:
                print("Konfirmasi password tidak sesuai.")
            else:
                break
    while True:
        nama = input_teks("Nama lengkap: ")
        if nama == "":
            print("Nama lengkap tidak boleh kosong!")
        else:
            break
    user_baru = {
        "username": username,
        "password_hash": hash_password(password),
        "role": "user",
        "saldo": "0",
        "nama": nama
    }
    data_users.append(user_baru)
    try:
        simpan_csv(FILE_USERS, KOLOM_USERS, data_users)
        print("\n✅ Registrasi berhasil! ✅")
        print("Silakan login menggunakan akun yang telah dibuat.")
        jeda()
    except OSError:
        data_users.remove(user_baru)
        print("Registrasi gagal karena data tidak dapat disimpan.")
        jeda()

def login():
    data_users = baca_csv(FILE_USERS, KOLOM_USERS)
    tampilkan_judul("Login", "🔐")
    percobaan = 0
    while percobaan < 3:
        username = input_teks("Username: ")
        password = input_password("Password: ")
        user = cari_user(username, data_users)
        if user is not None:
            if user["password_hash"] == hash_password(password):
                if user["role"] not in ROLE_PENGGUNA:
                    print("Role akun tidak valid.")
                    jeda()
                    return None
                try:
                    int(user["saldo"])
                except (ValueError, TypeError):
                    print("Saldo akun tidak valid. Periksa data pengguna.")
                    jeda()
                    return None
                print("\n✅ Login berhasil. ✅")
                print("\n👋 Selamat datang,", user["nama"], "👋")
                time.sleep(1)
                return user
        percobaan += 1
        sisa = 3 - percobaan
        print("❌ Username atau password salah. ❌")
        if sisa > 0:
            print("Sisa percobaan:", sisa)
    print("\nBatas percobaan login telah habis!")
    jeda()
    return None

# Pengelolaan daftar layanan klinik
def tampilkan_layanan():
    data_layanan = baca_csv_layanan()
    data_layanan.sort(key=kunci_id_layanan)
    isi_tabel = []
    for layanan in data_layanan:
        isi_tabel.append([
            layanan["id_layanan"],
            layanan["nama_layanan"],
            format_rupiah(layanan["harga"])
        ])
    if not isi_tabel:
        print("Belum ada layanan yang tersedia ⚠️")
        print("Silakan tambahkan layanan terlebih dahulu.")
    else:
        tampilkan_tabel(
            "✦  DAFTAR LAYANAN KLINIK  ✦",
            ["ID Layanan", "Nama Layanan", "Harga (Rp)"],
            isi_tabel
        )

def tambah_layanan():
    bersihkan_layar()
    tampilkan_judul("Tambah Layanan", "➕")
    data_layanan = baca_csv_layanan()
    while True:
        id_layanan = input_teks("ID layanan baru (L001): ").upper()
        if len(id_layanan) != 4 or not id_layanan.startswith("L00") or not id_layanan[3].isdigit():
            print("ID harus 4 karakter dengan format L00X ⚠️")
        elif cari_layanan(id_layanan, data_layanan) is not None:
            print("ID layanan sudah digunakan ⚠️")
        else:
            break
    while True:
        nama_layanan = input_teks("Nama layanan: ")
        nama_sudah_ada = any(
            layanan["nama_layanan"].lower() == nama_layanan.lower()
            for layanan in data_layanan
        )
        if nama_sudah_ada:
            print("Nama layanan sudah digunakan ⚠️")
        else:
            break
    harga = input_angka("Harga layanan: Rp", 1)
    layanan_baru = {
        "id_layanan": id_layanan,
        "nama_layanan": nama_layanan,
        "harga": str(harga)
    }
    data_layanan.append(layanan_baru)
    data_layanan.sort(key=kunci_id_layanan)
    try:
        simpan_csv_layanan(data_layanan)
        print("\n✅ Layanan berhasil ditambahkan. ✅")
    except OSError:
        data_layanan.remove(layanan_baru)
        print("Layanan gagal disimpan.")
    jeda()

def ubah_layanan():
    bersihkan_layar()
    tampilkan_layanan()
    data_layanan = baca_csv_layanan()
    print("\n✏️ Ubah Data Layanan ✏️")
    while True:
        id_layanan = input_teks("Masukkan ID layanan (L001): ").upper()
        if len(id_layanan) != 4 or not id_layanan.startswith("L00") or not id_layanan[3].isdigit():
            print("ID harus 4 karakter dengan format L00X ⚠️")
        else:
            break
    layanan = cari_layanan(id_layanan, data_layanan)
    if layanan is None:
        print("Layanan tidak ditemukan.")
        jeda()
        return
    print("\nData layanan yang dipilih:")
    print("Nama:", layanan["nama_layanan"])
    print("Harga:", format_rupiah(layanan["harga"]))
    nama_lama = layanan["nama_layanan"]
    harga_lama = layanan["harga"]
    while True:
        nama_baru = input_teks("Nama layanan baru: ")
        nama_duplikat = any(
            item["id_layanan"].lower() != layanan["id_layanan"].lower()
            and item["nama_layanan"].lower() == nama_baru.lower()
            for item in data_layanan
        )
        if nama_duplikat:
            print("Nama layanan sudah digunakan ⚠️")
        else:
            break
    layanan["nama_layanan"] = nama_baru
    layanan["harga"] = str(input_angka("Harga baru: Rp", 1))
    try:
        simpan_csv_layanan(data_layanan)
        print("\n✅ Data layanan berhasil diubah. ✅")
    except OSError:
        layanan["nama_layanan"] = nama_lama
        layanan["harga"] = harga_lama
        print("Data layanan gagal disimpan. Perubahan dibatalkan.")
    jeda()

def hapus_layanan():
    bersihkan_layar()
    tampilkan_layanan()
    data_layanan = baca_csv_layanan()
    print("\n✦ Hapus Layanan ✦")
    id_layanan = input_teks("Masukkan ID layanan: ")
    layanan = cari_layanan(id_layanan, data_layanan)
    if layanan is None:
        print("Layanan tidak ditemukan.")
        jeda()
        return
    if not konfirmasi("Yakin ingin menghapus layanan " + layanan["nama_layanan"] + "?"):
        print("Penghapusan dibatalkan.")
        jeda()
        return
    indeks = data_layanan.index(layanan)
    data_layanan.remove(layanan)
    try:
        simpan_csv_layanan(data_layanan)
        print("Layanan berhasil dihapus dari daftar.")
    except (OSError, ValueError, csv.Error) as error:
        data_layanan.insert(indeks, layanan)
        print("Layanan gagal dihapus:", error)
    jeda()

def menu_kelola_layanan():
    while True:
        bersihkan_layar()
        tampilkan_judul("Kelola Layanan Klinik", "🩺")
        print("1. Lihat layanan 🏥")
        print("2. Tambah layanan ➕")
        print("3. Ubah layanan ✏️")
        print("4. Hapus layanan 🗑️")
        print("0. Kembali ↩️")
        pilihan = input_teks("\nPilih menu: ")
        if pilihan == "1":
            bersihkan_layar()
            tampilkan_layanan()
            jeda()
        elif pilihan == "2":
            tambah_layanan()
        elif pilihan == "3":
            ubah_layanan()
        elif pilihan == "4":
            hapus_layanan()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak tersedia ⚠️")
            jeda()

# Pencatatan transaksi dan invoice
def buat_id_transaksi():
    data = baca_csv(FILE_TRANSAKSI, KOLOM_TRANSAKSI)
    nomor = len(data) + 1
    return "TRX" + datetime.now().strftime("%Y%m%d") + f"{nomor:04d}"

def simpan_transaksi(username, jenis, id_layanan="", nama_layanan="", jumlah=1,
                    nominal=0, saldo_awal=0, saldo_akhir=0, status="Berhasil"):
    data = baca_csv(FILE_TRANSAKSI, KOLOM_TRANSAKSI)
    data.append({
        "id_transaksi": buat_id_transaksi(),
        "waktu": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "username": username,
        "jenis": jenis,
        "id_layanan": id_layanan,
        "nama_layanan": nama_layanan,
        "jumlah": str(jumlah),
        "nominal": str(nominal),
        "saldo_awal": str(saldo_awal),
        "saldo_akhir": str(saldo_akhir),
        "status": status
    })
    simpan_csv(FILE_TRANSAKSI, KOLOM_TRANSAKSI, data)
    return data[-1]

def tampilkan_invoice(transaksi):
    garis = "─" * 44
    waktu_transaksi = transaksi.get("waktu") or datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    jenis = transaksi.get("jenis", "-").replace("_", " ").title()
    status = transaksi.get("status", "Tidak diketahui")
    ikon_status = "✅" if status.lower() == "berhasil" else "⚠️"
    tampilkan_judul("INVOICE KLINIK", "🏥", 44)
    print()
    print("📌 INFORMASI TRANSAKSI")
    print(garis)
    print(f"🆔 No. Transaksi : {transaksi.get('id_transaksi', '-')}")
    print(f"📅 Tanggal       : {waktu_transaksi}")
    print(f"👤 Pengguna      : {transaksi.get('username', '-')}")
    print(f"🗂️  Jenis         : {jenis}")
    if transaksi.get("nama_layanan"):
        print()
        print("🏥 RINCIAN LAYANAN")
        print(garis)
        print(f"💊 Layanan       : {transaksi.get('nama_layanan', '-')}")
        print(f"🔢 Jumlah        : {transaksi.get('jumlah', '1')}")
    print()
    print("💰 RINCIAN SALDO")
    print(garis)
    print(f"💵 Nominal       : {format_rupiah(transaksi.get('nominal', 0))}")
    print(f"⬅️  Saldo awal    : {format_rupiah(transaksi.get('saldo_awal', 0))}")
    print(f"➡️  Saldo akhir   : {format_rupiah(transaksi.get('saldo_akhir', 0))}")
    print(f"{ikon_status} Status        : {status}")
    print(garis)
    print("💙 Terima kasih telah menggunakan layanan kami.")

# Top-up saldo dan pembayaran layanan
def topup_saldo(user):
    bersihkan_layar()
    tampilkan_judul("Top-up Saldo", "💳")
    nominal = input_angka("Nominal top-up (Rp): ", 1000)
    if nominal > 10000000:
        print("Nominal maksimal top-up adalah Rp10.000.000.")
        jeda()
        return
    if not konfirmasi("Konfirmasi top-up " + format_rupiah(nominal) + "?"):
        print("Top-up dibatalkan.")
        jeda()
        return
    data_users = baca_csv(FILE_USERS, KOLOM_USERS)
    tersimpan = cari_user(user["username"], data_users)
    if tersimpan is None:
        print("Akun tidak ditemukan.")
        jeda()
        return
    saldo_awal = int(tersimpan["saldo"])
    saldo_akhir = saldo_awal + nominal
    tersimpan["saldo"] = str(saldo_akhir)
    try:
        simpan_csv(FILE_USERS, KOLOM_USERS, data_users)
        transaksi = simpan_transaksi(user["username"], "TOP_UP", nominal=nominal,
                                    saldo_awal=saldo_awal, saldo_akhir=saldo_akhir)
        user["saldo"] = str(saldo_akhir)
        print("\n╭────────────────────────────────────────────╮")
        print("│             ✅ TOP-UP BERHASIL ✅           ")
        print("╰────────────────────────────────────────────╯")
        tampilkan_invoice(transaksi)
    except (OSError, ValueError, csv.Error) as error:
        tersimpan["saldo"] = str(saldo_awal)
        try:
            simpan_csv(FILE_USERS, KOLOM_USERS, data_users)
        except OSError:
            pass
        print("❌ Top-up gagal disimpan:", error)
    jeda()

def bayar_layanan(user):
    bersihkan_layar()
    tampilkan_judul("Pembayaran Layanan", "🏥")
    tampilkan_layanan()
    data_layanan = baca_csv_layanan()
    if not data_layanan:
        print("Belum ada layanan yang terdaftar.")
        jeda()
        return
    layanan = cari_layanan(input_teks("\nMasukkan ID layanan: "), data_layanan)
    if layanan is None:
        print("ID layanan tidak ditemukan ⚠️")
        jeda()
        return
    jumlah = 1
    total = int(layanan["harga"])
    data_users = baca_csv(FILE_USERS, KOLOM_USERS)
    tersimpan = cari_user(user["username"], data_users)
    if tersimpan is None:
        print("Akun tidak ditemukan.")
        jeda()
        return
    saldo_awal = int(tersimpan["saldo"])
    if saldo_awal < total:
        print("❌ Saldo tidak mencukupi.")
        print("Total pembayaran:", format_rupiah(total))
        print("Saldo saat ini  :", format_rupiah(saldo_awal))
        jeda()
        return
    tampilkan_judul("Ringkasan Pembayaran", "🧾")
    tampilkan_tabel("🧾 Rincian Tagihan 🧾", ["Layanan", "Harga", "Jumlah", "Total"],
                    [[layanan["nama_layanan"], format_rupiah(layanan["harga"]),
                    jumlah, format_rupiah(total)]])
    if not konfirmasi("Lanjutkan pembayaran?"):
        print("Pembayaran dibatalkan.")
        jeda()
        return
    saldo_akhir = saldo_awal - total
    tersimpan["saldo"] = str(saldo_akhir)
    try:
        simpan_csv(FILE_USERS, KOLOM_USERS, data_users)
        transaksi = simpan_transaksi(user["username"], "PEMBAYARAN_LAYANAN",
                                    layanan["id_layanan"], layanan["nama_layanan"],
                                    jumlah, total, saldo_awal, saldo_akhir)
        user["saldo"] = str(saldo_akhir)
        print("\n╭────────────────────────────────────────────╮")
        print("│          ✅ PEMBAYARAN BERHASIL ✅          ")
        print("╰────────────────────────────────────────────╯")
        tampilkan_invoice(transaksi)
    except (OSError, ValueError, csv.Error) as error:
        tersimpan["saldo"] = str(saldo_awal)
        try:
            simpan_csv(FILE_USERS, KOLOM_USERS, data_users)
        except OSError:
            pass
        print("❌ Pembayaran gagal disimpan:", error)
    jeda()

# Riwayat transaksi dan pengelolaan pengguna
def tampilkan_riwayat(username=None):
    data = baca_csv(FILE_TRANSAKSI, KOLOM_TRANSAKSI)
    if username is not None:
        data = [x for x in data if x["username"].lower() == username.lower()]
    data.reverse()
    baris = [[x["id_transaksi"], x["waktu"], x["username"],
            x["jenis"].replace("_", " ").title(),
            x["nama_layanan"] or "-", format_rupiah(x["nominal"]), x["status"]]
            for x in data]
    tampilkan_tabel("📋 RIWAYAT TRANSAKSI 📋",
                    ["ID Transaksi", "Waktu", "Username", "Jenis", "Layanan", "Nominal", "Status"],
                    baris if baris else [["-", "-", "-", "-", "Belum ada transaksi", "-", "-"]])

def menu_kelola_pengguna():
    while True:
        bersihkan_layar()
        tampilkan_judul("Kelola Pengguna", "👥")
        data = baca_csv(FILE_USERS, KOLOM_USERS)
        tampilkan_tabel("👥 Daftar Pengguna 👥",
                        ["Username", "Nama", "Role", "Saldo"],
                        [[u["username"], u["nama"], u["role"], format_rupiah(u["saldo"])] for u in data])
        print("\n1. Ubah role pengguna")
        print("2. Hapus pengguna 🗑️")
        print("0. Kembali ↩️")
        pilihan = input_teks("Pilih menu: ")
        if pilihan == "0":
            return
        if pilihan == "1":
            username = input_teks("Username pengguna: ")
            target = cari_user(username, data)
            if target is None:
                print("Pengguna tidak ditemukan.")
            elif target["username"].lower() == "admin":
                print("Role akun admin utama tidak dapat diubah.")
            else:
                while True:
                    role = input_teks("Role baru (admin/user): ").lower()
                    if role in ROLE_PENGGUNA:
                        break
                    print("Role hanya boleh admin atau user. Silakan input lagi.")
                if konfirmasi("Ubah role menjadi " + role + "?"):
                    role_lama = target["role"]
                    target["role"] = role
                    try:
                        simpan_csv(FILE_USERS, KOLOM_USERS, data)
                        print("✅ Role pengguna berhasil diubah.")
                    except OSError:
                        target["role"] = role_lama
                        print("❌ Perubahan role gagal disimpan. Data dipulihkan.")
            jeda()
        elif pilihan == "2":
            username = input_teks("Username pengguna yang akan dihapus: ")
            target = cari_user(username, data)
            if target is None:
                print("Pengguna tidak ditemukan.")
            elif target["username"].lower() == "admin":
                print("Akun admin utama tidak dapat dihapus.")
            elif konfirmasi("Hapus akun " + target["username"] + "?"):
                indeks = data.index(target)
                data.remove(target)
                try:
                    simpan_csv(FILE_USERS, KOLOM_USERS, data)
                    print("✅ Pengguna berhasil dihapus.")
                except OSError:
                    data.insert(indeks, target)
                    print("❌ Pengguna gagal dihapus. Data dipulihkan.")
            jeda()
        else:
            print("Pilihan tidak tersedia ⚠️")
            jeda()

# Laporan transaksi untuk admin
def laporan_transaksi():
    data = baca_csv(FILE_TRANSAKSI, KOLOM_TRANSAKSI)
    berhasil = [x for x in data if x["status"] == "Berhasil"]
    total_topup = sum(int(x["nominal"]) for x in berhasil if x["jenis"] == "TOP_UP")
    total_bayar = sum(int(x["nominal"]) for x in berhasil if x["jenis"] == "PEMBAYARAN_LAYANAN")
    tampilkan_judul("Laporan Transaksi", "📊")
    tampilkan_tabel("📊 Ringkasan 📊", ["Indikator", "Jumlah"],
                    [["Total transaksi", len(data)],
                    ["Transaksi berhasil", len(berhasil)],
                    ["Total top-up", format_rupiah(total_topup)],
                    ["Total pembayaran layanan", format_rupiah(total_bayar)]])
    tampilkan_riwayat()

# Menu berdasarkan role pengguna
def menu_admin(user):
    while True:
        bersihkan_layar()
        tampilkan_judul("Administrasi Klinik", "🏥")
        print("Nama pengguna :", user["nama"])
        print("Role          : Admin")
        print("\n1. Kelola layanan")
        print("2. Kelola pengguna 👥")
        print("3. Lihat seluruh transaksi 📋")
        print("4. Laporan transaksi 📊")
        print("5. Logout 🚪")
        print("0. Keluar program 🚪")
        pilihan = input_teks("\nPilih menu: ")
        if pilihan == "1":
            menu_kelola_layanan()
        elif pilihan == "2":
            menu_kelola_pengguna()
        elif pilihan == "3":
            bersihkan_layar()
            tampilkan_riwayat()
            jeda()
        elif pilihan == "4":
            bersihkan_layar()
            laporan_transaksi()
            jeda()
        elif pilihan == "5":
            print("👋 Logout berhasil. 👋")
            jeda()
            break
        elif pilihan == "0":
            if konfirmasi("Yakin ingin keluar dari program?"):
                return False
        else:
            print("Pilihan tidak tersedia ⚠️")
            jeda()
    return True

def menu_user(user):
    while True:
        bersihkan_layar()
        data_users = baca_csv(FILE_USERS, KOLOM_USERS)
        user_tersimpan = cari_user(user["username"], data_users)
        if user_tersimpan is None:
            print("Data pengguna tidak ditemukan.")
            jeda()
            return True
        user["saldo"] = user_tersimpan["saldo"]
        tampilkan_judul("Layanan Klinik", "🩺")
        print("Nama pengguna :", user["nama"])
        print("Username      :", user["username"])
        print("Saldo         :", format_rupiah(user["saldo"]))
        print("\n1. Lihat layanan 🏥")
        print("2. Top-up saldo 💰")
        print("3. Bayar layanan 💳")
        print("4. Lihat riwayat transaksi 🧾")
        print("5. Logout 🚪")
        print("0. Keluar program 🚪")
        pilihan = input_teks("\nPilih menu: ")
        if pilihan == "1":
            bersihkan_layar()
            tampilkan_layanan()
            jeda()
        elif pilihan == "2":
            topup_saldo(user)
        elif pilihan == "3":
            bayar_layanan(user)
        elif pilihan == "4":
            bersihkan_layar()
            tampilkan_riwayat(user["username"])
            jeda()
        elif pilihan == "5":
            print("👋 Logout berhasil. 👋")
            jeda()
            break
        elif pilihan == "0":
            if konfirmasi("Yakin ingin keluar dari program?"):
                return False
        else:
            print("Pilihan tidak tersedia ⚠️")
            jeda()
    return True

# Menu autentikasi dan program utama
def menu_autentikasi():
    while True:
        bersihkan_layar()
        tampilkan_judul("Administrasi Transaksi Klinik", "🏥")
        print("1. Login 🔑")
        print("2. Registrasi pengguna 📝")
        print("0. Keluar program 🚪")
        pilihan = input_teks("\nPilih menu: ")
        if pilihan == "1":
            user = login()
            if user is not None:
                return user
        elif pilihan == "2":
            registrasi()
        elif pilihan == "0":
            if konfirmasi("Yakin ingin keluar dari program?"):
                return None
        else:
            print("Pilihan tidak tersedia ⚠️")
            jeda()

def main():
    try:
        inisialisasi_data()
        while True:
            user = menu_autentikasi()
            if user is None:
                bersihkan_layar()
                print(
                    "Terima kasih telah menggunakan "
                    "Administrasi Transaksi Klinik."
                )
                break
            if user["role"] == "admin":
                lanjut = menu_admin(user)
            else:
                lanjut = menu_user(user)
            if not lanjut:
                bersihkan_layar()
                print(
                    "Terima kasih telah menggunakan "
                    "Administrasi Transaksi Klinik."
                )
                break
    except FileNotFoundError as error:
        print("File tidak ditemukan:", error)
    except ValueError as error:
        print("Terjadi kesalahan pada data:", error)
    except OSError as error:
        print("Terjadi kesalahan saat mengakses file:", error)

if __name__ == "__main__":
    main()