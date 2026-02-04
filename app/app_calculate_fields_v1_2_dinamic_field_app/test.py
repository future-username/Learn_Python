import unittest
import tkinter as tk

from .calculator import NumberValidator, NumberNormalizer, EntryNormalizer, CalculatorApp


class TestNumberValidator(unittest.TestCase):
    def test_is_number_valid(self):
        self.assertTrue(NumberValidator.is_number("10"))
        self.assertTrue(NumberValidator.is_number("-5"))
        self.assertTrue(NumberValidator.is_number("3.14"))
        self.assertTrue(NumberValidator.is_number("0"))
        self.assertFalse(NumberValidator.is_number("abc"))
        self.assertFalse(NumberValidator.is_number(""))

    def test_is_int(self):
        self.assertTrue(NumberValidator.is_int("42"))
        self.assertFalse(NumberValidator.is_int("4.2"))

    def test_is_float(self):
        self.assertTrue(NumberValidator.is_float("3.14"))
        self.assertTrue(NumberValidator.is_float("-0.001"))
        self.assertFalse(NumberValidator.is_float("abc"))

    def test_positive_negative(self):
        self.assertTrue(NumberValidator.is_int_positive("5"))
        self.assertFalse(NumberValidator.is_int_positive("-5"))
        self.assertTrue(NumberValidator.is_float_negative("-1.5"))
        self.assertFalse(NumberValidator.is_float_negative("2.7"))


class TestNumberNormalizer(unittest.TestCase):
    def test_normalize_number(self):
        self.assertEqual(NumberNormalizer.normalize_number("  3,2 "), "3.2")
        self.assertEqual(NumberNormalizer.normalize_number(" 15 "), "15")
        self.assertEqual(NumberNormalizer.normalize_number(""), "0")
        self.assertEqual(NumberNormalizer.normalize_number("   "), "0")


class TestEntryNormalizer(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.entry = tk.Entry(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_normalize_entries(self):
        self.entry.insert(0, "  3,2  ")
        normalized = EntryNormalizer.normalize_entries(self.entry)
        self.assertEqual(normalized, "3.2")


class TestCalculatorApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = CalculatorApp(self.root, ammount=3)  # три поля для теста

    def tearDown(self):
        self.root.destroy()

    def test_calculate_plus_valid(self):
        entries = ["5", "10.5", "4.5"]
        for entry, val in zip(self.app.entry_fields, entries):
            entry.insert(0, val)
        self.app.calculate_plus()
        result = self.app.result_plus.get()
        self.assertEqual(result, "20")  # 5 + 10.5 + 4.5 = 20.0

    def test_calculate_plus_invalid(self):
        entries = ["5", "abc", "10"]
        for entry, val in zip(self.app.entry_fields, entries):
            entry.insert(0, val)
        self.app.calculate_plus()
        # Ошибка должна быть отображена в label_error
        self.assertIn("не является числом", self.app.label_error.cget("text"))


if __name__ == "__main__":
    unittest.main()
