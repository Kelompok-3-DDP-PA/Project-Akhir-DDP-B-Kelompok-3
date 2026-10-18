import csv
import os
import time
import random
import hashlib
from datetime import datetime
from prettytable import PrettyTable
from pwinput import pwinput

#Konfigurasi file
FILE_USERS = "users.csv"
FILE_LAYANAN = "layanan.csv"
FILE_TRANSAKSI = "transaksi.csv"

ROLE_PENGGUNA = ("admin", "user")
STATUS_LAYANAN = ("Aktif", "Nonaktif")

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
    "harga",
    "status"
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

#basic function
def bersihkan_layar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def jeda():
    input("\nTekan enter untuk melanjutkan...")

def input_password(pesan):
    return pwinput(pesan)

def input_angka(pesan, minimum=None):
    while True:
        try:
            angka = int(input(pesan))

            if minimum is not None and angka < minimum:
                print("Minimal input adalah", minimum)
            else:
                return angka

        except ValueError:
            print("Input harus berupa angka bulat!")

def konfirmasi(pesan):
    while True:
        pilihan = input(pesan + " (y/n): ").strip().lower()

        if pilihan == "y":
            return True
        elif pilihan == "n":
            return False
        else:
            print("Pilih y atau n !")

def format_rupiah(nominal):
    return "Rp" + format(int(nominal), ",").replace(",", ".")

def tampilkan_tabel(judul, kolom, data):
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = kolom

    for baris in data:
        tabel.add_row(baris)

    print(tabel)

#function csv
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

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#inisialisasi data
def inisialisasi_data():
    if not os.path.exists(FILE_USERS):
        data_users = [
            {
                "username": "admin",
                "password_hash": hash_password("AdminKlinik2026!"),
                "role": "admin",
                "saldo": "0",
                "nama": "Administrator Klinik"
            }
        ]

        simpan_csv(FILE_USERS, KOLOM_USERS, data_users)

    if not os.path.exists(FILE_LAYANAN):
        data_layanan = [
            {
                "id_layanan": "L001",
                "nama_layanan": "Konsultasi Umum",
                "harga": "50000",
                "status": "Aktif"
            },
            {
                "id_layanan": "L002",
                "nama_layanan": "Pemeriksaan Tekanan Darah",
                "harga": "20000",
                "status": "Aktif"
            },
            {
                "id_layanan": "L003",
                "nama_layanan": "Pemeriksaan Gula Darah",
                "harga": "35000",
                "status": "Aktif"
            },
            {
                "id_layanan": "L004",
                "nama_layanan": "Pemeriksaan Kolesterol",
                "harga": "45000",
                "status": "Aktif"
            },
            {
                "id_layanan": "L005",
                "nama_layanan": "Konsultasi Kesehatan",
                "harga": "40000",
                "status": "Aktif"
            }
        ]

        simpan_csv(FILE_LAYANAN, KOLOM_LAYANAN, data_layanan)

    if not os.path.exists(FILE_TRANSAKSI):
        simpan_csv(FILE_TRANSAKSI, KOLOM_TRANSAKSI, [])

#cari data
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

#regis pengguna
def registrasi():
    bersihkan_layar()

    print("=" * 45)
    print("          Registrasi Pengguna")
    print("=" * 45)

    data_users = baca_csv(FILE_USERS, KOLOM_USERS)

    #validasi usnm
    while True:
        username = input("Buat username: ").strip()

        if len(username) < 4:
            print("Username minimal 4 karakter!")

        elif not username.isalnum():
            print("Username hanya boleh menggunakan huruf dan angka!")

        elif cari_user(username, data_users) is not None:
            print("Username sudah digunakan!")

        else:
            break

    #validasi dan konfirm pw
    while True:
        password = input_password(
            "Buat password (minimal 8 karakter): "
        )
        
        if len(password) < 8:
            print("Password minimal 8 karakter!")
        
        else:
            password_konfirmasi = input_password(
                "Konfirmasi password: "
            )
        
            if password != password_konfirmasi:
                print("Password tidak sesuai!")
        
            else:
                break

    #input nama user
    while True:
        nama = input("Nama lengkap: ").strip()

        if nama == "":
            print("Input nama lengkap tidak boleh kosong!")

        else:
            break

    #akun regis otomatis jdi user
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
        print("\nRegistrasi berhasil!")
        print("Silakan login menggunakan akun yang telah dibuat.")
        
    except OSError:
        data_users.remove(user_baru)
        print("Registrasi gagal karena data tidak dapat disimpan.")
        
        jeda()

#login admin dn user
def login():
    data_users = baca_csv(FILE_USERS, KOLOM_USERS)

    print("\n" + "=" * 45)
    print("                    Login")
    print("=" * 45)

    percobaan = 0

    while percobaan < 3:
        username = input("Username: ").strip()
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
                
                print("\nLogin berhasil.")
                print("Selamat datang,", user["nama"])

                time.sleep(1)

                return user

        percobaan += 1
        sisa = 3 - percobaan
        
        print("Username atau password salah.")
        
        if sisa > 0:
            print("Sisa percobaan:", sisa)

    print("\nBatas percobaan login telah habis!")
    jeda()

    return None

#tampilan lyanan
def tampilkan_layanan(aktif_saja=False):
    data_layanan = baca_csv(FILE_LAYANAN, KOLOM_LAYANAN)
    isi_tabel = []

    for layanan in data_layanan:
        if aktif_saja and layanan["status"] != "Aktif":
            continue

        isi_tabel.append([

            layanan["id_layanan"],
            layanan["nama_layanan"],
            format_rupiah(layanan["harga"]),
            layanan["status"]
        ])

    tampilkan_tabel(
        "Daftar Layanan Klinik",
        ["ID Layanan", "Nama Layanan", "Harga", "Status"],
        isi_tabel
    )


