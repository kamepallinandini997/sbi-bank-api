"""
This module defines custom exception classes and FastAPI-compatible exception
response helpers for handling account-related errors in the banking system.

Defined Exceptions:
- AccountNotFoundException: Raised when a requested account is not found.
- InsufficientBalanceException: Raised when a withdrawal or transfer is attempted with insufficient funds.
- AccountAlreadyExistsException: Raised when attempting to create a duplicate account.

Exception Response Helpers:
- account_not_found_exception(): Returns HTTP 404 error with a standardized message.
- account_already_exists_exception(): Returns HTTP 400 error indicating duplicate account.
- insufficient_balance_exception(): Returns HTTP 400 error for insufficient funds.
"""

from fastapi import HTTPException, status

class AccountNotFoundException(Exception):
    """Exception raised when an account is not found."""
    pass

class InsufficientBalanceException(Exception):
    """Exception raised when an account has insufficient balance."""
    pass

class AccountAlreadyExistsException(Exception):
    """Exception raised when an account with same id already exists."""
    pass

def account_not_found_exception():
    """
    Return HTTP 404 Not Found exception for missing account.

    Returns:
        HTTPException: FastAPI HTTPException with 404 status and message.
    """
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Account not found."
    )

def account_already_exists_exception():
    """
    Return HTTP 400 Bad Request exception for duplicate account creation.

    Returns:
        HTTPException: FastAPI HTTPException with 400 status and message.
    """
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Account already exists."
    )

def insufficient_balance_exception():
    """
    Return HTTP 400 Bad Request exception for insufficient funds.

    Returns:
        HTTPException: FastAPI HTTPException with 400 status and message.
    """
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Account does not have sufficient balance."
    )
