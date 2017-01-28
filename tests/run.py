import os
import sys

if __name__ == '__main__':
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    taxjar_dir = os.path.join(tests_dir, os.path.pardir)
    sys.path.append(taxjar_dir)

    from taxjar.client import TaxJarClient
    from taxjar.exceptions import TaxJarResponseError
    import time

    taxjar = TaxJarClient("4761b5420b86988ca376712b20f743cb")
    rate = taxjar.rates_for_location('90210')
    print(rate)
    cats = taxjar.categories()
    print(cats)
    taxes = taxjar.tax_for_order({ 'shipping': 0, 'to_zip': 66085, 'to_state': 'KS', 'to_country': 'US', 'amount': 100.0 })
    print(taxes)
    orders = taxjar.list_orders({ 'from_transaction_date': '2016/01/01', 'to_transaction_date': '2017/01/01' })
    print(orders)
    order = taxjar.show_order('113-9883150-1814669')
    print(order)

    tid = str(int(time.time()))
    order = taxjar.create_order({'transaction_id': tid, 'transaction_date': '2016-05-14', 'from_state': 'CA', 'from_city': 'Santa Barbara', 'from_street': '1218 State St','from_country': 'US','from_zip': '93101','to_country': 'US','to_state': 'CA','to_city': 'Los Angeles','to_street': '123 Palm Grove Ln','to_zip': '90002','amount': 16.5,'shipping': 1.5,'sales_tax': 0.95, 'line_items': [{'quantity': 1, 'product_identifier': '12-34243-9', 'description': 'Fuzzy Widget', 'unit_price': 15, 'sales_tax': 0.95}]})
    print(order)

    order = taxjar.update_order(tid, {'transaction_id': tid, 'from_city': "Santo Barbara"})
    print(order)

    order = taxjar.delete_order(tid)
    print(order)

    orders = taxjar.list_refunds({ 'from_transaction_date': '2016/01/01', 'to_transaction_date': '2017/01/01' })
    print(orders)

    tid = str(int(time.time()))
    order = taxjar.create_refund({'transaction_id': tid, 'transaction_date': '2016-05-14', 'transaction_reference_id': tid, 'from_state': 'CA', 'from_city': 'Santa Barbara', 'from_street': '1218 State St','from_country': 'US','from_zip': '93101','to_country': 'US','to_state': 'CA','to_city': 'Los Angeles','to_street': '123 Palm Grove Ln','to_zip': '90002','amount': 16.5,'shipping': 1.5,'sales_tax': 0.95, 'line_items': [{'quantity': 1, 'product_identifier': '12-34243-9', 'description': 'Fuzzy Widget', 'unit_price': 15, 'sales_tax': 0.95}]})
    print(order)

    order = taxjar.show_refund(tid)
    print(order)

    order = taxjar.update_refund(tid, {'transaction_id': tid, 'from_city': "Santo Barbara", 'amount': 16.5})
    print(order)

    order = taxjar.delete_refund(tid)
    print(order)

    regions = taxjar.nexus_regions()
    print(regions)

    validation = taxjar.validate("FR40303265045")
    print(validation)

    rates = taxjar.summary_rates()
    print(rates)
