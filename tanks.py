from scene import *
from math import pi, cos

class Tank (object):
	def __init__(self, position, color):
		self.position = position
		self.size = Size(100, 100)
		self.color = color
		self.arm_angle = 0
	def draw(self):
		translate(self.position.x, self.position.y)
		v = [(0, 30), (10, 30), (10, 70), (100, 30), (90, 70), (90, 30)]
		fill(self.color)
		triangle_strip(v)
		rect(20, 70, 60, 30)
		fill(0)
		ellipse(-15, 0, 30, 30)
		ellipse(75, 0, 30, 30)
		rect(0, 0, 90, 30)
		fill(0.6, 0.4, 0.8)
		for i in range(4):
			start = i/4.0
			ellipse(i*100/4.0, 0, 100.0/4, 100./4.)
		
class Tanks (Scene):
	def setup(self):
		self.tank1 = Tank(self.bounds.center(), (.06, .5, .77))
		def terrain_func(x):
			return (-cos(x*(pi*2.0))+1.0)/8.0 + 1.0/3.0
		self.terrain_func = terrain_func
		self.terraincolor = (.77, .27, .1)
	def draw(self):
		density = 100
		for i in range(density):
			start = i/float(density)
			end = (i+1.0)/float(density)
			smaller = min(self.terrain_func(start), self.terrain_func(end))
			rect(start*self.bounds.w, 0, self.bounds.w/float(density), smaller*self.bounds.h)	
			if self.terrain_func(start) < self.terrain_func(end):
				v = [(start*self.bounds.w, self.terrain_func(start)*self.bounds.h), (end*self.bounds.w, self.bounds.h*self.terrain_func(start)), (end*self.bounds.w, self.bounds.h*self.terrain_func(end))]
			else:
				v = [(start*self.bounds.w, self.terrain_func(end)*self.bounds.h), (end*self.bounds.w, self.bounds.h*self.terrain_func(end)), (start*self.bounds.w, self.bounds.h*self.terrain_func(start))]
			triangle_strip(v)
		self.tank1.draw()
	def touch_began(self, touch):
		pass

game = Tanks()
run(game, show_fps = True)
