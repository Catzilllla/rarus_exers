# rarus_exers

### 1 ###
Есть односвязный список символов. Вывести его элементы задом наперед за один проход
```
var_1:
characters = ['a', 'b', 'c']
print(characters[::-1])

var_2:
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

```

### 2 ###
Задача 1. Есть строка арифметического выражения, в которой содержатся открывающие “(” и закрывающие скобки “)”. Необходимо написать функцию, которая проверит корректность расстановки скобок. При этом скобки - проверяется только последовательность расставления скобок, а операторы и операнды при проверке не учитываются
```

```

### 3 ###
Задача 2. В учебном заведении в конце каждого года обучения подводят итоги. В частности, составляют списки ребят, которые учились в этом году на отлично.
Нужно написать функцию, которая поможет преподавателям вычислить перечень ребят, которые “скатились” - в прошлом году были отличниками, а в текущем не попали в этот список. Запрещено использовать предоставляемые языком программирования функции групповой обработки элементов массивов
(например, сортировка, объединение, копирование).

Входные параметры:
- A - отличники прошлого года;
- Nа - количество элементов в массиве A;
- B - отличники текущего года;
- Nb - количество элементов в массиве B.
Результат функции:
- Массив “скатившихся” ребят.

```

```