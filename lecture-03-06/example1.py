import datetime
vozila = {
# key: value
# oib
# 
    1: ("Kamion", "Iveco", "OS 001 ZZ", "2015", "45000"),
    2: ("Kamion", "Iveco", "OS 002 ZZ", "2015", "47000"),
    3: ("Tegljač", "MAN", "RI 001 ZZ", "2018", "78000"),
    4: ("Tegljač", "MAN", "RI 002 ZZ", "2020", "97000"),
    5: ("Kombi", "Mercedes Benz", "ST 001 ZZ", "2013", "12000"),
    6: ("Kombi", "Vokswagen", "ST 002 ZZ", "2021", "35000"),
    7: ("Dostavno vozilo", "Volkswagen", "ZG 001 ZZ", "2010", "9000"),
    8: ("Dostavno vozilo", "Volkswagen", "ZG 002 ZZ", "2010", "9300")
}

val = (1, "Kamion")
val2 = (1, ["Kamion"])
val3 = ((1), "Kamion")
val4 = ([1], ("Kamion", "Iveco"))

#val4[1] =  ("Kamion", "Iveco")
val4[1][1]

tCurrentYear = 2023
print("ID  Tip             Proizvođač      Reg.oznaka   God      Cijena u EUR     Star   Skup")
print("____________________________________________________________________")
for val in vozila.items():
    # val = (1,  ("Kamion", "Iveco", "OS 001 ZZ", "2015", "45000"))
    
    if tCurrentYear - int(val[1][3]) > 10:
    #if !!!2023 - "2015"!!! > 10:
    # val[0] vraća 1
    # val[1] vraća ("Kamion", "Iveco", "OS 001 ZZ", "2015", "45000")
    # val[1][3] vraća "2015"
        tStar = "DA"
    else:
        tStar = "NE"
    if float(val[1][4]) > 10000:
        tSkup = "DA"
    else:
        tSkup = "NE"
    print(f"{val[0]}    {val[1][0] : <15}  {val[1][1] : <15} {val[1][2] : <10} {val[1][3] : <8} {('%06.2f' % float(val[1][4])): >14} {tStar: >5} {tSkup: >5}")