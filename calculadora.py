print("Bem vindo à calculadora!")
while True:
    input_usuario = input("Digite a operação (+, -, *, /) ou 'sair' para encerrar: ")
    if input_usuario.lower() == "sair":
        print("Então tchau! Sei nem por que você veio aqui.")
        break
    if input_usuario in ('+', '-', '*', '/'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número:"))
        if input_usuario == '+':
            resultado = num1 + num2
            print(resultado)
        elif input_usuario == '-':
            resultado = num1 - num2
            print(resultado)
        elif input_usuario == '*':
            resultado = num1 * num2
            print(resultado)
        elif input_usuario == '/':
            if num2 != 0:
                resultado = num1 / num2
                print(resultado)
            else:

                print("Erro: Divisão por zero não é permitido.")
