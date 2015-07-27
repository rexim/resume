import unittest
from generate_resume import is_filtered, filter_by_tags

class TestGenerateResume(unittest.TestCase):
    def test_is_filtered(self):
        self.assertFalse(is_filtered([], ['c++', 'java']))
        self.assertFalse(is_filtered(5, ['c++', 'java']))
        self.assertFalse(is_filtered({}, ['c++', 'java']))
        self.assertTrue(is_filtered({ 'tags': ['c++'] }, ['c++', 'java']))

    def test_filter_by_tags(self):
        input_data = {
            'tags': ['c++', 'python'],
            'entries': [
                {
                    'title': 'foo'
                },
                {
                    'title': 'bar',
                    'tags': ['c++', 'java']
                },
                {
                    'title': 'baz',
                    'tags': ['c++', 'python']
                }
            ]
        }

        expected_output = {
            'tags': ['c++', 'python'],
            'entries': [
                {
                    'title': 'foo'
                },
                {
                    'title': 'bar',
                    'tags': ['c++', 'java']
                }
            ]
        }

        self.assertEqual(filter_by_tags(input_data, ['c++', 'java']), expected_output)

if __name__ == '__main__':
    unittest.main()
