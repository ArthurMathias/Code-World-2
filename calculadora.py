print('bem-vindo à calculatroxa broxa!')

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = int(input("Escolha a operação (1-4): "))

if operacao == 1:
    resultado = a + b
    print("Resultado da adição: ", resultado)
elif operacao == 2:
    resultado = a - b
    print("Resultado da subtração: ", resultado)
elif operacao == 3:
    resultado = a * b
    print("Resultado da multiplicação: ", resultado)
elif operacao == 4:
    if b != 0:
        resultado = a / b
        print("Resultado da divisão: ", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")