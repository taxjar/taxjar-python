class Error(Exception):
    """Base class for TaxJar-related errors"""

class ResponseError(Error):
    """Response errors (400, 500)"""

class ConnectionError(Error):
    """Connection errors"""

class TypeError(Error):
    """Factory errors"""
