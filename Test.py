import List
import Node

def check_index(ret_val, correct_val) :	# Function to check if the functions I call in the test are returning the correct indicies
	if ret_val == correct_val:
		print("Index check passed.")
	else :
		print("ERROR: Index check FAILED")

list = List.List()

# Testing add_node
list.add_node("SEAS GWU", 10.5, 100.1)
list.add_node("Eiffel Tower", 11.9, 100.0)
list.print_list()

# Testing clear_list
list.clear_list()
list.print_list()

# Testing add_sorted_node
check_index(list.add_sorted_node("New location 1", 10.7, 50.5), 0)
check_index(list.add_sorted_node("New location 2", 10.8, 100), 1)
check_index(list.add_sorted_node("New location 3", 20, 75), 1)

# Testing append_node
check_index(list.append_node("New Location 4", 20, 74), 3) 
list.print_list()