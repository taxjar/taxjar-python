from setuptools import setup

setup(
    name='taxjar',
    version='1.9.2',
    description='Sales tax API client for Python',
    author='TaxJar',
    author_email='support@taxjar.com',
    url='https://github.com/taxjar/taxjar-python',
    download_url='https://github.com/taxjar/taxjar-python/archive/v1.9.2.zip',
    packages=['taxjar', 'taxjar.data'],
    classifiers=[
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Office/Business",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    install_requires=[
        'requests >= 2.13.0',
        'jsonobject >= 0.9.10'
    ],
    tests_require=[
        'mock'
    ]
)
