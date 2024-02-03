import pygame
import random

data = open("Resources/best_score.txt", "r")
best_score = data.read()
if best_score == "":
    best_score = 0
data.close()

pygame.init()
# the main window
win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Run and Collect")
# these are all the images needed for the game
walkRight = [pygame.image.load('Resources/right_1.png'), pygame.image.load('Resources/right_2.png'),
             pygame.image.load("Resources/right_3.png"),
             pygame.image.load('Resources/right_1.png'), pygame.image.load('Resources/right_2.png'),
             pygame.image.load('Resources/right_3.png'),
             pygame.image.load('Resources/right_1.png'), pygame.image.load('Resources/right_2.png'),
             pygame.image.load('Resources/right_3.png')]
walkLeft = [pygame.image.load('Resources/left_1.png'), pygame.image.load('Resources/left_2.png'),
            pygame.image.load('Resources/left_3.png'),
            pygame.image.load('Resources/left_1.png'), pygame.image.load('Resources/left_2.png'),
            pygame.image.load('Resources/left_3.png'),
            pygame.image.load('Resources/left_1.png'), pygame.image.load('Resources/left_2.png'),
            pygame.image.load('Resources/left_3.png')]
char = [pygame.image.load('Resources/standing_1.png'), pygame.image.load('Resources/standing_2.png'),
        pygame.image.load('Resources/standing_3.png'),
        pygame.image.load('Resources/standing_1.png'), pygame.image.load('Resources/standing_2.png'),
        pygame.image.load('Resources/standing_3.png'),
        pygame.image.load('Resources/standing_1.png'), pygame.image.load('Resources/standing_2.png'),
        pygame.image.load('Resources/standing_3.png')]
money_100 = pygame.image.load('Resources/100.png')
money_50 = pygame.image.load('Resources/50.png')
bg = pygame.image.load('Resources/bg.png')
bg_2 = pygame.image.load('Resources/bg_2.png')
bullet1 = pygame.image.load('Resources/dogecoin.png')
hp = pygame.image.load('Resources/hp_1.png')
game_over = pygame.image.load('Resources/gameover.png')
no_dg = pygame.image.load('Resources/no_dg.png')
plus = pygame.image.load('Resources/plus_hp.png')
green = pygame.image.load('Resources/green.png')
speed1 = pygame.image.load('Resources/speed.png')
dollar1 = pygame.image.load('Resources/dollar.png')

bullet_sound = pygame.mixer.Sound('Resources/uh.mp3')
hp_sound = pygame.mixer.Sound('Resources/hp.mp3')
deth_sound = pygame.mixer.Sound('Resources/wasted.mp3')
dollar_sound = pygame.mixer.Sound('Resources/kassa.mp3')
money_sound = pygame.mixer.Sound('Resources/money.mp3')
revival_sound = pygame.mixer.Sound('Resources/revival.mp3')
for_all_sound = pygame.mixer.Sound('Resources/for_all.mp3')


# just a mini function to create a random number from 1 to 0
def one_or_none():
    return random.randint(0, 1)


def one_to_five():
    return random.randint(1, 4)


# random data needed for random cordinats
q = 0


def info(input):
    global q
    if input == "rx":
        if one_or_none() == 1:
            q = 0
            return 0
        else:
            q = 500
            return 500
    elif input == "ry":
        return random.randint(35, 330)
    elif input == "rw":
        if q == 500:
            return -1
        else:
            return 1
    elif input == "mx":
        return random.randint(10, 480)


# the main class player
class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8
        self.left = False
        self.right = False
        self.stand = True
        self.walkCount = 0
        self.hitbox = (self.x + 8, self.y + 10, 40, 60)

    # to draw the pleyer animation
    def draw_man(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        if self.stand:
            win.blit(char[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            # it's hitbox
        self.hitbox = (self.x + 8, self.y + 10, 40, 60)

    # if a bullet hits it
    def hit_bullet(self):
        bullet_sound.play()
        global hpCount
        bullets.pop(bullets.index(bullet))
        # if a bullet hits it then we decrease the hp
        if hpCount == 3:
            all_hp[2].x = 700
        elif hpCount == 2:
            all_hp[1].x = 700
        elif hpCount == 1:
            all_hp[0].x = 700
        hpCount -= 1
        # if player collects the money

    def hit_money100(self):
        money_sound.play()
        global score
        score += 100
        money100.pop(money100.index(m))

    def hit_money50(self):
        money_sound.play()
        global score
        score += 50
        money50.pop(money50.index(m))

    def hit_no_dg(self):
        for_all_sound.play()
        global dg_hit
        noDg.pop(noDg.index(dg))
        dg_hit = True

    def hit_plusik(self):
        hp_sound.play()
        global hpCount
        plusiks.pop(plusiks.index(plusik))
        if hpCount == 3:
            pass
        elif hpCount == 2:
            hpCount += 1
            all_hp[2].x = 460
        elif hpCount == 1:
            all_hp[1].x = 425

    def hit_speed(self):
        for_all_sound.play()
        global five_
        five_ = True
        speed_.pop(speed_.index(speed))
        man.vel = 12

    def hit_dollar(self):
        dollar_sound.play()
        global five_s_dollar_F
        five_s_dollar_F = True
        dollars.pop(dollars.index(dollar))


# class
class Hp:
    def __init__(self, x, y, lost, index):
        self.x = x
        self.y = y
        self.lost = lost
        self.index = index

    def draw(self, win):
        win.blit(hp, (self.x, self.y))


# class bullet
class Snaryad:
    def __init__(self, x, y, way):
        self.x = x
        self.y = y
        self.way = way
        self.vel = 12 * way
        self.hitbox = (self.x - 6, self.y - 6, 10, 10)

    def draw(self, win):
        win.blit(bullet1, (self.x - 6, self.y - 6))
        self.hitbox = (self.x - 6, self.y - 6, 10, 10)


# money money money
class Money100:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_money(self, win):
        win.blit(money_100, (self.x, self.y))
        self.hitbox = (self.x, self.y, 14, 30)


class Money50:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_money(self, win):
        win.blit(money_50, (self.x, self.y))
        self.hitbox = (self.x, self.y, 14, 30)
    # the objects that turn off appearing bullets


class No_dg:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_dg(self, win):
        win.blit(no_dg, (self.x, self.y))
        self.hitbox = (self.x - 6, self.y - 6, 10, 10)


class PlusHp:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_plusik_(self, win):
        win.blit(plus, (self.x, self.y))


class Speed:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_speed(self, win):
        win.blit(speed1, (self.x, self.y))


class Dollar:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_dollar(self, win):
        win.blit(dollar1, (self.x, self.y))
        global many_dollars
        many_dollars = True


# variables
five_s = 0
five_ = False
clock = pygame.time.Clock()
run = True
ticks = 0
bullets = []
money100 = []
money50 = []
noDg = []
plusiks = []
speed_ = []
dollars = []
man = Player(220, 130, 60, 71)
dg_hit = False
ten_sec = 0
alarm = 0
all_hp = [Hp(390, 7, False, 0), Hp(425, 7, False, 1), Hp(460, 7, False, 2)]
hpCount = 3
gameover = False
score = 0
deth = 0
font = pygame.font.SysFont("Arial", 32)
five_s_dollar = 0
five_s_dollar_F = False


# if player loses
def redrawGame_over():
    win.blit(game_over, (0, 0))
    win.blit(text_score, (140, 15))
    win.blit(text_best_score, (190, 68))
    pygame.display.update()


# the loop that draws everything
def redrawGameWindow():
    win.blit(bg, (0, 0))
    for bullet in bullets:
        bullet.draw(win)
    man.draw_man(win)
    for i in all_hp:
        i.draw(win)
    for m in money100:
        m.draw_money(win)
    for m in money50:
        m.draw_money(win)
    for dg in noDg:
        dg.draw_dg(win)
    for plusik in plusiks:
        plusik.draw_plusik_(win)
    for speed in speed_:
        speed.draw_speed(win)
    for dollar in dollars:
        dollar.draw_dollar(win)
    win.blit(bg_2, (0, 0))
    win.blit(text_score, (320, 415))
    if dg_hit == True:
        win.blit(green, (102, 455))
    if five_ == True:
        win.blit(green, (165, 455))
    if five_s_dollar_F == True:
        win.blit(green, (230, 455))
    pygame.display.update()


# the main loop
while run == True:
    if gameover == False:
        if ten_sec >= 270:
            alarm = one_to_five()
            ten_sec = 0
        else:
            ten_sec += 1
        clock.tick(27)
        ticks += 2
        second = round(ticks / 60)
        if five_s_dollar_F == True:
            if five_s_dollar >= 135:
                five_s_dollar = 0
                five_s_dollar_F = False
            else:
                five_s_dollar += 1

        if five_ == True:
            if five_s >= 135:
                five_s = 0
                five_ = False
                man.vel = 8
            else:
                five_s += 1
        text_score = font.render(str(score), 0, (255, 193, 0))

        if hpCount == 0:
            gameover = True
        # dollar
        for dollar in dollars:
            if dollar.y > 480:
                dollars.pop(dollars.index(dollar))
            else:
                dollar.y += 5

        if len(dollars) < 1 and second >= 0:
            if alarm == 4:
                dollars.append(Dollar(info("mx"), 0))
                alarm = 0
        for dollar in dollars:
            if dollar.y - 7 < man.hitbox[1] + man.hitbox[3] and dollar.y + 14 > man.hitbox[1]:
                if dollar.x - 7 < man.hitbox[0] + man.hitbox[2] and dollar.x + 14 > man.hitbox[0]:
                    man.hit_dollar()
        # speed
        for speed in speed_:
            if speed.y > 480:
                speed_.pop(speed_.index(speed))
            else:
                speed.y += 5
        if alarm == 3:
            if len(speed_) < 1 and second >= 0:
                speed_.append(Speed(info("mx"), 0))
                alarm = 0

        for speed in speed_:
            if speed.y - 7 < man.hitbox[1] + man.hitbox[3] and speed.y + 14 > man.hitbox[1]:
                if speed.x - 7 < man.hitbox[0] + man.hitbox[2] and speed.x + 14 > man.hitbox[0]:
                    man.hit_speed()
        # hp plus
        for plusik in plusiks:
            if plusik.y > 480:
                plusiks.pop(plusiks.index(plusik))
            else:
                plusik.y += 5
        if alarm == 1:
            if len(plusiks) < 1 and second >= 0:
                plusiks.append(PlusHp(info("mx"), 0))
                alarm = 0

        for plusik in plusiks:
            if plusik.y - 7 < man.hitbox[1] + man.hitbox[3] and plusik.y + 14 > man.hitbox[1]:
                if plusik.x - 7 < man.hitbox[0] + man.hitbox[2] and plusik.x + 14 > man.hitbox[0]:
                    man.hit_plusik()
        # all about no dg
        for dg in noDg:
            if dg.y > 480:
                noDg.pop(noDg.index(dg))
            else:
                dg.y += 5

        if alarm == 2:
            if len(noDg) < 1 and second >= 0:
                noDg.append(No_dg(info("mx"), 0))
                alarm = 0

        for dg in noDg:
            if dg.y - 6 < man.hitbox[1] + man.hitbox[3] and dg.y + 6 > man.hitbox[1]:
                if dg.x - 6 < man.hitbox[0] + man.hitbox[2] and dg.x > man.hitbox[0]:
                    man.hit_no_dg()

        # all about money
        # for money 100
        for m in money100:
            if m.y < man.hitbox[1] + man.hitbox[3] and m.y + 30 > man.hitbox[1]:
                if m.x - 7 < man.hitbox[0] + man.hitbox[2] and m.x + 20 > man.hitbox[0]:
                    man.hit_money100()
        for money in money100:
            if money.y > 480:
                money100.pop(money100.index(money))
            else:
                money.y += 5

        if len(money100) < 1 and second >= 15 and second < 50:
            money100.append(Money100(info("mx"), 0))
        elif len(money100) < 2 and second >= 50:
            money100.append(Money100(info("mx"), 0))
        # for money 50
        for m in money50:
            if m.y < man.hitbox[1] + man.hitbox[3] and m.y + 30 > man.hitbox[1]:
                if m.x - 7 < man.hitbox[0] + man.hitbox[2] and m.x + 20 > man.hitbox[0]:
                    man.hit_money50()
        for money in money50:
            if money.y > 480:
                money50.pop(money50.index(money))
            else:
                money.y += 5

        if five_s_dollar_F == True:
            if len(money50) < 100:
                money50.append(Money50(info("mx"), 0))
        if len(money50) < 1 and second >= 5 and second < 20:
            money50.append(Money50(info("mx"), 0))
        elif len(money50) < 2 and second >= 20:
            money50.append(Money50(info("mx"), 0))
        # all about bullets
        for bullet in bullets:
            if bullet.y - 6 < man.hitbox[1] + man.hitbox[3] and bullet.y + 6 > man.hitbox[1]:
                if bullet.x - 6 < man.hitbox[0] + man.hitbox[2] and bullet.x > man.hitbox[0]:
                    man.hit_bullet()
        for bullet in bullets:
            if bullet.x < 520 and bullet.x > -20:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
        if dg_hit == False:
            sc = second
            if len(bullets) < 1 and second >= 1 and second < 12:
                bullets.append(Snaryad(info("rx"), info("ry"), info("rw")))
            elif len(bullets) < 2 and second >= 12 and second < 37:
                bullets.append(Snaryad(info("rx"), info("ry"), info("rw")))
            elif len(bullets) < 3 and second >= 37 and second < 56:
                bullets.append(Snaryad(info("rx"), info("ry"), info("rw")))
            elif len(bullets) < 4 and second >= 56 and second < 320:
                bullets.append(Snaryad(info("rx"), info("ry"), info("rw")))
            elif len(bullets) < 5 and second >= 320:
                bullets.append(Snaryad(info("rx"), info("ry"), info("rw")))
        else:
            if sc + 5 <= second:
                dg_hit = False

            # all about keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if man.x > man.vel:
                man.x -= man.vel
                man.left = True
                man.right = False
                man.stand = False

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if man.x < 500 - man.vel - man.width:
                man.x += man.vel
                man.left = False
                man.right = True
                man.stand = False
        else:
            man.left = False
            man.right = False
            man.stand = True

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if man.y > 37:
                man.y -= man.vel

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if man.y < 300:
                man.y += man.vel

        redrawGameWindow()
        # if gameover = True
    else:
        text_score = font.render(str(score), 0, (0, 0, 0))

        if deth == 0:
            deth_sound.play()
            deth += 1
            if score > int(best_score):
                best_score = str(score)
                data = open("Resources/best_score.txt", "w")
                data.write(str(score))
                data.close()
        text_best_score = font.render(str(best_score), 0, (0, 0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            gameover = False
            score = 0
            man.x = 220
            man.y = 130
            man.vel = 8
            second, ticks = 0, 0
            hpCount = 3
            five_ = False
            five_s_dollar_F = False
            dg_hit = False
            all_hp = [Hp(390, 7, False, 0), Hp(425, 7, False, 1), Hp(460, 7, False, 2)]
            bullets.clear()
            money100.clear()
            money50.clear()
            noDg.clear()
            plusiks.clear()
            speed_.clear()
            dollars.clear()
            revival_sound.play()
            deth = 0
        redrawGame_over()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
