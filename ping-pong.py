from random import randint
from pygame import *
font.init()
 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("racket.png"), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.speed = player_speed
        self.rect.x = player_x

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 600
win_height = 500
speed_x = 3
speed_y = 3
window = display.set_mode((win_width, win_height))
display.set_caption('пинг-понг')


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 70:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed

player1 = Player('racket.png', 30, 200, 4, 50, 150)
player2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball', 200, 200, 4, 50, 50 )

left = 0
right = 0

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
        player1.update_l()
        player2.update_r()
        ball.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > win_width:
            ball.rect.x = randint(80, win_width - 80)
            ball.rect.y = 0
            left += 1

    if ball.rect.y < win_width:
            ball.rect.x = randint(80, win_width - 80)
            ball.rect.y = 0
            right += 1
    
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    
    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= -1

    if left >= 3:
        window.blit(winr, (200, 200))
        run = False

    if right >= 3:
        window.blit(winl, (200, 200))
        run = False

display.update()
clock.tick(FPS)
