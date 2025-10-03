sala = input("qual o tamanho da sala? [pequena, media ou grande?:]")
numero_pessoas = int(input("qual o numero de pessoas?:"))
if sala == "pequena" or numero_pessoas <= 5:
    print("ideia para reunioes com ate 5 pessoas")
elif sala == "medida" or numero_pessoas ==(6,7,8,9,10,11,12,13,14):
    print("adequada para reunioes de 6 a 15 pessoas.")
elif sala == "grande" or numero_pessoas >= 15:
    print("para reunioes com mais de 15 pessoas ou reunioes executivas.")
else:
    print("sala nao encontrada")
    