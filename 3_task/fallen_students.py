import unittest


def fallen_student(A, Na, B, Nb):
    fallen_list = []
    
    for i in range(0, Na):
        if A[i] not in B[i]:
            fallen_list.append(A[i])
    
    return fallen_list


class TestFindSlidings(unittest.TestCase):
    def test_list_1(self):
        A = ['Иванов', 'Петров', 'Сидоров', 'Мариванна']
        B = ['Зумеров', 'Петров', 'Скуффов', 'Скибиди', 'Эшкере']
        Na = len(A)
        Nb = len(B)

        C = ['Иванов', 'Сидоров', 'Мариванна']

        self.assertEqual(C, fallen_student(A, Na, B, Nb))

    def test_list_2(self):
        A = []
        B = ['Зумеров', 'Петров', 'Скуффов', 'Скибиди', 'Эшкере']
        Na = len(A)
        Nb = len(B)

        C = []

        self.assertEqual(C, fallen_student(A, Na, B, Nb))

if __name__ == '__main__':
    unittest.main()