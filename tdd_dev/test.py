# tests.py (Первый этап: пишем падающий тест)
import unittest


# main.py (Второй этап: минимальная реализация)
def is_even(num):
    return num % 2 == 0


# tests.py (Третий этап: добавляем больше тестов)
class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(4))

    def test_odd_number(self):
        self.assertFalse(is_even(5))

    def test_zero(self):
        self.assertTrue(is_even(0))

    def test_negative_even(self):
        self.assertTrue(is_even(-2))

    def test_negative_odd(self):
        self.assertFalse(is_even(-3))


# if __name__ == '__main__':
#     unittest.main()


# class TestIsEven(unittest.TestCase):
#     def test_even_number(self):
#         self.assertTrue(is_even(4))  # Тест упадёт здесь


if __name__ == '__main__':
    unittest.main()
