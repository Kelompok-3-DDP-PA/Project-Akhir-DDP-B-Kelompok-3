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