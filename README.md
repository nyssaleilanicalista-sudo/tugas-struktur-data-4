# tugas-struktur-data-4
# Big Integer ADT (Abstract Data Type)

Proyek ini mengimplementasikan **Big Integer ADT** menggunakan bahasa Python. [cite_start]Tujuan utamanya adalah untuk mengatasi keterbatasan kapasitas penyimpanan integer pada level *hardware* (seperti limit 64-bit) dengan memindahkan logika penyimpanan dan operasi ke level *software*[cite: 2, 7].

## 📋 Deskripsi Tugas
Berdasarkan instruksi praktikum, implementasi ini mencakup:
* [cite_start]**Penyimpanan Node**: Setiap digit angka disimpan dalam sebuah node terpisah dalam *Singly Linked List*[cite: 25].
* [cite_start]**Urutan Digit**: Node diurutkan dari digit paling tidak signifikan (*least-significant*) ke yang paling besar untuk memudahkan operasi aritmatika[cite: 26].
* [cite_start]**Kapasitas**: Mampu menangani angka lebih dari 19 digit, melampaui batas arsitektur 64-bit konvensional[cite: 4, 5, 6].

## 🛠️ Fitur Utama
Program ini mendukung fungsionalitas berikut:
* [cite_start]**`BigInteger(initValue)`**: Inisialisasi angka melalui string[cite: 10].
* [cite_start]**`toString()`**: Mengonversi kembali struktur *linked list* menjadi string angka yang dapat dibaca[cite: 11].
* [cite_start]**Aritmatika**: Mendukung operasi penjumlahan (`+`) dan perkalian (`*`)[cite: 14, 16, 17].
* [cite_start]**Assignment Combo Operators**: Mendukung operator gabungan seperti `+=` dan `*=`[cite: 36, 38, 40].

## 🏗️ Struktur Data
[cite_start]Contoh representasi angka `45839` dalam memori[cite: 27]:
```text
head -> [9] -> [3] -> [8] -> [5] -> [4] -> None
```
[cite_start]*(Urutan terbalik memudahkan proses 'carry' atau simpanan saat penjumlahan)*[cite: 26].

## 🚀 Cara Penggunaan
Cukup jalankan script Python dan gunakan kelas `BigInteger` seperti contoh di bawah:

```python
# Membuat objek Big Integer
num1 = BigInteger("9223372036854775808") # Angka di atas limit 64-bit
num2 = BigInteger("100")

# Melakukan penjumlahan
hasil = num1 + num2
print(f"Hasil: {hasil.toString()}")

# Menggunakan assignment operator
num1 += num2
print(f"Update num1: {num1.toString()}")
```
