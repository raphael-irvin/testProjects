class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        cur = self.head  #self.head is like the arrow/pointer that's going to pierce/traverse through the llist
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        cur = self.head
        total_length = 0
        while cur.next != None:
            total_length += 1
            cur = cur.next
        return total_length
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print (elems)

my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)

print(f'The length of the linked list is {my_list.length()}')
my_list.display()