class Node:
	 next_node = None
	 latitude = None
	 longitude = None
	 name = None

	 def __init__(self, name, lat, lon):
	 	self.latitude = lat
	 	self.longitude = lon
	 	self.name = name

	 def print_node(self):
	 	print("Name:", self.name)
	 	print("\tLatitude:", self.latitude)
	 	print("\tLongitude:", self.longitude)
	 	print("\n")