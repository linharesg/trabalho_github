def validacao_usuario(usuario):
    while True:
        if usuario not in usuarios.keys():
            usuario = input("Usuário não encontrado! Informe novamente: ")
            continue
        break
    return usuario


def efetuar_login() -> str:  # 1
    print("Insira seu usuário e senha para efetuar o login.")
    usuario_informado = input("Usuário: ")
    usuario_informado = validacao_usuario(usuario_informado)
    print(f"Usuario informado: {usuario_informado}")

    senha_informada = input("Senha: ")

    if usuarios[usuario_informado]["senha"] == senha_informada:
        conta_logada = usuario_informado
        input(f"Seja bem-vindo, {usuarios[usuario_informado]['Nome']}!")
    else:
        conta_logada = 0
        input("Senha inválida! Aperte qualquer tecla para retornar ao Menu.")
    return conta_logada


def criar_conta():  # 3

    nome = input("Informe seu nome completo: ")
    email = input("informe seu e-mail: ")
    aux = 0
    while aux == 0:
        aux = 1
        for i, vale in usuarios.items():
            if usuarios[i]["Email"] == email:
                email = input(f"O nome de usuário {email} não está disponível! Escolha outro:")
                aux = 0

    telefone = input("Informe seu telefone")
    usuario = input("Informe o nome para seu usuário:")

    while True:
        if usuario in usuarios.keys():
            usuario = input(f"O nome de usuário {usuario} não está disponível! Escolha outro:")
            continue
        break
    senha = input("Informe sua senha: ")

    usuarios[usuario] = {
        "Nome: ": nome,
        "Email": email,
        "Telefone": telefone,
        "senha": senha
    }
    input(f"\nConta criada com sucesso! Você está logado como {usuario}.")
    return usuario




def adicionar_favorito(id_carro: str, conta_logada: str) -> None:  # 4
    pass
    return



def exibir_favoritos(id_usuario) -> None:  # 5
    pass
    return



carros_anunciados = {
"car_1": {"Marca": "Ford", "Modelo": "Focus", "Cor": "Vermelho", "Ano": 2010, "km": 56000, "Preço": 89190},
"car_2": {"Marca": "Hyundai", "Modelo": "HB20", "Cor": "Preto", "Ano": 2020, "km": 10000, "Preço": 90000},
"car_3": {"Marca": "Chevrolet", "Modelo": "Vectra", "Cor": "Branco", "Ano": 2001, "km": 180000, "Preço": 43000},
"car_4": {"Marca": "Ford", "Modelo": "Fusion", "Cor": "Preto", "Ano": 2015, "km": 60000, "Preço": 100000}
}

usuarios = {
"gabriel.96": {"Nome": "Gabriel Linhares", "Email": "linhares.gs96@gmail.com", "Telefone": "47 99979 0581", "senha": "1234"},
"fulano2000": {"Nome": "Fulano da Silva", "Email": "fulano@gmail.com", "Telefone": "47 99999 8888", "senha": "3456"},
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
            if conta_logada != 0:
                input(f"Você já está logado com o usuário {conta_logada}!")
            else:
                conta_logada = efetuar_login()

        case "2":
            pass




        case "3":  # Criar conta
            if conta_logada != 0:
                input("Antes de criar outra conta, é necessário sair da conta que está logada!")
            else:
                conta_logada = criar_conta()

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
