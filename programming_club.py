class Enemy:
	def __init__(self, name, size, color, damage):
		self.name = name
		self.size = size
		self.color = color
		self.damage = damage
	def do_damage(self):
		print self.name + " does " + str(self.damage) + " damage."

# Goblin is a subclass of Enemy -> so it has all of the functionality that Enemy has
class Goblin (Enemy):
	def steal(self):
		print self.name + " steals all of your gold."

class BadBaker (Enemy):
	def bake_cookies(self):
		print self.name + " bakes cookies, but they're raw!"
		
george = Goblin("George", 50, "green", 20)

george.do_damage()

xander = BadBaker("Xander", 30, "white", -20)

xander.bake_cookies()