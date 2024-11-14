class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, isbn):
        self.__judul = judul
        self.__pengarang = pengarang
        self.__tahun_terbit = tahun_terbit
        self.__isbn = isbn
        self.__status = 'tersedia'

    def tampilkan_info_buku(self):
        return f"Judul: {self.__judul}, Pengarang: {self.__pengarang}, Tahun Terbit: {self.__tahun_terbit}, ISBN: {self.__isbn}, Status: {self.__status}"

    def pinjam(self):
        self.__status = 'dipinjam'

    def kembalikan(self):
        self.__status = 'tersedia'

    def is_tersedia(self):
        return self.__status == 'tersedia'


class BukuDigital(Buku):
    def __init__(self, judul, pengarang, tahun_terbit, isbn, ukuran_file):
        super().__init__(judul, pengarang, tahun_terbit, isbn)
        self.__ukuran_file = ukuran_file

    def tampilkan_info_buku(self):
        return super().tampilkan_info_buku() + f", Ukuran File: {self.__ukuran_file} MB"


class Anggota:
    def __init__(self, nama, nomor_anggota, alamat):
        self.__nama = nama
        self.__nomor_anggota = nomor_anggota
        self.__alamat = alamat
        self.__daftar_pinjaman = []

    def tampilkan_info_anggota(self):
        info = f"Nama: {self.__nama}, Nomor Anggota: {self.__nomor_anggota}, Alamat: {self.__alamat}"
        if self.__daftar_pinjaman:
            info += f", Buku Dipinjam: {[buku.tampilkan_info_buku() for buku in self.__daftar_pinjaman]}"
        return info

    def pinjam_buku(self, buku):
        self.__daftar_pinjaman.append(buku)

    def kembalikan_buku(self, buku):
        self.__daftar_pinjaman.remove(buku)


class Perpustakaan:
    def __init__(self):
        self.__daftar_buku = []
        self.__daftar_anggota = []

    def tambah_buku(self, buku):
        self.__daftar_buku.append(buku)

    def tambah_anggota(self, anggota):
        self.__daftar_anggota.append(anggota)

    def daftar_buku_tersedia(self):
        return [buku.tampilkan_info_buku() for buku in self.__daftar_buku if buku.is_tersedia()]

    def pinjam_buku(self, nomor_anggota, isbn):
        anggota = next((a for a in self.__daftar_anggota if a._Anggota__nomor_anggota == nomor_anggota), None)
        buku = next((b for b in self.__daftar_buku if b._Buku__isbn == isbn), None)

        if anggota and buku and buku.is_tersedia():
            anggota.pinjam_buku(buku)
            buku.pinjam()
            return f"Buku '{buku._Buku__judul}' berhasil dipinjam oleh {anggota._Anggota__nama}."
        return "Proses peminjaman gagal."

    def kembalikan_buku(self, nomor_anggota, isbn):
        anggota = next((a for a in self.__daftar_anggota if a._Anggota__nomor_anggota == nomor_anggota), None)
        buku = next((b for b in self.__daftar_buku if b._Buku__isbn == isbn), None)

        if anggota and buku in anggota._Anggota__daftar_pinjaman:
            anggota.kembalikan_buku(buku)
            buku.kembalikan()
            return f"Buku '{buku._Buku__judul}' berhasil dikembalikan oleh {anggota._Anggota__nama}."
        return "Proses pengembalian gagal."


def main():
    perpustakaan = Perpustakaan()

    while True:
        print("\n=== Aplikasi Manajemen Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Tambah Anggota")
        print("3. Daftar Buku Tersedia")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. Tampilkan Info Anggota")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            judul = input(" Masukkan judul buku: ")
            pengarang = input("Masukkan pengarang buku: ")
            tahun_terbit = input("Masukkan tahun terbit: ")
            isbn = input("Masukkan ISBN: ")
            buku_baru = Buku(judul, pengarang, tahun_terbit, isbn)
            perpustakaan.tambah_buku(buku_baru)
            print("Buku berhasil ditambahkan.")

        elif pilihan == '2':
            nama = input("Masukkan nama anggota: ")
            nomor_anggota = input("Masukkan nomor anggota: ")
            alamat = input("Masukkan alamat: ")
            anggota_baru = Anggota(nama, nomor_anggota, alamat)
            perpustakaan.tambah_anggota(anggota_baru)
            print("Anggota berhasil ditambahkan.")

        elif pilihan == '3':
            print("Daftar Buku Tersedia:")
            for info in perpustakaan.daftar_buku_tersedia():
                print(info)

        elif pilihan == '4':
            nomor_anggota = input("Masukkan nomor anggota: ")
            isbn = input("Masukkan ISBN buku yang ingin dipinjam: ")
            print(perpustakaan.pinjam_buku(nomor_anggota, isbn))

        elif pilihan == '5':
            nomor_anggota = input("Masukkan nomor anggota: ")
            isbn = input("Masukkan ISBN buku yang ingin dikembalikan: ")
            print(perpustakaan.kembalikan_buku(nomor_anggota, isbn))

        elif pilihan == '6':
            nomor_anggota = input("Masukkan nomor anggota: ")
            anggota = next((a for a in perpustakaan._Perpustakaan__daftar_anggota if a._Anggota__nomor_anggota == nomor_anggota), None)
            if anggota:
                print(anggota.tampilkan_info_anggota())
            else:
                print("Anggota tidak ditemukan.")

        elif pilihan == '0':
            print("Terima kasih telah menggunakan aplikasi manajemen perpustakaan.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()