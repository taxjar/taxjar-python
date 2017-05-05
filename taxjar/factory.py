from taxjar.data import (
    TaxJarRate,
    TaxJarCategories,
    TaxJarTax,
    TaxJarOrder,
    TaxJarOrders,
    TaxJarRegions,
    TaxJarValidation,
    TaxJarSummaryRates
)
from taxjar.exceptions import TaxJarTypeError

class TaxJarTypeFactory(object):
    @staticmethod
    def build(data_type):
        classes_by_type = {
            'rate': TaxJarRate,
            'categories': TaxJarCategories,
            'tax': TaxJarTax,
            'orders': TaxJarOrders,
            'order': TaxJarOrder,
            'refunds': TaxJarOrders,
            'refund': TaxJarOrder,
            'regions': TaxJarRegions,
            'validation': TaxJarValidation,
            'summary_rates': TaxJarSummaryRates
        }
        if data_type not in classes_by_type:
            raise TaxJarTypeError("Unknown data type: " + data_type)
        return classes_by_type[data_type]
