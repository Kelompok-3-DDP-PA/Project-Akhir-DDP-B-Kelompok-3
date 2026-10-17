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