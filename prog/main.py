# Copyright 2025 - Mariana

def exibirBoneco(qtd_erros):
    erros = [
        ''' ------
    |    |
    |    
    |    
    |    
    |    
    ------
    ''',
    ''' ------
    |    |
    |    0
    |    
    |    
    |    
    ------
    ''',
    ''' ------
    |    |
    |    0
    |    |
    |    
    |    
    ------
    ''',
    ''' ------
    |    |
    |    0
    |   /|
    |    
    |    
    ------
    ''',
    ''' ------
    |    |
    |    0
    |   /|\\
    |    
    |    
    ------
    ''',
    ''' ------
    |    |
    |    0
    |   /|\\
    |   /
    |    
    ------
    ''',
    ''' ------
    |    |
    |    0
    |   /|\\
    |   / \\
    |    
    ------
    '''
    ]

    possiveis_erros = len(erros) - 1

    tentativas_restantes = possiveis_erros - qtd_erros
    print(f'Tentativas restantes: {tentativas_restantes}')
    
    if qtd_erros > possiveis_erros:
        print(f'Perdeu o jogo!')
        return 0
    
    # Mostra o estado do boneco na forca
    print(erros[qtd_erros])

    return 0

def main():
    config = {
        'tema': 'animais',
        'palavras': [
            'Leão', 'Tigre', 'Elefante', 'Girafa', 'Zebra',
            'Hipopótamo', 'Rinoceronte', 'Lobo', 'Raposa', 'Urso',
            'Canguru', 'Coala', 'Gorila', 'Chimpanzé', 'Antílope',
            'Pinguim', 'Golfinho', 'Tubarão', 'Coruja', 'Águia', 
            'Galinha', 'Vaca', 'Cobra', 'Piranha', ''
        ],
        'tentativas': 6
    }

    


    return 0

main()
