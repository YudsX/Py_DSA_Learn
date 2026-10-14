def hitung_zakat_maal_berantai(aset_keluarga: dict, nisab: float = 85000000, persentase_zakat: float = 0.025) -> float:
    """
    Fungsi rekursif untuk menghitung total zakat maal berantai dari aset keluarga besar.
    """
    total_zakat = 0.0
    
    # Base Case & Rekursi: Iterasi setiap anggota/cabang dalam himpunan aset keluarga
    for anggota, data in aset_keluarga.items():
        total_aset_anggota = data.get("total_aset", 0)
        
        # Hitung zakat anggota jika memenuhi nisab
        if total_aset_anggota >= nisab:
            zakat_anggota = total_aset_anggota * persentase_zakat
        else:
            zakat_anggota = 0.0
            
        total_zakat += zakat_anggota
        
        # Langkah Rekursif: Jika anggota memiliki cabang/sub-keluarga berantai
        if "sub_keluarga" in data and data["sub_keluarga"]:
            total_zakat += hitung_zakat_maal_berantai(
                data["sub_keluarga"], 
                nisab=nisab, 
                persentase_zakat=persentase_zakat
            )
            
    return total_zakat


# PENGUJIAN KODE 
if __name__ == "__main__":
    # Struktur data berantai aset keluarga besar (Pohon / Nested Dict)
    aset_wakaf_keluarga = {
        "Keluarga_Kakek": {
            "total_aset": 150_000_000, # Memenuhi nisab -> Zakat: 3.750.000
            "sub_keluarga": {
                "Keluarga_Anak_1": {
                    "total_aset": 100_000_000, # Memenuhi nisab -> Zakat: 2.500.000
                    "sub_keluarga": {
                        "Keluarga_Cucu_1": {
                            "total_aset": 50_000_000, # Tidak memenuhi nisab -> Zakat: 0
                            "sub_keluarga": {}
                        }
                    }
                },
                "Keluarga_Anak_2": {
                    "total_aset": 200_000_000, # Memenuhi nisab -> Zakat: 5.000.000
                    "sub_keluarga": {}
                }
            }
        }
    }

    # Hitung zakat (Nisab standar misal 85 Juta rupiah, zakat 2.5%)
    total_zakat = hitung_zakat_maal_berantai(aset_wakaf_keluarga)
    
    print("=== HASIL PERHITUNGAN ZAKAT MAAL BERANTAI ===")
    print(f"Total Zakat Maal Keseluruhan: Rp {total_zakat:,.2f}")