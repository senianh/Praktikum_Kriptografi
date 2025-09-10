# 🔐 Hill Cipher - Implementasi Python

Program ini adalah implementasi **Hill Cipher** dalam bahasa Python untuk melakukan **enkripsi, dekripsi, dan pencarian kunci** dari pasangan plaintext & ciphertext.  
Dibuat sebagai tugas mata kuliah **Kriptografi**.

---

## 📌 Deskripsi
Hill Cipher adalah algoritma kriptografi klasik berbasis **aljabar linear**. Algoritma ini menggunakan operasi matriks dengan aritmatika modulo 26 untuk mengubah plaintext menjadi ciphertext dan sebaliknya.  

Hill Cipher adalah salah satu algoritma kriptografi klasik berbasis aljabar linear. Algoritma ini dikembangkan oleh Lester S. Hill pada tahun 1929.
Prinsip kerjanya:
- Plaintext (teks asli) diubah menjadi bentuk numerik.
- Proses enkripsi dilakukan menggunakan perkalian matriks kunci dengan vektor plaintext.
- Operasi dilakukan dalam modulo 26 (jumlah huruf alfabet).
- Untuk dekripsi, digunakan invers matriks kunci.

Keunggulan Hill Cipher dibanding cipher klasik lain (misalnya Caesar atau Vigenère) adalah menggunakan blok huruf sekaligus (bukan satu huruf per satu kali enkripsi). Hal ini membuatnya lebih kuat terhadap analisis frekuensi.

Dalam program ini, proses enkripsi dan dekripsi dilakukan menggunakan matriks kunci berordo 2x2. Program juga dapat mencari kunci matriks jika diberikan pasangan plaintext dan ciphertext.

---
## Fitur Implementasi Python

Implementasi Python biasanya mencakup:
- Konversi karakter ↔ angka (A=0, B=1, ..., Z=25).
- Enkripsi: C = (K × P) mod 26, dengan K = matriks kunci, P = vektor plaintext, C = ciphertext.
- Dekripsi: P = (K⁻¹ × C) mod 26, dengan K⁻¹ = invers dari matriks kunci dalam mod 26.

---

## ✨ Fitur Program
- 🔑 **1. Enkripsi** input plaintext → ciphertext  
- 🔓 **2. Dekripsi** input ciphertext → plaintext  
- 🕵️ **3. Cari Kunci** input plaintext & ciphertext → tampilkan matriks kunci.
- ⚡ **4.Test Otomatis** menjalankan contoh kasus PYTHON  → PUTVUP
- 📤 **5. Keluar.**
- Mendukung padding otomatis (`X`) jika panjang plaintext tidak sesuai ordo matriks  
- Invers matriks dihitung menggunakan **aritmatika modulo 26**

---
## Contoh Penggunaan


