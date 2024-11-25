"""
AHMAD MUFIE NURRIZZIQIE 152022071
Mk : Pemdas 
Kelas : FF
"""

# Data panen
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

""" SOAL TUGAS GITHUB"""

# 1. Tampilkan seluruh data
print(data_panen)

# 2. Tampilkan jumlah hasil panen jagung dari lokasi2
hasil_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"\nJumlah hasil panen jagung dari lokasi2: {hasil_jagung_lokasi2}")

# 3. Tampilkan nama lokasi dari lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"\nNama lokasi dari lokasi3: {nama_lokasi3}")

# 4. Masukkan jumlah hasil panen padi dan kedelai ke dalam variabel yang berbeda
    # 'i' adalah lokasinya,  'j' adalah hasil panen nya
hasil_padi = {i: j['hasil_panen']['padi'] for i, j in data_panen.items()}
hasil_kedelai = {i: j['hasil_panen']['kedelai'] for i, j in data_panen.items()}

print("\nHasil Panen Padi:")
print(hasil_padi)

print("\nHasil Panen Kedelai:")
print(hasil_kedelai)

# 5. Variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi
hasil_padi = []
hasil_kedelai = []
    # 'i' adalah lokasinya,  'j' adalah hasil panen nya
for i, j in data_panen.items():
    hasil_padi.append(j['hasil_panen']['padi'])
    hasil_kedelai.append(j['hasil_panen']['kedelai'])

print("\nHasil Panen Padi di Setiap Lokasi:", hasil_padi)
print("\nHasil Panen Kedelai di Setiap Lokasi:", hasil_kedelai)

# 6. Buat percabangan untuk perhatian khusus
print("\nStatus Lokasi Berdasarkan Hasil Panen:")
    # 'i' adalah lokasinya,  'j' adalah hasil panen nya
for i, j in data_panen.items():
    padi = j['hasil_panen']['padi']
    jagung = j['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"{j['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{j['nama_lokasi']} dalam kondisi baik.")
