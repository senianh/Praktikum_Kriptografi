"""
Nama Program : lsb.py
Nama         : Senia Nur Hasanah
NPM          : 140810230021
Deskripsi    : Buat program encode dan decode steganography yang dapat menyembunyikan sebuah pesan atau file gambar (Bahasa Pemrograman Bebas).
"""

from PIL import Image

# -----------------------------
# Fungsi Encode (Menyembunyikan Pesan)
# -----------------------------
def encode_image(input_image, message, output_image):
    img = Image.open(input_image)
    encoded = img.copy()
    width, height = img.size
    index = 0
    message += chr(0)  # tanda akhir pesan (null char)

    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))  # ambil RGB pixel
            for n in range(3):  # untuk R, G, B
                if index < len(message) * 8:
                    bit = (ord(message[index // 8]) >> (7 - index % 8)) & 1
                    pixel[n] = (pixel[n] & ~1) | bit
                    index += 1
            encoded.putpixel((x, y), tuple(pixel))
            if index >= len(message) * 8:
                encoded.save(output_image)
                print(f"✅ Pesan berhasil disembunyikan dalam: {output_image}")
                return
    encoded.save(output_image)
    print("⚠️ Pesan terlalu panjang untuk gambar ini!")

# -----------------------------
# Fungsi Decode (Membaca Pesan)
# -----------------------------
def decode_image(stego_image):
    img = Image.open(stego_image)
    width, height = img.size
    bits = []
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            for n in range(3):
                bits.append(pixel[n] & 1)
    chars = []
    for b in range(0, len(bits), 8):
        byte = 0
        for bit in bits[b:b+8]:
            byte = (byte << 1) | bit
        if byte == 0:  # null char = akhir pesan
            break
        chars.append(chr(byte))
    return ''.join(chars)

# -----------------------------
# Contoh Penggunaan Program
# -----------------------------
if __name__ == "__main__":
    print("===== Program Steganografi LSB =====")
    print("1. Encode (sembunyikan pesan)")
    print("2. Decode (baca pesan)\n")

    choice = input("Pilih menu (1/2): ")

    if choice == "1":
        input_image = input("Masukkan nama file gambar (misal: input.png): ")
        message = input("Masukkan pesan yang ingin disembunyikan : ")
        output_image = input("Masukkan nama file output (misal: stego.png): ")
        encode_image(input_image, message, output_image)

    elif choice == "2":
        stego_image = input("Masukkan nama file gambar hasil encode : ")
        secret = decode_image(stego_image)
        print("\n🔍 Pesan rahasia tersembunyi : ")
        print(secret)
    else:
        print("Pilihan tidak valid.")
