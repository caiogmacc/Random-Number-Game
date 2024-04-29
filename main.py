import random as rd

# Definindo o intervalo do jogo
a = int(input("\nDigite o número de início do intervalo: "))
b = int(input("\nDigite o número de fim do intervalo: "))

# Definindo o número de chutes do jogador
chutes = int(input("\nDigite a quantidade de chutes que você quer fazer: "))

# Verificando se o número de chutes é menor que 5
while (chutes < 5):
    print("\nFaça no mínimo 5 chutes")
    chutes = int(input("\nDigite a quantidade de chutes que você quer fazer: "))

# Gerando o número secreto aleatório
numero = rd.randint(a, b)

# Variável para armazenar a resposta do jogador
resposta = ''

# Variavel para armazenar os chutes
tentativas = []

# Função para limpar a tela
def clear():
    print ("\n" * 130) 
        

# Função para fornecer a primeira dica
def dica1(numero):
    if numero % 3 == 0:
        return '\n#Dica 1: Seu número é divisível por 3'
    elif numero % 5 == 0:
        return '\n#Dica 1: Seu número é divisível por 5'
    else:
        return '\n#Dica 1: Seu número não é divisível por 3 ou 5'

# Função para fornecer a segunda dica
def dica3(numero):
    mult = 0
    for count in range(2, numero):
        if (numero % count == 0):
            mult += 1

    if (mult == 0):
        return '\n#Dica 2: Seu número é primo!'
    else:
        return '\n#Dica 2: Seu número não é primo!'

# Função para fornecer a terceira dica
def dica2(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

# Função principal do jogo
def jogo(numero, resposta, chutes,tentativas):
    contador = 0

    while (resposta != numero):
        resposta = int(input('\nDigite o seu chute: '))
        tentativas.append(resposta)

        mm = ''

        if resposta > numero:
            mm = 'menor'
        elif resposta < numero:
            mm = 'maior'
        else:
            print(f'\nVocê acertou! Seu número era {numero}')
            break

        print(f'\nNúmero errado, seu número é {mm} que {resposta}')
        print(f'Chutes até agora: {tentativas}')

        contador += 1

        if contador == chutes -4:
            print('\nChute outro número')

        if contador == chutes - 3:
            dica_1 = dica1(numero)
            print(dica_1)
            print('\nRestam 3 tentativas!')

        if contador == chutes - 2:
            dica_2 = dica2(numero)
            print(f'\n#Dica 3: Seu número é {dica_2}\nRestam 2 tentativas!')

        if contador == chutes-1:
            dica_3 = dica3(numero)
            print(f'{dica_3}\nÚltima tentativa!')
           

        if contador == chutes and numero != resposta:
            print('\nNão foi dessa vez! O número sorteado era', numero)
            print('\nTente novamente')
            numero = resposta

jogo(numero, resposta, chutes, tentativas)

if resposta == numero:
    print(f'\nVocê acertou! Seu número era {numero}')
