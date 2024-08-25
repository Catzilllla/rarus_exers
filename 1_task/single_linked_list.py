import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next_address = None
    
    def append_head(self, next_node_value):
        head = Node(data=next_node_value)
        buffer = self
        while buffer.next_address:
            buffer = buffer.next_address
        buffer.next_address = head


def print_backward(mylinkedList, callback):
    if mylinkedList == None:
        return
    
    head = mylinkedList
    tail = mylinkedList.next_address

    print_backward(tail, callback)
    callback(head.data)


class TestNode(unittest.TestCase):
    def test_print_backward(self):
        node = Node(-1)

        for data_symb in range(0, 10):
            node.append_head(data_symb)

        expected_output = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
        actual_output = []

        def callback(data):
            actual_output.append(data)

        print_backward(node, callback)

        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()