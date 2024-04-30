import pickle

def calculate_inheritance(total_assets, total_debts, will, medical_expenses, funeral_expenses, family_members, dt_model):
    inheritance_status = {}
    total_inheritance = total_assets - total_debts - will - medical_expenses - funeral_expenses

    for relationship, _ in family_members.items():
        # Pastikan hubungan keluarga terdefinisi dalam model
        if relationship.startswith("total_"):
            # Ubah hubungan keluarga menjadi yang diinginkan untuk mencocokkan model
            prediction_key = relationship.replace("total_", "hw_")
            if prediction_key not in dt_model:
                print(f"Error: No model found for {prediction_key}")
                continue
            # Ambil nilai atribut yang mempengaruhi prediksi warisan
            predictors = [family_members[key] for key in family_members.keys() if key.startswith("total_")]
            # Lakukan prediksi menggunakan model yang sesuai untuk setiap jenis anggota keluarga
            prediction = predict_inheritance(predictors, dt_model[prediction_key])
            inheritance_status[relationship] = prediction

    # Ambil nilai pembagian warisan
    total_inheritance_share = calculate_inheritance_share(total_assets, total_debts, will, medical_expenses, funeral_expenses, family_members, inheritance_status)
    
    return total_inheritance, inheritance_status, *total_inheritance_share


def predict_inheritance(predictors, dt_model):
    model = dt_model['model']
    prediction_proba = model.predict_proba([predictors])[0]
    
    if prediction_proba[1] >= 0.5:
        prediction_string = 'TIDAK DAPAT'
    else:
        prediction_string = 'DAPAT'
    
    return prediction_string

def load_model(filename):
    with open(filename, 'rb') as file:
        models = pickle.load(file)
    return models

def calculate_individual_inheritance(inheritance_status):
    # Menghitung bagian masing-masing anggota keluarga yang dapat mewarisi
    inheritance_count = sum([1 for status in inheritance_status.values() if status == 'DAPAT'])
    return inheritance_count

def calculate_inheritance_share(total_assets, total_debts, will, medical_expenses, funeral_expenses, family_members, dt_model):
    total_inheritance = total_assets - total_debts - will - medical_expenses - funeral_expenses
    inheritance_status = {}  # Inisialisasi dictionary untuk menyimpan status warisan

    # Mengambil nilai atribut yang diperlukan untuk perhitungan
    suami = family_members.get("total_suami", 0)
    istri = family_members.get("total_istri", 0)
    anak_laki = family_members.get("total_al", 0)
    anak_perempuan = family_members.get("total_ap", 0)
    cucu_laki = family_members.get("total_cl", 0)
    cucu_perempuan = family_members.get("total_cp", 0)
    ayah = family_members.get("total_ayah", 0)
    ibu = family_members.get("total_ibu", 0)
    kakek = family_members.get("total_kakek", 0)
    nenek = family_members.get("total_nenek", 0)
    saudara_seibu = family_members.get("total_si", 0)
    saudara_laki_kandung = family_members.get("total_sdlk", 0)
    saudara_perempuan_kandung = family_members.get("total_sdpk", 0)

    share_suami = 0
    share_istri = 0
    share_al = 0
    share_ap = 0
    share_cl = 0
    share_cp = 0
    share_ayah = 0
    share_ibu = 0
    share_kakek = 0
    share_nenek = 0
    share_si = 0
    share_sdlk = 0
    share_sdpk = 0

    for relationship, status in inheritance_status.items():
        if status == 'TIDAK DAPAT':
            if relationship == "suami":
                share_suami = 0
            if relationship == "istri":
                share_istri = 0
            if relationship == "ayah":
                share_ayah = 0
            if relationship == "ibu":
                share_ibu = 0
            if relationship == "kakek":
                share_kakek = 0
            if relationship == "nenek":
                share_nenek = 0
            if relationship == "si":
                share_si = 0
            if relationship == "sdlk":
                share_sdlk = 0
            if relationship == "sdpk":
                share_sdpk = 0

        # Periksa apakah hasil prediksi adalah 'DAPAT'
        elif inheritance_status[relationship] == 'DAPAT':
            # Menerapkan aturan sesuai dengan hubungan keluarga
            if relationship == "suami":
                if suami > 0 and anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
                    share_suami = (1 / 2) * total_inheritance
                elif suami > 0 and ((anak_laki > 0 or cucu_laki > 0) or (anak_perempuan > 0 or cucu_perempuan > 0)):
                    share_suami = (1 / 4) * total_inheritance
                elif suami > 0 and anak_laki == 0 and cucu_laki == 0:
                    conditions = [
                        ((3 / 13), (ayah > 0 or kakek > 0 ) or (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                        ((3 / 13), (ayah > 0 or kakek > 0) or (ibu > 0 or nenek > 0) and anak_perempuan == 1 and cucu_perempuan > 0),
                        ((3 / 13), (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                        ((3 / 13), (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and anak_perempuan == 0 and cucu_perempuan == 1),
                        ((3 / 15), (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                        ((3 / 15), (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and anak_perempuan == 1 and cucu_perempuan > 0),
                        ((3 / 7), ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_seibu == 0 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0),
                        ((3 / 7), ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_seibu == 1 and saudara_perempuan_kandung == 1  and ibu == 0 and nenek == 0),
                        ((3 / 8), ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0),
                        ((3 / 8), ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung >= 2 and saudara_perempuan_kandung == 1 and ibu == 0 and nenek > 0),
                        ((3 / 9), ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung >= 2 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek > 0),
                        ((3 / 8), saudara_seibu == 1 and saudara_perempuan_kandung == 1  and (ibu > 0 or nenek > 0)),
                        ((3 / 9), saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0)),
                        ((3 / 9), saudara_perempuan_kandung >= 2 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0) and nenek > 0),
                        ((3 / 10), saudara_perempuan_kandung >= 2 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0) and nenek > 0),
                        ((3 / 8), saudara_seibu == 0 and saudara_perempuan_kandung > 0 and ibu > 0 and nenek == 0),
                        ((3 / 7), saudara_seibu == 0 and saudara_perempuan_kandung == 1 and ibu == 0 and nenek > 0),
                        ((3 / 8), saudara_seibu == 0 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek > 0)
                    ]
                    for value, condition in conditions:
                        if condition:
                            share_suami = value * total_inheritance
                            break
                else :
                    share_suami = 0

            if relationship == "istri":
                if istri > 0 and anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
                    share_istri = (1 / 4) * total_inheritance
                elif istri > 0 and (anak_laki > 0 or cucu_laki > 0 or anak_perempuan > 0 or cucu_perempuan > 0):
                    share_istri = (1 / 8) * total_inheritance
                elif istri > 0 and anak_laki == 0 and cucu_laki == 0:
                    conditions = [
                        ((3 / 27), (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                        ((3 / 27), (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and anak_perempuan == 1 and cucu_perempuan > 0),
                        ((3 / 15), (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and anak_perempuan >= 2 and cucu_perempuan > 0),
                        ((3 / 13), ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and (saudara_seibu == 1 or saudara_perempuan_kandung >= 2) and ibu == 0 and nenek == 0),
                        ((3 / 13), ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and (saudara_seibu >= 2 or saudara_perempuan_kandung == 1) and ibu == 0 and nenek == 0),
                        ((3 / 15), ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_seibu >= 2 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0),
                        ((3 / 13), saudara_seibu == 1 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0)),
                        ((3 / 15), saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0)),
                        ((3 / 15), saudara_perempuan_kandung >= 2 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0) and nenek > 0),
                        ((3 / 17), saudara_perempuan_kandung >= 2 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0) and nenek > 0),
                        ((3 / 13), saudara_seibu == 0 and saudara_perempuan_kandung > 0 and ibu > 0 and nenek == 0),
                        ((3 / 13), saudara_seibu == 0 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek > 0)
                    ]
                    for value, condition in conditions:
                        if condition:
                            share_istri = value * total_inheritance
                            break
                else:
                    share_istri = 0

            if relationship == "ayah":
                if ayah > 0:
                    if anak_perempuan == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
                        if (suami == 0 or istri == 0) and ibu == 0 and kakek == 0 and nenek == 0 and saudara_seibu == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                            share_ayah = total_inheritance
                        elif ibu > 0 or suami > 0 or istri > 0 or nenek > 0:
                            # Menghitung bagian dari ahli waris
                            share_ayah = total_inheritance - (share_ibu + share_suami + share_istri + share_nenek)
                    elif anak_laki > 0 or cucu_laki > 0:
                        share_ayah = (1 / 6) * total_inheritance
                    elif anak_laki == 0 or cucu_laki == 0:
                        share_ayah = 0
                        conditions = [
                            (1 / 4, anak_perempuan == 1 or cucu_perempuan == 1),
                            (1 / 5, anak_perempuan >= 2 or cucu_perempuan >= 2),
                            (1 / 5, anak_perempuan == 1 and cucu_perempuan > 0),
                            (1 / 5, (ibu > 0 or nenek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            (1 / 6, (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            (1 / 6, (ibu > 0 or nenek > 0) and anak_perempuan > 0 and cucu_perempuan > 0),
                            (3 / 16, suami > 0 and ibu == 0 and nenek == 0 and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            (2 / 13, suami > 0 and ibu == 0 and nenek == 0 and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            (2 / 13, (suami > 0 and (ibu > 0 or nenek > 0)) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            (2 / 15, (suami > 0 and (ibu > 0 or nenek > 0)) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            (2 / 15, (suami > 0 and (ibu > 0 or nenek > 0)) and anak_perempuan > 0 and cucu_perempuan > 0),
                            (2 / 13, suami > 0 and anak_perempuan >= 2 and cucu_perempuan > 0),
                            (7 / 32, istri > 0 and ibu == 0 and nenek == 0 and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            (7 / 40, istri > 0 and ibu == 0 and nenek == 0 and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            (7 / 40, (istri > 0 and (ibu > 0 or nenek > 0)) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            (4 / 27, (istri > 0 and (ibu > 0 or nenek > 0)) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            (4 / 27, (istri > 0 and (ibu > 0 or nenek > 0)) and anak_perempuan > 0 and cucu_perempuan > 0),
                            (7 / 40, istri > 0 and anak_perempuan == 1 and cucu_perempuan > 0)
                        ]
                        for value, condition in conditions:
                            if condition:
                                share_ayah = value * total_inheritance
                                break
                else:
                    share_ayah = 0

            if relationship == "ibu":
                if ibu > 0:
                    if anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
                        if (suami == 0 or istri == 0) and ayah == 0 and kakek == 0 and nenek == 0 and saudara_seibu == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                            share_ibu = total_inheritance
                        elif ayah > 0 or suami > 0 or istri > 0 or kakek > 0:
                            share_ibu = total_inheritance - (share_suami + share_istri)
                        elif suami > 0 and (ayah > 0 or kakek > 0):
                            share_ibu = (1 / 6) * total_inheritance
                        elif istri > 0 and ayah > 0:
                            share_ibu = (1 / 4) * total_inheritance
                        elif istri > 0 and kakek > 0:
                            share_ibu = (1 / 3) * total_inheritance
                    elif anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0 and saudara < 2:
                        share_ibu = (1 / 3) * total_inheritance
                    elif anak_laki > 0 or cucu_laki > 0 or saudara_laki_kandung > 0:
                        share_ibu = (1 / 6) * total_inheritance
                    elif anak_laki == 0 and cucu_laki == 0 and saudara_laki_kandung == 1:
                        share_ibu = (1 / 3) * total_inheritance
                    elif anak_laki == 0 and cucu_laki == 0:
                        conditions = [
                            ((1 / 4), anak_perempuan == 1 or cucu_perempuan == 1),
                            ((1 / 5), anak_perempuan >= 2 or cucu_perempuan >= 2),
                            ((1 / 5), (ayah > 0 or kakek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((1 / 6), (ayah > 0 or kakek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((1 / 5), (ayah == 0 and kakek == 0) and anak_perempuan > 0 and cucu_perempuan > 0),
                            ((1 / 6), (ayah > 0 or kakek > 0) and anak_perempuan > 0 and cucu_perempuan > 0),
                            ((3 / 16), suami > 0 and (ayah == 0 and kakek == 0) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((2 / 13), suami > 0 and (ayah == 0 and kakek == 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((2 / 13), (suami > 0 and (ayah > 0 or kakek > 0)) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((2 / 15), (suami > 0 and (ayah > 0 or kakek > 0)) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((2 / 15), (suami > 0 and (ayah > 0 or kakek > 0)) and anak_perempuan > 0 and cucu_perempuan > 0),
                            ((2 / 13), suami > 0 and anak_perempuan > 0 and cucu_perempuan > 0),
                            ((7 / 32), istri > 0 and (ayah == 0 and kakek == 0) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((7 / 40), istri > 0 and (ayah == 0 and kakek == 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((7 / 40), (istri > 0 and (ayah > 0 or kakek > 0)) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((4 / 27), (istri > 0 and (ayah > 0 or kakek > 0)) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((4 / 27), (istri > 0 and (ayah > 0 or kakek > 0)) and anak_perempuan > 0 and cucu_perempuan > 0),
                            ((7 / 40), istri > 0 and anak_perempuan > 0 and cucu_perempuan > 0)
                        ]
                        for value, condition in conditions:
                            if condition:
                                share_ibu = value * total_inheritance
                                break
                else:       
                    share_ibu = 0

            if relationship == "kakek":
                if kakek > 0 and ayah == 0:
                    if anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
                        if (suami == 0 or istri == 0) and ayah == 0 and ibu == 0 and nenek == 0 and saudara_seibu == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                            share_kakek = total_inheritance
                        elif ibu > 0 or suami > 0 or istri > 0 or nenek > 0:
                            share_kakek = total_inheritance - (share_ibu + share_suami + share_istri + share_nenek)
                    elif anak_laki > 0 or cucu_laki > 0:  
                        share_kakek = (1 / 6) * total_inheritance
                    elif anak_laki == 0 and cucu_laki == 0:
                        conditions = [
                            ((1 / 4), (ibu == 0 and nenek == 0) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((1 / 5), (ibu == 0 and nenek == 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((1 / 5), (ibu > 0 or nenek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((1 / 6), (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((1 / 5), (ibu == 0 and nenek == 0) and anak_perempuan > 0 and cucu_perempuan > 0),
                            ((1 / 6), (ibu > 0 or nenek > 0) and anak_perempuan > 0 and cucu_perempuan > 0),
                            ((3 / 16), suami > 0 and (ibu == 0 and nenek == 0) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((2 / 13), suami > 0 and (ibu == 0 and nenek == 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((2 / 13), (suami > 0 and (ibu > 0 or nenek > 0)) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((2 / 15), (suami > 0 and (ibu > 0 or nenek > 0)) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((2 / 13), suami > 0 and (ibu == 0 and nenek == 0) and anak_perempuan > 0 and cucu_perempuan > 0),
                            ((2 / 15), (suami > 0 and (ibu > 0 or nenek > 0)) and anak_perempuan > 0 and cucu_perempuan > 0),
                            ((7 / 32), istri > 0 and (ibu == 0 and nenek == 0) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((7 / 40), istri > 0 and (ibu == 0 and nenek == 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((7 / 40), (istri > 0 and (ibu > 0 or nenek > 0)) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((4 / 27), (istri > 0 and (ibu > 0 or nenek > 0)) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((7 / 40), istri > 0 and (ibu == 0 and nenek == 0) and anak_perempuan > 0 and cucu_perempuan > 0),
                            ((4 / 27), (istri > 0 and (ibu > 0 or nenek > 0)) and anak_perempuan > 0 and cucu_perempuan > 0)
                        ]
                        for value, condition in conditions:
                            if condition:
                                share_kakek = value * total_inheritance
                                break
                else:
                    share_kakek = 0

            if relationship == "nenek":
                if nenek > 0 and ibu == 0:
                    if anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
                        conditions = [
                            (total_inheritance, (suami == 0 or istri == 0) and ayah == 0 and ibu == 0 and kakek == 0 and saudara_seibu == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0),
                            (total_inheritance - (share_suami + share_istri), ayah > 0 or suami > 0 or istri > 0 or kakek > 0),
                            ((1 / 6) * total_inheritance, (ayah > 0 or kakek > 0) and suami > 0),
                            ((1 / 3) * total_inheritance, (ayah > 0 or kakek > 0) and istri > 0),
                            ((1 / 3) * total_inheritance, kakek > 0 and ayah == 0 and suami == 0 and istri == 0)
                        ]
                        for value, condition in conditions:
                            if condition:
                                share_nenek = value
                                break
                    elif anak_laki > 0 or cucu_laki > 0 or anak_perempuan > 0 or cucu_perempuan > 0:  
                        share_nenek = (1 / 6) * total_inheritance
                    elif anak_laki == 0 and cucu_laki == 0:
                        conditions = [
                            ((1 / 4), (ayah == 0 and kakek == 0) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((1 / 5), (ayah == 0 and kakek == 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((1 / 5), (ayah > 0 or kakek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((1 / 6), (ayah > 0 or kakek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((1 / 5), (ayah == 0 and kakek == 0) and anak_perempuan > 0 and cucu_perempuan > 0),
                            ((1 / 6), (ayah > 0 or kakek > 0) and anak_perempuan > 0 and cucu_perempuan > 0),
                            ((1 / 2), (ayah == 0 and kakek == 0 and saudara_laki_kandung == 0) and saudara_seibu == 1 and saudara_perempuan_kandung == 0 and suami == 0 and istri == 0),
                            ((1 / 3), (ayah == 0 and kakek == 0 and saudara_laki_kandung == 0) and saudara_seibu >= 2 and saudara_perempuan_kandung == 0 and suami == 0 and istri == 0),
                            ((1 / 5), (ayah == 0 and kakek == 0) and saudara_seibu == 1 and saudara_perempuan_kandung == 1 and suami == 0 and istri == 0),
                            ((1 / 6), (ayah == 0 and kakek == 0) and saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and suami == 0 and istri == 0),
                            ((1 / 6), (ayah == 0 and kakek == 0) and saudara_seibu >= 2 and saudara_perempuan_kandung == 1 and suami == 0 and istri == 0),
                            ((1 / 7), (ayah == 0 and kakek == 0) and saudara_seibu >= 2 and saudara_perempuan_kandung >= 2 and suami == 0 and istri == 0),
                            ((1 / 8), (ayah == 0 and kakek == 0) and saudara_seibu == 1 and saudara_perempuan_kandung == 1 and suami > 0 and istri == 0),
                            ((1 / 9), (ayah == 0 and kakek == 0) and saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and suami > 0 and istri == 0),
                            ((1 / 9), (ayah == 0 and kakek == 0) and saudara_seibu >= 2 and saudara_perempuan_kandung == 1 and suami > 0 and istri == 0),
                            ((1 / 10), (ayah == 0 and kakek == 0) and saudara_seibu >= 2 and saudara_perempuan_kandung >= 2 and suami > 0 and istri == 0),
                            ((2 / 13), (ayah == 0 and kakek == 0) and saudara_seibu == 1 and saudara_perempuan_kandung == 1 and suami == 0 and istri > 0),
                            ((2 / 15), (ayah == 0 and kakek == 0) and saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and suami == 0 and istri > 0),
                            ((2 / 15), (ayah == 0 and kakek == 0) and saudara_seibu >= 2 and saudara_perempuan_kandung == 1 and suami == 0 and istri > 0),
                            ((2 / 17), (ayah == 0 and kakek == 0) and saudara_seibu >= 2 and saudara_perempuan_kandung >= 2 and suami == 0 and istri > 0),
                            ((1 / 4), (ayah == 0 and kakek == 0) and saudara_seibu == 1 and saudara_perempuan_kandung == 0 and suami > 0),
                            ((1 / 6), (ayah == 0 and kakek == 0) and saudara_seibu >= 2 and saudara_perempuan_kandung == 0 and suami > 0),
                            ((3 / 8), (ayah == 0 and kakek == 0) and saudara_seibu == 1 and saudara_perempuan_kandung == 0 and istri > 0),
                            ((1 / 4), (ayah == 0 and kakek == 0) and saudara_seibu >= 2 and saudara_perempuan_kandung == 0 and istri > 0),
                            ((1 / 4), (ayah == 0 and kakek == 0) and saudara_seibu == 0 and saudara_perempuan_kandung == 1 and suami == 0 and istri == 0),
                            ((1 / 5), (ayah == 0 and kakek == 0) and saudara_seibu == 0 and saudara_perempuan_kandung >= 2 and suami == 0 and istri == 0),
                            ((1 / 7), (ayah == 0 and kakek == 0) and saudara_seibu == 0 and saudara_perempuan_kandung == 1 and suami > 0 and istri == 0),
                            ((1 / 8), (ayah == 0 and kakek == 0) and saudara_seibu == 0 and saudara_perempuan_kandung >= 2 and suami > 0 and istri == 0),
                            ((3 / 16), (ayah == 0 and kakek == 0) and saudara_seibu == 0 and saudara_perempuan_kandung == 1 and suami == 0 and istri > 0),
                            ((2 / 13), (ayah == 0 and kakek == 0) and saudara_seibu == 0 and saudara_perempuan_kandung >= 2 and suami == 0 and istri > 0)
                        ]
                        for value, condition in conditions:
                            if condition:
                                share_nenek = value * total_inheritance
                                break
                    elif anak_laki == 0 and cucu_laki > 0 and suami > 0 and anak_perempuan > 0 and cucu_perempuan > 0:
                        share_nenek = (2 / 13) * total_inheritance
                    else:  # Jika ada ibu
                        share_nenek = 0  # Nenek = 0 (tidak mewarisi)
                else:
                    share_nenek = 0
    
            if relationship == "al":  # Anak laki-laki
                if anak_laki > 0:
                    # Menghitung bagian dari ahli waris
                    bagian_ahli_waris = share_suami + share_istri + share_ayah + share_ibu + share_kakek + share_nenek

                    # Hitung sisa dari total warisan
                    sisa = total_inheritance - bagian_ahli_waris
                    
                    # Cek kondisi tambahan
                    if anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0 and (suami == 0 or istri == 0) and ayah == 0 and ibu == 0 and kakek == 0 and nenek == 0:
                        share_al = total_inheritance
                    elif anak_perempuan == 0 and (suami > 0 or istri > 0 or ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0):
                        share_al = sisa
                    elif anak_perempuan > 0:
                        share_al = (2 / 3) * sisa
                else:
                    share_al = 0

            if relationship == "ap":  # Anak perempuan
                if anak_perempuan > 0:
                    bagian_ahli_waris = sum([share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek])
                    sisa = total_inheritance - bagian_ahli_waris

                    if anak_laki == 0 and cucu_laki == 0:
                        if anak_perempuan == 1:
                            if ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0:
                                share_ap = (3 / 4) * total_inheritance 
                            elif (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0) and cucu_perempuan == 0:
                                share_ap = (9 / 16) * total_inheritance
                            elif (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0) and cucu_perempuan > 0:
                                share_ap = (6 / 13) * total_inheritance
                            elif (ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0):
                                share_ap = (6 / 13) * total_inheritance
                        elif anak_perempuan >= 2:
                            if ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0:
                                share_ap = (4 / 5) * total_inheritance
                            elif (ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0) or (saudara_laki_kandung > 0 or saudara_perempuan_kandung > 0):
                                share_ap = (2 / 3) * total_inheritance
                    elif ayah == 0 and kakek == 0:
                        conditions = [
                            ((1 / 4), (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((1 / 5), (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((1 / 5), (ibu > 0 or nenek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1)),
                            ((1 / 6), (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                            ((1 / 5), anak_perempuan > 0 and cucu_perempuan > 0),
                            ((1 / 6), anak_perempuan > 0 and cucu_perempuan > 0),
                            ((1 / 2), saudara_seibu == 1 and saudara_perempuan_kandung == 0 and suami == 0 and istri == 0),
                            ((1 / 3), saudara_seibu >= 2 and saudara_perempuan_kandung == 0 and suami == 0 and istri == 0),
                            ((1 / 5), saudara_seibu == 1 and saudara_perempuan_kandung == 1 and suami == 0 and istri == 0),
                            ((1 / 6), saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and suami == 0 and istri == 0),
                            ((1 / 6), saudara_seibu >= 2 and saudara_perempuan_kandung == 1 and suami == 0 and istri == 0),
                            ((1 / 7), saudara_seibu >= 2 and saudara_perempuan_kandung >= 2 and suami == 0 and istri == 0),
                            ((1 / 8), saudara_seibu == 1 and saudara_perempuan_kandung == 1 and suami > 0 and istri == 0),
                            ((1 / 9), saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and suami > 0 and istri == 0),
                            ((1 / 9), saudara_seibu >= 2 and saudara_perempuan_kandung == 1 and suami > 0 and istri == 0),
                            ((1 / 10), saudara_seibu >= 2 and saudara_perempuan_kandung >= 2 and suami > 0 and istri == 0),
                            ((2 / 13), saudara_seibu == 1 and saudara_perempuan_kandung == 1 and suami == 0 and istri > 0),
                            ((2 / 15), saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and suami == 0 and istri > 0),
                            ((2 / 15), saudara_seibu >= 2 and saudara_perempuan_kandung == 1 and suami == 0 and istri > 0),
                            ((2 / 17), saudara_seibu >= 2 and saudara_perempuan_kandung >= 2 and suami == 0 and istri > 0),
                            ((1 / 4), saudara_seibu == 1 and saudara_perempuan_kandung == 0 and suami > 0),
                            ((1 / 6), saudara_seibu >= 2 and saudara_perempuan_kandung == 0 and suami > 0),
                            ((3 / 8), saudara_seibu == 1 and saudara_perempuan_kandung == 0 and istri > 0),
                            ((1 / 4), saudara_seibu >= 2 and saudara_perempuan_kandung == 0 and istri > 0),
                            ((1 / 4), saudara_seibu == 0 and saudara_perempuan_kandung == 1 and suami == 0 and istri == 0),
                            ((1 / 5), saudara_seibu == 0 and saudara_perempuan_kandung >= 2 and suami == 0 and istri == 0),
                            ((1 / 7), saudara_seibu == 0 and saudara_perempuan_kandung == 1 and suami > 0 and istri == 0),
                            ((1 / 8), saudara_seibu == 0 and saudara_perempuan_kandung >= 2 and suami > 0 and istri == 0),
                            ((3 / 16), saudara_seibu == 0 and saudara_perempuan_kandung == 1 and suami == 0 and istri > 0),
                            ((2 / 13), saudara_seibu == 0 and saudara_perempuan_kandung >= 2 and suami == 0 and istri > 0)
                        ]
                        for value, condition in conditions:
                            if condition:
                                share_ap = value * total_inheritance
                                break
            
            if relationship == "cl":  # Cucu laki-laki dari anak laki-laki
                if cucu_laki > 0 and anak_laki == 0:
                    bagian_ahli_waris = sum([share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek])
                    sisa = total_inheritance - bagian_ahli_waris

                    # Cek kondisi tambahan
                    if cucu_perempuan == 0 and anak_perempuan == 0 and (suami == 0 or istri == 0) and ayah == 0 and ibu == 0 and kakek == 0 and nenek == 0:
                        share_cl = total_inheritance
                    elif cucu_perempuan == 0:
                        if (suami > 0 or istri > 0 or ibu > 0 or kakek > 0 or nenek > 0):
                            share_cl = sisa
                        elif ayah > 0 and suami == 0 and istri == 0 and ibu == 0 and kakek == 0 and nenek == 0:
                            share_cl = (cucu_laki/(ayah + cucu_laki)) * total_inheritance
                        elif ayah > 0 and (suami > 0 or istri > 0 or ibu > 0 or kakek > 0 or nenek > 0):
                            share_cl = (cucu_laki/(ayah + cucu_laki)) * sisa
                    elif cucu_perempuan > 0:
                        conditions = [
                            ((2 / 3), anak_perempuan >= 0 and suami == 0 and istri == 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                            ((2 / 3), anak_perempuan >= 0 and (suami > 0 or istri > 0) and ayah == 0 and ibu == 0 and kakek == 0 and nenek == 0),
                            (0, anak_perempuan >= 2 and suami > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                            (0, anak_perempuan >= 2 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0))),
                            ((2 / 3), anak_perempuan >= 0 and (suami > 0 or istri > 0) and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0))),
                            ((2 / 3), anak_perempuan >= 0 and istri > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                            ((2 / 3), anak_perempuan >= 0 and ((ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0))),
                            (((cucu_laki / (ayah + cucu_laki)) * 2 / 3), anak_perempuan == 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0))),
                            (((cucu_laki / (ayah + cucu_laki)) * 2 / 3), anak_perempuan == 0 and (suami > 0 or istri > 0) and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0))),
                            (0, anak_perempuan > 0 and suami > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0))),
                            (0, anak_perempuan >= 2 and suami > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0)))
                        ]
                        for value, condition in conditions:
                            if condition:
                                share_cl = value * sisa
                                break
                else:
                    share_cl = 0
            
            if relationship == "cp":  # Cucu perempuan dari anak laki-laki
                if cucu_perempuan > 0 and anak_laki == 0:
                    # Menghitung bagian dari ahli waris
                    bagian_ahli_waris = sum([share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek])
                    sisa = total_inheritance - bagian_ahli_waris

                    if cucu_laki > 0:
                        share_cp = (1 / 3) * sisa  # Bagian jika ada cucu perempuan dan cucu laki-laki, tetapi tidak ada anak laki-laki
                        if anak_perempuan > 0 and (suami > 0 or istri > 0) and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0)):
                            share_cp = 0
                    elif cucu_laki == 0:
                        conditions = [
                            ((1 / 2), anak_perempuan == 0 and cucu_perempuan == 1 and suami == 0 and istri == 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                            ((3 / 4), anak_perempuan == 0 and cucu_perempuan == 1 and suami == 0 and istri == 0 and (ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0)),
                            ((3 / 5), anak_perempuan == 0 and cucu_perempuan == 1 and suami == 0 and istri == 0 and (ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0)),
                            ((2 / 3), anak_perempuan == 0 and cucu_perempuan >= 2 and suami == 0 and istri == 0),
                            ((4 / 5), anak_perempuan == 0 and cucu_perempuan >= 2 and suami == 0 and istri == 0),
                            ((2 / 3), anak_perempuan == 0 and cucu_perempuan >= 2 and suami > 0),
                            ((8 / 13), anak_perempuan == 0 and cucu_perempuan >= 2 and suami > 0),
                            ((7 / 10), anak_perempuan == 0 and cucu_perempuan >= 2 and istri > 0),
                            ((16 / 27), anak_perempuan == 0 and cucu_perempuan >= 2 and istri > 0),
                            ((1 / 5), anak_perempuan == 1 and suami == 0 and istri == 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                            ((1 / 6), anak_perempuan == 1 and suami == 0 and istri == 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0))),
                            ((1 / 4), anak_perempuan == 1 and suami > 0 and (ayah == 0 and ibu == 0 and kakek == 0 and nenek == 0)),
                            ((2 / 13), anak_perempuan == 1 and suami > 0),
                            ((2 / 15), anak_perempuan == 1 and suami > 0),
                            ((7 / 32), anak_perempuan == 1 and istri > 0),
                            ((7 / 40), anak_perempuan == 1 and istri > 0),
                            ((4 / 27), anak_perempuan == 1 and istri > 0),
                            ((1 / 3), anak_perempuan >= 2 and cucu_laki > 0),
                            ((1 / 6), anak_perempuan >= 2 and (saudara_laki_kandung > 0 or saudara_perempuan_kandung > 0))
                        ]
                        for value, condition in conditions:
                            if condition:
                                share_cp = value * total_inheritance
                                break
                    else:
                        share_cp = 0
                else:
                    share_cp = 0

            if relationship == "si":
                # Menghitung bagian dari ahli waris
                bagian_ahli_waris = sum([share_suami, share_istri, share_ibu, share_nenek])
                sisa = total_inheritance - bagian_ahli_waris

                if saudara_seibu == 1 and ayah == 0 and kakek == 0 and anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
                    if suami == 0 and istri == 0 and ibu == 0 and nenek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                        share_si = total_inheritance 
                    elif saudara_laki_kandung > 0:
                        share_si = (1 / 6) * total_inheritance
                    elif saudara_laki_kandung == 0:
                        conditions = [
                            ((1 / 4) * total_inheritance, suami == 0 and istri == 0 and saudara_perempuan_kandung == 1),
                            ((1 / 5) * total_inheritance, suami == 0 and istri == 0 and saudara_perempuan_kandung >= 2),
                            ((1 / 5) * total_inheritance, suami == 0 and istri == 0 and (ibu > 0 or nenek > 0) and saudara_perempuan_kandung == 1),
                            ((1 / 6) * total_inheritance, suami == 0 and istri == 0 and (ibu > 0 or nenek > 0) and saudara_perempuan_kandung >= 2),
                            ((1 / 7) * total_inheritance, suami > 0 and saudara_perempuan_kandung == 1 and ibu == 0 and nenek == 0),
                            ((1 / 8) * total_inheritance, suami > 0 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0),
                            ((1 / 8) * total_inheritance, suami > 0 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0)),
                            ((1 / 9) * total_inheritance, suami > 0 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0)),
                            ((3 / 16) * total_inheritance, istri > 0 and saudara_perempuan_kandung == 1 and ibu == 0 and nenek == 0),
                            ((2 / 13) * total_inheritance, istri > 0 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0),
                            ((2 / 13) * total_inheritance, istri > 0 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0)),
                            ((2 / 15) * total_inheritance, istri > 0 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0))
                        ]
                        for value, condition in conditions:
                            if condition:
                                share_si = value
                                break
                    else:
                        share_si = sisa
                elif saudara_seibu >= 2 and ayah == 0 and kakek == 0 and anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
                    conditions = [
                        (total_inheritance, suami == 0 and istri == 0 and ibu == 0 and nenek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0),
                        ((1 / 3) * total_inheritance, saudara_laki_kandung > 0),
                        ((2 / 5) * total_inheritance, saudara_perempuan_kandung == 1),
                        ((1 / 3) * total_inheritance, saudara_perempuan_kandung >= 2),
                        ((1 / 3) * total_inheritance, suami == 0 and istri == 0 and (ibu > 0 or nenek > 0) and saudara_perempuan_kandung == 1),
                        ((2 / 7) * total_inheritance, suami == 0 and istri == 0 and (ibu > 0 or nenek > 0) and saudara_perempuan_kandung >= 2),
                        ((2 / 8) * total_inheritance, suami > 0 and saudara_perempuan_kandung == 1 and ibu == 0 and nenek == 0),
                        ((2 / 9) * total_inheritance, suami > 0 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0),
                        ((2 / 9) * total_inheritance, suami > 0 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0)),
                        ((2 / 10) * total_inheritance, suami > 0 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0)),
                        ((4 / 13) * total_inheritance, istri > 0 and saudara_perempuan_kandung == 1 and ibu == 0 and nenek == 0),
                        ((4 / 15) * total_inheritance, istri > 0 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0),
                        ((4 / 15) * total_inheritance, istri > 0 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0)),
                        ((4 / 17) * total_inheritance, istri > 0 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0))
                    ]
                    for value, condition in conditions:
                        if condition:
                            share_si = value
                            break
                    else:
                        share_si = sisa
                else:
                    share_si = 0
            
            if relationship == "sdlk":
                if saudara_laki_kandung > 0 and anak_laki == 0 and cucu_laki == 0 and ayah == 0 and kakek == 0:
                    # Menghitung bagian dari ahli waris
                    bagian_ahli_waris = sum([share_suami, share_istri, share_ibu, share_nenek, share_ap, share_cp, share_si])
                    sisa = total_inheritance - bagian_ahli_waris

                    if saudara_perempuan_kandung > 0:
                        share_sdlk = (2 / 3) * sisa
                    elif saudara_perempuan_kandung == 0:
                        if suami == 0 and istri == 0 and ibu == 0 and nenek == 0 and anak_perempuan == 0 and cucu_perempuan == 0:
                            share_sdlk = total_inheritance
                        else:
                            share_sdlk = sisa
                    else:
                        share_sdlk = 0
                else:
                    share_sdlk = 0
        
            elif relationship == "sdpk":
                if saudara_perempuan_kandung > 0 and anak_laki == 0 and cucu_laki == 0 and ayah == 0 and kakek == 0:
                    # Menghitung bagian dari ahli waris
                    bagian_ahli_waris = sum([share_suami, share_istri, share_ibu, share_nenek, share_ap, share_cp, share_si])
                    sisa = total_inheritance - bagian_ahli_waris

                    if saudara_laki_kandung > 0:
                        share_sdpk = (1 / 3) * sisa
                    elif saudara_laki_kandung == 0:
                        if suami == 0 and istri == 0 and ibu == 0 and nenek == 0 and anak_perempuan == 0 and cucu_perempuan == 0:
                            share_sdlk = total_inheritance
                        else:
                            share_sdlk = sisa
                else: 
                    share_sdpk = 0
        
    return share_ap, share_al, share_cl , share_cp, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, share_si, share_sdlk, share_sdpk

def print_inheritance_status(inheritance_status):
    for relationship, status in inheritance_status.items():
        print(f"Status warisan untuk {relationship}: {status}")
