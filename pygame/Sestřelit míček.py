import pygame
import random

# Inicializujeme Pygame
pygame.init()

# Otevřeme okno hry o velikosti 640x480 pixelů
screen = pygame.display.set_mode((640, 480))

# Nastavíme titulek okna
pygame.display.set_caption("Sestřelit míček")

# # Nastavíme pozadí okna na bílou barvu
screen.fill((255, 255, 255))

# # Vytvoříme míček jako kruh o průměru 50 pixelů
# ball = pygame.draw.circle(screen, (0, 0, 255), (320, 240), 50)

# # Překreslíme obsah okna
# pygame.display.flip()

# Nastavíme počáteční skóre na 0
score = 0

# Create a new ball at a random position
x = random.randint(0, 640)
y = random.randint(0, 480)
ball = pygame.draw.circle(screen, (0, 0, 255), (x, y), 50)

# Draw the new ball and the score
pygame.draw.circle(screen, (0, 0, 255), ball.center, 50)
score_text = f"Score: {score}"
score_font = pygame.font.Font(None, 36)
score_surface = score_font.render(score_text, True, (0, 0, 0))
screen.blit(score_surface, (20, 20))

# Update the display
pygame.display.flip()

# Hra běží, dokud nezavřeme okno nebo nedosáhneme skóre 10 bodů
running = True
while running:
    # Získáme seznam událostí
    for event in pygame.event.get():
        # Pokud bylo okno zavřeno, ukončíme hru
        if event.type == pygame.QUIT:
            running = False
        # Pokud byl stisknut mezerník, zkontrolujeme, zda míček byl sestřelen
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Získáme souřadnice myši
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Zjistíme, zda míček byl sestřelen (pokud se myš nachází v míčku)
            if ball.collidepoint((mouse_x, mouse_y)):
                # Zvýšíme skóre o 1 bod
                score += 1
                # Pokud hráč dosáhl skóre 10 bodů, ukončíme hru
                if score >= 10:
                    running = False
                # Jinak vytvoříme nový míček na náhodné pozici
                else:
                    x = random.randint(0, 640)
                    y = random.randint(0, 480)
                    ball = pygame.draw.circle(screen, (0, 0, 255), (x, y), 50)
    # Vymažeme předchozí obsah okna
    screen.fill((255, 255, 255))
    # Vykreslíme nový míček a skóre
    pygame.draw.circle(screen, (0, 0, 255), ball.center, 50)
score_text = f"Score: {score}"
score_font = pygame.font.Font(None, 36)
score_surface = score_font.render(score_text, True, (0, 0, 0))
screen.blit(score_surface, (20, 20))

# Update the display
pygame.display.flip()