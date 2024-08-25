import unittest

def fallen_student(A, Na, B, Nb):
    fallen_list = []
    



class TestFindSlidings(unittest.TestCase):
    def test_empty_list(self):
        A = ['Иванов', 'Петров', 'Сидоров', 'Мариванна']
        Na = len(A)
        
        B = ['Зумеров', 'Петров', 'Скуффов', 'Скибиди', 'Эшкере']
        Nb = len(B)

        C = ['Иванов', 'Сидоров', 'Мариванна']

        self.assertEqual([], fallen_student([]))

if __name__ == '__main__':
    unittest.main()