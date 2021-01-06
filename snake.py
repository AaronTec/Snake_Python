import pygame as py
import sys
from pygame.locals import *
import random

clock = py.time.Clock()

py.init()

py.display.set_caption('SNAKE by Aaron')

WINDOW_SIZE = (505,505)
BLUE = (0,0,255)

screen = py.display.set_mode((WINDOW_SIZE))


snakeplayer = py.Rect(50,50,15,15)

food = py.Rect(250,250,15,15)





def walldetection():
	if snakeplayer.right >= 505 or snakeplayer.left <= 0:
		py.quit()
		sys.exit()
	if snakeplayer.bottom >= 505 or snakeplayer.top <= 0:	
		py.quit()
		sys.exit()


class Snake(object):
	def __init__(self, x,y):
		self.player_location = [x,y]
		self.moving_up = False
		self.moving_down = True
		self.moving_right = False
		self.moving_left = False
		self.grow = False
		self.move = 15
		self.tracker_loc = []
		self.sense = 5



	def draw(self,screen):

# Snake hitting body detection_______________

# When the snake moves the head of the snake records its location in self.tracker_loc
# each location coodinates creates a rect (the snakes body) 
# the self.tracer_loc list is only allowed to be a certain size. to increase the size
# of self.tracker_loc (the snake's body) self.sense 's value needs to be increased.
		try:
			dect = self.tracker_loc.index((self.player_location[0],self.player_location[1]))

			if dect >= 0:
				py.quit()
				sys.exit()
		except:
			pass
#______________________________________________       

		self.tracker_loc.append((self.player_location[0],self.player_location[1]))

		if len(self.tracker_loc) >= self.sense: # this makes self.tracker_loc(the body) as long as the trail. by deleteing at index(0)
			self.tracker_loc.pop(0)

#If self Grow the snake will enlarge__________________________

		if self.grow:
			self.sense += 1
#_____________________________________________________________


		for i in self.tracker_loc: # Creating a Rect at each recorded coordinate self.tracker_loc
			snakeplayer.x = i[0]
			snakeplayer.y = i[1]
			py.draw.rect(screen,(70,194,88),snakeplayer)

#Moving the snake_____________________________________________
		if self.moving_left:
			self.player_location[0] -= self.move
					
		if self.moving_right:
			self.player_location[0] += self.move

		if self.moving_up:
			self.player_location[1] -= self.move

		if self.moving_down:
			self.player_location[1] += self.move

	def eating(self):
		py.draw.rect(screen,(252,186,3),food)
		if snakeplayer.colliderect(food):
			self.sense += 3
			food.x = random.randint(1,495)
			food.y = random.randint(1,495)

		


player = Snake(50,50)

while True:
	screen.fill((0,0,0))

	player.draw(screen)

	walldetection()
	player.eating()
	

	for event in py.event.get():
		if event.type == QUIT:
			py.quit()
			sys.exit()

		if event.type == KEYDOWN:
			if event.key == K_a:
				player.moving_left = True
			if event.key == K_d:
				player.moving_right = True
			if event.key == K_w:
				player.moving_up = True
			if event.key == K_s:
				player.moving_down = True
			if event.key == K_SPACE:
				player.grow = True

		if event.type == KEYUP:
			if event.key == K_SPACE:
				player.grow = False

		if event.type == KEYDOWN:
			if event.key == K_d or event.key == K_s or event.key == K_w :
				player.moving_left = False
			if event.key == K_a or event.key == K_s or event.key == K_w:
				player.moving_right = False
			if event.key == K_a or event.key == K_s or event.key == K_d:
				player.moving_up = False
			if event.key == K_a or event.key == K_w or event.key == K_d:
					player.moving_down = False


	py.display.update()
	clock.tick(15)
