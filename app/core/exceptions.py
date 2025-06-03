from fastapi import HTTPException, status

class AccountNotFoundException (Exception):
    """Exception raised when an account is not found."""
    pass

class  InsufficientBalanceException (Exception):
    """Exception raised when an account has insufficient balance."""
    pass

class  AccountAlreadyExistsException  (Exception):
    """Exception raised when an account with same id already exists."""
    pass

def account_not_found_exception():
    return HTTPException (
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Account not found."
    )

def account_already_exists_exception():
    return HTTPException (
        status_code = status.HTTP_400_BAD_REQUEST,
        detail = "Account already exists."
    )

def insufficient_balance_exception():
    return HTTPException (
        status_code = status.HTTP_400_BAD_REQUEST,
        detail = "Account does not have sufficient balance."
    )