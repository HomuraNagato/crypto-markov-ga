#lecture-6.1.py

'''
A class allows us to create objects that contain multiple values and parameters.
When we begin a new class, we require def __init__(self, [more values]):

'''

class Point:

	def __init__(self, x, y):
		# this is the initialization method called when we create a point.
		# it takes 2 arguments, x and y, which must be numbers

		self.x = x
		self.y = y

	def __str__(self):
		# the point's string method, when a print on an object is called, the __str__method is called
		return "A Point at coordinates " + str((self.x, self.y))

	def move_point(self, delta_x, delta_y):
		# moves this Point delta_x units in the x-direction
		# and delta_y in the y x-direction

		self.x += delta_x
		self.y += delta_y
		return (self.x, self.y)

	def move_point_incorrect(self, delta_x, delta_y):
		# an incorrect implementation of move_point, because we don't change
		# the _attributes_ self.x and self.y;, instead we only change the local variable x and y
		x = self.x + delta_x
		y = self.y + delta_y
		return (x, y)

myPoint = Point(7, 4)
print "After initializing the Point:", myPoint # will also print from _str__ method

print myPoint.move_point_incorrect(-1, 5) # this prints a one time change, but isn't stored
print "After moving the point incorrectly:", myPoint # changes local variables so doesn't work
print myPoint.move_point(-1, 5)
print "After moving the point correctly:", myPoint # changes object's attributes so works!