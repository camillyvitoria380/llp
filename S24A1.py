bugs = [
    {"descricao": "Erro ao salvar", "gravidade": "alta", "quantidade": 8},
    {"descricao": "Falha login", "gravidade": "média", "quantidade": 3},
    {"descricao": "Tela travando", "gravidade": "alta", "quantidade": 6},
    {"descricao": "Texto cortado", "gravidade": "baixa", "quantidade": 2},
    {"descricao": "Erro conexão", "gravidade": "média", "quantidade": 7}
]

print("Relatório de Bugs:\n")

for bug in bugs:
    print(f"{bug['descricao']} - Gravidade: {bug['gravidade']} - Reportado: {bug['quantidade']} vezes")

print("\nBugs Prioritários (mais de 5 reportagens):\n")

for bug in bugs:
    if bug["quantidade"] > 5:
        print(f"{bug['descricao']} - Gravidade: {bug['gravidade']}")
