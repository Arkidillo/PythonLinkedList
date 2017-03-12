import Node

class List:
	__head = None

	def print_list(self):
		curr_node = self.__head
		i = 0

		print("PRINTING LIST:  \n")
		while curr_node is not None:
			print("Index: ", i)
			print("Data: ", curr_node.data)
			print("\n")

			curr_node = curr_node.next_node
			i += 1

	def insert_node(self, data):	# Inserts a node at the head of the list
		new_node = Node.Node(data)

		new_node.next_node = self.__head
		self.__head = new_node