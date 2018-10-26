from taxjar.data.rate import TaxJarRate
from taxjar.data.category import TaxJarCategories
from taxjar.data.tax import TaxJarTax
from taxjar.data.order import TaxJarOrder, TaxJarOrders
from taxjar.data.customer import TaxJarCustomer, TaxJarCustomers
from taxjar.data.region import TaxJarRegions
from taxjar.data.address import TaxJarAddress, TaxJarAddresses
from taxjar.data.validation import TaxJarValidation
from taxjar.data.summary_rate import TaxJarSummaryRates
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
            'customer': TaxJarCustomer,
            'customers': TaxJarCustomers,
            'regions': TaxJarRegions,
            'addresses': TaxJarAddresses,
            'validation': TaxJarValidation,
            'summary_rates': TaxJarSummaryRates
        }
        if data_type not in classes_by_type:
            raise TaxJarTypeError("Unknown data type: " + data_type)
        return classes_by_type[data_type]
