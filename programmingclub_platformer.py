# coding: utf-8
from scene import *

default_walking_speed = 5
default_running_speed = 8

class Character:
	def __init__(self, position, size, sprite):
		self.position = position
		self.size = size
		self.sprite = sprite
		self.vx = 0
		self.vy = 0
	def move(self, terrain, direction, speed):
		pass
	def walk(self, terrain, direction):
		self.move(terrain, direction, default_walking_speed)	
	def run(self, direction):
		self.move(terrain, direction, default_running_speed)
	def jump(self):
		pass
	def draw(self):
		fill(.55, .21, 1.0)
		rect(self.position.x, self.position.y, self.size.w, self.size.h)
		
class Player (Character):
	pass

class Enemy (Character):
	pass
	
class Terrain:
	def __init__(self, hitbox):
		self.hitbox = hitbox
	def can_walk(self, position, direction):
		# position is a Point
		# direction is a number of pixels i'm trying to walk
		
		# returns a number representing the number of pixels you can walk before you run into something
		pass
	def can_jump(self, position, distance):
		# position is a Point
		# distance is the number of pixels i'm trying to jump
		
		# returns a number representing the number of pixels you can travel upwards before you run into something
		pass
	def can_fall(self, position, distance):
		# position is a Point
		# distance is the number of pixels gravity would cause me to fall
		
		# returns a number representing the number of pixels you can travel downwards before you run into something
		pass
		
class FloweryTerrain (Terrain):
	# whoever the hell wanted flowers can draw a sprite with flowers for this one
	pass
	
# i've written the Platform subclass of Terrain here. it would be fully functional if can_walk, can_jump, and can_stand are defined in the Terrain class.
class Platform (Terrain):
	def __init__(self, x, y, w, h, sprite = None):
		def hitbox_func(point):
			# the Rect class allows usage of the "in" keyword to determine whether a point is within a given Rect.
			# syntax:
			# Point in Rect
			# this returns True if the Point is within the bounds of the Rect
			return point in Rect(x, y, w, h)
		
		# i can call the __init__ function of the Terrain class directly if i've overriden it but still want its functionality. in this case, i still need the self.hitbox attribute defined, but i don't want to just define it myself in case i add something to Terrain's __init__ later.
		Terrain.__init__(self, hitbox_func)
		
		# my __init__ method took x, y, w, and h as parameters. i would like to keep these values just as they are, so i can use them in the draw method. right now, they're just local variables, and they will dissapear from my program as soon as the __init__ method returns (or ends.) since i want to keep them, i define them as attributes of myself:
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		
		# i also defined sprite as a default parameter to the __init__ method (sprite = None). this means that a user of this class could write:
		# Platform(0, 0, 300, 30)
		# notice that the fifth parameter, sprite, is missing. this will still compile fine, but in the body of my __init__ function, the sprite variable will be set to None. in this case, i just set my sprite attribute to whatever it may be and move on to handle this case in the draw method.
		self.sprite = sprite
	def draw(self):
		# here, i test if the sprite is None:
		if self.sprite == None:
			# if there was no sprite given, just replace it with a white rectangle
			fill(1,1,1)
			rect(self.x, self.y, self.w, self.h)
		else:
			# if there is a sprite, draw it
			image(self.sprite, x = self.x, y = self.y, w = self.w, h = self.h)

class Game (Scene):
	def setup(self):
		self.character = Character(self.bounds.center(), Size(50, 100), None)
	def draw(self):
		background(.25, 1.0, .32)
		self.character.draw()
		
platformer = Game()
run(platformer)
