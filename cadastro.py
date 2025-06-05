def cadastrar_nome(cadastro):
    novo_nome = input("Digite o nome da pessoa:")
    cadastro.append(novo_nome)
    print(f"usuario {novo_nome} foi adicionado com sucesso!")

def  menu():
    cadastro = []
    while True: 
        print("\n------cadastro de funcionarios-----------------")
        print("[1] Cadastrar pessoa")
        print("[2] lista pessoas")
        print("[3] excluir pessoas")
        print("[0] ")
        opção = input("Escolha uma opção:")

 
        if opção == '1':
           cadastrar_nome(cadastro)
        elif opção == '2':
            print("\nlista de nomes cadastrados:")
            for i, nome in enumerate(cadastro, start=1):
                print(f"{i}. {nome}")
        elif opção == '3':
            excluir_nome = input("Digite o nome para excluir:")
            if excluir_nome in cadastro:
                cadastro.remove(excluir_nome)
                print(f"{excluir_nome} foi removido.")
            else:
                print("Nome não encontrado.")
        elif opção == "0":
            print("Saindo...")
            break
        else:
            print("!!! opção invalida. tente novamente. !!!")
menu()