import unittest
from WDC.core.switch import Case
from WDC.core.coverage import Coverage


class TestCaseClass(unittest.TestCase):

    def test_case_exception_init(self):
        with self.assertRaisesRegex(TypeError, 'Please, provide a comparison related to some coverage as an argument.'):
            Case('condition', 'return_value')

    def test_case_exception_set_return_value(self):
        test_coverage1 = Coverage("AvgLandTemp")
        with self.assertRaisesRegex(TypeError, "The type of the instance you passed is not allowed."):
            Case(test_coverage1 > 30, 'return_value')


if __name__ == '__main__':
    unittest.main()
