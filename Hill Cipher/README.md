# 🔐 Hill Cipher - Implementasi Python

Program ini adalah implementasi **Hill Cipher** dalam bahasa Python untuk melakukan **enkripsi, dekripsi, dan pencarian kunci** dari pasangan plaintext & ciphertext.  
Dibuat sebagai tugas mata kuliah **Kriptografi**.

---

## 📌 Deskripsi
Hill Cipher adalah algoritma kriptografi klasik berbasis **aljabar linear**. Algoritma ini menggunakan operasi matriks dengan aritmatika modulo 26 untuk mengubah plaintext menjadi ciphertext dan sebaliknya.  

Dalam program ini, proses enkripsi dan dekripsi dilakukan menggunakan matriks kunci berordo 2x2. Program juga dapat mencari kunci matriks jika diberikan pasangan plaintext dan ciphertext.

---

## ✨ Fitur Program
- 🔑 **Enkripsi** plaintext → ciphertext  
- 🔓 **Dekripsi** ciphertext → plaintext  
- 🕵️ **Cari Kunci** dari pasangan plaintext dan ciphertext  
- ⚡ **Test Otomatis** kasus `PYTHON → PUTVUP`  
- Mendukung padding otomatis (`X`) jika panjang plaintext tidak sesuai ordo matriks  
- Invers matriks dihitung menggunakan **aritmatika modulo 26**

---

## 📂 Struktur Repository
