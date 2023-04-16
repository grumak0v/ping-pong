# ping-pong
#Bauum, Bauum

from pygame import *
font.init()
 
class GameSprite(sprite.Sprite):
    def __init__(self, playerl_image, playerl_x, playerl_y, playerl_speed, playerr_image, playerr_x, playerr_y, playerr_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("racketl_image"), (65, 65))
        self.speedl = playerl_speed
        self.rect = self.image.get_rect()
        self.rect.xl = playerl_x
        self.rect.yl = playerl_y
        self.speed = player_speed
        self.rect.xr = playerr_x
        self.rect.yr = playerr_y
        self.image = transform.scale(image.load("racketr_image"), (65, 65))
        self.speedr = playerr_speed
 
    def reset(self):
        window.blit(self.image, (self.rect.xl, self.rect.yl, self.rect.xr, self.rect.yr))

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('пинг-понг')
background  = transform.scale(image.load('phonk.jpg'), (win_width, win_height))

class Playerl(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.yl > 5:
            self.rect.yl -= self.speed
        if keys[K_S] and self.rect.yl < win_height - 70:
            self.rect.yl += self.speed

playerl = Playerl('hero.png', 5, win_height - 90, 4)
playerr = Playerr('hero.png', 5, win_height - 0, 4)

class Playerr(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.yr > 5:
            self.rect.yr -= self.speed
        if keys[K_DOWN] and self.rect.yr < win_height - 70:
            self.rect.yr += self.speed

class Tenis_ball(GameSprite):
    def __init__(self, self.rect.y, self.rect.x, playerl_image, playerl_x, playerl_y, playerl_speed, playerr_image, playerr_x, playerr_y, playerr_speed):
        GameSprite.__init__(self, playerl_image, playerl_x, playerl_y, playerl_speed, playerr_image, playerr_x, playerr_y, playerr_speed, self.rect.y, self.rect.x)
        self.diraction = 'left'
    def update(self):
        if sprite.collide_rect(playerl, tenis_ball):
            self.diraction = 'right'
        if sprite.collide_rect(playerr, tenis_ball):
            self.diraction = 'left'
        if self.diraction == 'left':
            self.rect.x -= self.speed
        if self.rect.y > 5:
            self.diraction = 'down'
        if self.rect.y < win_height - 70:
            self.diraction = 'up'
        else:
            self.rect.x += self.speed   

game = True
finish = False
clock = time.Clock()
FPS = 60
font = font.Font(None, 70)
winl = font.render('LEFT WIN!', True, (255, 215, 0))
winr = font.render('RIGHT LOSE!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
 
 
    if not finish:
        # Отображение фона игрока и врага
        window.blit(background, (0, 0))
        Playerl.update()
        Playerr.update()
        Tenis_ball.update()

    if sprite.collide_rect(playerl, tenis_ball):
            
            window.blit(win, (200, 200))

display.update()
clock.tick(FPS)