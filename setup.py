from setuptools import setup

setup(
    name='taxjar',
    version='0.0.1',
    description='Sales tax API client for Python',
    author='TaxJar',
    author_email='support@taxjar.com',
    url='https://github.com/taxjar/taxjar-python',
    packages=['taxjar'],
    install_requires=[
        'requests >= 2.13.0'
    ],
    tests_require=[
        'mock'
    ]
)
