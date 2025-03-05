def tampilkan_nama_nim(nama, nim):
    garis = "=" * 43
    print(f"\n{garis}")
    print(f"Nama: {nama}")
    print(f"NIM: {nim}")
    print(f"{garis}")

# Input dari pengguna
nama = "PRAWIDITYA SAHRUL AKBAR"
nim = "312410146"

# Menjalankan fungsi
tampilkan_nama_nim(nama, nim)

def hitung_biaya_pengiriman(berat, jarak, jenis_pengiriman, status_member):
    # Biaya dasar
    biaya_total = 10000
    
    # Detail perhitungan
    perhitungan = []
    
    # Menambahkan biaya dasar
    perhitungan.append(["Biaya Dasar", 10000])

    # Menambahkan biaya jika berat paket melebihi 5 kg
    if berat > 5:
        biaya_total += 5000
        perhitungan.append(["Biaya Berat > 5 kg", 5000])
    
    # Menambahkan biaya jika jarak pengiriman lebih dari 10 km
    if jarak > 10:
        biaya_total += 8000
        perhitungan.append(["Biaya Jarak > 10 km", 8000])
    
    # Menambahkan biaya jika memilih pengiriman express
    if jenis_pengiriman.lower() == "express":
        biaya_total += 20000
        perhitungan.append(["Biaya Pengiriman Express", 20000])
    
    # Memberikan diskon 10% jika pelanggan adalah member
    diskon = 0
    if status_member.lower() == "member":
        diskon = biaya_total * 0.1
        biaya_total -= diskon
        perhitungan.append(["Diskon Member (10%)", -diskon])
    
    # Menampilkan tabel perhitungan secara manual
    print(f"{'Keterangan':<25} {'Biaya (Rp)'}")
    print("="*40)
    for item in perhitungan:
        print(f"{item[0]:<25} {item[1]:>10}")
    
    print("="*40)
    print(f"{'Total Biaya Pengiriman':<25} {biaya_total:>10.2f}")
    
    return biaya_total

# Mengambil input dari pengguna
try:
    berat_paket = float(input("Masukkan berat paket (kg): "))
    jarak_pengiriman = float(input("Masukkan jarak pengiriman (km): "))
    jenis_pengiriman = input("Masukkan jenis pengiriman (biasa/express): ").lower()
    status_member = input("Apakah Anda member? (member/non-member): ").lower()

    # Menghitung dan menampilkan biaya pengiriman
    total_biaya = hitung_biaya_pengiriman(berat_paket, jarak_pengiriman, jenis_pengiriman, status_member)

except ValueError:
    print("Input yang Anda masukkan tidak valid. Pastikan menggunakan angka untuk berat dan jarak.")
