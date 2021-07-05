import unittest
from Calculator import Calculator
from CsvReader import CsvReader

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
        CsvReader.data = []

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 4)

    def test_addition(self):
        test_data = CsvReader('addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value1'], row['Value2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        test_data = CsvReader('multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.mul(row['Value1'], row['Value2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_subtraction(self):
        test_data = CsvReader('subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sub(row['Value1'], row['Value2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_division(self):
        test_data = CsvReader('division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.div(row['Value2'], row['Value1']), float(row['Result']))
            self.assertEqual(self.calculator.result, round(float(row['Result']),9))

    def test_square(self):
        test_data = CsvReader('square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sq(row['Value1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_squareroot(self):
        test_data = CsvReader('squareroot.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sqrt(row['Value1']), round(float(row['Result']),8))
            self.assertEqual(self.calculator.result, round(float(row['Result']),8))




if __name__ == '__main__':
    unittest.main()