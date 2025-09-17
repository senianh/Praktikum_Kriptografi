# 🔐 ElGamal 

Algoritma ElGamal ditemukan oleh ilmuwan Mesir, yaitu Taher ElGamal pada tahun 1985, merupakan algoritma kriptografi kunci publik.
Algoritma Elgamal terdiri dari 3 proses yaitu pembentukan kunci, enkripsi, dan dekripsi.


---

## 👩‍💻 Identitas
- **Nama Program** : Vigenere dan ElGamal Cipher  
- **Nama** : Senia Nur Hasanah  
- **NPM** : 140810230021  
- **Deskripsi** : Program ini mengimplementasikan algoritma **Vigenere Cipher** (berbasis substitusi huruf dengan kunci teks) dan **ElGamal Cipher** (berbasis kriptografi kunci publik).  

---

## ⚡ Fitur Utama

---

**ElGamal**
- Enkripsi plaintext huruf besar (A–Z) dengan parameter (p, g, x, k).

- Dekripsi ciphertext kembali ke plaintext.

- Menampilkan tabel proses (c1, c2, cara hitung, hasil dekripsi).

- Ciphertext ditampilkan dalam bentuk pasangan (c1, c2).

---

**Menu Interaktif**
- Menu utama : enkripsi, dekripsi, atau gabungan (enkripsi + dekripsi).

---

## 📝 Contoh Penggunaan ElGamal

---


1. Enkripsi

2. Dekripsi

3. Enkripsi + Dekripsi

0. Kembali


Pilih:
---
Input: 1 
---
Enkripsi 
---

Masukkan bilangan prima p: 37

Masukkan generator g: 3

Masukkan private key x: 2

Masukkan ephemeral key k: 15

Masukkan plaintext (huruf besar A-Z): EZKRIPTOGRAFI

---

Kunci publik: p=37, g=3, y=9

Shared value y^k mod p dihitung sekali: 9^15 mod 37 = 10

---


Proses Enkripsi ElGamal

| Char | m  | c1                | c2                |
|------|----|--------------------|-------------------|
| E    | 4  | 3^15 mod 37 = 11  | (4 * 10) mod 37 = 3  |
| Z    | 25 | 3^15 mod 37 = 11  | (25 * 10) mod 37 = 28 |
| K    | 10 | 3^15 mod 37 = 11  | (10 * 10) mod 37 = 26 |
| R    | 17 | 3^15 mod 37 = 11  | (17 * 10) mod 37 = 22 |
| I    | 8  | 3^15 mod 37 = 11  | (8 * 10) mod 37 = 6  |
| P    | 15 | 3^15 mod 37 = 11  | (15 * 10) mod 37 = 2 |
| T    | 19 | 3^15 mod 37 = 11  | (19 * 10) mod 37 = 5 |
| O    | 14 | 3^15 mod 37 = 11  | (14 * 10) mod 37 = 29 |
| G    | 6  | 3^15 mod 37 = 11  | (6 * 10) mod 37 = 23 |
| R    | 17 | 3^15 mod 37 = 11  | (17 * 10) mod 37 = 22 |
| A    | 0  | 3^15 mod 37 = 11  | (0 * 10) mod 37 = 0 |
| F    | 5  | 3^15 mod 37 = 11  | (5 * 10) mod 37 = 13 |
| I    | 8  | 3^15 mod 37 = 11  | (8 * 10) mod 37 = 6 |



Jawaban Akhir (Ciphertext):

(11, 3) (11, 28) (11, 26) (11, 22) (11, 6) (11, 2) (11, 5) (11, 29) (11, 23) (11, 22) (11, 0) (11, 13) (11, 6)

---
Input: 2
---
Dekripsi
---

Masukkan bilangan prima p: 37

Masukkan generator g: 3

Masukkan private key x: 2

Masukkan nilai c1 (hanya sekali): 11

Masukkan list c2 (pisahkan dengan spasi): 3 28 26 22 6 2 5 29 23 22 0 13 6

---

Proses Dekripsi ElGamal

| c1 | c2 | Perhitungan (cara)                     | Decrypted |
|----|----|-----------------------------------------|-----------|
| 11 | 3  | (3 * 26 mod 37 = 4, s = 11^2 mod 37=10) | E         |
| 11 | 28 | (28 * 26 mod 37 = 25, s=11^2 mod 37=10) | Z         |
| 11 | 26 | (26 * 26 mod 37 = 10, s=11^2 mod 37=10) | K         |
| 11 | 22 | (22 * 26 mod 37 = 17, s=11^2 mod 37=10) | R         |
| 11 | 6  | (6 * 26 mod 37 = 8, s=11^2 mod 37=10)   | I         |
| 11 | 2  | (2 * 26 mod 37 = 15, s=11^2 mod 37=10)  | P         |
| 11 | 5  | (5 * 26 mod 37 = 19, s=11^2 mod 37=10)  | T         |
| 11 | 29 | (29 * 26 mod 37 = 14, s=11^2 mod 37=10) | O         |
| 11 | 23 | (23 * 26 mod 37 = 6, s=11^2 mod 37=10)  | G         |
| 11 | 22 | (22 * 26 mod 37 = 17, s=11^2 mod 37=10) | R         |
| 11 | 0  | (0 * 26 mod 37 = 0, s=11^2 mod 37=10)   | A         |
| 11 | 13 | (13 * 26 mod 37 = 5, s=11^2 mod 37=10)  | F         |
| 11 | 6  | (6 * 26 mod 37 = 8, s=11^2 mod 37=10)   | I         |


Hasil dekripsi (Plaintext): EZKRIPTOGRAFI

---
Input: 3
---
Enkripsi + Dekripsi
---
Masukkan bilangan prima p: 37

Masukkan generator g: 3

Masukkan private key x: 2

Masukkan ephemeral key k: 15

Masukkan plaintext (huruf besar A-Z): EZKRIPTOGRAFI

---

Kunci publik: p=37, g=3, y=9

Shared value y^k mod p dihitung sekali: 9^15 mod 37 = 10

---


Proses Enkripsi ElGamal

| Char | m  | c1                | c2                |
|------|----|--------------------|-------------------|
| E    | 4  | 3^15 mod 37 = 11  | (4 * 10) mod 37 = 3  |
| Z    | 25 | 3^15 mod 37 = 11  | (25 * 10) mod 37 = 28 |
| K    | 10 | 3^15 mod 37 = 11  | (10 * 10) mod 37 = 26 |
| R    | 17 | 3^15 mod 37 = 11  | (17 * 10) mod 37 = 22 |
| I    | 8  | 3^15 mod 37 = 11  | (8 * 10) mod 37 = 6  |
| P    | 15 | 3^15 mod 37 = 11  | (15 * 10) mod 37 = 2 |
| T    | 19 | 3^15 mod 37 = 11  | (19 * 10) mod 37 = 5 |
| O    | 14 | 3^15 mod 37 = 11  | (14 * 10) mod 37 = 29 |
| G    | 6  | 3^15 mod 37 = 11  | (6 * 10) mod 37 = 23 |
| R    | 17 | 3^15 mod 37 = 11  | (17 * 10) mod 37 = 22 |
| A    | 0  | 3^15 mod 37 = 11  | (0 * 10) mod 37 = 0 |
| F    | 5  | 3^15 mod 37 = 11  | (5 * 10) mod 37 = 13 |
| I    | 8  | 3^15 mod 37 = 11  | (8 * 10) mod 37 = 6 |



Jawaban Akhir (Ciphertext):

(11, 3) (11, 28) (11, 26) (11, 22) (11, 6) (11, 2) (11, 5) (11, 29) (11, 23) (11, 22) (11, 0) (11, 13) (11, 6)

---

Proses Dekripsi ElGamal

| c1 | c2 | Perhitungan (cara)                     | Decrypted |
|----|----|-----------------------------------------|-----------|
| 11 | 3  | (3 * 26 mod 37 = 4, s = 11^2 mod 37=10) | E         |
| 11 | 28 | (28 * 26 mod 37 = 25, s=11^2 mod 37=10) | Z         |
| 11 | 26 | (26 * 26 mod 37 = 10, s=11^2 mod 37=10) | K         |
| 11 | 22 | (22 * 26 mod 37 = 17, s=11^2 mod 37=10) | R         |
| 11 | 6  | (6 * 26 mod 37 = 8, s=11^2 mod 37=10)   | I         |
| 11 | 2  | (2 * 26 mod 37 = 15, s=11^2 mod 37=10)  | P         |
| 11 | 5  | (5 * 26 mod 37 = 19, s=11^2 mod 37=10)  | T         |
| 11 | 29 | (29 * 26 mod 37 = 14, s=11^2 mod 37=10) | O         |
| 11 | 23 | (23 * 26 mod 37 = 6, s=11^2 mod 37=10)  | G         |
| 11 | 22 | (22 * 26 mod 37 = 17, s=11^2 mod 37=10) | R         |
| 11 | 0  | (0 * 26 mod 37 = 0, s=11^2 mod 37=10)   | A         |
| 11 | 13 | (13 * 26 mod 37 = 5, s=11^2 mod 37=10)  | F         |
| 11 | 6  | (6 * 26 mod 37 = 8, s=11^2 mod 37=10)   | I         |


Hasil dekripsi (Plaintext): EZKRIPTOGRAFI
