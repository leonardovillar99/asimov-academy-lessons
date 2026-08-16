ent1 = input('Estou com fome? (Digite s para sim ou n para não): ')

if ent1 == 's':
    ent2 = input('Tenho comida em casa? (Digite s para sim ou n para não): ')
    if ent2 == 's':
        print('Preparar uma refeição -> Comer a comida.')
    else:
        print('Ir ao mercado -> Voltar para casa -> Preparar uma refeição -> Comer a comida.')
else:
    print('Até logo!')