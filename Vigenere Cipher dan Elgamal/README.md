# 🔐 Vigenere dan ElGamal Cipher

Program ini dibuat untuk memenuhi tugas mata kuliah **Kriptografi**.  
Berisi implementasi **Vigenere Cipher** dan **ElGamal Cipher** lengkap dengan proses enkripsi dan dekripsi.

Vigenere Cipher merupakan sebuah bentuk polyalphabetic cipher, dimana akan dilakukan beberapa substitusi alfabet. Proses enkripsi manual umumnya memanfaatkan Vigenere Table/Square.
Proses enkripsi menggunakan Plain Text & Key. (Key pada kasus ini merupakan text lain, bukan angka)


Algoritma ElGamal ditemukan oleh ilmuwan Mesir, yaitu Taher ElGamal pada tahun 1985, merupakan algoritma kriptografi kunci publik.
Algoritma Elgamal terdiri dari 3 proses yaitu pembentukan kunci, enkripsi, dan dekripsi.


---

## 👩‍💻 Identitas
- **Nama Program** : Vigenere dan ElGamal Cipher  
- **Nama** : Senia Nur Hasanah  
- **NPM** : 140810230021  
- **Deskripsi** : Program ini mengimplementasikan algoritma **Vigenere Cipher** (berbasis substitusi huruf dengan kunci teks) dan **ElGamal Cipher** (berbasis kriptografi kunci publik).  

---

##⚡ Fitur Utama

 **1. Vigenere Cipher**
 - Enkripsi teks dengan kunci alfabet.
 
 - Dekripsi ciphertext kembali ke plaintext.

- Menampilkan tabel proses per karakter (nilai numerik, key, operasi mod 26).

---

**2. ElGamal**
- Enkripsi plaintext huruf besar (A–Z) dengan parameter (p, g, x, k).

- Dekripsi ciphertext kembali ke plaintext.

- Menampilkan tabel proses (c1, c2, cara hitung, hasil dekripsi).

- Ciphertext ditampilkan dalam bentuk pasangan (c1, c2).

---

**3. Menu Interaktif**
- Menu utama: pilih Vigenere Cipher atau ElGamal.

- Submenu enkripsi, dekripsi, atau gabungan (enkripsi + dekripsi).

---

## 📝 Contoh Penggunaan
**1. Vigenere Cipher**

=== MENU KRIPTOGRAFI ===

1. Vigenere Cipher

2. ElGamal

0. Keluar

Pilih menu: 

Input: 1

---

--- Vigenere Cipher ---
1. Enkripsi
2. Dekripsi
3. Enkripsi + Dekripsi
0. Kembali
Pilih:

Input: 3

---
Masukkan plaintext: KRIPTOGRAFI

Masukkan key: kunci


Tabel Proses Enkripsi Vigenere:

No  PT  n(PT) K   n(K)  (PT+K)mod26 CT 

1   K   10    K   10    20       U

2   R   17    U   20    11       L

3   I   8     N   13    21       V

4   P   15    C   2     17       R

5   T   19    I   8     1        B

6   O   14    K   10    24       Y

7   G   6     U   20    0        A

8   R   17    N   13    4        E

9   A   0     C   2     2        C

10  F   5     I   8     13       N

11  I   8     K   10    18       S


Ciphertext: ULVRBYAECNS

Tabel Proses Dekripsi Vigenere:

No  CT  n(CT) K   n(K)  (CT-K)mod26 PT

1   U   20    K   10    10       K

2   L   11    U   20    17       R

3   V   21    N   13    8        I

4   R   17    C   2     15       P

5   B   1     I   8     19       T

6   Y   24    K   10    14       O

7   A   0     U   20    6        G

8   E   4     N   13    17       R

9   C   2     C   2     0        A

10  N   13    I   8     5        F

11  S   18    K   10    8        I


Hasil Dekripsi: KRIPTOGRAFI


---
=== MENU KRIPTOGRAFI ===

1. Vigenere Cipher

2. ElGamal

0. Keluar

Pilih menu: 

Input: 2

---
--- ElGamal Cipher ---

1. Enkripsi

2. Dekripsi
3. Enkripsi + Dekripsi

0. Kembali

Pilih: 3

Masukkan bilangan prima p: 37

Masukkan generator g: 3

Masukkan private key x: 2

Masukkan ephemeral key k: 15

Masukkan plaintext (huruf besar A-Z): EZKRIPTOGRAFI



Kunci publik: p=37, g=3, y=9

Shared value y^k mod p dihitung sekali: 9^15 mod 37 = 10



=== Enkripsi ===

Char  m     c1                c2

E     4     c1=3^15 mod 37=11 c2=4*10 mod 37=3

Z     25    c1=3^15 mod 37=11 c2=25*10 mod 37=28

K     10    c1=3^15 mod 37=11 c2=10*10 mod 37=26

R     17    c1=3^15 mod 37=11 c2=17*10 mod 37=22

I     8     c1=3^15 mod 37=11 c2=8*10 mod 37=6

P     15    c1=3^15 mod 37=11 c2=15*10 mod 37=2

T     19    c1=3^15 mod 37=11 c2=19*10 mod 37=5

O     14    c1=3^15 mod 37=11 c2=14*10 mod 37=29

G     6     c1=3^15 mod 37=11 c2=6*10 mod 37=23

R     17    c1=3^15 mod 37=11 c2=17*10 mod 37=22

A     0     c1=3^15 mod 37=11 c2=0*10 mod 37=0

F     5     c1=3^15 mod 37=11 c2=5*10 mod 37=13

I     8     c1=3^15 mod 37=11 c2=8*10 mod 37=6


Jawaban Akhir (Ciphertext):

(11, 3) (11, 28) (11, 26) (11, 22) (11, 6) (11, 2) (11, 5) (11, 29) (11, 23) (11, 22) (11, 0) (11, 13) (11, 6)


=== Dekripsi ===

c1    c2    m (cara)                           Decrypted

11    3     (3*26 mod 37=4, s=11^2 mod 37=10)  E

11    28    (28*26 mod 37=25, s=11^2 mod 37=10)Z

11    26    (26*26 mod 37=10, s=11^2 mod 37=10)K

11    22    (22*26 mod 37=17, s=11^2 mod 37=10)R

11    6     (6*26 mod 37=8, s=11^2 mod 37=10)  I

11    2     (2*26 mod 37=15, s=11^2 mod 37=10) P

11    5     (5*26 mod 37=19, s=11^2 mod 37=10) T

11    29    (29*26 mod 37=14, s=11^2 mod 37=10)O

11    23    (23*26 mod 37=6, s=11^2 mod 37=10) G

11    22    (22*26 mod 37=17, s=11^2 mod 37=10)R

11    0     (0*26 mod 37=0, s=11^2 mod 37=10)  A

11    13    (13*26 mod 37=5, s=11^2 mod 37=10) F

11    6     (6*26 mod 37=8, s=11^2 mod 37=10)  I


Hasil dekripsi (Plaintext): EZKRIPTOGRAFI

---
