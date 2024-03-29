import Classes3                                             #Imports modules
import pygame
import random
import time
import Game4
import mysql.connector

BLACK = (  0,   0,   0)                                     #Sets Color Presets
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
ALPHA = (255,   0, 255)

GREEN = (188, 202, 126)
GREENBR = (202, 223, 189)

FILL  = "I Don't Know!"                                     #My Filler Variable

def main(puntuacion,nombre):
    """ Main Function of the Game """
    pygame.init()

    size = (1200,700)                                       #Set size of Window
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Crusader Dig")              #Title

    player  = Classes3.Player(puntuacion,nombre)                              #Creates Instance of Player and Tunnel System
    tunnels = Classes3.Tiles()
        
    background = pygame.image.load("Level3.png").convert()   #Uploads Images
    explosion  = pygame.image.load("explosion.png").convert()
    explosion.set_colorkey(ALPHA)
    
    gameover = pygame.image.load("game over.png").convert_alpha()
    youwin   = pygame.image.load("nextlevel.png").convert_alpha()
    object1find   = pygame.image.load("img/Teotihuacan1.png").convert_alpha()
    object2find   = pygame.image.load("img/Teotihuacan2.png").convert_alpha()
    object3find   = pygame.image.load("img/Teotihuacan3.png").convert_alpha()
    object5find   = pygame.image.load("img/Teotihuacan5.png").convert_alpha()
    lista_con_objetos = [True, True, True, True, True]

    pausevar = False


    done = False                                            #Set While Variable
    clock = pygame.time.Clock()
    
    obdiro = 0b1111                                         #Preset info to add tunnels
    indiro = 0b1111

    objlist = pygame.sprite.Group()                         #Creates lists of entities
    obslist = pygame.sprite.Group()
    enemylist = pygame.sprite.Group()
    deathlist = pygame.sprite.Group()
      # Inicialización de la fuente
    fuente = pygame.font.Font(None, 60)

    for obj in range(3):                                    #Creates Entities and Adds them to Lists
        objective = Classes3.Objective()
        objective.rect.x = objective.coord[obj][0]
        objective.rect.y = objective.coord[obj][1]
        objlist.add(objective)
            
    for obs in range(15):
        obstacle = Classes3.Obstacle()
        obstacle.rect.x = obstacle.coord[obs][0]
        obstacle.rect.y = obstacle.coord[obs][1]
        obslist.add(obstacle)

    for ene in range(3):
        enecoord = [[200,300],[700,500], [400,400]]
        enemy = Classes3.Enemy1()
        enemy.rect.x = enecoord[ene][0]
        enemy.rect.y = enecoord[ene][1]
        enemylist.add(enemy)
        deathlist.add(enemy)

    
            


    while not done:
        """ Main Game Loop """
    
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:           #close Game
                done = True
                
            if event.type == pygame.KEYDOWN:        #Restart Game
                if event.key == pygame.K_ESCAPE:
                    done = True
                    main(5,player.name)
                
                if event.key == pygame.K_LEFT:
                    player.easy = True
                    if player.change == [0,0]:
                        player.move(0,1,-1)#Moves Player
                    player.rotatable = True
                    obdiro = 0b1110                 #Tunnel Directions
                    indiro = 0b1101
                    player.rotate(FILL,FILL, "Left",FILL, player.imageL, FILL)#Rotates PLayer

                if event.key == pygame.K_RIGHT:
                    player.easy = True
                    if player.change == [0,0]:
                        player.move(0,1, 1)
                    player.rotatable = True
                    obdiro = 0b1101
                    indiro = 0b1110
                    player.rotate(FILL,FILL, "Right",FILL, player.imageR, FILL)

                if event.key == pygame.K_UP:
                    player.easy = False
                    if player.change == [0,0]:
                        player.move(1,0,-1)
                    player.rotatable = True
                    backgroundcoord = 1
                    obdiro = 0b1011
                    indiro = 0b0111

                if event.key == pygame.K_DOWN:
                    player.easy = False
                    if player.change == [0,0]:
                        player.move(1,0, 1)
                    player.rotatable = True
                    obdiro = 0b0111
                    indiro = 0b1011

                if event.key == pygame.K_SPACE:
                    if player.inventory == 8 :
                        done = True
                        pygame.quit()
                        Game4.main(player.inventory,player.name)     

        if player.change[0] > 0 or player.change[0] < 0:    #Allows Player to move on only one axis at a time    
            player.change[1] = 0
        if player.change[1] > 0 or player.change[1] < 0:
            player.change[0] = 0
        
        player.pos[0] += player.change[0]               #Move Player
        player.pos[1] += player.change[1]
        
        if player.pos[1] < 0:                         #Set limits at edges of screen
            player.pos[1] = 0
        if player.pos[1] > 600:
            player.pos[1] = 600
        if player.pos[0] < 0:
            player.pos[0] = 0
        if player.pos[0] > 1200:
            player.pos[0] = 1200
        if player.queue > 0:
            player.queue -= 1
        else:
            player.change = [0,0]
            
        player.rect.x = player.pos[0]                   #Sets Collision Box
        player.rect.y = player.pos[1]


        if player.change == [0,0]:                                                   #Adds tunnels
            player.tunnelpos[0] = player.pos[0]//100
            player.tunnelpos[1] = player.pos[1]//100 
            if not player.tunnelpos[1] == 0:
                tunnels.addtunnel(player.tunnelpos[0], player.tunnelpos[1],obdiro)
        else:
            if not player.cachetunnel[1] == 0:
                tunnels.addtunnel(player.cachetunnel[0],player.cachetunnel[1],indiro)
            player.cachetunnel = player.tunnelpos

        for obstacle in obslist:                        #Checks if Player collides with obstacle
            if player.rect.colliderect(obstacle.rect):
                player.pos[0] -= player.change[0]       #Bounces Back Player
                player.pos[1] -= player.change[1]

                player.change[:] = [0, 0]


        if player.change == [0,0]:                                          #Delete and record collisions with objectives
            objcollide = pygame.sprite.spritecollide(player,objlist,True)    
        for objective in objcollide:
            player.inventory +=1    


        for enemy in enemylist:                                                    #Access each enemy
            if enemy.change == [0, 0]:
                enemy.change[:] = random.choice([(-1, 0), (1, 0), (0, 1), (0, -1)])#Randomly choose direction
            if (enemy.rect.y + enemy.rect.x) % 100 == 0:
                x = enemy.rect.x // 100
                y = enemy.rect.y // 100
                tile = tunnels.tilemap[y][x]
                if random.random() > 0.66:
                    enemy.change[:] = [0, 0]                    
                elif y == 0:
                    enemy.change[:] = [0, 1]
                elif tile & 0b1000 and enemy.change[1] == -1:           #Check for tunnel
                    enemy.change[1] = 0
                elif tile & 0b0100 and enemy.change[1] == 1:
                    enemy.change[1] = 0
                elif tile & 0b0010 and enemy.change[0] == -1:
                    enemy.change[0] = 0
                elif tile & 0b0001 and enemy.change[0] == 1:
                    enemy.change[0] = 0
 
            x, y = enemy.change
            if enemy.rect.y + y >= 600 or enemy.rect.y + y <= 0 or enemy.rect.x + x >= 1200 or enemy.rect.x + x <= 0: #Enemy can't leave screen
                enemy.change[:] = [0, 0]
            else:
                enemy.rect.y += y * 2               #Move Enemy
                enemy.rect.x += x * 2
                
            if enemy.change[0] == 1:                #Rotate Enemy
                enemy.image = enemy.imager
            if enemy.change[0] == -1:
                enemy.image = enemy.imagel
            enemy.image.set_colorkey(ALPHA)




        backgroundcoord = [0,0]                         #Draw the Background
        screen.blit(background,backgroundcoord)

        
        for row in range(13):                           #Draw Tunnels
            for column in range(12):
                screen.blit(tunnels.texture[tunnels.tilemap[row][column]],(column*100,row*100))

        objlist.draw(screen)                            #Draw Objectives
        obslist.draw(screen)                            #Draw Obstacles
        enemylist.draw(screen)                          #Draw Enemies

        player.Image.set_colorkey(ALPHA)
        screen.blit(player.Image,player.pos)            #Draw Player

        deathcollide = pygame.sprite.spritecollide(player,deathlist,False) #Check for collisions between Player and Enemies
        for death in deathcollide:
            deathtime = 30
            if deathtime > 0:                       #Draw Death Animation
                player.die()
                screen.blit(explosion,player.pos)
                deathtime -=1
            player.life = 0

                #If all objectives obtained
        texto = f"Puntuación : {player.inventory}00"
        letrero = fuente.render(texto, False, WHITE)
        screen.blit(letrero, (900- fuente.size(texto)[0] / 2, 10))  

        texto = f"Nivel             : 003"
        letrero = fuente.render(texto, False, WHITE)
        screen.blit(letrero, (900- fuente.size(texto)[0] / 2, 60))     
        
 
        


        if player.life == 0:                #If dead
            screen.blit(gameover, [0,0])      #Draw Game Over
            
        if player.inventory == 6 and lista_con_objetos[0]:           #If all objectives obtained
            screen.blit(object1find, [0,0])
            pygame.display.flip()        #Draw You Win!
            time.sleep(2)
            lista_con_objetos[0]=False
             
        if player.inventory == 7 and lista_con_objetos[1]:           #If all objectives obtained
            screen.blit(object2find, [0,0])
            pygame.display.flip()        #Draw You Win!
            time.sleep(2)
            lista_con_objetos[1]=False
             
        if player.inventory == 8 and lista_con_objetos[2]:           #If all objectives obtained
            screen.blit(object3find, [0,0])
            pygame.display.flip()        #Draw You Win!
            time.sleep(2)
            lista_con_objetos[2]=False
            screen.blit(object5find, [0,0])
            pygame.display.flip()        #Draw You Win!
            time.sleep(2)

        if player.inventory == 8: 
            miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='kukulcan' )
            cur = miConexion.cursor()
            cur.execute( "UPDATE usuarios set nivel = '"+str(3)+"', puntuacion = '"+str(player.inventory)+"' WHERE usuario = '"+player.name+"'" )
            row = cur.fetchone()
            miConexion.commit()
            miConexion.close()
            screen.blit(youwin, [0,0])         #Draw You Win!


        pygame.display.flip()               #Update Screen
        clock.tick(60)                      #Set Framerate



                
