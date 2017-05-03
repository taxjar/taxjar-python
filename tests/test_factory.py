import unittest
from mock import MagicMock, patch
from taxjar.factory import TypeFactory
from taxjar.exceptions import TypeError

class TestTaxJarFactory(unittest.TestCase):
    def test_key_translation(self):
        klass = TypeFactory.build('order')
        self.assertEqual(klass.__name__, 'TaxJarOrder')

    def test_bad_key_is_raised(self):
        self.assertRaises(TypeError, TypeFactory.build, 'hi')
