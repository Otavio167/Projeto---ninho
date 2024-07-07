import musica
import player
import os
import pygame

while True:
    
    print('''
SpotNinho - Music App!

1 - Escutar PlayList completa.
2 - Listar músicas.
3 - Informações das músicas.
4 - Sair.''')

    escolha = int(input("\nInsira uma opção (número): "))

    if escolha == 1:
        
        cont = 0
        
        while cont < len(musica.musicas):
            
            music = musica.musicas[cont]
            
            play = player.Player(music)
            
            play.start()
            
            musica_pausada = False 

            while True:
                
                print('''\n1 - Pausar.
2 - Despausar.
3 - Próxima.
4 - Anterior.
5 - sair da playlist.''')
                
                comando = input("\nInsira uma opção: ")

                if comando == '1':
                    
                    play.pausar()
                    
                    musica_pausada = True

                elif comando == '2' and musica_pausada:
                    
                    play.despausar()
                    
                    musica_pausada = False

                elif comando == '3':
                    
                    play.parar()
                    
                    break

                elif comando == '5':
                    
                    play.parar()
                    
                    cont = len(musica.musicas)  
                    
                    break
                
                elif comando  == '4' and cont != 0:
                    
                    music = musica.musicas[cont - 1]
                    
                    play  = player.Player(music)
                    
                    play.start()
                    
                    cont = cont - 1

                if not musica_pausada and not pygame.mixer.music.get_busy():
                    
                    break

            if comando == 'sair':
                
                break

            if not musica_pausada:
                
                cont += 1

        print("\nVoltando ao menu principal...")
        
        os.system("PAUSE")
        
        


    
    
    
    
        

     





