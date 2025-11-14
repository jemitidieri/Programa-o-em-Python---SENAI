import pygame

pygame.init()

tela = pygame.display.set_mode((300,200))
pygame.display.set_caption('Titulo')
run = True

while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False


    tela.fill('pink')
    pygame.draw.rect(tela,'blue',(145,95,5,5))
    pygame.draw.circle(tela, 'red', (100,50), 50)
    pygame.draw.ellipse(tela,'green',(150,50,25,50))

    pygame.display.flip()



pygame.quit()

