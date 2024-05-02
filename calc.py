def hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance):
    print("Nilai suami:", suami) 
    print("Anak laki-laki:", anak_laki)   
    print("Anak perempuan:", anak_perempuan)   
    print("Cucu laki-laki:", cucu_laki)
    print("Cucu perempuan:", cucu_perempuan)
    
    # Inisialisasi variabel bagi hasil untuk suami
    share_suami = 0

    if suami > 0:
        if anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
            share_suami = (1 / 2) * total_inheritance
        elif (anak_laki > 0 or cucu_laki > 0 or anak_perempuan > 0 or cucu_perempuan > 0):
            share_suami = (1 / 4) * total_inheritance
        elif anak_laki == 0 and cucu_laki == 0:
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
                ((3 / 8), saudara_seibu == 1 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0)),
                ((3 / 9), saudara_seibu == 1 and saudara_laki_kandung == 0 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0)),
                ((3 / 9), saudara_seibu >= 2 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0)),
                ((3 / 10), saudara_seibu >= 2 and saudara_laki_kandung == 0 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0)),
                ((3 / 8), saudara_seibu == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung > 0 and ibu > 0 and nenek == 0),
                ((3 / 7), saudara_seibu == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 1 and ibu == 0 and nenek > 0),
                ((3 / 8), saudara_seibu == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek > 0)
            ]
            for value, condition in conditions:
                if condition:
                    share_suami = value * total_inheritance
                    break
    else :
        share_suami = 0

    return share_suami

def hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance):
    if istri > 0:
        if anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
            share_istri = (1 / 4) * total_inheritance
        elif (anak_laki > 0 or cucu_laki > 0 or anak_perempuan > 0 or cucu_perempuan > 0):
            share_istri = (1 / 8) * total_inheritance
        elif anak_laki == 0 and cucu_laki == 0:
            conditions = [
                ((3 / 27), (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2)),
                ((3 / 27), (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and anak_perempuan == 1 and cucu_perempuan > 0),
                ((3 / 15), (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and anak_perempuan >= 2 and cucu_perempuan > 0),
                ((3 / 13), ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and (saudara_seibu == 1 or saudara_perempuan_kandung >= 2) and ibu == 0 and nenek == 0),
                ((3 / 13), ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and (saudara_seibu >= 2 or saudara_perempuan_kandung == 1) and ibu == 0 and nenek == 0),
                ((3 / 15), ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_seibu >= 2 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0),
                ((3 / 13), saudara_laki_kandung == 0 and saudara_seibu == 1 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0)),
                ((3 / 15), saudara_laki_kandung == 0 and saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0)),
                ((3 / 15), saudara_laki_kandung == 0 and saudara_seibu >= 2 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0)),
                ((3 / 17), saudara_laki_kandung == 0 and saudara_seibu >= 2 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0)),
                ((3 / 13), saudara_laki_kandung == 0 and saudara_seibu == 0 and saudara_perempuan_kandung > 0 and ibu > 0 and nenek == 0),
                ((3 / 13), saudara_laki_kandung == 0 and saudara_seibu == 0 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek > 0)
            ]
            for value, condition in conditions:
                if condition:
                    share_istri = value * total_inheritance
                    break
    else:
        share_istri = 0
    
    return share_istri

def hitung_bagian_ayah(ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri):
    if ayah > 0:
        if anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
            if (suami == 0 or istri == 0) and ibu == 0 and nenek == 0 and saudara_seibu == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
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
    
    return share_ayah

def hitung_bagian_ibu(ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri):
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
        elif anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0 and (saudara_seibu + saudara_perempuan_kandung + saudara_laki_kandung) < 2:
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
    
    return share_ibu

def hitung_bagian_kakek(kakek, ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri):
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
                ((4 / 27), (istri > 0 and (ibu > 0 or nenek > 0)) and anak_perempuan > 0 and cucu_perempuan > 0),
                ((7 / 40), istri > 0 and (ibu == 0 and nenek == 0) and anak_perempuan > 0 and cucu_perempuan > 0),
                ((4 / 27), (istri > 0 and (ibu > 0 or nenek > 0)) and anak_perempuan > 0 and cucu_perempuan > 0)
            ]
            for value, condition in conditions:
                if condition:
                    share_kakek = value * total_inheritance
                    break
    else:
        share_kakek = 0

    return share_kakek

def hitung_bagian_nenek(nenek, ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri):
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

    return share_nenek

def hitung_bagian_anak_laki(anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, kakek, nenek, total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek):
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

    return share_al

def hitung_bagian_anak_perempuan(anak_perempuan, anak_laki, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, kakek, nenek, total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung):
    if anak_perempuan > 0:
        bagian_ahli_waris = sum([share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek])
        sisa = total_inheritance - bagian_ahli_waris

        if anak_laki == 0 and cucu_laki == 0 and cucu_perempuan == 0 and (suami == 0 or istri == 0) and ayah == 0 and ibu == 0 and kakek == 0 and nenek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
            share_ap = total_inheritance
        elif anak_laki > 0:
            share_ap = (1 / 3) * sisa
        elif anak_laki == 0:
            if anak_perempuan == 1:
                conditions = [
                    ((3 / 4), ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0),
                    ((3 / 5), (ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0)),
                    ((1 / 2), saudara_laki_kandung > 0 or saudara_laki_kandung > 0),
                    ((3 / 4), suami > 0 and (ayah == 0 or ibu == 0 or kakek == 0 or nenek == 0) and cucu_perempuan == 0),
                    ((9 / 16), suami > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0) and cucu_perempuan == 0),
                    ((6 / 13), suami > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0) and cucu_perempuan > 0),
                    ((6 / 13), suami > 0 and (ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0)),
                    ((21 / 32), istri > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0) or cucu_perempuan > 0),
                    ((21 / 40), istri > 0 and (ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0)),
                    ((1 / 2), cucu_perempuan > 0 and cucu_laki > 0),
                    ((3 / 5), cucu_perempuan > 0 and cucu_laki == 0 and suami == 0 and istri == 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                    ((6 / 13), cucu_perempuan > 0 and cucu_laki == 0 and suami > 0 and (ibu > 0 or ayah > 0 or kakek > 0 or nenek > 0)),
                    ((21 / 40), cucu_perempuan > 0 and cucu_laki == 0 and istri > 0 and (ibu > 0 or ayah > 0 or kakek > 0 or nenek > 0)),
                    ((1 / 2), cucu_perempuan > 0 and cucu_laki == 0 and suami == 0 and istri == 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0))),
                    ((6 / 15), cucu_perempuan > 0 and cucu_laki == 0 and suami > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0))),
                    ((12 / 27), cucu_perempuan > 0 and cucu_laki == 0 and istri > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0)))
                ]
                for value, condition in conditions:
                    if condition:
                        share_ap = value * total_inheritance
                        break
            elif anak_perempuan >= 2:
                conditions = [
                    ((4 / 5), ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0),
                    ((2 / 3), (ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0) or (saudara_laki_kandung > 0 or saudara_perempuan_kandung > 0)),
                    ((2 / 3), suami > 0 and (ayah == 0 or ibu == 0 or kakek == 0 or nenek == 0) and cucu_perempuan == 0),
                    ((8 / 13), suami > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0) and cucu_perempuan == 0),
                    ((8 / 13), suami > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0) and cucu_perempuan > 0),
                    ((8 / 15), suami > 0 and (ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0)),
                    ((2 / 3), istri > 0 and (ayah == 0 or ibu == 0 or kakek == 0 or nenek == 0)),
                    ((7 / 10), istri > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                    ((16 / 27), istri > 0 and (ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0)),
                    ((2 / 3), cucu_perempuan > 0 and cucu_laki > 0),
                    ((4 / 5), cucu_perempuan > 0 and cucu_laki == 0 and suami == 0 and istri == 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                    ((8 / 13), cucu_perempuan > 0 and cucu_laki == 0 and suami > 0 and (ibu > 0 or ayah > 0 or kakek > 0 or nenek > 0)),
                    ((7 / 10), cucu_perempuan > 0 and cucu_laki == 0 and istri > 0 and (ibu > 0 or ayah > 0 or kakek > 0 or nenek > 0)),
                    ((2 / 3), cucu_perempuan > 0 and cucu_laki == 0 and suami == 0 and istri == 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0))),
                    ((8 / 15), cucu_perempuan > 0 and cucu_laki == 0 and suami > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0))),
                    ((16 / 27), cucu_perempuan > 0 and cucu_laki == 0 and istri > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0)))
                ]
                for value, condition in conditions:
                    if condition:
                        share_ap = value * total_inheritance
                        break
    else:
        share_ap = 0

    return share_ap

def hitung_bagian_cucu_laki(cucu_laki, anak_laki, cucu_perempuan, anak_perempuan, suami, istri, ayah, ibu, kakek, nenek, total_inheritance, share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek):
    if cucu_laki > 0 and anak_laki == 0:
        bagian_ahli_waris = sum([share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek])
        sisa = total_inheritance - bagian_ahli_waris

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
                (((cucu_laki / (ayah + cucu_laki)) * sisa), anak_perempuan == 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0))),
                (((cucu_laki / (ayah + cucu_laki)) * sisa), anak_perempuan == 0 and (suami > 0 or istri > 0) and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0))),
                (0, anak_perempuan > 0 and suami > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0))),
                (0, anak_perempuan >= 2 and suami > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0)))
            ]
            for value, condition in conditions:
                if condition:
                    share_cl = value * sisa
                    break
    else:
        share_cl = 0

    return share_cl

def hitung_bagian_cucu_perempuan(cucu_perempuan, cucu_laki, anak_laki, anak_perempuan, suami, istri, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek):
    if cucu_perempuan > 0 and anak_laki == 0:
        # Menghitung bagian dari ahli waris
        bagian_ahli_waris = sum([share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek])
        sisa = total_inheritance - bagian_ahli_waris

        if cucu_laki == 0 and anak_perempuan == 0 and (suami == 0 or istri == 0) and ayah == 0 and ibu == 0 and kakek == 0 and nenek == 0 and saudara_seibu == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
            share_cp = total_inheritance
        elif cucu_laki > 0:
            share_cp = (1 / 3) * sisa  # Bagian jika ada cucu perempuan dan cucu laki-laki, tetapi tidak ada anak laki-laki
            if anak_perempuan > 0 and (suami > 0 or istri > 0) and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0)):
                share_cp = 0
        elif cucu_laki == 0:
            if anak_perempuan == 0 and cucu_perempuan == 1:
                conditions = [
                    ((1 / 2), anak_perempuan == 0 and cucu_perempuan == 1),
                    ((3 / 4), suami == 0 and istri == 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                    ((3 / 5), suami == 0 and istri == 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0))),
                    ((9 / 16), suami > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                    ((6 / 13), suami > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0))),
                    ((21 / 32), istri > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                    ((21 / 40), istri > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0)))
                ]
                for value, condition in conditions:
                    if condition:
                        share_cp = value * sisa
                        break
            elif anak_perempuan == 0 and cucu_perempuan >= 2:
                conditions = [
                    ((2 / 3), anak_perempuan == 0 and cucu_perempuan >= 2),
                    ((4 / 5), suami == 0 and istri == 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                    ((2 / 3), suami == 0 and istri == 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0))),
                    ((8 / 13), suami > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                    ((8 / 15), suami > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0))),
                    ((7 / 10), istri > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                    ((16 / 27), istri > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0)))
                ]
                for value, condition in conditions:
                    if condition:
                        share_cp = value * sisa
                        break
            elif anak_perempuan == 1:
                conditions = [
                    ((1 / 5), suami == 0 and istri == 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                    ((1 / 6), suami == 0 and istri == 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0))),
                    ((1 / 4), suami > 0 and ayah == 0 and ibu == 0 and kakek == 0 and nenek == 0),  # Bagian jika ada cucu perempuan, satu anak perempuan, dan tidak ada cucu laki-laki atau anak laki-laki
                    ((2 / 13), suami > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                    ((2 / 15), suami > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0))),
                    ((7 / 32), istri > 0 and ayah == 0 and ibu == 0 and kakek == 0 and nenek == 0),
                    ((7 / 40), istri > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0)),
                    ((4 / 27), istri > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0) or (ibu > 0 and kakek > 0) or (kakek > 0 and nenek > 0)))
                ]
                for value, condition in conditions:
                    if condition:
                        share_cp = value * sisa
                        break
            elif anak_perempuan >= 2:
                if cucu_laki > 0:
                    share_cp = (1 / 3) * sisa
                elif cucu_laki == 0:
                    share_cp = 0
            elif anak_perempuan > 0 and (saudara_laki_kandung > 0 or saudara_perempuan_kandung > 0):
                share_cp = (1 / 6) * total_inheritance
        else:
            share_cp = 0
    else:
        share_cp = 0

    return share_cp

def hitung_bagian_si(total_inheritance, share_suami, share_istri, share_ibu, share_nenek, saudara_seibu, ayah, kakek, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_laki_kandung, saudara_perempuan_kandung):
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
                ((1 / 4), suami == 0 and istri == 0 and saudara_perempuan_kandung == 1),
                ((1 / 5), suami == 0 and istri == 0 and saudara_perempuan_kandung >= 2),
                ((1 / 5), suami == 0 and istri == 0 and (ibu > 0 or nenek > 0) and saudara_perempuan_kandung == 1),
                ((1 / 6), suami == 0 and istri == 0 and (ibu > 0 or nenek > 0) and saudara_perempuan_kandung >= 2),
                ((1 / 7), suami > 0 and saudara_perempuan_kandung == 1 and ibu == 0 and nenek == 0),
                ((1 / 8), suami > 0 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0),
                ((1 / 8), suami > 0 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0)),
                ((1 / 9), suami > 0 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0)),
                ((3 / 16), istri > 0 and saudara_perempuan_kandung == 1 and ibu == 0 and nenek == 0),
                ((2 / 13), istri > 0 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0),
                ((2 / 13), istri > 0 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0)),
                ((2 / 15), istri > 0 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0))
            ]
            for value, condition in conditions:
                if condition:
                    share_si = value * total_inheritance
                    break
        else:
            share_si = sisa
    elif saudara_seibu >= 2 and ayah == 0 and kakek == 0 and anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
        conditions = [
            (total_inheritance, suami == 0 and istri == 0 and ibu == 0 and nenek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0),
            ((1 / 3), saudara_laki_kandung > 0),
            ((2 / 5), saudara_perempuan_kandung == 1),
            ((1 / 3), saudara_perempuan_kandung >= 2),
            ((1 / 3), suami == 0 and istri == 0 and (ibu > 0 or nenek > 0) and saudara_perempuan_kandung == 1),
            ((2 / 7), suami == 0 and istri == 0 and (ibu > 0 or nenek > 0) and saudara_perempuan_kandung >= 2),
            ((2 / 8), suami > 0 and saudara_perempuan_kandung == 1 and ibu == 0 and nenek == 0),
            ((2 / 9), suami > 0 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0),
            ((2 / 9), suami > 0 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0)),
            ((2 / 10), suami > 0 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0)),
            ((4 / 13), istri > 0 and saudara_perempuan_kandung == 1 and ibu == 0 and nenek == 0),
            ((4 / 15), istri > 0 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0),
            ((4 / 15), istri > 0 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0)),
            ((4 / 17), istri > 0 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0))
        ]
        for value, condition in conditions:
            if condition:
                share_si = value * total_inheritance
                break
        else:
            share_si = sisa
    else:
        share_si = 0

    return share_si

def hitung_bagian_sdlk(total_inheritance, share_suami, share_istri, share_ibu, share_nenek, share_ap, share_cp, share_si, saudara_laki_kandung, saudara_perempuan_kandung, anak_laki, cucu_laki, ayah, kakek, suami, istri, ibu, nenek, anak_perempuan, cucu_perempuan):
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

    return share_sdlk

def hitung_bagian_sdpk(total_inheritance, share_suami, share_istri, share_ibu, share_nenek, share_ap, share_cp, share_si, saudara_laki_kandung, saudara_perempuan_kandung, anak_laki, cucu_laki, ayah, kakek, suami, istri, ibu, nenek, anak_perempuan, cucu_perempuan):
    if saudara_perempuan_kandung > 0 and anak_laki == 0 and cucu_laki == 0 and ayah == 0 and kakek == 0:
        # Menghitung bagian dari ahli waris
        bagian_ahli_waris = sum([share_suami, share_istri, share_ibu, share_nenek, share_ap, share_cp, share_si])
        sisa = total_inheritance - bagian_ahli_waris

        if saudara_laki_kandung > 0:
            share_sdpk = (1 / 3) * sisa
        elif saudara_laki_kandung == 0:
            if suami == 0 and istri == 0 and ibu == 0 and nenek == 0 and anak_perempuan == 0 and cucu_perempuan == 0:
                share_sdpk = total_inheritance
            else:
                share_sdpk = sisa
    else: 
        share_sdpk = 0

    return share_sdpk

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

    # Periksa apakah hasil prediksi adalah 'DAPAT'
    for relationship, status in inheritance_status.items():
        if status == 'DAPAT':
            # Menerapkan aturan sesuai dengan hubungan keluarga
            if relationship == "suami":
                share_suami = hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance)
            if relationship == "istri":
                share_istri = hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance)
            if relationship == "ayah":
                share_ayah = hitung_bagian_ayah(ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri)
            if relationship == "ibu":
                share_ibu = hitung_bagian_ibu(ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
            if relationship == "kakek":
                share_kakek = hitung_bagian_ibu(kakek, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri)
            if relationship == "nenek":
                share_nenek = hitung_bagian_nenek(nenek, ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
            if relationship == "al":  # Anak laki-laki
                share_al = hitung_bagian_anak_laki(anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, kakek, nenek, total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek)
            if relationship == "ap":  # Anak perempuan
                share_ap = hitung_bagian_anak_perempuan(anak_perempuan, anak_laki, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, kakek, nenek, total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung)
            if relationship == "cl":  # Cucu laki-laki dari anak laki-laki
                share_cl = hitung_bagian_cucu_laki(cucu_laki, anak_laki, cucu_perempuan, anak_perempuan, suami, istri, ayah, ibu, kakek, nenek, total_inheritance, share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek)
            if relationship == "cp":  # Cucu perempuan dari anak laki-laki
                share_cp = hitung_bagian_cucu_perempuan(cucu_perempuan, cucu_laki, anak_laki, anak_perempuan, suami, istri, ayah, ibu, kakek, nenek, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek)
            if relationship == "si":  # Saudara seibu
                share_si = hitung_bagian_si(total_inheritance, share_suami, share_istri, share_ibu, share_nenek, saudara_seibu, ayah, kakek, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_laki_kandung, saudara_perempuan_kandung)           
            if relationship == "sdlk": # Saudara kandung laki-laki
                share_sdlk = hitung_bagian_sdlk(total_inheritance, share_suami, share_istri, share_ibu, share_nenek, share_ap, share_cp, share_si, saudara_laki_kandung, saudara_perempuan_kandung, anak_laki, cucu_laki, ayah, kakek, suami, istri, ibu, nenek, anak_perempuan, cucu_perempuan)
            if relationship == "sdpk": # Saudara kandung perempuan
                share_sdpk = hitung_bagian_sdpk(total_inheritance, share_suami, share_istri, share_ibu, share_nenek, share_ap, share_cp, share_si, saudara_laki_kandung, saudara_perempuan_kandung, anak_laki, cucu_laki, ayah, kakek, suami, istri, ibu, nenek, anak_perempuan, cucu_perempuan)
        
    return share_ap, share_al, share_cl , share_cp, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, share_si, share_sdlk, share_sdpk

def print_inheritance_status(inheritance_status):
    for relationship, status in inheritance_status.items():
        print(f"Status warisan untuk {relationship}: {status}")
