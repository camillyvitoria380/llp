distancia_totalx = input("qual a distancia?: 120,150:")
total_combustiveLY = input("quanto de combustivel?[15,25]:")
distancia_toalx1 = 120
total_combustivelx1 = 15
media1 = 120//15
media2 = 150//25

if distancia_totalx == "120" and total_combustiveLY == "15":
    print(f"a media e {media1:3f} km/1")
elif distancia_totalx == "150" and total_combustiveLY == "25":
    print(f"a media e {media2:3f} km/1")
else:
    print("nao encontrado")