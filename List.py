import Node

class List:
	__head = None

	def print_list(self):
		curr_node = self.__head
		i = 0

		print("PRINTING LIST:  \n")
		while curr_node is not None:
			print("Index: ", i)
			curr_node.print_node()

			curr_node = curr_node.next_node
			i += 1

	def add_node(self, name, lat, lon):	# Inserts a node at the head of the list
		new_node = Node.Node(name, lat, lon)

		new_node.next_node = self.__head
		self.__head = new_node