def calc_med():
    try:
        nota_1 = float(input('Insira a primeira nota: '))
        nota_2 = float(input('Insira a segunda nota: '))
    except (TypeError, ValueError):
        print('Insira um número válido')

    else:
        if 0 <= nota_1 <= 10 and 0 <= nota_2 <= 10:
            media = (nota_1 + nota_2) / 2
            print(f'A sua média foi: {media}')
            if media >= 6:
                print('Você foi aprovado!')
            else:
                print('Você foi reprovado!')
        else:
            print('Insira uma nota válida')
    finally:
        print('Fim da operação!')


calc_med()
