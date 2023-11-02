from desenho import forca

print('\x1b[2J\x1b[1;1H')
tentativas = c = 0
letra = ''
letras_erradas = []
letras_certas = []

palavra = input("Digite o nome da palavra: ").strip().lower()
dica = input("Digite a dica: ").strip()

while (tentativas != 6):
    print('\x1b[2J\x1b[1;1H')
    print('Dica:',dica)
    print(forca[tentativas])
    print(f'Letras erradas: {letras_erradas}')
    print(f'Letras certas: {letras_certas}')

    letra = input("\nLetra: ").lower()[0]
    if (letra in palavra):
        if (letra not in letras_certas):
            letras_certas.append(letra)
        for i in palavra:
            if (i in letras_certas):
                print(f"\033[4m{i}\033[m", end=' ')
                c += 1
            else:
                print('_', end=' ')
        if (c == len(palavra)):
            print('\x1b[2J\x1b[1;1H')
            print("\nDesafio cumprido!")
            break
        c = 0
        
    else:
        print(f'"{letra}" não existe nessa palavra')
        if (letra not in letras_erradas):
            letras_erradas.append(letra)
            tentativas += 1
        print('Tentativas restantes:', 6 - tentativas)
    
    input('\nenter para continuar')


print(forca[tentativas])
print(f'Tentativas esgotadas!\nPalavra certa: {palavra}')
input('\nenter para sair')
