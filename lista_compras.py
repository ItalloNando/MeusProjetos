import os

dentro = []
while True: 
    opcao = input('Selecione uma opção:'"\n[i]nserir [a]pagar [l]istar: ")

    if opcao == 'i':
        os.system('cls')
        coiso = input('valor: ')
        dentro.append(coiso)
        continue
    elif opcao == 'l':
        os.system('cls')
        for lista in range(len(dentro)):
            print(lista, dentro[lista])
    try:
        if opcao == 'a':
            apagar = int(input('Escolha o índice que deseja apagar: '))
            apagar_int = int(apagar)
            dentro.pop(apagar_int)
    except ValueError:
        os.system('cls')
        print('Por favor, selecione um número inteiro.')
    except IndexError:
        print('Por favor, adicione um index existente.')
    except Exception:
        print('Error desconhecido.')