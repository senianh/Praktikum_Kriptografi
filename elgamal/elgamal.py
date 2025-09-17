""" 
Nama Program  :  ElGamal
Nama          :  Senia Nur Hasanah
NPM           :  140810230021
Deskripsi     :  Implementasi enkripsi dan dekripsi ElGamal
"""

# ===============================
# ELGAMAL
# ===============================
def mod_exp(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

def elgamal_encrypt(p, g, x, k, plaintext):
    y = mod_exp(g, x, p)
    yk = mod_exp(y, k, p)
    c1 = mod_exp(g, k, p)
    c1_list, c2_list = [], []

    print("\n=== Enkripsi ===")
    print(f"{'Char':<6}{'m':<6}{'c1':<18}{'c2':<20}")
    for ch in plaintext:
        m = ord(ch) - ord('A')
        c2 = (m * yk) % p
        c1_list.append(c1)
        c2_list.append(c2)
        print(f"{ch:<6}{m:<6}{f'c1={g}^{k} mod {p}={c1}':<18}{f'c2={m}*{yk} mod {p}={c2}':<20}")

    # Cetak jawaban akhir dalam bentuk pasangan (c1, c2)
    print("\nJawaban Akhir (Ciphertext):")
    ciphertext_pairs = list(zip(c1_list, c2_list))
    for pair in ciphertext_pairs:
        print(pair, end=" ")
    print()
    return c1_list, c2_list

def elgamal_decrypt(p, g, x, c1_list, c2_list):
    print("\n=== Dekripsi ===")
    print(f"{'c1':<6}{'c2':<6}{'m (cara)':<35}{'Decrypted':<10}")
    decrypted_text = ""
    for i in range(len(c1_list)):
        c1_val = c1_list[i]
        c2_val = c2_list[i]
        s = mod_exp(c1_val, x, p)          # s = c1^x mod p
        s_inv = mod_exp(s, p-2, p)         # inverse dari s
        m = (c2_val * s_inv) % p           # plaintext numeric
        decrypted_text += chr(m + ord('A'))
        cara = f"({c2_val}*{s_inv} mod {p}={m}, s={c1_val}^{x} mod {p}={s})"
        print(f"{c1_val:<6}{c2_val:<6}{cara:<35}{chr(m + ord('A')):<10}")

    print("\nHasil dekripsi (Plaintext):", decrypted_text)
    return decrypted_text

def menu_elgamal():
    while True:
        print("\n--- ElGamal ---")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Enkripsi + Dekripsi")
        print("0. Kembali")
        pilih = input("Pilih: ")

        if pilih == "1":
            p = int(input("Masukkan bilangan prima p: "))
            g = int(input("Masukkan generator g: "))
            x = int(input("Masukkan private key x: "))
            k = int(input("Masukkan ephemeral key k: "))
            plaintext = input("Masukkan plaintext (huruf besar A-Z): ").upper()

            y = mod_exp(g, x, p)
            print(f"\nKunci publik: p={p}, g={g}, y={y}")
            yk = mod_exp(y, k, p)
            print(f"Shared value y^k mod p dihitung sekali: {y}^{k} mod {p} = {yk}\n")

            elgamal_encrypt(p, g, x, k, plaintext)

        elif pilih == "2":
            p = int(input("Masukkan bilangan prima p: "))
            g = int(input("Masukkan generator g: "))
            x = int(input("Masukkan private key x: "))

            c1 = int(input("Masukkan nilai c1 (hanya sekali): "))
            c2_list = list(map(int, input("Masukkan list c2 (pisahkan dengan spasi): ").split()))

            # buat list c1 yang panjangnya sama dengan c2_list
            c1_list = [c1] * len(c2_list)

            elgamal_decrypt(p, g, x, c1_list, c2_list)

        elif pilih == "3":
            p = int(input("Masukkan bilangan prima p: "))
            g = int(input("Masukkan generator g: "))
            x = int(input("Masukkan private key x: "))
            k = int(input("Masukkan ephemeral key k: "))
            plaintext = input("Masukkan plaintext (huruf besar A-Z): ").upper()

            y = mod_exp(g, x, p)
            print(f"\nKunci publik: p={p}, g={g}, y={y}")
            yk = mod_exp(y, k, p)
            print(f"Shared value y^k mod p dihitung sekali: {y}^{k} mod {p} = {yk}\n")

            c1_list, c2_list = elgamal_encrypt(p, g, x, k, plaintext)
            elgamal_decrypt(p, g, x, c1_list, c2_list)

        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu_elgamal()
