"""
Nama Program : hash.py
Nama         : Senia Nur Hasanah
NPM          : 140810230021
Deskripsi    : Membuat Program untuk SHA-1, MD5, HMAC-SHA256
"""

import hashlib
import hmac

file_path = "fasilitas-mahasiswa-4.png"

# Baca file dalam mode binary
with open(file_path, "rb") as f:
    file_data = f.read()

# SHA-1
sha1_hash = hashlib.sha1(file_data).hexdigest()
print("SHA1:", sha1_hash)

# MD5
md5_hash = hashlib.md5(file_data).hexdigest()
print("MD5:", md5_hash)

# HMAC-SHA256 dengan key "kripto25"
key = b"kripto25"
hmac_sha256_hash = hmac.new(key, file_data, hashlib.sha256).hexdigest()
print("HMAC-SHA256:", hmac_sha256_hash)
