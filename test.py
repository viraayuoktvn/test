import pickle
import calc

def main():
    # Input data
    total_assets = float(input("Total harta kepemilikan: "))
    total_debts = float(input("Total utang: "))
    will = float(input("Total wasiat: "))
    medical_expenses = float(input("Biaya perawatan selama sakit: "))
    funeral_expenses = float(input("Biaya pengurusan jenazah: "))
    
    # Input jumlah dan nilai prediksi untuk setiap jenis anggota keluarga
    family_members = {}

    # Input jumlah anggota keluarga untuk masing-masing jenis hubungan
    for relationship in ["ap", "al", "cp", "cl", "suami", "istri", "ayah", "ibu", "kakek", "nenek", "si", "sdlk", "sdpk"]:
        family_members[f"total_{relationship}"] = float(input(f"Total {relationship}: "))

    dt_model = calc.load_model("id3_without_pruning_model.pkl")
    
    total_inheritance, inheritance_status, share_ap, share_al, share_cl, share_cp, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, share_si, share_sdlk, share_sdpk = calc.calculate_inheritance(total_assets, total_debts, will, medical_expenses, funeral_expenses, family_members, dt_model)

    print("\nTotal harta waris yang dapat dibagikan:", total_inheritance)
    calc.print_inheritance_status(inheritance_status)
    print(f"Jumlah anggota keluarga yang dapat mewarisi: {calc.calculate_individual_inheritance(inheritance_status)}")
    print("Bagian masing-masing ahli waris:")
    print(f"Share Anak Perempuan: {share_ap}")
    print(f"Share Anak Laki-laki: {share_al}")
    print(f"Share Cucu Laki-laki: {share_cl}")
    print(f"Share Cucu Perempuan: {share_cp}")
    print(f"Share Suami: {share_suami}")
    print(f"Share Istri: {share_istri}")
    print(f"Share Ayah: {share_ayah}")
    print(f"Share Ibu: {share_ibu}")
    print(f"Share Kakek: {share_kakek}")
    print(f"Share Nenek: {share_nenek}")
    print(f"Share Si: {share_si}")
    print(f"Share SDLK: {share_sdlk}")
    print(f"Share SDPK: {share_sdpk}")

if __name__ == "__main__":
    main()
