
# 🔐 Vigenere 


Vigenere Cipher merupakan sebuah bentuk polyalphabetic cipher, dimana akan dilakukan beberapa substitusi alfabet. Proses enkripsi manual umumnya memanfaatkan Vigenere Table/Square.
Proses enkripsi menggunakan Plain Text & Key. (Key pada kasus ini merupakan text lain, bukan angka)


---

## 👩‍💻 Identitas
- **Nama Program** : Vigenere Cipher  
- **Nama** : Senia Nur Hasanah  
- **NPM** : 140810230021  
- **Deskripsi** : Program ini mengimplementasikan algoritma **Vigenere Cipher**

---

##⚡ Fitur Utama

 **1. Vigenere Cipher**
 - Enkripsi teks dengan kunci alfabet.
 
 - Dekripsi ciphertext kembali ke plaintext.

- Menampilkan tabel proses per karakter (nilai numerik, key, operasi mod 26).

---

**3. Menu Interaktif**
- Menu utama: enkripsi, dekripsi, atau gabungan (enkripsi + dekripsi).

---

## 📝 Contoh Penggunaan Vigenere Cipher

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

| No | PT  | n(PT) | K  | n(K) | (PT+K) mod 26 | CT |
|----|-----|-------|----|------|---------------|----|
| 1  | K   | 10    | K  | 10   | 20            | U  |
| 2  | R   | 17    | U  | 20   | 11            | L  |
| 3  | I   | 8     | N  | 13   | 21            | V  |
| 4  | P   | 15    | C  | 2    | 17            | R  |
| 5  | T   | 19    | I  | 8    | 1             | B  |
| 6  | O   | 14    | K  | 10   | 24            | Y  |
| 7  | G   | 6     | U  | 20   | 0             | A  |
| 8  | R   | 17    | N  | 13   | 4             | E  |
| 9  | A   | 0     | C  | 2    | 2             | C  |
| 10 | F   | 5     | I  | 8    | 13            | N  |
| 11 | I   | 8     | K  | 10   | 18            | S  |



Ciphertext: ULVRBYAECNS

---

Tabel Proses Dekripsi Vigenere:

| No | CT | n(CT) | K | n(K) | (CT - K) mod 26 | PT |
| -- | -- | ----- | - | ---- | --------------- | -- |
| 1  | U  | 20    | K | 10   | 10              | K  |
| 2  | L  | 11    | U | 20   | 17              | R  |
| 3  | V  | 21    | N | 13   | 8               | I  |
| 4  | R  | 17    | C | 2    | 15              | P  |
| 5  | B  | 1     | I | 8    | 19              | T  |
| 6  | Y  | 24    | K | 10   | 14              | O  |
| 7  | A  | 0     | U | 20   | 6               | G  |
| 8  | E  | 4     | N | 13   | 17              | R  |
| 9  | C  | 2     | C | 2    | 0               | A  |
| 10 | N  | 13    | I | 8    | 5               | F  |
| 11 | S  | 18    | K | 10   | 8               | I  |



Hasil Dekripsi: KRIPTOGRAFI

