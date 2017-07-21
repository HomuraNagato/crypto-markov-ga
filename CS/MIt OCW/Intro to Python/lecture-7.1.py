#lecture-7.1.py

'''
we can import modules with the import commange
'''

from graphics import * # I think the * is importing all

class Wheel():
	def __init__(self, center, wheel_radius, tire_radius):
		self.tire_circle = Circle(center, tire_radius)  # Where does Circle command come from?
		self.wheel_circle = Circle(center, wheel_radius)

	def draw(self, win): #what is win here? window?
		self.tire_circle.draw(win)
		self.wheel_circle.draw(win)

	def move(self, dx, dy):
		self.tire_circle.move(dx, dy)
		self.wheel_circle.move(dx, dy)

	def set_color(self, wheel_color, tire_color):
		self.tire_circle.setFill(tire_color)
		self.wheel_circle.setFill(wheel_color)

	def undraw(self):
		self.tire_circle.undraw()
		self.wheel_circle.undraw()

	def get_size(self):
		return self.tire_circle.getRadius()

	def get_center(self):
		return self.tire_circle.getCenter()


def main():
	# create a window with width and height of 700 and 500
	new_win = GraphWin('Wheel', 700, 500)

	wheel_center = Point(200, 200)
	tire_radius = 100

	# make a wheel_object
	new_wheel = Wheel(wheel_center, 0.6*tire_radius, tire_radius)

	#set it's wheel_colorn
	new_wheel.set_color('red', 'black')

	# and finally draw it
	new_wheel.draw(new_win)

	# run the window loop (must be the *last* line in your code)
	new_win.mainloop()

main()