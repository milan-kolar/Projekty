import pygame

# Inicializujeme Pygame
pygame.init()

# Otevřeme okno hry o velikosti 640x480 pixelů
screen = pygame.display.set_mode((640, 480))

# Nastavíme titulek okna
pygame.display.set_caption("Můj první Pygame program")

# Nastavíme pozadí okna na bílou barvu
screen.fill((255, 255, 255))

# Vytvoříme čtverec o velikosti 50x50 pixelů vlevo uprostřed okna
rect = pygame.Rect(290, 190, 50, 50)

# Vytvoříme šedý čtverec
pygame.draw.rect(screen, (192, 192, 192), rect)

# Překreslíme obsah okna
pygame.display.flip()

# Hra běží, dokud nezavřeme okno
running = True
while running:
    # Získáme seznam událostí
    for event in pygame.event.get():
        # Pokud bylo okno zavřeno, ukončíme hru
        if event.type == pygame.QUIT:
            running = False

# Ukončíme Pygame
pygame.quit()
