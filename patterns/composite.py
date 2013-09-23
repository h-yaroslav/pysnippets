#!/usr/bin/python

# Component
class Graphic:
	# Prints the graphic
	def printGraphic(self):
		pass
 
# Composite
class CompositeGraphic(Graphic):
 
	def __init__(self):
		# Collection of child graphics
		self.__mChildGraphics = []
 
	# Prints the graphic.
	def printGraphic(self):
		for graphic in self.__mChildGraphics:
			graphic.printGraphic()
 
	# Adds the graphic to the composition.
	def add(self, graphic):
		self.__mChildGraphics.append(graphic)
 
	# Removes the graphic from the composition.
	def remove(self, graphic):
		self.__mChildGraphics.remove(graphic)
 
# Leaf
class Ellipse(Graphic):
 
	def printGraphic(self):
		print "Ellipse"
 
def main():
	# Initialize four ellipses
	ellipse1 = Ellipse()
	ellipse2 = Ellipse()
	ellipse3 = Ellipse()
	ellipse4 = Ellipse()
 
	# Initialize three composite graphics
	graphic = CompositeGraphic()
	graphic1 = CompositeGraphic()
	graphic2 = CompositeGraphic()
 
	# Composes the graphics
	graphic1.add(ellipse1)
	graphic1.add(ellipse2)
	graphic1.add(ellipse3)
 
	graphic2.add(ellipse4)
 
	graphic.add(graphic1)
	graphic.add(graphic2)
 
	# Prints the complete graphic (four times the string "Ellipse")
	graphic.printGraphic()
 
if __name__ == "__main__":
	main()

