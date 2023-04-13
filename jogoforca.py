import random
from palavra import palavras
import string

print(palavras)

def validar_palavra(words):
    palavra = random.choice(palavras)
    while '_' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)
    return palavra.upper()

def jogoforca():
    palavra = validar_palavra(palavras)
    palavra_letra = set(palavra)
    alfabeto = set(string.ascii_uppercase)
    letra_usada = set()

    while len(palavra_letra) > 0:
        print('Voce usou essas letras: ', ' '.join(letra_usada))

        palavra_Lista = [letra if letra in letra_usada else '_' for letra in palavra]
        print('Palavra atual: ', ' '.join(palavra_Lista))


        letra_usuario = input('Adivinhe uma letra: ').upper()
        if letra_usuario in alfabeto - letra_usada:
           letra_usada.add(letra_usuario)
           if letra_usuario in palavra_letra:
                palavra_letra.remove(letra_usuario)

        elif letra_usuario in letra_usada:
         print('vc ja usou essa letra. tente de novo')

        else:
            print('caracter invalido')

jogoforca()





