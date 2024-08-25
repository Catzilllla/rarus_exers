class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.lenght = 0
        
        # ссылка на 1ый узел списка
        self.head = None

    def node_append(self, value):
        new_node = Node(value)
        self.head = new_node


    def print_data_list(self):
        while :
            pass


linked_list_obg = LinkedList()

for data_in_list in range(0, 10):
    linked_list_obg.node_append(data_in_list)
    print(data_in_list)