class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def Delete_first(self):
        if self.head:
            self.head = self.head.next
        else:
            print("Linked list is empty. Cannot delete.")
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def search(self, key):
        current = self.head
        position = 1

        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1

        return -1
    def print_reverse(self, node=None):
        if node is None:
            node = self.head
        
        if node is None:
            return
        
        self.print_reverse(node.next)
        print(node.data, end=" -> ")


my_list = LinkedList()


my_list.add_at_beginning(3)
my_list.add_at_beginning(7)
my_list.add_at_beginning(1)
my_list.add_at_beginning(5)
my_list.add_at_beginning(10)


my_list.display()




my_list.Delete_first()

my_list.display()

p=my_list.search(7)
print("Element found in ",p)


my_list.print_reverse()