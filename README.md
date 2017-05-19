# TaxJar Sales Tax API for Python

A sales tax API client for interacting with SmartCalcs by TaxJar.

* This wrapper supports 100% of the [TaxJar API Version 2](http://developers.taxjar.com/api/#introduction)
* Data returned from API calls are mapped to Python objects

## Supported Python Versions

Python 2.6+ or Python 3+

## Package Dependencies

TaxJar uses the [Requests](https://github.com/kennethreitz/requests) HTTP library for making RESTful requests to SmartCalcs.

## Getting Started

We recommend installing TaxJar via [PyPI](https://pypi.python.org/pypi) using [pip](https://github.com/pypa/pip). Before authenticating, [get your API key from TaxJar](https://app.taxjar.com/api_sign_up/plus/). Run the following command in your terminal:

```shell
pip install taxjar
```

## Authentication

To authenticate with our API, import the `taxjar` package and instantiate a new API client:

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')
```

## Usage

### List all tax categories

#### Definition

```python
client.categories
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.categories()
```

#### Example Response

```python
[
  <TaxJarCategory {
    'product_tax_code': '31000',
    'name': 'Digital Goods',
    'description': 'Digital products transferred electronically, meaning obtained by the purchaser by means other than tangible storage media.'
  }>,
  <TaxJarCategory {
    'product_tax_code': '20010',
    'name': 'Clothing',
    'description': ' All human wearing apparel suitable for general use'
  }>,
  <TaxJarCategory {
    'product_tax_code': '51010',
    'name': 'Non-Prescription',
    'description': 'Drugs for human use without a prescription'
  }>
]
```

### List tax rates for a location (by zip/postal code)

#### Definition

```python
client.rates_for_location
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

# United States (ZIP+4)
rates = client.rates_for_location('90404-3370')

# United States (ZIP w/ Optional Params)
rates = client.rates_for_location('90404', {
  'city': 'SANTA MONICA',
  'country': 'US'
})

# International Examples (Requires City and Country)
rates = client.rates_for_location('V5K0A1', {
  'city': 'VANCOUVER',
  'country': 'CA'
})

rates = client.rates_for_location('00150', {
  'city': 'HELSINKI',
  'country': 'FI'
})
```

#### Example Response

```python
<TaxJarRate {
  'city': 'SANTA MONICA',
  'zip': '90404',
  'combined_district_rate': '0.025',
  'state_rate': '0.0625',
  'city_rate': '0.0',
  'county': 'LOS ANGELES',
  'state': 'CA',
  'combined_rate': '0.0975',
  'county_rate': '0.01',
  'freight_taxable': False
}>
```

### Calculate sales tax for an order

#### Definition

```python
client.tax_for_order
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.tax_for_order({
  'to_country': 'US',
  'to_zip': '90002',
  'to_city': 'Los Angeles',
  'to_state': 'CA',
  'from_country': 'US',
  'from_zip': '92093',
  'from_city': 'San Diego',
  'amount': 15,
  'shipping': 1.5,
  'nexus_addresses': [{
    'country': 'US',
    'zip': '93101',
    'state': 'CA',
    'city': 'Santa Barbara',
    'street': '1218 State St.'
  }],
  'line_items': [{
    'quantity': 1,
    'unit_price': 15,
    'product_tax_code': 20010
  }]
})
```

#### Example Response

```python
<TaxJarTax {
  'breakdown': <TaxJarBreakdown {
    'special_district_taxable_amount': 15.0,
    'city_tax_rate': 0.0,
    'county_tax_collectable': 0.15,
    'county_taxable_amount': 15.0,
    'special_district_tax_collectable': 0.23,
    'line_items': [<TaxJarBreakdownLineItem {
      'special_district_taxable_amount': 15.0,
      'city_tax_rate': 0.0,
      'county_taxable_amount': 15.0,
      'special_district_amount': 0.23,
      'state_sales_tax_rate': 0.0625,
      'state_amount': 0.94,
      'city_taxable_amount': 0.0,
      'taxable_amount': 15.0,
      'special_tax_rate': 0.015,
      'state_taxable_amount': 15.0,
      'combined_tax_rate': 0.0875,
      'county_tax_rate': 0.01,
      'city_amount': 0.0,
      'county_amount': 0.15,
      'id': '1',
      'tax_collectable': 1.31
    }>],
    'taxable_amount': 15.0,
    'state_taxable_amount': 15.0,
    'combined_tax_rate': 0.0875,
    'state_tax_collectable': 0.94,
    'state_tax_rate': 0.0625,
    'city_tax_collectable': 0.0,
    'county_tax_rate': 0.01,
    'special_tax_rate': 0.015,
    'city_taxable_amount': 0.0,
    'tax_collectable': 1.31
  }>,
  'has_nexus': True,
  'tax_source': 'destination',
  'shipping': 1.5,
  'taxable_amount': 15.0,
  'rate': 0.0875,
  'freight_taxable': False,
  'amount_to_collect': 1.31,
  'order_total_amount': 16.5
}>
```

### List order transactions

#### Definition

```python
client.list_orders
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.list_orders({
  'from_transaction_date': '2016/01/01',
  'to_transaction_date': '2017/01/01'
})
```

#### Example Response

```python
['20', '21', '22']
```

### Show order transaction

#### Definition

```python
client.show_order
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.show_order('123')
```

#### Example Response

```python
<TaxJarOrder {
  'from_state': None,
  'line_items': [<TaxJarLineItem {
    'description': 'Fuzzy Widget',
    'unit_price': '15.0',
    'discount': '0.0',
    'product_identifier': '12-34243-9',
    'sales_tax': '0.95',
    'product_tax_code': None,
    'id': 0,
    'quantity': 1
  }>],
  'user_id': 1,
  'to_zip': '90002',
  'from_street': '1218 State St',
  'from_city': 'SANTA BARBARA',
  'from_zip': 93107,
  'to_country': 'US',
  'shipping': '1.5',
  'from_country': 'US',
  'to_city': 'LOS ANGELES',
  'to_street': '123 Palm Grove Ln',
  'transaction_date': '2016-03-10T00:00:00.000Z',
  'transaction_reference_id': None,
  'sales_tax': '0.95',
  'amount': '17.45',
  'transaction_id': '123',
  'to_state': 'CA'
}>
```

### Create order transaction

#### Definition

```python
client.create_order
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.create_order({
  'transaction_id': '123',
  'transaction_date': '2015/05/14',
  'from_state': 'CA',
  'from_city': 'Santa Barbara',
  'from_street': '1218 State St', 
  'from_country': 'US',
  'from_zip': '93101',
  'to_country': 'US',
  'to_state': 'CA',
  'to_city': 'Los Angeles',
  'to_street': '123 Palm Grove Ln',
  'to_zip': '90002',
  'amount': 16.5,
  'shipping': 1.5,
  'sales_tax': 0.95,
  'line_items': [{
    'quantity': 1,
    'product_identifier': '12-34243-9',
    'description': 'Fuzzy Widget',
    'unit_price': 15,
    'sales_tax': 0.95
  }]
})
```

#### Example Response

```python
<TaxJarOrder {
  'from_state': 'CA',
  'line_items': [<TaxJarLineItem {
    'description': 'Fuzzy Widget',
    'unit_price': '15.0',
    'discount': '0.0',
    'product_identifier': '12-34243-9',
    'sales_tax': '0.95',
    'product_tax_code': None,
    'id': 0,
    'quantity': 1
  }>],
  'user_id': 1,
  'to_zip': '90002',
  'from_street': '1218 State St',
  'from_city': 'SANTA BARBARA',
  'from_zip': '93101',
  'to_country': 'US',
  'shipping': '1.5',
  'from_country': 'US',
  'to_city': 'LOS ANGELES',
  'to_street': '123 Palm Grove Ln',
  'transaction_date': '2016-03-10T00:00:00.000Z',
  'transaction_reference_id': None,
  'sales_tax': '0.95',
  'amount': '17.45',
  'transaction_id': '123',
  'to_state': 'CA'
}>
```

### Update order transaction

#### Definition

```python
client.update_order
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.update_order('123', {
  'transaction_id': '123',
  'amount': 17,
  'shipping': 2,
  'line_items': [{
    'quantity': 1,
    'product_identifier': '12-34243-0',
    'description': 'Heavy Widget',
    'unit_price': 15,
    'sales_tax': 0.95
  }] 
})
```

#### Example Response

```python
<TaxJarOrder {
  'from_state': None,
  'line_items': [<TaxJarLineItem {
    'description': 'Heavy Widget',
    'unit_price': '15.0',
    'discount': '0.0',
    'product_identifier': '12-34243-0',
    'sales_tax': '0.95',
    'product_tax_code': None,
    'id': 0,
    'quantity': 1
  }>],
  'user_id': 1,
  'to_zip': '90002',
  'from_street': '1218 State St',
  'from_city': 'SANTA BARBARA',
  'from_zip': '93101',
  'to_country': 'US',
  'shipping': '1.5',
  'from_country': 'US',
  'to_city': 'LOS ANGELES',
  'to_street': '123 Palm Grove Ln',
  'transaction_date': '2016-03-10T00:00:00.000Z',
  'transaction_reference_id': None,
  'sales_tax': '0.95',
  'amount': '17.95',
  'transaction_id': '123',
  'to_state': 'CA'
}>
```

### Delete order transaction

#### Definition

```python
client.delete_order
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.delete_order('123')
```

#### Example Response

```python
<TaxJarOrder {
  'from_state': None,
  'line_items': [],
  'user_id': 1,
  'to_zip': None,
  'from_street': None,
  'from_city': None,
  'from_zip': None,
  'to_country': None,
  'shipping': None,
  'from_country': None,
  'to_city': None,
  'to_street': None,
  'transaction_date': None,
  'transaction_reference_id': None,
  'sales_tax': None,
  'amount': None,
  'transaction_id': '123',
  'to_state': None
}>
```

### Listing refund transactions

#### Definition

```python
client.list_refunds
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.list_refunds({
  'from_transaction_date': '2016/01/01',
  'to_transaction_date': '2017/01/01'
})
```

#### Example Response

```python
['203', '204', '205']
```

### Show refund transaction

#### Definition

```python
client.show_refund
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.show_refund('321')
```

#### Example Response

```python
<TaxJarRefund {
  'from_state': 'CA',
  'line_items': [<TaxJarLineItem {
    'description': 'Heavy Widget',
    'unit_price': '15.0',
    'discount': '0.0',
    'product_identifier': '12-34243-0',
    'sales_tax': '0.95',
    'product_tax_code': None,
    'id': 0,
    'quantity': 1
  }>],
  'user_id': 1,
  'to_zip': '90002',
  'from_street': '1218 State St',
  'from_city': 'SANTA BARBARA',
  'from_zip': 93107,
  'to_country': 'US',
  'shipping': '1.5',
  'from_country': 'US',
  'to_city': 'LOS ANGELES',
  'to_street': '123 Palm Grove Ln',
  'transaction_date': '2016-03-10T00:00:00.000Z',
  'transaction_reference_id': '123',
  'sales_tax': '0.95',
  'amount': '17.45',
  'transaction_id': '321',
  'to_state': 'CA'
}>
```

### Create refund transaction

#### Definition

```python
client.create_refund
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.create_refund({
  'transaction_id': '321',
  'transaction_date': '2016-05-14',
  'transaction_reference_id': '123',
  'from_state': 'CA',
  'from_city': 'Santa Barbara',
  'from_street': '1218 State St',
  'from_country': 'US',
  'from_zip': '93101',
  'to_country': 'US',
  'to_state': 'CA',
  'to_city': 'Los Angeles',
  'to_street': '123 Palm Grove Ln',
  'to_zip': '90002',
  'amount': 16.5,
  'shipping': 1.5,
  'sales_tax': 0.95,
  'line_items': [{
    'quantity': 1,
    'product_identifier': '12-34243-9',
    'description': 'Fuzzy Widget',
    'unit_price': 15,
    'sales_tax': 0.95
  }]
})
```

#### Example Response

```python
<TaxJarRefund {
  'from_state': 'CA',
  'line_items': [<TaxJarLineItem {
    'description': 'Fuzzy Widget',
    'unit_price': '15.0',
    'discount': '0.0',
    'product_identifier': '12-34243-9',
    'sales_tax': '0.95',
    'product_tax_code': None,
    'id': 0,
    'quantity': 1
  }>],
  'user_id': 1,
  'to_zip': '90002',
  'from_street': '1218 State St',
  'from_city': 'SANTA BARBARA',
  'from_zip': 93107,
  'to_country': 'US',
  'shipping': '1.5',
  'from_country': 'US',
  'to_city': 'LOS ANGELES',
  'to_street': '123 Palm Grove Ln',
  'transaction_date': '2016-03-10T00:00:00.000Z',
  'transaction_reference_id': '123',
  'sales_tax': '0.95',
  'amount': '17.45',
  'transaction_id': '321',
  'to_state': 'CA'
}>
```

### Update refund transaction

#### Definition

```python
client.update_refund
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.update_refund('321', {
  'transaction_id': '321',
  'amount': 17,
  'shipping': 2,
  'sales_tax': 0.95,
  'line_items': [{
    'quantity': 1,
    'product_identifier': '12-34243-0',
    'description': 'Heavy Widget',
    'unit_price': 15,
    'sales_tax': 0.95
  }] 
})
```

#### Example Response

```python
<TaxJarRefund {
  'from_state': 'CA',
  'line_items': [<TaxJarLineItem {
    'description': 'Heavy Widget',
    'unit_price': '15.0',
    'discount': '0.0',
    'product_identifier': '12-34243-0',
    'sales_tax': '0.95',
    'product_tax_code': None,
    'id': 0,
    'quantity': 1
  }>],
  'user_id': 1,
  'to_zip': '90002',
  'from_street': '1218 State St',
  'from_city': 'SANTA BARBARA',
  'from_zip': 93107,
  'to_country': 'US',
  'shipping': '1.5',
  'from_country': 'US',
  'to_city': 'LOS ANGELES',
  'to_street': '123 Palm Grove Ln',
  'transaction_date': '2016-03-10T00:00:00.000Z',
  'transaction_reference_id': '123',
  'sales_tax': '0.95',
  'amount': '17.95',
  'transaction_id': '321',
  'to_state': 'CA'
}>
```

### Delete refund transaction

#### Definition

```python
client.delete_refund
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.delete_refund('321')
```

#### Example Response

```python
<TaxJarRefund {
  'from_state': None,
  'line_items': [],
  'user_id': 1,
  'to_zip': None,
  'from_street': None,
  'from_city': None,
  'from_zip': None,
  'to_country': None,
  'shipping': None,
  'from_country': None,
  'to_city': None,
  'to_street': None,
  'transaction_date': None,
  'transaction_reference_id': None,
  'sales_tax': None,
  'amount': None,
  'transaction_id': '321',
  'to_state': None
}>
```

### List nexus regions

#### Definition

```python
client.nexus_regions
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

nexus_regions = client.nexus_regions()
```

#### Example Response

```python
[
  <TaxJarRegion {
    'country_code': 'US',
    'country': 'United States',
    'region_code': 'CA',
    'region': 'California'
  }>,
  <TaxJarRegion {
    'country_code': 'US',
    'country': 'United States',
    'region_code': 'NY',
    'region': 'New York'
  }>,
  <TaxJarRegion {
    'country_code': 'US',
    'country': 'United States',
    'region_code': 'WA',
    'region': 'Washington'
  }>
]
```

### Validate a VAT number

#### Definition

```python
client.validate
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.validate({
  'vat': 'FR40303265045'
})
```

#### Example Response

```python
<TaxjarValidation {
  'valid': True,
  'exists': True,
  'vies_available': True,
  'vies_response': <TaxJarViesResponse {
    'country_code': 'FR',
    'vat_number': '40303265045',
    'request_date': '2016-02-10',
    'valid': True,
    'name': 'SA SODIMAS',
    'address': "11 RUE AMPERE\n26600 PONT DE L ISERE"
  }>
}>
```


### Summarize tax rates for all regions

#### Definition

```python
client.summary_rates
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.summary_rates()
```

#### Example Response

```python
[
  <TaxJarSummaryRate {
    'average_rate': <TaxJarAverageRate {
      'rate': 0.0827,
      'label': 'Tax'
    }>,
    'region_code': 'CA',
    'minimum_rate': <TaxJarMinimumRate {
      'rate': 0.065,
      'label': 'State Tax'
    }>,
    'country': 'US',
    'region': 'California',
    'country_code': 'US'
  }>,
  <TaxJarSummaryRate {
    'average_rate': <TaxJarAverageRate {
      'rate': 0.12,
      'label': 'PST'
    }>,
    'region_code': 'BC',
    'minimum_rate': <TaxJarMinimumRate {
      'rate': 0.05,
      'label': 'GST'
    }>,
    'country': 'Canada',
    'region': 'British Columbia',
    'country_code': 'CA'
  }>,
  <TaxJarSummaryRate {
    'average_rate': <TaxJarAverageRate {
      'rate': 0.2,
      'label': 'VAT'
    }>,
    'region_code': None,
    'minimum_rate': <TaxJarMinimumRate {
      'rate': 0.2,
      'label': 'VAT'
    }>,
    'country': 'United Kingdom',
    'region': None,
    'country_code': 'UK'
  }>
]
```

### Custom Options

Pass additional parameters when instantiating the client for the following options:

#### Timeouts

Set request timeout in seconds (default is 5 seconds):

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78', options={'timeout':30})
```

## Tests

A `unittest` test suite is available to ensure API functionality:

```shell
$ python -m unittest discover tests
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new pull request
