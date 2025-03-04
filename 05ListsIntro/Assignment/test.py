import unittest
import yaml
import inspect
import main
import os

def test_function_definition(test_case, module, function_name, expected_num_args):
    # check the function is defined
    function_defined = hasattr(module, function_name)
    test_case.assertTrue(function_defined, f"{function_name} is not defined in {module.__name__}")

    # check the function takes correct # arguments
    function = getattr(module, function_name)
    signature = inspect.signature(function)
    num_arguments = len(signature.parameters)

    test_case.assertEqual(num_arguments, expected_num_args, f"{function_name} should take {expected_num_args} argument(s)")

def execute_test(test_case, module, function_name, data):
    test_function_definition(test_case, module, function_name, len(data[function_name][0]["input"]))
    func = getattr(module, function_name)
    for row in data[function_name]:
      with test_case.subTest(arguments=row["input"]):
          arguments = row["input"]
          expected_result = row["output"]
          result = func(*arguments)
          test_case.assertEqual(result, expected_result, f"{function_name}({', '.join(map(str, arguments))}) was expected to return:\n{expected_result}\nInstead, it returned:\n{result}\n")

class TestFunctions(unittest.TestCase):
    longMessage = False

    @classmethod
    def setUpClass(cls):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, "testing_data.yaml"), "r") as file:
            cls.data = yaml.safe_load(file)

    def test_make_abc(self):
        execute_test(self, main, "make_abc", self.data)
    
    def test_equal_edges(self):
        execute_test(self, main, "equal_edges", self.data)

    def test_common_edge(self):
        execute_test(self, main, "common_edge", self.data)

    def test_all_the_same(self):
        execute_test(self, main, "all_the_same", self.data)
    
    def test_all_unique(self):
        execute_test(self, main, "all_unique", self.data)

    def test_increasing(self):
        execute_test(self, main, "increasing", self.data)

    def test_all_true(self):
        execute_test(self, main, "all_true", self.data)

    def test_mostly_true(self):
        execute_test(self, main, "mostly_true", self.data)
    
    def test_make_copy(self):
        execute_test(self, main, "make_copy", self.data)
    
    def test_repeat_thrice(self):
        execute_test(self, main, "repeat_thrice", self.data)
    
    def test_make_reversed_copy(self):
        execute_test(self, main, "make_reversed_copy", self.data)
    
    def test_reverse_in_place(self):
        execute_test(self, main, "reverse_in_place", self.data)
    
if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False, catchbreak=False)
