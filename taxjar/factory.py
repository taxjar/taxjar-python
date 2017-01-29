from taxjar.data import *

class TaxJarTypeFactory:
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
        return classes_by_type[data_type]
