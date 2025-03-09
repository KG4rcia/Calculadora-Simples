# Perguntando qual o tipo de operação pro usuário.

operação = str(input("Qual o tipo de operação que você deseja?: "))

if operação == "soma" or "Soma":
    pegar_numero = int(input("Qual o primeiro número?: "))
    pegar_numero2 = int(input("E o segundo?: "))
    soma_geral = pegar_numero + pegar_numero2
    print(soma_geral)

elif operação == "divisão" or "Divisão":
    pegar_numero = int(input("Qual o primeiro número?: "))
    pegar_numero2 = int(input("E o segundo?: "))
    divisão_geral = pegar_numero + pegar_numero2
    print(divisão_geral)

elif operação == "Multiplicação" or "multiplicação":
    pegar_numero = int(input("Qual o primeiro número?: "))
    pegar_numero2 = int(input("E o segundo?: "))
    multi_geral = pegar_numero + pegar_numero2
    print(multi_geral)

elif operação == "subtração" or "Subtração" or "menos" or "Menos":
    pegar_numero = int(input("Qual o primeiro número?: "))
    pegar_numero2 = int(input("E o segundo?: "))
    subt_geral = pegar_numero + pegar_numero2
    print(subt_geral)
else:
    print("Não foi informado o tipo de operação.")