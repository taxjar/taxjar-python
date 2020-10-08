# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.9.1] - 2020-10-08
- Fix issue with custom user agent on non-Unix platforms

## [1.9.0] - 2020-03-31
- Add information to custom user agent for debugging and informational purposes

## [1.8.0] - 2019-10-18
- Add trove classifiers to `setup.py` for informational purposes

## [1.7.0] - 2019-09-30
- Accept params when showing or deleting transactions (e.g., `provider`)

## [1.6.0] - 2018-11-01
- Support address validation via `validate_address` method

## [1.5.0] - 2018-09-17
- Add `jurisdictions` object to `tax_for_order` response

## [1.4.0] - 2018-07-31
- Update `validate` function signature (`validate('1234')` to `validate({'vat': '1234'})`)

## [1.3.0] - 2018-05-03
- Support customer exemptions

## [1.2.0] - 2018-03-21
- Sandbox environment support with `api_url` and custom headers

## [1.1.3] - 2018-01-05
- Use https for API access

## [1.1.2] - 2017-06-09
- Fix improper handling of `400` error response

## [1.1.1] - 2017-06-06
- Support Australia / SST `country_rate` in `rates_for_location`

## [1.1.0] - 2017-05-19
- Add MIT License
- Add `breakdown` property to `tax_for_order` response
- Support VAT validation

## [1.0.0] - 2017-05-05
- Initial release

[Unreleased]: https://github.com/taxjar/taxjar-python/compare/v1.9.1...HEAD
[1.9.1]: https://github.com/taxjar/taxjar-python/compare/v1.9.0...v1.9.1
[1.9.0]: https://github.com/taxjar/taxjar-python/compare/v1.8.0...v1.9.0
[1.8.0]: https://github.com/taxjar/taxjar-python/compare/v1.7.0...v1.8.0
[1.7.0]: https://github.com/taxjar/taxjar-python/compare/v1.6.0...v1.7.0
[1.6.0]: https://github.com/taxjar/taxjar-python/compare/v1.5.0...v1.6.0
[1.5.0]: https://github.com/taxjar/taxjar-python/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/taxjar/taxjar-python/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/taxjar/taxjar-python/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/taxjar/taxjar-python/compare/v1.1.3...v1.2.0
[1.1.3]: https://github.com/taxjar/taxjar-python/compare/v1.1.2...v1.1.3
[1.1.2]: https://github.com/taxjar/taxjar-python/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/taxjar/taxjar-python/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/taxjar/taxjar-python/compare/v1.0.0...v1.1.0
