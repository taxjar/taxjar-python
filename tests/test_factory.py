import unittest
from taxjar.factory import TaxJarTypeFactory
from taxjar.exceptions import TaxJarTypeError

class TestTaxJarFactory(unittest.TestCase):
    def test_key_translation(self):
        klass = TaxJarTypeFactory.build('order')
        self.assertEqual(klass.__name__, 'TaxJarOrder')

    def test_bad_key_is_raised(self):
        self.assertRaises(TaxJarTypeError, TaxJarTypeFactory.build, 'hi')
