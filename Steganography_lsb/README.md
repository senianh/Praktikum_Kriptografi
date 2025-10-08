# 🕵️‍♀️ Program Steganografi Menggunakan Metode LSB (Least Significant Bit)

## 📌 Deskripsi Program
Program ini dibuat untuk **menyembunyikan (encode)** dan **membaca kembali (decode)** sebuah **pesan rahasia** di dalam file gambar menggunakan metode **Least Significant Bit (LSB)**.  
Metode LSB bekerja dengan cara mengganti bit terakhir dari setiap nilai warna (R, G, B) pada pixel gambar dengan bit-bit dari pesan rahasia.  
Perubahan tersebut sangat kecil sehingga **tidak terlihat oleh mata manusia**.

---

## ⚙️ Cara Kerja Program

### 🔹 Encode (Menyembunyikan Pesan)
1. Program membaca gambar input (`input.png`).
2. Pesan rahasia diubah menjadi representasi biner (bit-bit).
3. Bit-bit pesan disisipkan ke dalam **bit terakhir (LSB)** dari setiap komponen warna **R, G, dan B** di pixel gambar.
4. Gambar hasil proses disimpan sebagai **`stego_output.png`** yang tampak sama dengan gambar asli.

### 🔹 Decode (Membaca Pesan)
1. Program membaca gambar hasil encode (`stego_output.png`).
2. Program mengambil bit-bit terakhir dari setiap pixel RGB.
3. Bit-bit tersebut disusun kembali menjadi karakter teks.
4. Pesan rahasia ditampilkan kembali di layar terminal.

---

## 🧠 Alur Program

[ Pesan Rahasia ]
↓
Konversi ke Bit
↓
[ Cover Image ] → Ubah bit terakhir setiap pixel → [ Stego Image ]
↓
Decode kembali ke teks


---

## 📂 Struktur Folder
│
├── lsb.py
├── input.png
├── stego_output.png
├── screenshot_encode.png
├── screenshot_decode.png
└── README.md



---

## 🚀 Cara Menjalankan Program
---

===== Program Steganografi LSB =====
1. Encode (sembunyikan pesan)
2. Decode (baca pesan)

---
# Encode
Pilih menu (1/2): 1
Masukkan nama file gambar (misal: input.png): input.png
Masukkan pesan yang ingin disembunyikan : Halo Dunia dari Senia!
Masukkan nama file output (misal: stego.png): stego_output.png
✅ Pesan berhasil disembunyikan dalam: stego_output.png

---
# Decode
Pilih menu (1/2): 2
Masukkan nama file gambar hasil encode : stego_output.png

🔍 Pesan rahasia tersembunyi :
Halo Dunia dari Senia!





