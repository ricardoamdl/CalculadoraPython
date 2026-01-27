numero1 = input("Digite um número: ")
numero2 = input("Digite outro número: ")

numero1 = float(numero1)
numero2 = float(numero2)

print("Escolhe qual operação tu quer usar:")
print("+ : Soma")
print("- : Subtração")
print("* : Multiplicação")
print("/ : Divisão")

operacao = input("Digite o símbolo da operação")

if operacao == "+":
    resultado = numero1 + numero2
    print("Ei zé, oresultado da soma é: ", resultado)

elif operacao == "-":
    resultado = numero1 - numero2
    print("Ei zé, o resultado da subtração é: ", resultado)   

elif operacao == "*":
        resultado = numero1 * numero2
        print("Ei zé, o resultado da multiplicação é: ", resultado)

elif operacao == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
            print("Ei zé, o resultado da divisão é: ", resultado)
        else:
            print("Erro: Não existe divisão por zero zezin!")