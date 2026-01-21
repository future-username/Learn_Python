import unittest
from tkinter import Tk, Entry, END
from app.app_calculate_fields_v1_static_app.main import NumberValidator, NumberNormalizer, EntryNormalizer


class TestNumberValidator(unittest.TestCase):

    def test_is_int_positive(self):
        self.assertTrue(NumberValidator.is_int_positive("10"))
        self.assertFalse(NumberValidator.is_int_positive("-5"))
        self.assertFalse(NumberValidator.is_int_positive("0"))
        self.assertFalse(NumberValidator.is_int_positive("10.5"))
        self.assertFalse(NumberValidator.is_int_positive("abc"))

    def test_is_int_negative(self):
        self.assertTrue(NumberValidator.is_int_negative("-10"))
        self.assertFalse(NumberValidator.is_int_negative("5"))
        self.assertFalse(NumberValidator.is_int_negative("0"))
        self.assertFalse(NumberValidator.is_int_negative("-10.5"))
        self.assertFalse(NumberValidator.is_int_negative("abc"))

    def test_is_int(self):
        self.assertTrue(NumberValidator.is_int("10"))
        self.assertTrue(NumberValidator.is_int("-10"))
        self.assertTrue(NumberValidator.is_int("0"))
        self.assertFalse(NumberValidator.is_int("10.5"))
        self.assertFalse(NumberValidator.is_int("abc"))

    def test_is_float_positive(self):
        self.assertTrue(NumberValidator.is_float_positive("10.5"))
        self.assertFalse(NumberValidator.is_float_positive("-5.5"))
        self.assertFalse(NumberValidator.is_float_positive("0.0"))
        self.assertFalse(NumberValidator.is_float_positive("10"))
        self.assertFalse(NumberValidator.is_float_positive("abc"))

    def test_is_float_negative(self):
        self.assertTrue(NumberValidator.is_float_negative("-10.5"))
        self.assertFalse(NumberValidator.is_float_negative("5.5"))
        self.assertFalse(NumberValidator.is_float_negative("0.0"))
        self.assertFalse(NumberValidator.is_float_negative("-10"))
        self.assertFalse(NumberValidator.is_float_negative("abc"))

    def test_is_float(self):
        self.assertTrue(NumberValidator.is_float("10.5"))
        self.assertTrue(NumberValidator.is_float("-10.5"))
        self.assertFalse(NumberValidator.is_float("0.0"))
        self.assertFalse(NumberValidator.is_float("10"))
        self.assertFalse(NumberValidator.is_float("abc"))

    def test_is_number(self):
        self.assertTrue(NumberValidator.is_number("10"))
        self.assertTrue(NumberValidator.is_number("-10"))
        self.assertTrue(NumberValidator.is_number("10.5"))
        self.assertTrue(NumberValidator.is_number("-10.5"))
        self.assertFalse(NumberValidator.is_number("abc"))
        self.assertTrue(NumberValidator.is_number("0"))
        self.assertTrue(NumberValidator.is_number("0.0"))


class TestNumberNormalizer(unittest.TestCase):

    def test_normalize_number(self):
        self.assertEqual(NumberNormalizer.normalize_number("1 000,50"), "1000.50")
        self.assertEqual(NumberNormalizer.normalize_number("1.000,50"), "1.000.50")
        self.assertEqual(NumberNormalizer.normalize_number("100"), "100")
        self.assertEqual(NumberNormalizer.normalize_number("-5,2"), "-5.2")
        self.assertEqual(NumberNormalizer.normalize_number("   2,3   "), "2.3")


class TestEntryNormalizer(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.entry = Entry(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_normalize_entries(self):
        self.entry.insert(0, "1 234,56")
        normalized_value = EntryNormalizer.normalize_entries(self.entry)
        self.assertEqual(normalized_value, "1234.56")
        self.assertEqual(self.entry.get(), "1234.56")

        self.entry.delete(0, END)
        self.entry.insert(0, "-7,89")
        normalized_value = EntryNormalizer.normalize_entries(self.entry)
        self.assertEqual(normalized_value, "-7.89")
        self.assertEqual(self.entry.get(), "-7.89")

        self.entry.delete(0, END)
        self.entry.insert(0, "  100  ")
        normalized_value = EntryNormalizer.normalize_entries(self.entry)
        self.assertEqual(normalized_value, "100")
        self.assertEqual(self.entry.get(), "100")


if __name__ == '__main__':
    unittest.main()