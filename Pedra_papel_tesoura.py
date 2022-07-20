'''
Code created by a Brazilian, Eliézer.M, so it's in Portuguese.
started on 07/16/2022 and ended on 07/19/2022 at 22:25 pm

'''

from random import choice

def onegame():
       
    p_p_t = ['Pedra','Papel','Tesoura']
    print('''
|==================================================|
|                                                  |   
|   Primeiramente você deve informar qual deseja   |
|   jogar: "Pedra", "Papel" ou "Tesoura". Logo     |
|   depois o computador ira jogar contra você.     |
|                                                  |
|==================================================|
                        | |
                        | |
                        | |
                        | |
                        | |
                        | |
                        | |
                       _|_|_

''')

    while True:
        ps = choice(p_p_t)
        ti = input('Informe "Pedra", "Papel" ou "Tesoura": ')
        
        #CONDICIONAIS JOGADOR

        if ti == 'Pedra' and ps == 'Tesoura':
            print()
            print('Pedra x Tesoura')
            print('Parabens Você venceu!')
            print()
            again = int(input('Deseja Jogar novamente? 1-Sim 2-Não: '))
            if again == 1:
                continue
            else:
                break
            
        elif ti == 'Papel' and ps == 'Pedra':
            print()
            print('Papel x Pedra')
            print('Parabens Você venceu!')
            print()
            again = int(input('Deseja Jogar novamente? 1-Sim 2-Não: '))
            if again == 1:
                continue
            else:
                break
            
            
        elif ti == 'Tesoura' and ps == 'Papel':
            print()
            print('Tesoura x Papel')
            print('Parabens Você venceu!')
            print()
            again = int(input('Deseja Jogar novamente? 1-Sim 2-Não: '))
            if again == 1:
                continue
            else:
                break
            
        
        #CONDICIONAIS COMPUTADOR
        
        if ps == 'Pedra' and ti == 'Tesoura':
            print()
            print('Pedra x Tesoura')
            print('Você Perdeu! :(')
            print()
            again = int(input('Deseja Jogar novamente? 1-Sim 2-Não: '))
            if again == 1:
                continue
            else:
                break
            
        elif ps == 'Papel' and ti == 'Pedra':
            print()
            print('Pedra x Papel')
            print('Você Perdeu! :(')
            print()
            again = int(input('Deseja Jogar novamente? 1-Sim 2-Não: '))
            if again == 1:
                continue
            else:
                break
            
        elif ps == 'Tesoura' and ti == 'Papel':
            print()
            print('Tesoura x Papel')
            print('Você Perdeu! :(')
            print()
            again = int(input('Deseja Jogar novamente? 1-Sim 2-Não: '))
            if again == 1:
                continue
            else:
                break    

        #CASO HAJA JOGADAS IGUAIS
        elif ti == 'Pedra' and ps == 'Pedra' or ti == 'Papel' and ps == 'Papel' or ti == 'Tesoura' and ps == 'Tesoura':
            print()
            print('================================')
            print('Jogadas iguais, jogue novamente:')
            print('================================')
            print()
        
            
def treegame():
    ax = 0
    player = 0
    computador = 0

    p_p_t = ['Pedra','Papel','Tesoura']
    print('''
|==================================================|
|                                                  |
|   Primeiramente você deve informar qual deseja   |
|   jogar: "Pedra", "Papel" ou "Tesoura". Logo     |
|   depois o computador ira jogar contra você.     |
|                                                  |
|==================================================|
                        | |
                        | |
                        | |
                        | |
                        | |
                        | |
                        | |
                       _|_|_

''')
    
    while True:
        
        ps = choice(p_p_t)
        ti = input('Informe "Pedra", "Papel" ou "Tesoura": ')
        
        #CONDICIONAIS JOGADOR

        if ti == 'Pedra' and ps == 'Tesoura':
            print()
            print('Pedra x Tesoura')
            print('Parabens Você venceu!')
            print()
            print('Player +1')
            player+=1
            ax+=1
            print()
           
        elif ti == 'Papel' and ps == 'Pedra':
            print()
            print('Papel x Pedra')
            print('Parabens Você venceu!')
            print()
            print('Player +1')
            player+=1
            ax+=1
            print()
            
            
        elif ti == 'Tesoura' and ps == 'Papel':
            print()
            print('Tesoura x Papel')
            print('Parabens Você venceu!')
            print()
            print('Player +1')
            player+=1
            ax+=1
            print()
            
            
        
        #CONDICIONAIS COMPUTADOR
        
        if ps == 'Pedra' and ti == 'Tesoura':
            print()
            print('Pedra x Tesoura')
            print('Você Perdeu! :(')
            print()
            print('Computador +1')
            computador+=1
            ax+=1
            print()
            
                
            
        elif ps == 'Papel' and ti == 'Pedra':
            print()
            print('Pedra x Papel')
            print('Você Perdeu! :(')
            print()
            print('Computador +1')
            computador+=1
            ax+=1
            print()
            
            
        elif ps == 'Tesoura' and ti == 'Papel':
            print()
            print('Tesoura x Papel')
            print('Você Perdeu! :(')
            print()
            print('Computador +1')
            computador+=1
            ax+=1
            print()
                
        #CASO HAJA JOGADAS IGUAIS
        elif ti == 'Pedra' and ps == 'Pedra' or ti == 'Papel' and ps == 'Papel' or ti == 'Tesoura' and ps == 'Tesoura':
            print()
            print('================================')
            print('Jogadas iguais, jogue novamente:')
            print('================================')
            print()

        
        #VERIFICAÇÃO DE QUEM VENCEU
        if ax == 3:
            if player > computador:
                print('Parabens! você ganhou!')
                print('''
    player = {}
    computador = {}
    '''.format(player,computador)) 
                again = int(input('Deseja Jogar novamente? 1-Sim 2-Não: '))
                if again == 1:
                        treegame()
                elif again == 2:
                    break
                break
            elif computador > player:
                print('Computador Venceu!')
                print('''
    player = {}
    computador = {}
    '''.format(player,computador)) 
                again = int(input('Deseja Jogar novamente? 1-Sim 2-Não: '))
                if again == 1:
                        treegame()
                elif again == 2:
                    break
            break
    

#INICIO JOGO

print('''

Bem-vindo(a) ao Pedra Papel Tesoura :)

''')
typegame = input('Deseja melhor de três? digite sim ou nao: ')
print()
if typegame == 'nao' or typegame == 'Nao' or typegame == 'não' or typegame == 'Não' or typegame == 'NAO' or typegame == 'NÃO':
    onegame()

elif typegame == 'sim' or typegame == 'Sim' or typegame == 'SIM':
    treegame()















