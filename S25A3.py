cinema=[[0 for _ in range(8)]for _ in range(5)]

matriz=[
[1,2,3,4,5,6,7,8],
[9,10,11,12,13,14,15,16],
[17,18,19,20,21,22,23,24],
[25,26,27,28,29,30,31,32],
[33,34,35,36,37,38,39,40]
]
def reserva_assento(cinema,linha,coluna):
    posiçao_l=-1
    posiçao_coluna=-1

def cancelar_assento(cinema,linha,coluna):
    posiçao_linha = linha - 1
    posiçao_coluna = coluna - 1
    if 0 <= posiçao_linha < 5 and  0 <= posiçao_coluna < 8:
        if cinema[posiçao_linha][posiçao_coluna] == 1:
            cinema[posiçao_linha][posiçao_linha] = 0
            print(f"\na cadeira [{linha}][{coluna}]foi cancelada")
        else:
            print(f"a cadeira[{linha}][{coluna}]continua livre")
    else:
        print(f"a cadeira[{linha}][{coluna}]não e válida")

def exibir(cinema,linha,coluna):
    for i in range(linha):
        for j in range(coluna):
            print(cinema[i][j], end=' ')
        print()

def execucao(cinema,dim_linha,dim_coluna, linha, coluna):
    print("cinema sem reservas")
    exibir(cinema, dim_linha, dim_coluna)
    reserva_assento(cinema, linha, coluna)
    print("cinema depois da reserva")
    exibir(cinema, dim_linha, dim_coluna)

if __name__=='__main__':
    execucao(cinema, 5,8, 1,3)
        


