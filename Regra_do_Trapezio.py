## Área do trapézio ##
## Developed by: Sadigueira ##

import math
import time

def menu():
    print('\n')
    print('Regra do Trapézio')
    print('\n')
    print('******* Menu *******')
    print('1 - Começar calculos')
    print('2 - Sair')
    print('********************')
    print('\n')
    
menu()

opcao = int(input('Digite a sua opcao:'))
while opcao < 1 or opcao >2:
    print('opcao invalida!!!')
    opcao = int(input('Digite a sua opcao:'))
    
while opcao == 2:
    print('Programa encerrando!')
    break

while opcao ==1:
    a = float(input('Digite o valor de a:'))
    b = float(input('Digite o valor de b:'))

    while a >= b:
        print('Valor de A precisa ser menor que B')
        a = float(input('Digite o valor de a:'))
        b = float(input('Digite o valor de b:'))
    
    n = int(input('Digite o numero de intervalos:'))
    
    while n <= 0:
        print('Valor de n precisa ser maior que 0!')
        n = int(input('Digite o numero de intervalos:'))

    area_total = 0
    x = a
    h = (b - a) / n
    
    ## Função da equação ##
    funcao = 1/math.sqrt(1+3*x) 
    i = 0

    while i < n:
        x = x + h
        y2 = 1/math.sqrt(1+3*x)
        area_trapezio = ((funcao + y2) / 2) * h
        area_total = area_total + area_trapezio
        funcao = y2
        i = i + 1
    
    print('Área total:', area_total)
    time.sleep(1)
    
    menu()
    
    opcao = int(input('Digite a sua opcao:'))
    
    while opcao < 1 or opcao >2:
        print('opcao invalida!!!')
        opcao = int(input('Digite a sua opcao:'))
    
    while opcao == 2:
        print('Programa encerrando!')
        break


