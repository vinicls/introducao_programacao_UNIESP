#TED AULAS 12 E 13

#CRIAR DICIONÁRIO, OU GLOSSÁRIO



dicionario = {'Phyton' : 'Linguagem de Programação', 
            'HTML' : 'Liguagem de Marcação',
            'Algoritimo' : 'Sequencia de passos para um objetivo',
            'Sistema Operacional' : 'Gerenciador de recursos de um sistema',
            'Visual Studio Code' : 'Editor de código-fonte'
}

for l in dicionario:
    print(f'A palavra é {l} e o seu significado é {dicionario[l]}')
    print('-' * 120)
