"""
Nama Program : hillCipher.py
Nama         : Senia Nur Hasanah
NPM          : 140810230021
Deskripsi    : Membuat Program untuk enkripsi, dekripsi, dan mencari kunci Hill Cipher
"""

import numpy as np

# ------------------------
# Helper
# ------------------------
def char_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_char(n):
    return chr((n % 26) + ord('A'))

def text_to_nums(text):
    return [char_to_num(c) for c in text.upper() if c.isalpha()]

def nums_to_text(nums):
    return ''.join(num_to_char(n) for n in nums)

def modinv(a, m=26):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def mat_mult(A, B):
    n = len(A)
    m = len(B[0])
    result = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 26
    return result

def mat_mult_vec(A, v):
    n = len(A)
    result = [0]*n
    for i in range(n):
        for j in range(n):
            result[i] += A[i][j] * v[j]
        result[i] %= 26
    return result

def mat_inv2(M):
    # inverse khusus 2x2
    a, b = M[0]
    c, d = M[1]
    det = (a*d - b*c) % 26
    inv_det = modinv(det, 26)
    if inv_det is None:
        return None
    return [[( d*inv_det)%26, (-b*inv_det)%26],
            [(-c*inv_det)%26, ( a*inv_det)%26]]

# ------------------------
# Encrypt / Decrypt
# ------------------------
def encrypt(plaintext, key):
    n = len(key)
    pt_nums = text_to_nums(plaintext)
    if len(pt_nums) % n != 0:
        pt_nums += [char_to_num('X')] * (n - len(pt_nums) % n)

    ct_nums = []
    for i in range(0, len(pt_nums), n):
        block = pt_nums[i:i+n]
        enc = mat_mult_vec(key, block)
        ct_nums.extend(enc)
    return nums_to_text(ct_nums)

def decrypt(ciphertext, key):
    n = len(key)
    ct_nums = text_to_nums(ciphertext)
    inv_key = mat_inv2(key)
    if inv_key is None:
        raise ValueError("Kunci tidak invertible")
    pt_nums = []
    for i in range(0, len(ct_nums), n):
        block = ct_nums[i:i+n]
        dec = mat_mult_vec(inv_key, block)
        pt_nums.extend(dec)
    return nums_to_text(pt_nums)

# ------------------------
# Cari Kunci
# ------------------------
def find_key_analytic(plaintext, ciphertext, n):
    pt_nums = text_to_nums(plaintext)
    ct_nums = text_to_nums(ciphertext)

    if len(pt_nums) < n*n or len(ct_nums) < n*n:
        return None

    # ambil n*n huruf pertama
    P = [[pt_nums[i*n+j] for j in range(n)] for i in range(n)]
    C = [[ct_nums[i*n+j] for j in range(n)] for i in range(n)]

    P_inv = mat_inv2(P)
    if P_inv is None:
        return None

    key = mat_mult(C, P_inv)
    return key

def find_key_bruteforce(plaintext, ciphertext, n=2):
    pt_nums = text_to_nums(plaintext)
    ct_nums = text_to_nums(ciphertext)

    P_blocks = [pt_nums[i:i+n] for i in range(0, len(pt_nums), n)]
    C_blocks = [ct_nums[i:i+n] for i in range(0, len(ct_nums), n)]

    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    key = [[a,b],[c,d]]
                    valid = True
                    for p, ciph in zip(P_blocks, C_blocks):
                        enc = mat_mult_vec(key, p)
                        if [x%26 for x in enc] != [y%26 for y in ciph]:
                            valid = False
                            break
                    if valid:
                        return key
    return None

def find_key(plaintext, ciphertext, n=2):
    key = find_key_analytic(plaintext, ciphertext, n)
    if key:
        print("[+] Kunci ditemukan metode analitik")
        return key
    else:
        return find_key_bruteforce(plaintext, ciphertext, n)

# ------------------------
# Menu
# ------------------------
def main():
    while True:
        print("\n===== Hill Cipher Menu =====")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Cari Kunci (Plain & Cipher)")
        print("4. Test otomatis (PYTHON -> PUTVUP)")
        print("0. Keluar")
        pilihan = input("Pilih menu : ")
        if pilihan == "1":
            pt = input("Masukkan plaintext: ")
            key = [[7,6],[2,5]]
            print("Ciphertext:", encrypt(pt, key))
        elif pilihan == "2":
            ct = input("Masukkan ciphertext: ")
            key = [[7,6],[2,5]]
            print("Plaintext:", decrypt(ct, key))
        elif pilihan == "3":
            pt = input("Masukkan plaintext: ")
            ct = input("Masukkan ciphertext: ")
            n = int(input("Ordo matriks kunci (contoh 2): "))
            key = find_key(pt, ct, n)
            if key:
                print("Key matrix:")
                for row in key:
                    print(row)
            else:
                print("Tidak ditemukan kunci")
        elif pilihan == "4":
            pt, ct = "PYTHON", "PUTVUP"
            key = find_key(pt, ct, 2)

            # Enkripsi
            print("\n=== Enkripsi ===")
            print("Asal Plaintext :", pt)
            enc = encrypt(pt, key)
            print("Hasil Ciphertext:", enc)

            # Dekripsi
            print("\n=== Dekripsi ===")
            print("Asal Ciphertext:", ct)
            dec = decrypt(ct, key)
            print("Hasil Plaintext :", dec)

            # Cari Kunci
            print("\n=== Cari Kunci ===")
            print("Plaintext :", pt)
            print("Ciphertext:", ct)
            print("Kunci ditemukan:")
            for row in key:
                print(row)

        elif pilihan == "0":
            break
        else:
            print("Pilihan salah!")

if __name__ == "__main__":
    main()
