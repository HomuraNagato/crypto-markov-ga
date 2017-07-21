#lecture-8.1.py
# inheritance

'''
Making a program that stores information about a users computer
'''

class Computer:
	def __init__(self, color, mnftr): #mnftr stands for manufacturer
		self.compu_color = color
		self.mnftr = mnftr
		self.os = ""

	def install_os(self, new_os):
		self.os = new_os

	def which_os(self):
		return self.os

c = Computer("black", "lenovo")
print c.which_os()

class Apple(Computer):
	# this class inherits from Computer because it is a Computer (where self might go!)
	# it is a specialized subset of Computer

	def __init__(self, color):
		# inherit Computer's init method, so call the init method of our superclass
		Computer.__init__(self, color, "Macintosh")
		self.ilife_installed = False

	def install_ilife(self):
		self.ilife_installed = True

my_computer = Apple("silver")
your_computer = Apple("white")
print my_computer.compu_color # silver
print your_computer.compu_color # white
print my_computer.mnftr # Macintosh
print my_computer.mnftr # Macintosh

my_computer.install_os("OS X")
print my_computer.os # OS X
print your_computer.os # ""
print my_computer.ilife_installed # False
my_computer.install_ilife()
print my_computer.ilife_installed # True