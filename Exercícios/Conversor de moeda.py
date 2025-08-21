dolar_atual = 5.47  # valor do dia 21/08/2025
while True:
    escolha = input('Digite a opção de "dolar" para converter dólar para real ou "real" para converter real para dólar: ').lower()

    if escolha == 'dolar':
        dolar = float(input('Digite a quantidade de dólares para converter em reais: '))
        valor_real = dolar * dolar_atual
        print(f'O valor é igual a: R${valor_real:.2f} reais')
        break
    elif escolha == 'real':
        real = float(input('Digite a quantidade de reais para converter em dólares: '))
        valor_dolar = real / dolar_atual
        print(f'O valor em dólares é: US${valor_dolar:.2f}')
        break
    else:
        print('Opção inválida. Tente novamente.\n')
