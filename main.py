setpoint = 50
data_output = [
    50, 49, 47, 45, 43, 52, 54, 57, 51, 48, 46, 44, 53, 55, 42,
    51.9, 47.9, 54.9, 44.9, 49.5
]


def hitung_error(setpoint, output):
    return abs(setpoint - output)

def status_error(error):
    if error <= 2:
        return "STABIL"
    elif error <= 5:
        return "WARNING"
    else:
        return "TIDAK STABIL"

def rata_rata(data_error):
    return sum(data_error) / len(data_error)

def main():
    daftar_error = []
    jumlah_kategori = {"STABIL": 0, "WARNING": 0, "TIDAK STABIL": 0}

    print("="*10, "MONITORING ERROR TERHADAP SETPOINT", "="*10)

    for nomor, output in enumerate(data_output, start=1):
        error = hitung_error(setpoint, output)
        status = status_error(error)

        daftar_error.append(error)
        jumlah_kategori[status] += 1

        print(f"{nomor:02d} Output = {output:<5} | Error = {error:.2f} -> {status}")

    print()
    print("===== RINGKASAN =====")
    print(f"Total data   : {len(data_output)}")
    for kategori, jumlah in jumlah_kategori.items():
        print(f"{kategori:<13}: {jumlah}")
    print(f"Rata-rata    : {rata_rata(daftar_error):.2f}")
    print(f"Maksimum     : {max(daftar_error):.2f}")
    print(f"Minimum      : {min(daftar_error):.2f}")


if __name__ == "__main__":
    main()