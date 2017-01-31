# TaxJar Sales Tax API for Python 3

A client for interacting with SmartCalcs by TaxJar.

* This wrapper supports 100% of the [TaxJar API Version 2](http://developers.taxjar.com/api/#introduction)
* Data returned from API calls are mapped into Python objects

## Supported Python Versions

Python 3 or greater

## Installation

FIXME

```shell
pip install taxjar-python
```

## Quick Start Guide

First, [get an API key from TaxJar](https://app.taxjar.com/api_sign_up/plus/).

## Usage

### List all tax categories

#### Definition

```python
client.categories
```

#### Example Request

```python
client = TaxJarClient('your key here')
client.categories
```

### List tax rates for a location (by zip/postal code)

#### Definition

```python
client.rates_for_location
```

#### Example Request

```python
client = TaxJarClient('your key here')
rates = client.rates_for_location('90404-3370')

# TODO - optional params not supported yet
# United States (ZIP w/ Optional Params)
client.rates_for_location('90404', {
  'city': 'SANTA MONICA',
  'country': 'US'
})
```

### Calculate Sales tax for an order

#### Definition

```python
client.tax_for_order
```

#### Example Request

```python
client = TaxJarClient('your key here')
client.tax_for_order({
  'shipping': 0,
  'to_zip': 66085,
  'to_state': 'KS',
  'to_country': 'US',
  'amount': 100.0
})
```

### List order transactions

#### Definition

```python
client.list_orders
```

#### Example Request

```python
client = TaxJarClient('your key here')
client.list_orders({
  'from_transaction_date': '2016/01/01',
  'to_transaction_date': '2017/01/01'
})
```

### Show order transaction

#### Definition

```python
client.show_order
```

#### Example Request

```python
client = TaxJarClient('your key here')
client.show_order('123')
```

### Create order transaction

#### Definition

```python
client.create_order
```

#### Example Request

```python
client = TaxJarClient('your key here')

client.create_order({
  'transaction_id': tid,
  'transaction_date': '2016-05-14',
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

### Update order transaction

#### Definition

```python
client.update_order
```

#### Example Request

```python
client = TaxJarClient('your key here')
client.update_order(tid, {
  'transaction_id': tid,
  'from_city': "Santo Barbara"
})
```

### Delete order transaction

#### Definition

```python
client.delete_order
```

#### Example Request

```python
client = TaxJarClient('your key here')
client.delete_order('123')
```

### Listing refund transactions

#### Definition

```python
client.list_refunds
```

#### Example Request

```python
client = TaxJarClient('your key here')
client.list_refunds({
  'from_transaction_date': '2016/01/01',
  'to_transaction_date': '2017/01/01'
})
```

### Show refund transaction

#### Definition

```python
client.show_refund
```

#### Example Request

```python
client = TaxJarClient('your key here')
client.show_refund('321')
```

### Create refund transaction

#### Definition

```python
client.create_refund
```

#### Example Request

```python
client = TaxJarClient('your key here')
client.create_refund({
  'transaction_id': tid,
  'transaction_date': '2016-05-14',
  'transaction_reference_id': tid,
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

### Update refund transaction

#### Definition

```python
client.update_refund
```

#### Example Request

```python
client = TaxJarClient('your key here')
client.update_refund(tid, {
  'transaction_id': tid,
  'from_city': "Santo Barbara",
  'amount': 16.5
})
```

### Delete refund transaction

#### Definition

```python
client.delete_refund
```

#### Example Request

```python
client = TaxJarClient('your key here')
client.delete_refund('321')
```

### List nexus regions

#### Definition

```python
client.nexus_regions
```

#### Example Request

```python
client = TaxJarClient('your key here')
nexus_regions = client.nexus_regions
```

### Validate a VAT number

#### Definition

```python
client.validate
```

#### Example Request

```python
client = TaxJarClient('your key here')
client.validate({
  'vat': 'FR40303265045'
})
```


### Summarize tax rates for all regions

#### Definition

```python
client.summary_rates
```

#### Example Request

```python
client = TaxJarClient('your key here')
client.summary_rates
```

### Custom Options

#### TODO - not supported

Set request timeout in seconds:

```python
client.tax_for_order({ timeout: 30 })
```

## Tests

A unittest test suite is available to ensure API functionality:

```shell
$ python -m unittest discover tests
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new pull request
