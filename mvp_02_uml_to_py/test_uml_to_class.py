import unittest
from mvp_02_uml_to_py.generate_interface_from_uml import generate_python_classes,extract_all_interfaces, extract_compositions





# tests.py (Третий этап: добавляем больше тестов)
class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        with open('uml_class_line.puml', 'r') as uml_class:
            uml_content = uml_class.read()

        with open('generated_classes_for_test.py', 'r') as output_data:
            output_data = output_data.read()

        interfaces = extract_all_interfaces(uml_content)
        compositions = extract_compositions(uml_content)
        self.assertEqual(generate_python_classes(interfaces, compositions), output_data)

    # def test_odd_number(self):
    #     self.assertFalse(is_even(5))
    #
    # def test_zero(self):
    #     self.assertTrue(is_even(0))
    #
    # def test_negative_even(self):
    #     self.assertTrue(is_even(-2))
    #
    # def test_negative_odd(self):
    #     self.assertFalse(is_even(-3))


if __name__ == '__main__':
    unittest.main()