departamento = input("qual seu departamento? [DS, marketing, rh ou p&d]:")
if departamento == "DS":
    print("equipamento mais adequado e laptops com alto desempenho")
elif departamento == "marketing":
    print("e recomendado tablets para facilitar a apresentacao e mobilidade")
elif departamento == "RH":
    print("e recomendavel computadores desktop devido a sua estabilidade e custo-beneficio")
elif departamento == "p&d":
    print("e necessario equipamentos com especificacoes de ultima geracao. ")
else:
    print("departamento nao encontrado")  