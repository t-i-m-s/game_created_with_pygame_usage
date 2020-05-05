import pygame
import math
import random

pygame.init()
win = pygame.display.set_mode((450,338))
pygame.display.set_caption("Tank Battles!!!")

jump = -4
jump_event = False
falling_event = False
fall = 0

person_right = [pygame.image.load('tank_right.png'),pygame.image.load('tank_right_up.png')]
person_left = [pygame.image.load('tank_left.png'),pygame.image.load('tank_left_up.png')]

lift = 0# пушка
width = 40#38
length = 60
x = 250
y = 220
side = 1# в какую сторону смотрит
speed = 10# скорость передвижения гг
speed_45 = 0# для траектория снаряда (для косинуса)
step = 470# респ противника
process = 0 # счетчик кадров взрыва
exp_count = [0] # кол-во умерших противников

magazine = []
magazine_45 = []
enemys_magazine = []
enemies = []
explosioned = []
falling_progress = [5,10,20,50,100]

class Ammo():
	def __init__(self, x, y, width, length, color, side):
		self.x = x
		self.y = y
		self.width = width
		self.length = length
		self.color = color
		self.speed = side*10
	def moving(self, win):
		pygame.draw.rect(win,self.color,(self.x, self.y, self.width, self.length))
class Enemies():
	def __init__(self, x, y, image, step, rang):
		self.x = x
		self.y = y
		self.image = image
		self.step = step
		self.rang = rang
	def moving(self, win):
		win.blit(self.image,(self.x,self.y))
def easy():
	for bullet in magazine:
		if bullet.x < 500 and bullet.x > 0:
			bullet.x += bullet.speed
		else:
	 		magazine.remove(bullet)

	for bullet in magazine:
		bullet.moving(win)

	for bullet in magazine_45:
		if bullet.x < 500 and bullet.x > 0 and bullet.y > 0 and bullet.y < 260:
			if bullet.speed < 0:
				bullet.x += bullet.speed
				bullet.y += bullet.speed*math.cos(speed_45)
			else:
				bullet.x += bullet.speed
				bullet.y += -bullet.speed*math.cos(speed_45)
		else:
	 		magazine_45.remove(bullet)
	for bullet in magazine_45:
		bullet.moving(win)

	for enemy in enemies:
		enemy.x -= enemy.step
	for enemy in enemies:
		enemy.moving(win)
	if len(enemies) > 0:
		if len(enemys_magazine) < 1:
			if y > 200 and y < 225:
				enemys_magazine.append(Ammo(enemies[0].x,enemies[0].y+23,7,2,(255,0,0),-1))

	if len(enemys_magazine) > 0:
		for bullet in enemys_magazine:
			if bullet.x < 500 and bullet.x > 0:
				bullet.x += bullet.speed/2
			else:
		 		enemys_magazine.remove(bullet)
	for bullet in enemys_magazine:
		bullet.moving(win)
	#pygame.draw.rect(win, (128,128,128), (100,190,50,7))
# def falling():
# 	falling_event = True
# 	if falling_progress[fall] < 220 - y:
# 		y += falling_progress[fall]
# 		fall += 1
# 	else:
# 		y = 220
# 		fall = 0
# 		falling_event = False
#
#
# def mainheroes_collision():
# 	if x > 45 and x < 150:
# 		if jump < 0 and math.fabs(jump**3) > y - 190:
# 			y -= y - 190
# 			jump_event = False
# 			jump = -4
# 			falling()

def collicion():
	if magazine[0].x >= enemies[0].x and magazine[0].x <= enemies[0].x + 60:
		if magazine[0].y >= 235 and magazine[0].y <= 250:
			explosioned.append(enemies[0].x)
			explosioned.append(enemies[0].y)
			explosioned.append(enemies[0].rang)
			enemies.remove(enemies[0])
			magazine.remove(magazine[0])
			exp_count[0] += 1
def collicion_45():
	if magazine_45[0].x >= enemies[0].x and magazine_45[0].x <= enemies[0].x + 60:
		if magazine_45[0].y >= 235 and magazine_45[0].y <= 250:
			explosioned.append(enemies[0].x)
			explosioned.append(enemies[0].y)
			explosioned.append(enemies[0].rang)
			enemies.remove(enemies[0])
			magazine_45.remove(magazine_45[0])
			exp_count[0] += 1
def off_screen():
	if enemies[0].x < -40:
		enemies.remove(enemies[0])

run = True
while run:
	pygame.time.delay(45)
	win.blit(pygame.image.load('wall.jpg'),(0,0))
	#win.fill((255,0,0))

	if side == 1:
		win.blit(person_right[lift], (x,y))
	if side == -1:
		win.blit(person_left[lift], (x,y))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				run = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and x > 0 and falling_event == False:
		if y < 177 and y >= 170 and x < 155:
			print("catch - 1")
			jump_event = False
			jump = -4
			falling_event = True
		else:
			x -= speed
			side = -1
	if keys[pygame.K_RIGHT] and x < 450 - width and falling_event == False:
		if y < 177 and y >= 170 and x > 37:
			print("catch")
			jump_event = False
			jump = -4
			falling_event = True
		else:
			x += speed
			side = 1
	if keys[pygame.K_SPACE] and falling_event == False:
		jump_event = True
	if jump_event:
		y += jump**3
		jump += 1
		if jump == 5:
			jump_event = False
			jump = -4

	if keys[pygame.K_UP]:
		if lift < 1:
			lift += 1
	if keys[pygame.K_DOWN]:
		if lift > 0:
			lift -= 1
	if keys[pygame.K_f]:
		if len(magazine) < 1 and len(magazine_45) < 1:
			if side == 1:
				if lift == 0:
					magazine.append(Ammo(x+60,y+23,7,2,(0,0,0),side))
				if lift == 1:
					magazine_45.append(Ammo(x+50,y+6,7,2,(0,0,0),side))
			else:
				if lift == 0:
					magazine.append(Ammo(x,y+23,7,2,(0,0,0),side))
				if lift == 1:
					magazine_45.append(Ammo(x+10,y+6,7,2,(0,0,0),side))

	if len(enemies) == 0:
		if exp_count[0] < 5:
			enemies.append(Enemies(470,220,person_left[0],3,1))
		else:
			enemies.append(Enemies(470,227,pygame.image.load('boss_left.png'),5,2))
			exp_count[0] = 0

	easy()
	if len(magazine) > 0:
		collicion()
	if len(magazine_45) > 0:
		collicion_45()

	if len(magazine_45) > 0:
		if speed_45 < math.pi:
			speed_45 += 0.1
	else:
		speed_45 = 0
	if len(enemies) > 0:
		off_screen()

	if len(explosioned) > 0:
		if process < 3:
			if explosioned[2] == 1:
				win.blit(pygame.image.load('tank_left_exp.png'), (explosioned[0],explosioned[1]))
			if explosioned[2] == 2:
				win.blit(pygame.image.load('boss_left_exp.png'), (explosioned[0]-10,explosioned[1]-45))
			process += 1
		else:
			process = 0
			explosioned.remove(explosioned[2])
			explosioned.remove(explosioned[1])
			explosioned.remove(explosioned[0])
	pygame.draw.rect(win, (128,128,128), (100,190,50,7))

	if x > 37 and x < 155:
		if jump_event:
			if jump < 0 and math.fabs(jump**3) > y - 177:
				y -= y - 177
				jump_event = False
				jump = -4
				falling_event = True
	if y < 170:
		if x > 37 and x < 155:
			jump_event = False
			jump = -4
			if falling_progress[fall] < 190 - y:
				y += falling_progress[fall]
				fall += 1
			else:
				y = 190
				fall = 0
				falling_event = False

	if falling_event:
		if falling_progress[fall] < 220 - y:
			y += falling_progress[fall]
			fall += 1
		else:
			y = 220
			fall = 0
			falling_event = False

	pygame.display.update()

pygame.quit()
