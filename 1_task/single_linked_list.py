import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next_address = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next_address = self.head
        self.head = new_node


def print_backward(mylinkedList):
        actual_output = []
        tail = mylinkedList.head
        
        if tail == None:
            return
        else:
            while tail:
                actual_output.append(tail.data)
                tail = tail.next_address

        return actual_output


class TestNode(unittest.TestCase):
    def test_print_backward(self):

        ll_node = LinkedList()

        for data_symb in range(0, 10):
            ll_node.push(data_symb)

        expected_output = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(expected_output, print_backward(ll_node))

if __name__ == '__main__':
    unittest.main()