# Practice mutating lists
# The starter code will print the full list after each change

# Create a list called my_list
my_list = [10, 20, 30, 40, 50]
print(my_list)

# Assign the first list item the value 5
my_list[0] = 5
print(my_list)
# Assign the last list item the value 'dog'
last_item = len(my_list) - 1
my_list[last_item] = 'dog'
print(my_list)

# Remove the second item in the list
my_list.pop(1)
print(my_list)

# Add another item to the end of the list with value False
my_list.append(False)
print(my_list)
print("The number of items in the list is ",len(my_list))
# print the statement:
# "The number of items in the list is [X]"
# With the number of list items for [X] (so, 2 if the list has 2 items)
# You can use len(my_list) to get the number of elements in my_list
