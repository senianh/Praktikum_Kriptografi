""" 
Nama Program  :  Vigenere Cipher
Nama          :  Senia Nur Hasanah
NPM           :  140810230021
Deskripsi     :  Implementasi enkripsi dan dekripsi Vigenere Cipher
"""

# ===============================
# VIGENERE CIPHER
# ===============================
def vigenere_encrypt_process(plaintext, key):
    print("\nTabel Proses Enkripsi Vigenere:")
    print("{:<3} {:<3} {:<5} {:<3} {:<5} {:<8} {:<3}".format(
        "No","PT","n(PT)","K","n(K)","(PT+K)mod26","CT"))
    
    ciphertext = ""
    key = key.lower()
    key_nums = [ord(k) - ord('a') for k in key]
    key_index = 0

    for i, char in enumerate(plaintext.upper()):
        if char.isalpha():
            p = ord(char) - ord('A')
            k = key_nums[key_index % len(key_nums)]
            c = (p + k) % 26
            ct_char = chr(c + ord('A'))
            ciphertext += ct_char
            print("{:<3} {:<3} {:<5} {:<3} {:<5} {:<8} {:<3}".format(
                i+1, char, p, key[key_index % len(key_nums)].upper(), k, c, ct_char
            ))
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt_process(ciphertext, key):
    print("\nTabel Proses Dekripsi Vigenere:")
    print("{:<3} {:<3} {:<5} {:<3} {:<5} {:<8} {:<3}".format(
        "No","CT","n(CT)","K","n(K)","(CT-K)mod26","PT"))
    
    plaintext = ""
    key = key.lower()
    key_nums = [ord(k) - ord('a') for k in key]
    key_index = 0

    for i, char in enumerate(ciphertext.upper()):
        if char.isalpha():
            c = ord(char) - ord('A')
            k = key_nums[key_index % len(key_nums)]
            p = (c - k) % 26
            pt_char = chr(p + ord('A'))
            plaintext += pt_char
            print("{:<3} {:<3} {:<5} {:<3} {:<5} {:<8} {:<3}".format(
                i+1, char, c, key[key_index % len(key_nums)].upper(), k, p, pt_char
            ))
            key_index += 1
        else:
            plaintext += char
    return plaintext

def menu_vigenere():
    while True:
        print("\n--- Vigenere Cipher ---")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Enkripsi + Dekripsi")
        print("0. Kembali")
        pilih = input("Pilih: ")

        if pilih == "1":
            pt = input("Masukkan plaintext: ")
            key = input("Masukkan key: ")
            ct = vigenere_encrypt_process(pt, key)
            print("\nCiphertext:", ct)
        elif pilih == "2":
            ct = input("Masukkan ciphertext: ")
            key = input("Masukkan key: ")
            pt = vigenere_decrypt_process(ct, key)
            print("\nPlaintext:", pt)
        elif pilih == "3":
            pt = input("Masukkan plaintext: ")
            key = input("Masukkan key: ")
            ct = vigenere_encrypt_process(pt, key)
            print("\nCiphertext:", ct)
            pt2 = vigenere_decrypt_process(ct, key)
            print("\nHasil Dekripsi:", pt2)
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu_vigenere()
