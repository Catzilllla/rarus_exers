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

    def pop(self):
        if self.head == None:
            return None
        
        popped_node = self.head
        self.head = self.head.next_address
        return popped_node.data

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False


def is_valid_bracket(arifm_expression):

    linked_list = LinkedList()

    for symb in arifm_expression:
        if symb == '(':
            linked_list.push(symb)
        elif symb == ')':
            if linked_list.is_empty():  # if empty =  false
                return False
            linked_list.pop()

    return linked_list.is_empty()  # if empty = True


class TestNode(unittest.TestCase):
    def test_valid_expressions(self):
        self.assertTrue(is_valid_bracket("(a + b) * (c - d)"))
        self.assertTrue(is_valid_bracket("((a + b) * c)"))
        self.assertTrue(is_valid_bracket("((a + b))"))

    def test_invalid_expressions(self):
        self.assertFalse(is_valid_bracket("(a + b * (c - d)"))
        self.assertFalse(is_valid_bracket("a + b) * c"))
        self.assertFalse(is_valid_bracket(")a + b) * c"))
        self.assertFalse(is_valid_bracket(")("))
        self.assertFalse(is_valid_bracket("((((())))"))


if __name__ == '__main__':
    unittest.main()