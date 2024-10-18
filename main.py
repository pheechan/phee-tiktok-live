import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = 
run = True
while run == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
































































"""import pygame
import time
import Background_layers as bg
# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Load background layers
background_layers = [
    pygame.image.load(f"background_layer_{i}.png") for i in range(10)
]

# Scale background layers
background_layers = [
    pygame.transform.scale(layer, (WIDTH, HEIGHT)) for layer in background_layers
]

# Load character and monster images for animations
character_idle_images = [pygame.image.load(f"adventurer-idle-0{i}.png") for i in range(3)]
character_attack_images = [pygame.image.load(f"cadventurer-attack1-0{i}.png") for i in range(1, 4)]
monster_images = [pygame.image.load(f"monster_{i}.png") for i in range(1, 4)]

# Scale character and monster images
character_idle_images = [pygame.transform.scale(img, (100, 100)) for img in character_idle_images]
character_attack_images = [pygame.transform.scale(img, (100, 100)) for img in character_attack_images]
monster_images = [pygame.transform.scale(img, (100, 100)) for img in monster_images]

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Attack the Monster")

# Character and Monster positions
character_pos = (WIDTH - 150, HEIGHT // 2 - 50)
monster_pos = (50, HEIGHT // 2 - 50)

# Monster HP
monster_hp = 100

# Font for displaying HP
font = pygame.font.Font(None, 36)

# Animation settings
character_idle_index = 0
character_attack_index = 0
monster_index = 0
animation_speed = 0.1  # seconds per frame
last_animation_time = time.time()

# Main game loop
running = True
attacking = False
attack_cooldown = 1  # seconds
last_attack_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current time
    current_time = time.time()

    # Check for attack
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and current_time - last_attack_time > attack_cooldown:
        attacking = True
        last_attack_time = current_time
        monster_hp -= 10  # Decrease monster HP by 10

    # Update animation frames
    if current_time - last_animation_time > animation_speed:
        last_animation_time = current_time
        character_idle_index = (character_idle_index + 1) % len(character_idle_images)
        character_attack_index = (character_attack_index + 1) % len(character_attack_images)
        monster_index = (monster_index + 1) % len(monster_images)

    # Draw background layers
    for layer in background_layers:
        screen.blit(layer, (0, 0))

    # Draw monster
    screen.blit(monster_images[monster_index], monster_pos)

    # Draw character
    if attacking:
        screen.blit(character_attack_images[character_attack_index], character_pos)
        if character_attack_index == len(character_attack_images) - 1:
            attacking = False
    else:
        screen.blit(character_idle_images[character_idle_index], character_pos)

    # Display monster HP
    hp_text = font.render(f"HP: {monster_hp}", True, (255, 0, 0))
    screen.blit(hp_text, (monster_pos[0], monster_pos[1] - 30))

    # Check if monster is dead
    if monster_hp <= 0:
        running = False

    # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()"""