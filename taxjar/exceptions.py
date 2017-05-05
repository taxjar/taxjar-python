class TaxJarError(Exception):
    """Base class for TaxJar-related errors"""

class TaxJarResponseError(TaxJarError):
    """Response errors (400, 500)"""

class TaxJarConnectionError(TaxJarError):
    """Connection errors"""

class TaxJarTypeError(TaxJarError):
    """Factory errors"""
