# Perguntando qual o tipo de operação pro usuário.
while True:
    operação = input("Qual o tipo de operação que você quer realizar?: ").strip().lower()

    if operação == "sair":
        print("Fechando programa...")
        break
    try:
        if operação == "mais" or operação == "soma" or operação == "adição":
            pegar_numero = int(input("Qual o primeiro número?: "))
            pegar_numero2 = int(input("E o segundo?: "))
            soma_geral = pegar_numero + pegar_numero2
            print(soma_geral)

        elif operação == "divisão":
            pegar_numero = int(input("Qual o primeiro número?: "))
            pegar_numero2 = int(input("E o segundo?: "))
            divisão_geral = pegar_numero / pegar_numero2
            print(divisão_geral)

        elif operação == "Multiplicação" or operação == "vezes":
            pegar_numero = int(input("Qual o primeiro número?: "))
            pegar_numero2 = int(input("E o segundo?: "))
            multi_geral = pegar_numero * pegar_numero2
            print(multi_geral)

        elif operação == "subtração" or operação == "menos":
            pegar_numero = int(input("Qual o primeiro número?: "))
            pegar_numero2 = int(input("E o segundo?: "))
            subt_geral = pegar_numero - pegar_numero2
            print(subt_geral)
        else:
            print("Não foi informado o tipo de operação.")
        
    except ValueError:
        print("Digite um valor válido.")
