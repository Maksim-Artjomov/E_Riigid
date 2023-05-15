from mymodule import *

riik_pealinn, pealinn_riik,riigid=failist_to_dict("E_riigid.txt")

while True:
    v=int(input(f"1-Otsi riik/pealinn\n2-Lisa\n3-Muuda\n4-Mang\n\n"))
    if v==1:

        valik = int(input("1-riik_pealinn\n2-pealinn_riik\n"))
        if valik == 1:
            riik=input("sissesta riik: ")
            if riik in riik_pealinn:
                print(f"pealinn on {riik_pealinn[riik]}")
            else:
                print("riik ei ole leitud")
        else:
            pealinn=input("sissesta pealinn: ")
            if pealinn in pealinn_riik:
                print(f"riik on {pealinn_riik[pealinn]}")
            else:
                print("pealinn ei ole leitud")

    elif v==2:

        uusriik=input("lisa riik: ")
        uuspealinn=input("lisa pealinn: ")

        riik_pealinn[uusriik] = uuspealinn
        pealinn_riik[uuspealinn] = uusriik
        riigid.append(uusriik) 

        Lisa_failisse("E_riigid.txt",uusriik,uuspealinn)
    elif v==3:
        muuda_riik("E_riigid.txt",riik_pealinn, pealinn_riik)
    elif v==4:
        mang(riik_pealinn)