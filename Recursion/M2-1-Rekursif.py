# Program   : Partisi Wilayah Distribusi Darurat Bencana MDMC
# Nilai AIK : Cepat Tanggap, Solidaritas Ta'awun, & Kepemimpinan Terpadu

def partisi_zona_bencana(nama_zona: str, jumlah_jiwa: int, batas_aman: int = 250, level: int = 1):
    """Membagi wilayah terdampak bencana secara rekursif menjadi sub-posko tanggap."""
    indent = "  " * level
    if jumlah_jiwa <= batas_aman:
        print(f"{indent}--> [SUB-POSKO MANDIRI] {nama_zona}: Melayani {jumlah_jiwa} jiwa (Regu Siaga {level})")
        return 1
    
    print(f"{indent}[PARTISI LEVEL {level}] {nama_zona} ({jumlah_jiwa} jiwa) melebihi batas {batas_aman} jiwa.")
    tengah = jumlah_jiwa // 2
    posko_a = partisi_zona_bencana(f"{nama_zona}-Sektor Barat", tengah, batas_aman, level + 1)
    posko_b = partisi_zona_bencana(f"{nama_zona}-Sektor Timur", jumlah_jiwa - tengah, batas_aman, level + 1)
    return posko_a + posko_b

print("=== MANAJEMEN ZONASI TANGGAP BENCANA MDMC PERSYARIKATAN ===")
total_sub_posko = partisi_zona_bencana("Kawasan Lereng Merapi", 1800, batas_aman=300)
print("-" * 65)
print(f"Total Sub-Posko Lapangan yang Wajib Didirikan: {total_sub_posko} Posko Unit")