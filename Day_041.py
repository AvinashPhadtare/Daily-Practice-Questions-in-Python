# QUESTION:-
# Implement a singly linked list with the following operations:
#
# 1. append(val)  -> Add a node at the end
# 2. prepend(val) -> Add a node at the front
# 3. delete(val)  -> Remove the first occurrence of val
# 4. reverse()    -> Reverse the linked list IN PLACE
#                    (do not create a new list)
# 5. to_list()   -> Convert linked list to a Python list
# 6. __len__     -> Return the number of nodes
# 7. __str__     -> Return the linked list as a string
#
# Build the linked list using a Node class and a LinkedList class.
#
# Then:
# Create a list [1, 2, 3, 4, 5]
# Reverse it
# Delete 3
# Prepend 0
# Print the result.

# Solution:- 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            return

        # Start from the first node
        current = self.head

        # Move until the last node
        while current.next is not None:
            current = current.next

        # Connect last node to new node
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)

        # New node points to the current first node
        new_node.next = self.head

        # New node becomes the first node
        self.head = new_node

    def delete(self, value):
        # Empty list
        if self.head is None:
            return

        # If the first node contains the value
        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head

        # Find the node before the node to delete
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return

            current = current.next

    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next

            current.next = previous

            previous = current
            current = next_node

        self.head = previous

    def to_list(self):
        result = []
        current = self.head

        while current is not None:
            result.append(current.value)
            current = current.next

        return result

    def __len__(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    def __str__(self):
        return " -> ".join(str(value) for value in self.to_list())


# -------------------------
# Example Usage 
# -------------------------

linked_list = LinkedList()

# Create [1, 2, 3, 4, 5]
for value in [1, 2, 3, 4, 5]:
    linked_list.append(value)

# Reverse
linked_list.reverse()

# Delete 3
linked_list.delete(3)

# Add 0 at the front
linked_list.prepend(0)

# Print result
print(linked_list)

# Print length
print("Length:", len(linked_list))
