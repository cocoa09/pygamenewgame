import pygame, sys, random, math

class Square(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        super(Square, self).__init__()
        self.image = pygame.Surface((20,200), pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x,y))
    
    def move(self, deltax, deltay):
        if self.rect.left <= 0 or self.rect.right>1200:
            deltax *= -4
        if self.rect.top <= 0 or self.rect.bottom > 600:
            deltay *= -4

        self.rect.centerx += deltax
        self.rect.centery += deltay

class Ball(pygame.sprite.Sprite):
    def __init__(self,size,x,y, color, velocity):
        super(Ball, self).__init__()
        self.image = pygame.Surface((20,20), pygame.SRCALPHA, 32)
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x,y))
        self.deltax = velocity

        self.deltax = random.choice([-1,1])
        self.deltay = random.choice([-1,1])

    def move(self):
        if self.rect.left <= -0:
            self.kill()
            screen.blit(text_2, (500,200))
        if  self.rect.right >= 1200:
            self.kill()
            screen.blit(text_1, (500,200))
        if self.rect.top <= -0 or self.rect.bottom >= 600:
            self.deltay *= -1
        speed_mod = 1
        p_list = pygame.sprite.spritecollide(self,squares,False)
        if p_list:
            self.deltax *= -1
            self.image.fill(p_list[0].color)
            speed_mod*=1.3
            self.deltax*=speed_mod
            self.deltay*=speed_mod
        self.rect.centerx += self.deltax*2
        self.rect.centery += self.deltay*2
class Ball_yay(pygame.sprite.Sprite):
    def __init__(self,size,x,y, color,):
        super(Ball_yay, self).__init__()
        self.image = pygame.Surface((20,20), pygame.SRCALPHA, 32)
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x,y))
    def yay(self):
        yay_list = pygame.sprite.spritecollide(self,pong,False)
        if yay_list:
            screen.blit(text_yay, (500,200))




pygame.init()

# Set up the screen dimensions
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("pong")

# Create clock to later control frame rate
clock = pygame.time.Clock()
rand_xpos= random.randint(300,900)
rand_ypos= random.randint(150,150)
sq1 = Square(1180,300,"blue")
sq2 = Square(20,300,"red")
squares = pygame.sprite.Group()
squares.add(sq1)
squares.add(sq2)
pong = Ball(20, 600, 300, "white", 2)
pongs = pygame.sprite.Group()
pongs.add(pong)
yay=Ball_yay(10,rand_xpos,rand_ypos,(255, 234, 0))
yays=pygame.sprite.Group()
yays.add(yay)
# Main game loop
running = True
font_yay = pygame.font.SysFont('Arial',100)
font = pygame.font.SysFont('Arial', 50)
text_1 = font.render('red wins!!!', True, (255, 50, 50))
text_2 = font.render('blue wins!!!', True, (50, 50, 255))
text_yay= font_yay.render('YAY!!!YAY!!!:)', True, (255, 234, 0))

while running:
    # Event handling

    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False
    screen.fill((50,0,0))

        # Get the state of all keys
    keys = pygame.key.get_pressed()

     #Update rectangle position based on key presses
    # if keys[pygame.K_LEFT]:
    #     sq.rect.x -= 2
    # if keys[pygame.K_RIGHT]:
    #     sq.rect.x += 2
    # if keys[pygame.K_UP]:
    #     sq.rect.y -= 2
    # if keys[pygame.K_DOWN]:
    #     sq.rect.y += 2
    
    # if keys[pygame.K_LEFT]:
    #     sq1.move(-2,0)
    # if keys[pygame.K_RIGHT]:
    #     sq1.move(2,0)
    if keys[pygame.K_n]:
        sq1.move(0,-4)
    if keys[pygame.K_m]:
        sq1.move(0,4)
    
    # if keys[pygame.K_a]:
    #     sq2.move(-2,0)
    # if keys[pygame.K_d]:
    #     sq2.move(2,0)
    if keys[pygame.K_x]:
        sq2.move(0,-4)
    if keys[pygame.K_c]:
        sq2.move(0,4)
    pong.move()
    squares.draw(screen)
    pongs.draw(screen)
    yays.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

