"""
This module implements the core business logic for managing customer accounts
in the banking system. It provides asynchronous functions to create accounts,
fund accounts, and withdraw funds, while ensuring proper validation and
exception handling.

Key Functions:
- create_customer_account(customer_id: str): Creates a new account with zero balance.
    Raises
        AccountAlreadyExistsException if the account already exists.
- fund_customer_account(customer_id: str, amount: float): Adds the specified amount to the
    customer's account balance.
    Raises
        AccountNotFoundException if the account does not exist.
- withdraw_from_customer_account(customer_id: str, amount: float): Deducts the specified amount
  from the customer's account balance. 
    Raises 
        AccountNotFoundException if the account does not exist and 
        InsufficientBalanceException if funds are insufficient.

"""

import _asyncio
import logging
from app.core.logging import configure_logger
from app.db.database import accounts

from app.core.exceptions import (
    AccountNotFoundException, 
    InsufficientBalanceException, 
    AccountAlreadyExistsException
)

# logger = configure_logger()
# from app.core.logging import logger
logger = logging.getLogger(__name__)

async def create_customer_account(customer_id: str):
    """
    Create a new customer account with an initial balance of 0.0.

    Args:
        customer_id (str): The unique identifier for the customer.

    Raises:
        AccountAlreadyExistsException: If an account with the given customer_id already exists.
    """
    if customer_id in accounts:
        logger.warning(f"account already exists with customer id {customer_id}")
        raise AccountAlreadyExistsException()
    accounts[customer_id] = 0.0    

async def fund_customer_account(customer_id: str, amount: float):
    """
    Add funds to an existing customer account.

    Args:
        customer_id (str): The unique identifier for the customer.
        amount (float): The amount to add to the account balance.

    Returns:
        float: The updated account balance.

    Raises:
        AccountNotFoundException: If the account does not exist.
    """
    if customer_id not in accounts:
        logger.warning(f"account does not exists with customer id {customer_id}")
        raise AccountNotFoundException()
    accounts[customer_id] += amount
    return accounts[customer_id]

async def withdraw_from_customer_account(customer_id: str, amount: float):
    """
    Withdraw funds from an existing customer account.

    Args:
        customer_id (str): The unique identifier for the customer.
        amount (float): The amount to withdraw from the account.

    Returns:
        float: The updated account balance.

    Raises:
        AccountNotFoundException: If the account does not exist.
        InsufficientBalanceException: If the account balance is insufficient for the withdrawal.
    """
    if customer_id not in accounts:
        logger.warning(f"account does not exists with customer id {customer_id}")
        raise AccountNotFoundException()
    if accounts[customer_id] < amount:
        logger.warning(f"account does not balance for customer id {customer_id}, current balance {accounts[customer_id]}")
        raise InsufficientBalanceException()
    accounts[customer_id] -= amount
    return accounts[customer_id]
