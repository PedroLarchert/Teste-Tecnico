# 1. Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.#
def fibonacci(number):

    fibonacci = [0,1]
    x = 1
    num = fibonacci[x]
    while num < number:
 
        num = fibonacci[x] + fibonacci[x-1]
        fibonacci.append(num)
        x += 1 

    if number in fibonacci:   
        return 'Pertence a sequencia'
    else:
        return 'Nao pertence a sequencia'

#num = int(input())
##print(fibonacci(num))


#2.Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def Existe_A(string):

    counter = 0
    for letra in string:
        if letra.lower() == 'a':
            counter += 1
    
    if counter > 0 :
        mensagem = 'a string possui ' + str(counter) + ' letras "a"'
    else:
        mensagem= 'a string não possui a letra "a"'

    return mensagem

#str = input()
#print(Existe_A(str))

