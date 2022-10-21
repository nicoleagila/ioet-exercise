import unittest
from functions import *


class TestFileToDict(unittest.TestCase):
    def test_correct_keys(self):
        """
        Test that it generate the correct keys from a file
        """
        name = "schedule2.txt"
        result = file_to_dict(name).keys()
        self.assertIn("RENE", result)
        self.assertIn("ASTRID", result)


class TestRangeHours(unittest.TestCase):
    def test_correct_hour(self):
        """
        Test that detail the hour that are between a time frame in 1 hour
        """
        data = "11:30-11:45"
        result = range_hours(data)
        self.assertEqual(result, {11})

    def test_correct_hours(self):
        """
        Test that detail the hours that are between a time frame in more than 1 hour
        """
        data = "10:30-12:45"
        result = range_hours(data)
        self.assertEqual(result, {10,11,12})


class TestMatch(unittest.TestCase):
    def test_is_a_match(self):
        """
        Test that check if two schedules match
        """
        data = {'RENE': {'MO': {10, 11}, 'TU': {10, 11}, 'TH': {1, 2}, 'SU': {20}}, 'ASTRID': {'MO': {10, 11}, 'TH': {12, 13}, 'SU': {20}}}
        result = is_a_match("ASTRID","RENE",data)
        self.assertNotEqual(0, result)


if __name__ == '__main__':
    unittest.main()