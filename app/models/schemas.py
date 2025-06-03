"""
This module defines the request models used by the banking API for account-related
operations. These models ensure input data validation using Pydantic, providing
structured and type-safe request bodies for API endpoints.

Defined Request Schemas:
- CreateAccountRequest: Used for account creation requests; requires customer ID.
- FundAccountRequest: Used to fund an existing account; requires customer ID and amount.
- WithdrawRequest: Used for withdrawal requests; requires customer ID and amount.
"""

from pydantic import BaseModel

class CreateAccountRequest(BaseModel):
    """
    Request schema for creating a new customer account.

    Attributes:
        customer_id (str): Unique identifier for the customer.
    """
    customer_id: str

class FundAccountRequest(BaseModel):
    """
    Request schema for funding an existing customer account.

    Attributes:
        customer_id (str): Unique identifier for the customer.
        amount (float): Amount to be added to the account.
    """
    customer_id: str
    amount: float

class WithdrawRequest(BaseModel):
    """
    Request schema for withdrawing funds from a customer account.

    Attributes:
        customer_id (str): Unique identifier for the customer.
        amount (float): Amount to be withdrawn from the account.
    """
    customer_id: str
    amount: float
