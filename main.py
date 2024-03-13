import pygame
import sys
import random

# Inicializa o pygame
pygame.init()

# Define as dimensões da tela
largura_tela = 640
altura_tela = 480

# Define as cores
azul = (0, 0, 255)
amarelo = (255, 255, 0)

# Define as propriedades da cobra
tamanho_cobra = 20
velocidade_cobra = 15

# Inicializa a tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo da Cobra")

# Inicializa a cobra
cobra = [(largura_tela // 2, altura_tela // 2)]
direcao_cobra = (1, 0)

# Inicializa a comida
comida = (random.randint(0, largura_tela // tamanho_cobra - 1) * tamanho_cobra,
          random.randint(0, altura_tela // tamanho_cobra - 1) * tamanho_cobra)

# Inicializa a pontuação
pontuacao = 0

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualiza a posição da cobra
    cabeca_cobra = (cobra[0][0] + direcao_cobra[0] * tamanho_cobra,
                    cobra[0][1] + direcao_cobra[1] * tamanho_cobra)
    cobra.insert(0, cabeca_cobra)

    # Verifica se a cobra comeu a comida
    if cabeca_cobra == comida:
        comida = (random.randint(0, largura_tela // tamanho_cobra - 1) * tamanho_cobra,
                  random.randint(0, altura_tela // tamanho_cobra - 1) * tamanho_cobra)
        pontuacao += 1
    else:
        cobra.pop()

    # Verifica se a cobra bateu na parede
    if (cabeca_cobra[0] < 0 or cabeca_cobra[0] >= largura_tela or
            cabeca_cobra[1] < 0 or cabeca_cobra[1] >= altura_tela):
        print(f"Fim de jogo! Sua pontuação: {pontuacao}")
        pygame.quit()
        sys.exit()

    # Desenha a cobra e a comida
    tela.fill((0, 0, 0))
    for segmento in cobra:
        pygame.draw.rect(tela, azul, pygame.Rect(segmento[0], segmento[1], tamanho_cobra, tamanho_cobra))
    pygame.draw.rect(tela, amarelo, pygame.Rect(comida[0], comida[1], tamanho_cobra, tamanho_cobra))

    # Atualiza a tela
    pygame.display.flip()

    # Controla o movimento da cobra
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        direcao_cobra = (-1, 0)
    elif teclas[pygame.K_RIGHT]:
        direcao_cobra = (1, 0)
    elif teclas[pygame.K_UP]:
        direcao_cobra = (0, -1)
    elif teclas[pygame.K_DOWN]:
        direcao_cobra = (0, 1)

    # Controla a velocidade da cobra
    pygame.time.Clock().tick(velocidade_cobra)
