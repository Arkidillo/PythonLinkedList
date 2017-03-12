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

			curr_node = curr_node.next_node
			i += 1

	def insert_node(self, data):
		new_node = Node.Node(data)

		if self.__head is None:
			self.__head = new_node