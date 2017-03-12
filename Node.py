class Node:

	 def __init__(self, name, lat, lon):
	 	self.latitude = lat
	 	self.longitude = lon
	 	self.name = name
	 	self.next_node = None

	 def print_node(self):
	 	print("Name:", self.name)
	 	print("\tLatitude:", self.latitude)
	 	print("\tLongitude:", self.longitude)
	 	print("\n")