opcao = 0
opcao2 = 0
n1 = int(input('digite um numero: '))
n2 = int(input('digite o segundo numero: '))
while True:
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa')
    opcao = int(input('digite uma opção: '))
    if opcao == 1:
        print(f'o resultado da soma de {n1}+{n2}={n1+n2}')
        opcao2 = int(input('[1] voltar ao menu principal\n[2]sair\nDigite uma opção: '))
        if opcao2 == 1:
            continue
        elif opcao2 == 2:
            break
        else:
            print('digite uma opção válida')
    elif opcao == 2:
        print(f'o resultado de {n1}X{n2}={n1*n2}')
        opcao2 = int(input('[1] voltar ao menu principal\n[2]sair\nDigite uma opção: '))
        if opcao2 == 1:
            continue
        elif opcao2 == 2:
            break
        else:
            print('opção invalida')
    elif opcao == 3:
        print(f'entre o numero {n1} e {n2} o maior é {max(n2,n1)}')
        opcao2 = int(input('[1] voltar ao menu principal\n[2]sair\nDigite uma opção: '))
        if opcao2 == 1:
            continue
        elif opcao2 == 2:
            break
        else:
            print('opção invalida')
    elif opcao == 4:
        n1 = int(input('digite um numero: '))
        n2 = int(input('digite o segundo numero: '))
        continue
    elif opcao == 5:
        break
    else:
        print('digite uma opção valida')
        continue