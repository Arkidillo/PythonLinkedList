import Node

class List:

	def __init__(self):
		self.head = None

	def print_list(self): 	# Prints the entirety of the list
		curr_node = self.head
		i = 0


		print("\nPRINTING LIST:  \n")

		while curr_node is not None:	
			print("Index: ", i)
			curr_node.print_node()

			curr_node = curr_node.next_node
			i += 1

	def add_node(self, name, lat, lon):	# Inserts a node at the head of the list
		new_node = Node.Node(name, lat, lon)

		new_node.next_node = self.head
		self.head = new_node

	def append_node(self, name, lat, lon):	# Inserts a node at the end of the list, returns index it was added at
		new_node = Node.Node(name, lat, lon)
		curr_node = self.head

		if(self.head is None):
			self.head = new_node

		i = 1
		while(curr_node.next_node is not None):	# Advance to the end of the list
			curr_node = curr_node.next_node
			i += 1

		curr_node.next_node = new_node

		return i

	def add_sorted_node(self, name, lat, lon): # Inserts a node, sorted by its longitude (asc. order),  returns index it was added at
		new_node = Node.Node(name, lat, lon)
		curr_node = self.head

		if(curr_node is None):				# Case where head is None
			self.head = new_node
			return 0

		if(curr_node.longitude >= lon):		# Case where the new_node is sorted to the beginning of the list (need to update head in this case)
			new_node.next_node = self.head
			self.head = new_node
			return 0


		i = 1
		while(curr_node.next_node is not None):				# Advance to the end of the list
			if (curr_node.next_node.longitude >= lon):

				temp_next_node = curr_node.next_node		# Node stores the node after the place we want to insert the new_node
				curr_node.next_node = new_node				# Sets the previous node's next pointer to the new node
				new_node.next_node = temp_next_node   		# Sets the new node's next pointer to the node that used to be after curr_node
				return i


			curr_node = curr_node.next_node
			i += 1

		curr_node.next_node = new_node						# If the program has not returned yet, add the new node at the end

		return i

	def clear_list(self): 	# Will remove all nodes from the list
		self.head = None 	# Because of garbage collection, if we set head to None, there will be no pointers to the stack, thus all the nodes will be removed for us.

