# Program   : Rantai Rekam Medis Pasien RS PKU Muhammadiyah
# Nilai AIK : Amanah Rekam Medis, Perlindungan Jiwa (Hifdzun Nafs)

class NodeMedis:
    def __init__(self, waktu: str, tindakan: str, dokter: str):
        self.waktu = waktu
        self.tindakan = tindakan
        self.dokter = dokter
        self.next = None

class RekamMedisPKU:
    def __init__(self):
        self.head = None

    def catat_tindakan(self, waktu: str, tindakan: str, dokter: str):
        baru = NodeMedis(waktu, tindakan, dokter)
        if not self.head:
            self.head = baru
            return
        bantu = self.head
        while bantu.next:
            bantu = bantu.next
        bantu.next = baru

    def tampilkan_kronologi(self, nama_pasien: str):
        print(f"=== KRONOLOGI TINDAKAN PASIEN: {nama_pasien.upper()} ===")
        bantu = self.head
        no = 1
        while bantu:
            print(f"{no}. [{bantu.waktu}] {bantu.tindakan} (PPA: {bantu.dokter})")
            bantu = bantu.next
            no += 1

rm = RekamMedisPKU()
rm.catat_tindakan("08:00", "Pemeriksaan Tanda Vital & Triase IGD", "dr. Ahmad Dahlan")
rm.catat_tindakan("08:30", "Pemberian Cairan Infus Ringer Laktat", "Perawat Nabila")
rm.catat_tindakan("10:15", "Pemeriksaan USG Abdomen Cito", "dr. Sp.Rad")
rm.tampilkan_kronologi("Fauzan Azhim")