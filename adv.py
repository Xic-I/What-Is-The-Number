import time
import random
import sys

def Lv1():
    n=random.randrange(0,100)
    print('Level 1\n')

    while 1:
        r=int(input("Adivinhe um número de 0 a 100: "))

        if r > n:
            print('O número é menor')

        if r < n:
            print('O número é maior')

        if r > 100:
            print('O número sorteado é somente entre 0 a 100')

        if r < 0:
            print('O número sorteado é somente entre 0 a 100')

        if r == n:
            print('\nParabéns, você acertou o número sorteado. E o número era: '+str(n),'\n')
            time.sleep(2)

            print("Deseja continuar?\n")
            time.sleep(0)
            print("Sim\nNão\n")
            r2=input("Resposta: ")

        if r2 == 'sim' or r2 == 'Sim':
            time.sleep(1)
            Lv2()

        if r2 == 'não' or r2 == 'nao' or r2 == 'Não' or r2 == 'Nao':
            print("Saindo.....")
            time.sleep(1)
            sys.exit()

def Lv2():
    print('Level 2\n')
    n=random.randrange(0,500)
    
    while 1:
        r=int(input("Adivinhe um número de 0 a 500: "))

        if r > n:
            print('O número é menor')

        if r < n:
            print('O número é maior')

        if r > 500:
            print('O número é somente entre 0 a 500')

        if r < 0:
            print('O número é somente entre 0 a 500')

        if r == n:
            print('\nParabéns, você acertou o número sorteado. E o número era: '+str(n),'\n')
            time.sleep(2)

            print("Deseja continuar?\n")
            time.sleep(0)
            print("Sim\nNão\n")
            r2=input("Resposta: ")

        if r2 == 'sim' or r2 == 'Sim':
            time.sleep(1)
            Lv3()

        if r2 == 'não' or r2 == 'nao' or r2 == 'Não' or r2 == 'Nao':
            print("Saindo.....")
            time.sleep(1)
            sys.exit()


def Lv3():
    print('Level 3\n')
    n=random.randrange(0,1000)
    
    while 1:
        r=int(input("Adivinhe um número de 0 a 1000: "))

        if r > n:
            print('O número é menor')

        if r < n:
            print('O número é maior')

        if r > 1000:
            print('O número é somente entre 0 a 1000')

        if r < 0:
            print('O número é somente entre 0 a 1000')

        if r == n:
            print('\nParabéns, você acertou o número sorteado. E o número era: '+str(n),'\n')
            time.sleep(2)

            print("Deseja continuar?\n")
            time.sleep(0)
            print("Sim\nNão\n")
            r2=input("Resposta: ")

        if r2 == 'sim' or r2 == 'Sim':
            time.sleep(1)
            Lv4()

        if r2 == 'não' or r2 == 'nao' or r2 == 'Não' or r2 == 'Nao':
            print("Saindo.....")
            time.sleep(1)
            sys.exit()

def Lv4():
    print('Level 4\n')
    n=random.randrange(0,2000)
    
    while 1:
        r=int(input("Adivinhe um número de 0 a 2000: "))

        if r > n:
            print('O número é menor')

        if r < n:
            print('O número é maior')

        if r > 2000:
            print('O número é somente entre 0 a 2000')

        if r < 0:
            print('O número é somente entre 0 a 2000')

        if r == n:
            print('\nParabéns, você acertou o número sorteado. E o número era: '+str(n),'\n')
            time.sleep(2)

            print("Deseja continuar?\n")
            time.sleep(0)
            print("Sim\nNão\n")
            r2=input("Resposta: ")

        if r2 == 'sim' or r2 == 'Sim':
            time.sleep(1)
            Lv5()

        if r2 == 'não' or r2 == 'nao' or r2 == 'Não' or r2 == 'Nao':
            print("Saindo.....")
            time.sleep(1)
            sys.exit()

def Lv5():
    print('Level 5\n')
    print('Agora os números sorteados serão quebrados...Boa sorte\n')
    time.sleep(2)
    n=random.uniform(0,25)
    
    while 1:
        r=float(input("Adivinhe um número de 0 a 25: "))

        if r > n:
            print('O número é menor')

        if r < n:
            print('O número é maior')

        if r > 25:
            print('O número é somente entre 0 a 25')

        if r < 0:
            print('O número é somente entre 0 a 25')

        if r == n:
            print('\nParabéns, você acertou o número sorteado. E o número era: '+str(n),'\n')
            time.sleep(2)

            print("Deseja continuar?\n")
            time.sleep(0)
            print("Sim\nNão\n")
            r2=input("Resposta: ")

        if r2 == 'sim' or r2 == 'Sim':
            time.sleep(1)
            Lv6()

        if r2 == 'não' or r2 == 'nao' or r2 == 'Não' or r2 == 'Nao':
            print("Saindo.....")
            time.sleep(1)
            sys.exit()

def Lv6():
    print('Level 6\n')
    print('Caramba, ou você é muito sortudo ou muito bom para chegar até aqui\nEu creio mais na primeira opção\n')
    time.sleep(2)
    n=random.uniform(0,50)
    
    while 1:
        r=float(input("Adivinhe um número de 0 a 50: "))

        if r > n:
            print('O número é menor')

        if r < n:
            print('O número é maior')

        if r > 50:
            print('O número é somente entre 0 a 50')

        if r < 0:
            print('O número é somente entre 0 a 50')

        if r == n:
            print('\nParabéns, você acertou o número sorteado. E o número era: '+str(n),'\n')
            time.sleep(2)

            print("Deseja continuar?\n")
            time.sleep(0)
            print("Sim\nNão\n")
            r2=input("Resposta: ")

        if r2 == 'sim' or r2 == 'Sim':
            time.sleep(1)
            Lv7()

        if r2 == 'não' or r2 == 'nao' or r2 == 'Não' or r2 == 'Nao':
            print("Saindo.....")
            time.sleep(1)
            sys.exit()

def Lv7():
    print('Level 7\n')
    print('Troféu desbloqueado: Mão Quente\n')
    time.sleep(2)
    n=random.uniform(0,100)
    
    while 1:
        r=float(input("Adivinhe um número de 0 a 100: "))

        if r > n:
            print('O número é menor')

        if r < n:
            print('O número é maior')

        if r > 100:
            print('O número é somente entre 0 a 100')

        if r < 0:
            print('O número é somente entre 0 a 100')

        if r == n:
            print('\nParabéns, você acertou o número sorteado. E o número era: '+str(n),'\n')
            time.sleep(2)

            print("Deseja continuar?\n")
            time.sleep(0)
            print("Sim\nNão\n")
            r2=input("Resposta: ")

        if r2 == 'sim' or r2 == 'Sim':
            time.sleep(1)
            Lv8()

        if r2 == 'não' or r2 == 'nao' or r2 == 'Não' or r2 == 'Nao':
            print("Saindo.....")
            time.sleep(1)
            sys.exit()

def Lv8():
    print('Level 8\n')
    time.sleep(2)
    n=random.uniform(0,200)
    
    while 1:
        r=float(input("Adivinhe um número de 0 a 200: "))

        if r > n:
            print('O número é menor')

        if r < n:
            print('O número é maior')

        if r > 200:
            print('O número é somente entre 0 a 200')

        if r < 0:
            print('O número é somente entre 0 a 200')

        if r == n:
            print('\nParabéns, você acertou o número sorteado. E o número era: '+str(n),'\n')
            time.sleep(2)

            print("Deseja continuar?\n")
            time.sleep(0)
            print("Sim\nNão\n")
            r2=input("Resposta: ")

        if r2 == 'sim' or r2 == 'Sim':
            time.sleep(1)
            Lv9()

        if r2 == 'não' or r2 == 'nao' or r2 == 'Não' or r2 == 'Nao':
            print("Saindo.....")
            time.sleep(1)
            sys.exit()

def Lv9():
    print('Level 9\nÉ melhor se preparar pro level 10...\n')
    time.sleep(2)
    n=random.uniform(0,400)
    
    while 1:
        r=float(input("Adivinhe um número de 0 a 400: "))

        if r > n:
            print('O número é menor')

        if r < n:
            print('O número é maior')

        if r > 400:
            print('O número é somente entre 0 a 400')

        if r < 0:
            print('O número é somente entre 0 a 400')

        if r == n:
            print('\nParabéns, você acertou o número sorteado. E o número era: '+str(n),'\n')
            time.sleep(2)

            print("Deseja continuar?\n")
            time.sleep(0)
            print("Sim\nNão\n")
            r2=input("Resposta: ")

        if r2 == 'sim' or r2 == 'Sim':
            time.sleep(1)
            Lv6()

        if r2 == 'não' or r2 == 'nao' or r2 == 'Não' or r2 == 'Nao':
            print("Saindo.....")
            time.sleep(1)
            sys.exit()

def Lv10():
    print('Level 10\nWell, good luck. Now u have a limit time.')
    time.sleep(2)
    print('When the time runs out the game will restart.\nYou have 6 minutes')
    time.sleep(2)
    print('The timer unfortunately will not b shown because i was unable to show the time in real time. Good luck kid :)\n')
    time.sleep(2)
    print('Obs: if u dont insert a number when the time over, its ur last chance.')
    time.sleep(2)
    input('Press Enter when u are ready')

    print('The game started')

    n=random.uniform(0,10)
    limit=round(n,1)
    cronos1 = time.time()

    while 1:

        cronos2 = time.time()
        cronos = cronos2 - cronos1

        sec = int(cronos % 60)
        min = int(cronos // 60)
    
        if cronos > 5:
            print('Time over')
            Lv1()
        r=float(input("Guess a number from 0 to 1000: "))

        if r > limit:
            print('The number is lower')

        if r < limit:
            print('The number is greater')

        if r > 1000:
            print('The number is only between 0 to 1000')

        if r < 0:
            print('The number is only between 0 to 1000')

        if r == limit:
            print('\nCongratulations, u matched the drawn number. And the number is: '+str(limit),'\n')
            time.sleep(4)
            print('I see u finalized the game.\n')
            time.sleep(4)
            print('And if u are here u need a premium, or sleep.')
            time.sleep(4)
            print('Anyway, congratulations, now go out ur home dude, u need some solar light...')
            time.sleep(4)
            print('Bye man...')
            time.sleep(4)
            sys.exit()