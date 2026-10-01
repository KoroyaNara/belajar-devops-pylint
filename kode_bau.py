"""Modul contoh fungsi yang sudah mengikuti konvensi PEP 8."""


def hitung_total(nilai_a, nilai_b, daftar, tambahan):
    """Menghitung total dari beberapa nilai.

    Args:
        nilai_a: Bilangan pertama.
        nilai_b: Bilangan kedua.
        daftar: List yang elemen pertamanya ikut dijumlahkan.
        tambahan: Bilangan tambahan.

    Returns:
        Hasil penjumlahan semua nilai.
    """
    return nilai_a + nilai_b + daftar[0] + tambahan


def main():
    """Fungsi utama program."""
    hasil = hitung_total(1, 2, [3], 4)
    print(f"Total: {hasil}")


if __name__ == "__main__":
    main()