from pickle import LIST

import random

def failist_to_dict(f:str):
    riik_pealinn={}
    pealinn_riik={}
    riigid=[] 
    file=open(f,"r",encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split("-")
        riik_pealinn[k]=v 
        pealinn_riik[v]=k 
        riigid.append(k)
    file.close()
    return riik_pealinn,pealinn_riik,riigid 

def Lisa_failisse(fail:str,riik:str, pealinn:str):
    f=open(fail,"a",encoding="utf-8-sig")
    f.write(riik+"-"+pealinn+"\n")
    f.close()
def muuda_riik(fail:str, riikpealinn:dict,pealinnriik:dict):
        x=input("vana riik: ")
        if x in riikpealinn:
            y=input("uus riik: ")
            k=input(f"uus pealinn: ")

            vana_pealinn = riikpealinn[x]

            riikpealinn.pop(x)
            riikpealinn[y]=k

            pealinnriik.pop(vana_pealinn)
            pealinnriik[k]=y

            f=open(fail,"w",encoding="utf-8-sig")
            for riik in riikpealinn:
                f.write(riik+"-"+riikpealinn[riik]+"\n")

def mang(riik_pealinn:dict):

    while True:
        riik = random.choice(list(riik_pealinn.keys()))
        kasutaja_pealinn=input(f"sisestage riigi {riik} pealinn : ")

        if riik_pealinn[riik] == kasutaja_pealinn:
            print("oige")
        else:
            print(f"vale. oige pealinn on {riik_pealinn[riik]}")
            break