import random as rd

a = int(input("\nDigite o numero de começo do intervalo: "))

b = int(input("\nDigite o numero de fim do intervalo: "))

chutes = int(input("\nDigite a quantidade de chutes que você quer fazer: "))

while (chutes < 5):
    print("\nFaça no minimo 5 chutes")
    chutes = int(input("\nDigite a quantidade de chutes que você quer fazer: "))
    

numero = rd.randint(a,b)

resposta = ''

def dica1(numero):
    if numero % 3 == 0:
        return '\n#Dica 1: Seu numero é divisivel por 3'
    elif numero % 5 == 0:
        return '\n#Dica 1: Seu numero é divisivel por 5'
    else:
        return' \n#Dica 1: Seu numero não é divisivel por 3 ou 5'

def dica2(numero):
    mult = 0

    for count in range(2,numero):
        if (numero % count == 0):
            mult += 1

    if(mult==0):
        return '\n#Dica 2: Seu número é primo!'
    else:
        return '\n#Dica 2: Seu número não é primo!'


def dica3(numero):
    if numero % 2 == 0:
        return'par'
    else:
        return 'impar'

def jogo(a,b,numero,resposta,chutes):

    contador = 0

    while (resposta != numero):

        resposta = int(input('\nDigite o numero do seu chute: '))
        
        mm =''
        
        if resposta > numero:
            mm='menor'

        elif resposta < numero:
            mm='maior'
        else:
             print(f'\nVocê acertou, muito bem! Seu numero realmente era {numero}')
             break
         
        print(f'\nNúmero errado, o seu numero é {mm} do que {resposta}')

        contador += 1
        
        
if contador == chutes-4:
            print('\nChute outro numero') 
        
        if contador == chutes-3:
            dica_1 = dica1(numero)
            print(dica_1)
            print('\nRestam 3 tentativas!')
        
        if contador == chutes-2:
            dica_2 = dica2(numero)
            print(dica_2)
            print('\nRestam 2 tentativas!')
        
        if contador == chutes-1:
            dica_3 = dica3(numero)
            print(f'\n#Dica 3: Seu numero é {dica_3}\nUltima tentativa!')
        if contador == chutes and numero != resposta:

            print('\nNão foi dessa vez! O numero sorteado foi', numero)
            print('\nTente novamente')
            numero = resposta
jogo(a,b,numero,resposta,chutes) 
         
if resposta == numero:
    print(f'\nVocê acertou, muito bem! Seu numero realmente era {numero}'
