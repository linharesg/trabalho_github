def validacao_usuario(usuario):
    pass




def efetuar_login() -> str:  # 1
    pass




def criar_conta():  # 3
    pass




def adicionar_favorito(id_carro: str, conta_logada: str) -> None:  # 4
    pass




def exibir_favoritos(id_usuario) -> None:  # 5
    pass

def carros_por_cor(cor: str) -> None:
    total_carros = 0
    print()
    for i in carros_anunciados:
        if carros_anunciados[i]['Cor'] == cor:
            print(f"ID {i}: {carros_anunciados[i]}")
            total_carros += 1
    if total_carros == 0:
        print("Não foram encontrados carros na cor informada!")
    return




carros_anunciados = {
    "car_1": {"Marca": "Ford", "Modelo": "Focus", "Cor": "Vermelho", "Ano": 2010, "km": 56000, "Preço": 89190},
    "car_2": {"Marca": "Hyundai", "Modelo": "HB20", "Cor": "Preto", "Ano": 2020, "km": 10000, "Preço": 90000},
    "car_3": {"Marca": "Chevrolet", "Modelo": "Vectra", "Cor": "Branco", "Ano": 2001, "km": 180000, "Preço": 43000},
    "car_4": {"Marca": "Ford", "Modelo": "Fusion", "Cor": "Preto", "Ano": 2015, "km": 60000, "Preço": 100000}
}

usuarios = {
    "gabriel.96": {"Nome": "Gabriel Linhares", "Email": "linhares.gs96@gmail.com", "Telefone": "47 99979 0581",
                   "senha": "1234"},
    "fulano2000": {"Nome": "Fulano da Silva", "Email": "fulano@gmail.com", "Telefone": "47 99999 8888",
                   "senha": "3456"},
    "souza21": {"Nome": "Alguem de Souza", "Email": "alguem@gmail.com", "Telefone": "47 88888 9999", "senha": "5678"},
}

favoritos = {
    "gabriel.96": ["car_1"],
    "souza21": ["car_2", "car_4"]
}

conta_logada = 0

while True:
    funcao = input("""
informe a função de acordo com o Menu:
1) Fazer Login
2) Sair da conta
3) Criar Conta
4) Adicionar carro ao favorito
5) Exibir favoritos
6) Anunciar carro
7) Pesquisar por anúncios
""")

    match funcao:

        case "1":  # Fazer Login
            pass




        case "2":
            pass




        case "3":  # Criar conta
            pass




        case "4":  # Adicionar aos favoritos
            pass




        case "5":  # Exibir favoritos
            pass




        case "5":  # Exibir favoritos
            pass




        case "6":  # Exibir favoritos
            pass




        case "7":  # Exibir favoritos
            pass




        case _:
            break
