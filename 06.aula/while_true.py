while True:
    numero = int(input("Informe um número: "))
    
    print(f'Dobro: {numero * 2}')
    print(f'Triplo: {numero * 3}')
    print(f'Quadrado: {numero ** 2}')

    resposta = input("\nDeseja continuar [S/N]: ").strip().lower()[0]
    print(resposta)
    if resposta == "n":
        break