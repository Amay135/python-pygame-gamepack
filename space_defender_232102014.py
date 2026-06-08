import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Defender")
clock = pygame.time.Clock()

class GameObject:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Player(GameObject):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.speed = 7
        self.lives = 100

        # mengubah player menjadi gambar pesawat
        self.image = pygame.image.load("pesawat.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.width = 80
        self.height = 80
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)



    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        # Mengembalikan peluru yang berasal dari tengah atas pemain
        return Bullet(self.rect.centerx - 2.5, self.rect.top, 5, 10, GREEN)
    
    
    def draw(self, surface):
        # Gambar pesawat di posisi player
        surface.blit(self.image, self.rect.topleft)


class Meteor(GameObject):
    def __init__(self, x, y, width, height, color, speed):
        super().__init__(x, y, width, height, color)
        self.speed = speed

        #mengubah gambar menjadi pesawat 1 dan pesawat 2
        self.images = [
            ("pesawatmusuh1.png", 80, 80, False),
            ("pesawatmusuh2.png", 50, 80, True),
        ]

        selected_image, self.width, self.height, rotate = random.choice(self.images)
        self.image = pygame.image.load(selected_image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        if rotate:
            self.image = pygame.transform.rotate(self.image, 180)
            
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        

    def fall(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    

class Bullet(GameObject):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.speed = -10

    def move(self):
        self.rect.y += self.speed

def main():
    player = Player(WIDTH // 2, HEIGHT - 60, 50, 30, BLUE)

    meteors = []
    bullets = []

    score = 0
    running = True

    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullets.append(player.shoot())
                
        keys = pygame.key.get_pressed()
        player.move(keys)

        if random.randint(1, 50) == 1:
            meteors.append(Meteor(random.randint(0, WIDTH - 40), 0, 40, 40, RED, random.randint(3, 7)))

        for meteor in meteors[:]:
            meteor.fall()
            if meteor.rect.top > HEIGHT:
                meteors.remove(meteor)
                player.lives -= 1
                if player.lives == 0:
                    print("Game Over! Your Score:", score)
                    running = False

        for bullet in bullets[:]:
            bullet.move()
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)

        for bullet in bullets[:]:
            for meteor in meteors[:]:
                if bullet.rect.colliderect(meteor.rect):
                    bullets.remove(bullet)
                    meteors.remove(meteor)
                    score += 1
                    break

        player.draw(screen)
        for meteor in meteors:
            meteor.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)

        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {player.lives}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
  