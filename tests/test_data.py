import unittest
from unittest.mock import MagicMock, patch
from taxjar.data import *

class TestTaxJarData(unittest.TestCase):
    def test_response_handling(self):
        data = TaxJarData({ 'keys': 'become', 'attributes': True })
        self.assertEqual(data.keys, 'become')
        self.assertTrue(data.attributes)

    def test_array_objects(self):
        categories = TaxJarCategories([{ 'name': 'cat1' }, { 'name': 'cat2' }])
        self.assertEqual(categories.data[0].name, 'cat1')
        self.assertEqual(categories.data[1].name, 'cat2')
