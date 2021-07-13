# TaxJar Sales Tax API for Python ![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/taxjar/taxjar-python?style=flat-square&label=release&sort=semver) [![Build Status](https://travis-ci.com/taxjar/taxjar-python.svg?branch=master)](https://travis-ci.com/taxjar/taxjar-python)

Official Python client for the [TaxJar API](https://www.taxjar.com/api/). For the API documentation, please visit [https://developers.taxjar.com/api](https://developers.taxjar.com/api/reference/?python).

* This wrapper supports 100% of the [TaxJar API Version 2](https://developers.taxjar.com/api/#introduction)
* Data returned from API calls are mapped to Python objects

<hr>

[Supported Python Versions](#supported-python-versions)<br>
[Package Dependencies](#package-dependencies)<br>
[Getting Started](#getting-started)<br>
[Authentication](#authentication)<br>
[Usage](#usage)<br>
[Custom Options](#custom-options)<br>
[Sandbox Environment](#sandbox-environment)<br>
[Tests](#tests)<br>
[Contributing](#contributing)

<hr>

## Supported Python Versions

Python 2.7+ or Python 3.4+

## Package Dependencies

TaxJar uses the following dependencies as specified in `setup.py`:

* [Requests](https://github.com/kennethreitz/requests) HTTP library for making RESTful requests to the TaxJar API.
* [jsonobject](https://github.com/dimagi/jsonobject) Simple JSON object mapping for Python.

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

You're now ready to use TaxJar! [Check out our quickstart guide](https://developers.taxjar.com/api/guides/python/#python-quickstart) to get up and running quickly.

## Usage

[`categories` - List all tax categories](#list-all-tax-categories-api-docs)<br>
[`tax_for_order` - Calculate sales tax for an order](#calculate-sales-tax-for-an-order-api-docs)<br>
[`list_orders` - List order transactions](#list-order-transactions-api-docs)<br>
[`show_order` - Show order transaction](#show-order-transaction-api-docs)<br>
[`create_order` - Create order transaction](#create-order-transaction-api-docs)<br>
[`update_order` - Update order transaction](#update-order-transaction-api-docs)<br>
[`delete_order` - Delete order transaction](#delete-order-transaction-api-docs)<br>
[`list_refunds` - List refund transactions](#list-refund-transactions-api-docs)<br>
[`show_refund` - Show refund transaction](#show-refund-transaction-api-docs)<br>
[`create_refund` - Create refund transaction](#create-refund-transaction-api-docs)<br>
[`update_refund` - Update refund transaction](#update-refund-transaction-api-docs)<br>
[`delete_refund` - Delete refund transaction](#delete-refund-transaction-api-docs)<br>
[`list_customers` - List customers](#list-customers-api-docs)<br>
[`show_customer` - Show customer](#show-customer-api-docs)<br>
[`create_customer` - Create customer](#create-customer-api-docs)<br>
[`update_customer` - Update customer](#update-customer-api-docs)<br>
[`delete_customer` - Delete customer](#delete-customer-api-docs)<br>
[`rates_for_location` - List tax rates for a location (by zip/postal code)](#list-tax-rates-for-a-location-by-zippostal-code-api-docs)<br>
[`nexus_regions` - List nexus regions](#list-nexus-regions-api-docs)<br>
[`validate_address` - Validate an address](#validate-an-address-api-docs)<br>
[`validate` - Validate a VAT number](#validate-a-vat-number-api-docs)<br>
[`summary_rates` - Summarize tax rates for all regions](#summarize-tax-rates-for-all-regions-api-docs)

<hr>


### List all tax categories <small>_([API docs](https://developers.taxjar.com/api/reference/?python#get-list-tax-categories))_</small>

> The TaxJar API provides product-level tax rules for a subset of product categories. These categories are to be used for products that are either exempt from sales tax in some jurisdictions or are taxed at reduced rates. You need not pass in a product tax code for sales tax calculations on product that is fully taxable. Simply leave that parameter out.

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

### Calculate sales tax for an order <small>_([API docs](https://developers.taxjar.com/api/reference/?python#post-calculate-sales-tax-for-an-order))_</small>

> Shows the sales tax that should be collected for a given order.

#### Definition

```python
client.tax_for_order
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.tax_for_order({
  'from_country': 'US',
  'from_zip': '94025',
  'from_state': 'CA',
  'from_city': 'Menlo Park',
  'from_street': '2825 Sand Hill Rd',
  'to_country': 'US',
  'to_zip': '94303',
  'to_state': 'CA',
  'to_city': 'Palo Alto',
  'to_street': '5230 Newell Road',
  'amount': 267.9,
  'shipping': 0,
  'nexus_addresses': [{
    'country': 'US',
    'state': 'CA'
  }],
  'line_items': [{
    'id': '1',
    'quantity': 1,
    'product_tax_code': '19005',
    'unit_price': 535.8,
    'discount': 267.9
  }]
})
```

#### Example Response

```python
<TaxJarTax {
    'taxable_amount': 0,
    'tax_source': 'destination',
    'shipping': 0,
    'rate': 0,
    'order_total_amount': 267.9,
    'jurisdictions': <TaxJarJurisdictions {
        'state': 'CA',
        'county': 'SAN MATEO',
        'country': 'US',
        'city': 'EAST PALO ALTO'
    }>,
    'has_nexus': True,
    'freight_taxable': False,
    'breakdown': <TaxJarBreakdown {
        'taxable_amount': 0,
        'tax_collectable': 0,
        'state_taxable_amount': 0,
        'state_tax_rate': 0,
        'state_tax_collectable': 0,
        'special_tax_rate': 0,
        'special_district_taxable_amount': 0,
        'special_district_tax_collectable': 0,
        'line_items': [<TaxJarBreakdownLineItem {
            'taxable_amount': 0,
            'tax_collectable': 0,
            'state_taxable_amount': 0,
            'state_sales_tax_rate': 0,
            'state_amount': 0,
            'special_tax_rate': 0,
            'special_district_taxable_amount': 0,
            'special_district_amount': 0,
            'id': '1',
            'county_taxable_amount': 0,
            'county_tax_rate': 0,
            'county_amount': 0,
            'combined_tax_rate': 0,
            'city_taxable_amount': 0,
            'city_tax_rate': 0,
            'city_amount': 0
        }>],
        'county_taxable_amount': 0,
        'county_tax_rate': 0,
        'county_tax_collectable': 0,
        'combined_tax_rate': 0,
        'county_tax_collectable': 0,
        'combined_tax_rate': 0,
        'city_taxable_amount': 0,
        'city_tax_rate': 0,
        'city_tax_collectable': 0
    }>,
    'amount_to_collect': 0
}>
```

### List order transactions <small>_([API docs](https://developers.taxjar.com/api/reference/?python#get-list-order-transactions))_</small>

> Lists existing order transactions created through the API.

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

### Show order transaction <small>_([API docs](https://developers.taxjar.com/api/reference/?python#get-show-an-order-transaction))_</small>

> Shows an existing order transaction created through the API.

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
    'transaction_id': '123',
    'user_id': 11836,
    'transaction_date': '2015-05-14T00:00:00Z',
    'transaction_reference_id': None,
    'from_country': 'US',
    'from_zip': '93107',
    'from_state': 'CA',
    'from_city': 'SANTA BARBARA',
    'from_street': '1281 State St',
    'to_country': 'US',
    'to_zip': '90002',
    'to_state': 'CA',
    'to_city': 'LOS ANGELES',
    'to_street': '123 Palm Grove Ln',
    'amount': 17,
    'shipping': 2,
    'sales_tax': '0.95',
    'line_items': [<TaxJarLineItem {
        'id': '1',
        'quantity': 1,
        'product_identifier': '12-34243-0',
        'product_tax_code': None,
        'description': 'Heavy Widget',
        'unit_price': 15,
        'discount': 0,
        'sales_tax': 0.95
    }>]
}>
```

### Create order transaction <small>_([API docs](https://developers.taxjar.com/api/reference/?python#post-create-an-order-transaction))_</small>

> Creates a new order transaction.

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
    'transaction_date': '2015/05/15',
    'from_country': 'US',
    'from_zip': '94025',
    'from_state': 'CA',
    'from_city': 'Menlo Park',
    'from_street': '2825 Sand Hill Rd',
    'to_country': 'US',
    'to_zip': '94303',
    'to_state': 'CA',
    'to_city': 'Palo Alto',
    'to_street': '5230 Newell Road',
    'amount': 267.9,
    'shipping': 0,
    'sales_tax': 0,
    'line_items': [{
        'id: '1',
        'quantity': 1,
        'description': 'Legal Services',
        'product_tax_code': '19005',
        'unit_price': 535.8,
        'discount': 267.9,
        'sales_tax': 0
    }]
})
```

#### Example Response

```python
<TaxJarOrder {
    'transaction_id': '123',
    'user_id': 11836,
    'provider': 'api',
    'transaction_date': '2015-05-15T00:00:00Z',
    'transaction_reference_id': None,
    'customer_id': None,
    'exemption_type': None,
    'from_country': 'US',
    'from_zip': '94025',
    'from_state': 'CA',
    'from_city': 'MENLO PARK,
    'from_street': '2825 Sand Hill Rd',
    'to_country': 'US',
    'to_zip': '94303',
    'to_state': 'CA',
    'to_city': 'PALO ALTO',
    'to_street': '5230 Newell Road',
    'amount': 267.9,
    'shipping': 0,
    'sales_tax': 0,
    'line_items': [<TaxJarLineItem {
        'id': '1',
        'quantity': 1
        'product_identifier': None,
        'product_tax_code': '19005',
        'description': 'Legal Services',
        'unit_price': 535.8,
        'discount': 267.9,
        'sales_tax': 0
    }>]
}>
```

### Update order transaction <small>_([API docs](https://developers.taxjar.com/api/reference/?python#put-update-an-order-transaction))_</small>

> Updates an existing order transaction created through the API.

#### Definition

```python
client.update_order
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.update_order('123', {
    'amount': 283.6,
    'shipping': 5,
    'sales_tax': 1.04,
    'line_items': [
        {
            'id': '1',
            'quantity': 1,
            'description': 'Legal Services',
            'product_tax_code': '19005',
            'unit_price': 535.8,
            'discount': 267.9,
            'sales_tax': 0
        },
        {
            'id': '2',
            'quantity': 2,
            'description': 'Hoberman Switch Pitch',
            'unit_price': 10.7,
            'discount': 10.7,
            'sales_tax': 1.04
        }
    ]
})
```

#### Example Response

```python
<TaxJarOrder {
    'transaction_id': '123',
    'user_id': 11836,
    'provider': 'api',
    'transaction_date': '2015-05-15T00:00:00Z',
    'transaction_reference_id': None,
    'customer_id': None,
    'exemption_type': None,
    'from_country': 'US',
    'from_zip': '94025',
    'from_city': 'MENLO PARK',
    'from_street': '2825 Sand Hill Rd',
    'to_country': 'US',
    'to_zip': '94303',
    'to_state': 'CA',
    'to_city': 'PALO ALTO',
    'to_street': '5230 Newell Road',
    'amount': 283.6,
    'shipping': 5,
    'sales_tax': 1.04,
    'line_items': [
        <TaxJarLineItem {
            'id': '1',
            'quantity': 1,
            'product_identifier': None,
            'product_tax_code': '19005',
            'description': 'Legal Services',
            'unit_price': 535.8,
            'discount': 267.9,
            'sales_tax': 0
        }>,
        <TaxJarLineItem {
            'id': '2',
            'quantity': 2,
            'product_identifier': None,
            'product_tax_code': None,
            'description': 'Hoberman Switch Pitch',
            'unit_price': 10.7,
            'discount': 10.7,
            'sales_tax': 1.04
        }>
    ]
}>
```

### Delete order transaction <small>_([API docs](https://developers.taxjar.com/api/reference/?python#delete-delete-an-order-transaction))_</small>

> Deletes an existing order transaction created through the API.

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
  'transaction_id': '123',
  'user_id': 11836,
  'provider': 'api',
  'transaction_date': None,
  'transaction_reference_id': None,
  'customer_id': None,
  'exemption_type': None,
  'from_country': None,
  'from_zip': None,
  'from_state': None,
  'from_city': None,
  'from_street': None,
  'to_country': None,
  'to_zip': None,
  'to_state': None
  'to_city': None,
  'to_street': None,
  'amount': None,
  'shipping': None,
  'sales_tax': None,
  'line_items': []
}>
```

### List refund transactions <small>_([API docs](https://developers.taxjar.com/api/reference/?python#get-list-refund-transactions))_</small>

> Lists existing refund transactions created through the API.

#### Definition

```python
client.list_refunds
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.list_refunds({
  'from_transaction_date': '2015/05/01',
  'to_transaction_date': '2015/05/31'
})
```

#### Example Response

```python
['20-refund', '21-refund', '22-refund']
```

### Show refund transaction <small>_([API docs](https://developers.taxjar.com/api/reference/?python#get-show-a-refund-transaction))_</small>

> Shows an existing refund transaction created through the API.

#### Definition

```python
client.show_refund
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.show_refund('20-refund')
```

#### Example Response

```python
<TaxJarRefund {
    'transaction_id': '20-refund',
    'user_id': 11836,
    'provider': 'api',
    'transaction_date': '2015-05-15T00:00:00Z',
    'transaction_reference_id': '20',
    'customer_id': None,
    'exemption_type': None,
    'from_country': 'US',
    'from_zip': '93107',
    'from_state': 'CA',
    'from_city': 'SANTA BARBARA',
    'from_street': '1218 State St',
    'to_country': 'US',
    'to_zip': '90002',
    'to_state': 'CA',
    'to_city': 'LOS ANGELES',
    'to_street': '123 Palm Grove Ln',
    'amount': -17,
    'shipping': -2,
    'sales_tax': -0.95,
    'line_items': [<TaxJarLineItem {
        'id': '1',
        'quantity': 1,
        'product_identifier': '12-34243-0',
        'product_tax_code': None,
        'description': 'Heavy Widget',
        'unit_price': -15,
        'discount': 0,
        'sales_tax': -0.95,
    }>]
}>
```

### Create refund transaction <small>_([API docs](https://developers.taxjar.com/api/reference/?python#post-create-a-refund-transaction))_</small>

> Creates a new refund transaction.

#### Definition

```python
client.create_refund
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.create_refund({
    'transaction_id': '123-refund',
    'transaction_reference_id': '123',
    'transaction_date': '2015-05-15',
    'from_country': 'US',
    'from_zip': '94025',
    'from_state': 'CA',
    'from_city': 'Menlo Park',
    'from_street': '2825 Sand Hill Rd',
    'to_country': 'US',
    'to_zip': '94303',
    'to_state': 'CA',
    'to_city': 'Palo Alto',
    'to_street': '5230 Newell Road',
    'amount': -5.35,
    'shipping': -0,
    'sales_tax': -0.52,
    'line_items': [
        {
            'id': '1',
            'quantity': 1,
            'description': 'Legal Services',
            'product_tax_code': '19005',
            'unit_price': -0,
            'discount': -0,
            'sales_tax': -0
        },
        {
            'id': '2',
            'quantity': 1,
            'description': 'Hoberman Switch Pitch',
            'unit_price': -0,
            'discount': -5.35,
            'sales_tax': -0.52
        }
    ]
})
```

#### Example Response

```python
<TaxJarRefund {
    'transaction_id': '123-refund',
    'user_id': 11836,
    'provider': 'api',
    'transaction_date': '2015-05-15T00:00:00Z',
    'transaction_reference_id': '123',
    'customer_id': None,
    'exemption_type': None,
    'from_country': 'US',
    'from_zip': '94025',
    'from_state': 'CA',
    'from_city': 'MENLO PARK',
    'from_street': '2825 Sand Hill Rd',
    'to_country': 'US',
    'to_zip': '94303',
    'to_state': 'CA',
    'to_city': 'PALO ALTO',
    'to_street': '5230 Newell Road',
    'amount': -5.35,
    'shipping': -0,
    'sales_tax': -0.52,
    'line_items': [
        <TaxJarLineItem {
            'id': '1',
            'quantity': 1,
            'product_identifier': None,
            'product_tax_code': '19005',
            'description': 'Legal Services',
            'unit_price': 0,
            'discount': 0,
            'sales_tax': 0
        }>,
        <TaxJarLineItem {
            'id': '2',
            'quantity': 1,
            'product_identifier': None,
            'product_tax_code': None,
            'description': 'Hoberman Switch Pitch',
            'unit_price': 0,
            'discount': -5.35,
            'sales_tax': -0.52
        }>
    ]
}>
```

### Update refund transaction <small>_([API docs](https://developers.taxjar.com/api/reference/?python#put-update-a-refund-transaction))_</small>

> Updates an existing refund transaction created through the API.

#### Definition

```python
client.update_refund
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.update_refund('123-refund', {
  'transaction_reference_id': '123',
  'amount': -10.35,
  'shipping': -5,
})
```

#### Example Response

```python
<TaxJarRefund {
    'transaction_id': '123-refund',
    'user_id': 11836,
    'provider': 'api',
    'transaction_date': '2015-05-15T00:00:00Z',
    'transaction_reference_id': '123',
    'customer_id': None,
    'exemption_type': None,
    'from_country': 'US',
    'from_zip': '94025',
    'from_state': 'CA',
    'from_city': 'MENLO PARK',
    'from_street': '2825 Sand Hill Rd',
    'to_country': 'US',
    'to_zip': '94303',
    'to_state': 'CA',
    'to_city': 'PALO ALTO',
    'to_street': '5230 Newell Road',
    'amount': -10.35,
    'shipping': -5,
    'sales_tax': 0,
    'line_items': [
        <TaxJarLineItem {
            'id': '1',
            'quantity': 1,
            'product_identifier': None,
            'product_tax_code': '19005',
            'description': 'Legal Services',
            'unit_price': 0,
            'discount': 0,
            'sales_tax': 0
        }>,
        <TaxJarLineItem {
            'id': '2',
            'quantity': 1,
            'product_identifier': None,
            'product_tax_code': None,
            'description': 'Hoberman Switch Pitch',
            'unit_price': 0,
            'discount': -5.35,
            'sales_tax': -0.52
        }>
    ]
}>
```

### Delete refund transaction <small>_([API docs](https://developers.taxjar.com/api/reference/?python#delete-delete-a-refund-transaction))_</small>

> Deletes an existing refund transaction created through the API.

#### Definition

```python
client.delete_refund
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.delete_refund('123-refund')
```

#### Example Response

```python
<TaxJarRefund {
  'transaction_id': '123-refund',
  'user_id': 11836,
  'provider': 'api',
  'transaction_date': None,
  'transaction_reference_id': None,
  'customer_id': None,
  'exemption_type': None,
  'from_country': None,
  'from_zip': None,
  'from_state': None,
  'from_city': None,
  'from_street': None,
  'to_country': None,
  'to_zip': None,
  'to_state': None,
  'to_city': None,
  'to_street': None,
  'amount': None,
  'shipping': None,
  'sales_tax': None,
  'line_items': []
}>
```

### List customers <small>_([API docs](https://developers.taxjar.com/api/reference/?python#get-list-customers))_</small>

> Lists existing customers created through the API.

#### Definition

```python
client.list_customers
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.list_customers()
```

#### Example Response

```python
['123', '124', '125']
```

### Show customer <small>_([API docs](https://developers.taxjar.com/api/reference/?python#get-show-a-customer))_</small>

> Shows an existing customer created through the API.

#### Definition

```python
client.show_customer
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.show_customer('123')
```

#### Example Response

```python
<TaxJarCustomer {
  'customer_id': '123',
  'exemption_type': 'wholesale',
  'exempt_regions': [<TaxJarExemptRegion {
    'country': 'US',
    'state': 'FL'
  }>, <TaxJarExemptRegion {
    'country': 'US',
    'state': 'PA'
  }>],
  'name': 'Dunder Mifflin Paper Company',
  'country': 'US',
  'state': 'PA',
  'zip': '18504',
  'city': 'Scranton',
  'street': '1725 Slough Avenue'
}>
```

### Create customer <small>_([API docs](https://developers.taxjar.com/api/reference/?python#post-create-a-customer))_</small>

> Creates a new customer.

#### Definition

```python
client.create_customer
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.create_customer({
  'customer_id': '123',
  'exemption_type': 'wholesale',
  'name': 'Dunder Mifflin Paper Company',
  'exempt_regions': [
    {
      'country': 'US',
      'state': 'FL'
    },
    {
      'country': 'US',
      'state': 'PA'
    }
  ],
  'country': 'US',
  'state': 'PA',
  'zip': '18504',
  'city': 'Scranton',
  'street': '1725 Slough Avenue'
})
```

#### Example Response

```python
<TaxJarCustomer {
  'customer_id': '123',
  'exemption_type': 'wholesale',
  'exempt_regions': [<TaxJarExemptRegion {
    'country': 'US',
    'state': 'FL'
  }>, <TaxJarExemptRegion {
    'country': 'US',
    'state': 'PA'
  }>],
  'name': 'Dunder Mifflin Paper Company',
  'country': 'US',
  'state': 'PA',
  'zip': '18504',
  'city': 'Scranton',
  'street': '1725 Slough Avenue'
}>
```

### Update customer <small>_([API docs](https://developers.taxjar.com/api/reference/?python#put-update-a-customer))_</small>

> Updates an existing customer created through the API.

#### Definition

```python
client.update_customer
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.update_customer('123', {
  'exemption_type': 'wholesale',
  'name': 'Sterling Cooper',
  'exempt_regions': [
    {
      'country': 'US',
      'state': 'NY'
    }
  ],
  'country': 'US',
  'state': 'NY',
  'zip': '10010',
  'city': 'New York',
  'street': '405 Madison Ave'
})
```

#### Example Response

```python
<TaxJarCustomer {
  'customer_id': '123',
  'exemption_type': 'wholesale',
  'exempt_regions': [<TaxJarExemptRegion {
    'country': 'US',
    'state': 'NY'
  }>],
  'name': 'Sterling Cooper',
  'country': 'US',
  'state': 'NY',
  'zip': '10010',
  'city': 'New York',
  'street': '405 Madison Ave'
}>
```

### Delete customer <small>_([API docs](https://developers.taxjar.com/api/reference/?python#delete-delete-a-customer))_</small>

> Deletes an existing customer created through the API.

#### Definition

```python
client.delete_customer
```

#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.delete_customer('123')
```

#### Example Response

```python
<TaxJarCustomer {
  'customer_id': '123',
  'exemption_type': 'wholesale',
  'exempt_regions': [<TaxJarExemptRegion {
    'country': 'US',
    'state': 'FL'
  }>, <TaxJarExemptRegion {
    'country': 'US',
    'state': 'PA'
  }>],
  'name': 'Dunder Mifflin Paper Company',
  'country': 'US',
  'state': 'PA',
  'zip': '18504',
  'city': 'Scranton',
  'street': '1725 Slough Avenue'
}>
```

### List tax rates for a location (by zip/postal code) <small>_([API docs](https://developers.taxjar.com/api/reference/?python#get-show-tax-rates-for-a-location))_</small>

> Shows the sales tax rates for a given location.
>
> **Please note this method only returns the full combined rate for a given location.** It does not support nexus determination, sourcing based on a ship from and ship to address, shipping taxability, product exemptions, customer exemptions, or sales tax holidays. We recommend using [`tax_for_order` to accurately calculate sales tax for an order](#calculate-sales-tax-for-an-order-api-docs).

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
  'combined_district_rate': 0.025,
  'state_rate': 0.0625,
  'city_rate': 0,
  'county': 'LOS ANGELES',
  'state': 'CA',
  'combined_rate': 0.0975,
  'county_rate': 0.01,
  'freight_taxable': False
}>
```

### List nexus regions <small>_([API docs](https://developers.taxjar.com/api/reference/?python#get-list-nexus-regions))_</small>

> Lists existing nexus locations for a TaxJar account.

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

### Validate an address <small>_([API docs](https://developers.taxjar.com/api/reference/?python#post-validate-an-address))_</small>

> Validates a customer address and returns back a collection of address matches. **Address validation requires a [TaxJar Plus](https://www.taxjar.com/plus/) subscription.**

#### Definition

```python
client.validate_address
```
#### Example Request

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78')

client.validate_address({
    'country': 'US',
    'state': 'AZ',
    'zip': '85297',
    'city': 'Gilbert',
    'street': '3301 South Greenfield Rd'
})
```

#### Example Response

```python
[
    <TaxJarAddress {
        'zip': '85297-2176',
        'street': '3301 S Greenfield Rd',
        'state': 'AZ',
        'country': 'US',
        'city': 'Gilbert'
    }>
]
```

### Validate a VAT number <small>_([API docs](https://developers.taxjar.com/api/reference/?python#get-validate-a-vat-number))_</small>

> Validates an existing VAT identification number against [VIES](http://ec.europa.eu/taxation_customs/vies/).

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
<TaxJarValidation {
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

### Summarize tax rates for all regions <small>_([API docs](https://developers.taxjar.com/api/reference/?python#get-summarize-tax-rates-for-all-regions))_</small>

> Retrieve minimum and average sales tax rates by region as a backup.
>
> This method is useful for periodically pulling down rates to use if the TaxJar API is unavailable. However, it does not support nexus determination, sourcing based on a ship from and ship to address, shipping taxability, product exemptions, customer exemptions, or sales tax holidays. We recommend using [`tax_for_order` to accurately calculate sales tax for an order](#calculate-sales-tax-for-an-order-api-docs).

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

## Sandbox Environment

You can easily configure the client to use the [TaxJar Sandbox](https://developers.taxjar.com/api/reference/?python#sandbox-environment):

```python
import taxjar
client = taxjar.Client(api_key='48ceecccc8af930bd02597aec0f84a78', api_url='https://api.sandbox.taxjar.com')
```

For testing specific [error response codes](https://developers.taxjar.com/api/reference/?python#errors), pass the custom `X-TJ-Expected-Response` header:

```python
client.set_api_config('headers', {
    'X-TJ-Expected-Response': '422'
})
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
