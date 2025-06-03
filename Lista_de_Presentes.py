def adicionar_ideia(lista_de_presentes, presente):
    """Adiciona uma novo presente a lista de presentes."""
    lista_de_presentes.append(presente)
    print("Ideia adicionada com sucesso!")
    return lista_de_presentes

def listar_presentes(lista_de_presentes):
    """Lista todas as ideias de presentes."""
    print("\n" * 15)
    print(f"{' ' * 15}Ideias de Presentes:{' ' * 15}")
    print("-" * 50)
    n = 1
    for presente in lista_de_presentes:
        print(f"{n} - {presente}")
        n += 1
    print("-" * 50)

def riscar_ideia(lista_de_presentes, presente):
    """Risca um presente da lista de presentes baseado no número do item."""
    lista_de_presentes.pop((presente - 1))
    print("Ideia riscada!")
    return lista_de_presentes

def exibir_menu():
    """Exibe o menu de opções."""
    print("Escolha uma opção:\n"\
        "1 - Ideias de presentes\n" \
        "2 - Lista de presentes\n" \
        "3 - Risacar ideia\n" \
        "4 - Sair"
        )
    

lista_de_presentes = []
continuar = True

# Cabeçalho do programa
print("Lista de Presentes para o seu Amorzinho")
print("_" * 50)
print('\n')

# Loop principal
while continuar:
    exibir_menu()
    opcao = input("Insira o que deseja fazer: ")

    if opcao == "1":
        presente = input("Insira uma ideia de presente: ")
        lista_de_presentes = adicionar_ideia(lista_de_presentes, presente)
    elif opcao == "2":
        listar_presentes(lista_de_presentes)
    elif opcao == "3":
        # Validação dos valores inseridos pelo usuário.
        presente = input("Ideia que deseja riscar: ")
        if not presente.isnumeric():
            print("Presente não encontrado, tente novamente")
        if int(presente) > len(lista_de_presentes):
            print("Presente não encontrado, tente novamente")
        elif int(presente) <= 0:
            print("Presente não encontrado, tente novamente")
        else:
             riscar_ideia(lista_de_presentes, int(presente))
    elif opcao == "4":
        print("Fechando Lista de Presentes")
        continuar = False
    else:
        print("Opção inválida, tente novamente")
    print('\n')

