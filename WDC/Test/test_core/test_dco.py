import unittest
from unittest.mock import MagicMock, Mock

from WDC.core.coverage import Coverage, AxisSubset
from WDC.core.dbc import Dbc
from WDC.core.dco import Dco
from WDC.helper.error_handling.err import VariableArgumentException
from WDC.helper.operations.numoperations import AggregationMethod
from WDC.core.switch import Case
from WDC.helper.util.useful_classes import RGB, Date


class TestDco(unittest.TestCase):
    def setUp(self):
        self.dbc = Dbc()
        coverage = Coverage("AvgLandTemp")
        self.dco = Dco(coverage, dbc=self.dbc)

    def test_successful_query(self):
        # spy on post query
        self.dbc.post_query = Mock(wraps=self.dbc.post_query)
        test_coverage = Coverage("AvgLandTemp")

        lat = AxisSubset('Lat', 53.08)
        lon = AxisSubset('Long', 8.80)
        ansi = AxisSubset('ansi', (Date(2014, 1), Date(2014, 12)))
        test_coverage.set_subset(lat, lon, ansi)

        # assert query and response
        response = self.dco.return_expression(
            AggregationMethod.max(test_coverage)).execute().decode('utf-8')
        self.dbc.post_query.assert_called_with(
            'for $i0 in (AvgLandTemp) return max($i0[Lat(53.08), Long(8.8), ansi("2014-01":"2014-12")])')
        self.assertEqual(
            response, '25.984251')

    def test_init_incorrect_coverage(self):
        with self.assertRaisesRegex(TypeError, 'All coverages must be instances of the Coverage class.'):
            self.dbc = Dbc()
            Dco('coverage1', 'coverage2', dbc=self.dbc)

    def test_init_not_dbc(self):
        with self.assertRaisesRegex(TypeError, 'A Dbc object must be passed.'):
            test_coverage = Coverage("AvgLandTemp")
            Dco(test_coverage, dbc='incorrect_dbc')

    def test_return_expression_scalar(self):
        self.dco.return_expression(120)
        self.assertEqual(self.dco._returnQuery, '120')

    def test_return_expression_coverage(self):
        correct_request = 'for $i0 in (AvgLandTemp) return $i0[ansi("2014-07"), Lat(53.08), Long(8.8)]'
        correct_return_query = '$i0[ansi("2014-07"), Lat(53.08), Long(8.8)]'
        self.dbc.post_query = MagicMock()
        # set up coverage data
        test_coverage = Coverage("AvgLandTemp")
        # set up subset data
        lat = AxisSubset('Lat', 53.08)
        lon = AxisSubset('Long', 8.80)
        ansi = AxisSubset('ansi', Date(2014, 7))
        test_coverage.set_subset(ansi, lat, lon)
        self.dco.return_expression(test_coverage).execute()
        # assertion
        self.assertEqual(self.dco._returnQuery, correct_return_query)
        self.dbc.post_query.assert_called_with(correct_request)

    def test_return_expression_operation(self):
        correct_return_query = '($i0[ansi("2014-07"), Lat(53.08), Long(8.8)] > 10)'
        # set up coverage data
        test_coverage = Coverage("AvgLandTemp")
        # set up subset data
        lat = AxisSubset('Lat', 53.08)
        lon = AxisSubset('Long', 8.80)
        ansi = AxisSubset('ansi', Date(2014, 7))
        test_coverage.set_subset(ansi, lat, lon)
        self.dco.return_expression(test_coverage > 10).execute()
        # assertion
        self.assertEqual(self.dco._returnQuery, correct_return_query)

    def test_return_expression_aggregate(self):
        correct_return_query = 'max($i0[ansi("2014-07"), Lat(53.08), Long(8.8)])'
        # set up coverage data
        test_coverage = Coverage("AvgLandTemp")
        # set up subset data
        lat = AxisSubset('Lat', 53.08)
        lon = AxisSubset('Long', 8.80)
        ansi = AxisSubset('ansi', Date(2014, 7))
        test_coverage.set_subset(ansi, lat, lon)
        self.dco.return_expression(
            AggregationMethod.max(test_coverage)).execute()
        # assertion
        self.assertEqual(self.dco._returnQuery, correct_return_query)

    def test_return_expression_fail(self):
        with self.assertRaisesRegex(TypeError, "The type of the instance you passed is not allowed."):
            self.dco.return_expression('incorrect type for return_expressions')

    def test_execute_with_encoding(self):
        correct_request = 'for $i0 in (AvgLandTemp) return encode($i0[ansi("2014-07"), Lat(53.08), Long(8.8)], "png")'
        self.dbc.post_query = MagicMock()
        # set up coverage data
        test_coverage = Coverage("AvgLandTemp")
        # set up subset data
        lat = AxisSubset('Lat', 53.08)
        lon = AxisSubset('Long', 8.80)
        ansi = AxisSubset('ansi', Date(2014, 7))
        test_coverage.set_subset(ansi, lat, lon)
        self.dco.return_expression(test_coverage).execute(return_format="png")
        # assertion
        self.dbc.post_query.assert_called_with(correct_request)

    def test_construct(self):
        values = [(1, 2), (3, 4)]
        operator = '>'
        self.dco.construct(values, operator)
        expected_query = "coverage myCoverage\nover $p x((1:2)), $q y((3:4)) values $p > $q"
        self.assertEqual(self.dco._returnQuery, expected_query)

    def test_clip(self):
        values = [(1, 2), (3, 4)]
        self.dco.clip(values)
        expected_query = f"clip({self.dco._coverages[0].variable}, POLYGON((1 2,3 4)))"
        self.assertEqual(self.dco._returnQuery, expected_query)

    def test_invalid_construct_type(self):
        values = [(1, "a"), (1, 2)]
        with self.assertRaisesRegex(VariableArgumentException, 'Tuple values are incorrect.'):
            self.dco.construct(values, '>')

    def test_invalid_construct_length(self):
        values = [(1, 2)]
        with self.assertRaisesRegex(VariableArgumentException, 'Argument must consist of a list of 2 tuples.'):
            self.dco.construct(values, '>')

    def test_invalid_clip(self):
        values = [(1, 2, 3)]
        with self.assertRaisesRegex(VariableArgumentException, 'Tuple values are incorrect.'):
            self.dco.clip(values)

    def test_switch_correct(self):
        correct_query = '''switch
case ($i0[Lat(35:75), Long(-20:40), ansi("2014-07")] = 99999) return {red: 255; green: 255; blue: 255}
case ($i0[Lat(35:75), Long(-20:40), ansi("2014-07")] > 30) return {red: 255; green: 0; blue: 255}
default return {red: 255; green: 0; blue: 0}
'''
        # set up coverage data
        test_coverage1 = Coverage("AvgLandTemp")
        test_coverage2 = Coverage("AvgLandTemp")
        # set up subset data
        lat = AxisSubset('Lat', (35, 75))
        lon = AxisSubset('Long', (-20, 40))
        ansi = AxisSubset('ansi', Date(2014, 7))
        test_coverage1.set_subset(lat, lon, ansi)
        test_coverage2.set_subset(lat, lon, ansi)
        # set up returns
        return1 = RGB(255, 255, 255)
        return2 = RGB(255, 0, 255)
        # set up cases

        case1 = Case(test_coverage1 == 99999, return1)
        case2 = Case(test_coverage2 > 30, return2)

        # run switch method with default case
        self.dco.switch(case1, case2, default=RGB(255, 0, 0))
        self.assertEqual(self.dco._returnQuery, correct_query)

    def test_switch_incorrect_case(self):
        with self.assertRaisesRegex(TypeError, 'All arguments must be instances of the Case class'):
            self.dco.switch('incorrect_case', default=RGB(255, 0, 0))
        with self.assertRaisesRegex(ValueError, "Empty arguments."):
            self.dco.switch(default=RGB(255, 0, 0))

    def test_switch_incorrect_default(self):
        with self.assertRaisesRegex(TypeError, 'The type of the instance you passed is not allowed.'):
            self.dco.switch(Case(Coverage('coverage1') == 1, RGB(
                255, 255, 255)), default='incorrect_default')


if __name__ == '__main__':
    unittest.main()
