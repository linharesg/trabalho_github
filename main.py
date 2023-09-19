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
    if conta_logada not in favoritos.keys():
        favoritos[conta_logada] = [id_carro]
        input("Carro adicionado aos favoritos! Digite qualquer telca para retornar ao Menu.")
        return
    favoritos[conta_logada].append(id_carro)
    input("Carro adicionado aos favoritos! Digite qualquer telca para retornar ao Menu.")
    return


def exibir_favoritos(id_usuario) -> None:  # 5
    if id_usuario == 0:
        input("Para exibir seus favoritos é necessário efetuar o login.").upper()
        return

    if id_usuario not in favoritos.keys():
        input("Você não possui nenhum carro adicionado aos favoritos!")
    else:
        for favoritados in favoritos[id_usuario]:
            for carro, caracteristicas in carros_anunciados.items():
                if favoritados == carro:
                    print(f"\n{carro}: ", end="")
                    for atributo, valor in caracteristicas.items():
                        print(f"{atributo}: {valor}", end=" | ")
    input("\n")
    return

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


def carros_por_marca(marca: str) -> None:
    total_carros = 0
    print()
    for i in carros_anunciados:
        if carros_anunciados[i]['Marca'] == marca:
            print(f"ID {i}: {carros_anunciados[i]}")
            total_carros += 1
    if total_carros == 0:
        print("Não foram encontrados carros da marca informada!")
    return


def anunciar_carro(marca: str, modelo: str, cor: str, ano: int, km: int, preco: float, sobre: str):
    """
    Essa função anuncia um carro em nosso programa
    """

    id_carro = "car_" + str(len(carros_anunciados) + 1)

    carro = {
            'Marca': marca,
            'Modelo': modelo,
            'Cor': cor,
            'Ano': ano,
            'Km': km,
            'Preco': preco,
            'Sobre': sobre
    }

    carros_anunciados[id_carro] = carro

    input("Carro anunciado com sucesso.")



carros_anunciados = {
"car_1": {"Marca": "Ford", "Modelo": "Focus", "Cor": "Vermelho", "Ano": 2010, "km": 56000, "Preço": 89190, "Sobre": "Descrição sobre o carro1"},
"car_2": {"Marca": "Hyundai", "Modelo": "HB20", "Cor": "Preto", "Ano": 2020, "km": 10000, "Preço": 90000, "Sobre": "Descrição sobre o carro2"},
"car_3": {"Marca": "Chevrolet", "Modelo": "Vectra", "Cor": "Branco", "Ano": 2001, "km": 180000, "Preço": 43000, "Sobre": "Descrição sobre o carro3"},
"car_4": {"Marca": "Ford", "Modelo": "Fusion", "Cor": "Preto", "Ano": 2015, "km": 60000, "Preço": 100000, "Sobre": "Descrição sobre o carro4"}
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
7) Filtrar por marca
8) Filtrar por cor
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
            if conta_logada == 0:
                resposta = input("Para adicionar um carro aos favoritos é necessário fazer o login.").upper()
                continue

            id_anuncio = input("Informe o ID do carro a ser adicionado aos favoritos: ")

            if id_anuncio not in (carros_anunciados.keys()):
                input(f"Não foi encontado nenhum carro de ID {id_anuncio}!")
                continue
            if id_anuncio in favoritos[conta_logada]:
                input("Você já tem este carro adicionado nos seus favoritos!")
                continue
            adicionar_favorito(id_anuncio, conta_logada)

            # print(favoritos)

        case "5":  # Exibir favoritos
            exibir_favoritos(conta_logada)

        case "6":  # Anunciar carro
            print("Digite abaixo as informações sobre o carro a ser anunciado: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            cor = input("Cor: ")
            ano = int(input("Ano: "))
            km = int(input("Km: "))
            preco = float(input("Preço: "))
            sobre = input("Sobre: ")

            anunciar_carro(marca, modelo, cor, ano, km, preco, sobre)

        case "7":  # Filtrar por marca
            marca = input("Digite a marca: ")
            carros_por_marca(marca)

        case "8": # Filtrar por cor
            cor = input("Digite a cor: ")
            carros_por_cor(cor)

        case _:
            input("Intrada inválida! Selecione uma das opções do Menu.")
            continue