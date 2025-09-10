# 🔐 Hill Cipher - Implementasi Python

Program ini adalah implementasi **Hill Cipher** dalam bahasa Python untuk melakukan **enkripsi, dekripsi, dan pencarian kunci** dari pasangan plaintext & ciphertext.  
Dibuat sebagai tugas mata kuliah **Kriptografi**.

---

## 📌 Deskripsi
Hill Cipher adalah algoritma kriptografi klasik berbasis **aljabar linear** yang dikembangkan oleh **Lester S. Hill pada tahun 1929**.  

Prinsip kerjanya:
- Plaintext (teks asli) diubah menjadi bentuk numerik (A=0, B=1, ..., Z=25).
- Enkripsi dilakukan dengan perkalian matriks kunci terhadap vektor plaintext:  
  **C = (K × P) mod 26**
- Dekripsi dilakukan dengan invers matriks kunci:  
  **P = (K⁻¹ × C) mod 26**
- Operasi dilakukan dalam **modulo 26** (jumlah huruf alfabet).

✨ **Keunggulan Hill Cipher**:  
Dibanding cipher klasik lain (misalnya Caesar atau Vigenère), Hill Cipher bekerja dengan **blok huruf sekaligus**, bukan satu huruf per enkripsi. Hal ini membuatnya lebih kuat terhadap analisis frekuensi.

Dalam program ini:
- Proses enkripsi dan dekripsi dilakukan dengan **matriks kunci 2x2**.  
- Program juga dapat mencari **matriks kunci** jika diberikan pasangan plaintext dan ciphertext.

---

## ⚙️ Fitur Implementasi Python
- Konversi karakter ↔ angka (A=0, B=1, ..., Z=25).  
- Enkripsi: `C = (K × P) mod 26`.  
- Dekripsi: `P = (K⁻¹ × C) mod 26`.  
- Invers matriks dihitung menggunakan **aritmatika modulo 26**.  
- Mendukung **padding otomatis (X)** jika panjang plaintext tidak sesuai ordo matriks.  

---

## ✨ Fitur Program
1. 🔑 **Enkripsi** plaintext → ciphertext  
2. 🔓 **Dekripsi** ciphertext → plaintext  
3. 🕵️ **Cari Kunci** dari pasangan plaintext & ciphertext  
4. ⚡ **Test Otomatis** kasus `PYTHON → PUTVUP`  
5. 📤 **Keluar Program**  

---

## ▶️ Contoh Penggunaan

### Menu Program

===== Hill Cipher Menu =====
1. Enkripsi
2. Dekripsi
3. Cari Kunci (Plain & Cipher)
4. Test otomatis (PYTHON -> PUTVUP)
0. Keluar
Pilih menu :

---

**1. Enkripsi** 

Masukkan plaintext: PYTHON

Ciphertext: PUTVUP

---

**2. Dekripsi** 

Masukkan ciphertext: PUTVUP

Plaintext: PYTHON

---

**3. Cari Kunci** 

Masukkan plaintext: PYTHON

Masukkan ciphertext: PUTVUP 

Ordo matriks kunci (contoh 2): 2

Key matrix:
[7, 6]

[2, 5]

---

**4. Test Otomatis** 

=== Enkripsi ===

Asal Plaintext : PYTHON

Hasil Ciphertext: PUTVUP


=== Dekripsi ===

Asal Ciphertext: PUTVUP

Hasil Plaintext : PYTHON

=== Cari Kunci ===

Plaintext : PYTHON

Ciphertext: PUTVUP

Kunci ditemukan:
[7, 6]

[2, 5]

---

**5. Keluar.**
Anda keluar dari Program, program akan berhenti berjalan.

---
## Catatan
- Program mendukung padding otomatis dengan huruf X jika panjang plaintext tidak sesuai ordo matriks.
- Invers matriks dihitung menggunakan aritmatika modulo 26.









