import unittest
from mvp_02_uml_to_py.generate_interface_from_uml import generate_python_classes, extract_all_interfaces, \
    extract_compositions


# tests.py (Третий этап: добавляем больше тестов)
class TestIsEven(unittest.TestCase):
    def test_class(self):
        with open('uml_class_for_test.puml', 'r') as uml_class:
            uml_content = uml_class.read()

        with open('ready_class_for_test.py', 'r') as output_data:
            output_data = output_data.read()

        interfaces = extract_all_interfaces(uml_content)
        compositions = extract_compositions(uml_content)
        line_get = generate_python_classes(interfaces, compositions).expandtabs(tabsize=4)
        line_result = output_data
        print(line_get)
        for index, (first, second) in enumerate(zip(line_get.split('\n'), line_result.split('\n'))):
            # print(first == second, '\t', first, second)
            self.assertEqual(first, second, f'{index}, {first=}, {second=}')
        # self.assertEqual(generate_python_classes(interfaces, compositions), output_data)

    def test_classes(self):
        with open('uml_class_line.puml', 'r') as uml_class:
            uml_content = uml_class.read()

        with open('generated_classes_for_test.py', 'r') as output_data:
            output_data = output_data.read()

        interfaces = extract_all_interfaces(uml_content)
        compositions = extract_compositions(uml_content)
        line_get = generate_python_classes(interfaces, compositions).expandtabs(tabsize=4)
        line_result = output_data
        for index, (first, second) in enumerate(zip(line_get.split('\n'), line_result.split('\n'))):
            self.assertEqual(first, second, f'{index}, {first=}, {second=}')
        # self.assertEqual(generate_python_classes(interfaces, compositions), output_data)




if __name__ == '__main__':
    unittest.main()
