import List
import Node

list = List.List()
list.add_node("SEAS GWU", 10.5, 100.1)
list.add_node("Eiffel Tower", 11.9, 100.0)
list.print_list()
list.clear_list()
list.print_list()
list.add_sorted_node("New location 1", 10.7, 50.5)
list.add_sorted_node("New location 2", 10.8, 100)
list.add_sorted_node("New location 3", 20, 75)
list.print_list()