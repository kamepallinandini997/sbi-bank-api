"""

This module implements the core business logic for managing customer accounts
in the banking system. It provides asynchronous functions to create accounts,
fund accounts, and withdraw funds, while ensuring proper validation and
exception handling.

Key Functions:
- create_customer_account(customer_id: str): Creates a new account with zero balance. Raises
  AccountAlreadyExistsException if the account already exists.
- fund_customer_account(customer_id: str, amount: float): Adds the specified amount to the
  customer's account balance. Raises AccountNotFoundException if the account does not exist.
- withdraw_from_customer_account(customer_id: str, amount: float): Deducts the specified amount
  from the customer's account balance. Raises AccountNotFoundException if the account does not
  exist and InsufficientBalanceException if funds are insufficient.

Uses an in-memory dictionary 'accounts' from the database module as the data store.
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
    if customer_id in accounts:
        logger.warning(f"account already exists with customer id {customer_id}")
        raise AccountAlreadyExistsException()
    accounts[customer_id] = 0.0    

async def fund_customer_account(customer_id: str, amount: float):
    if customer_id not in accounts:
        logger.warning(f"account does not exists with customer id {customer_id}")
        raise AccountNotFoundException()
    accounts[customer_id] += amount
    return accounts[customer_id]

async def withdraw_from_customer_account(customer_id: str, amount: float):
    if customer_id not in accounts:
        logger.warning(f"account does not exists with customer id {customer_id}")
        raise AccountNotFoundException()
    if accounts[customer_id] < amount:
        logger.warning(f"account does not balance for customer id {customer_id}, current balance {accounts[customer_id]}")
        raise InsufficientBalanceException()
    accounts[customer_id] -= amount
    return accounts[customer_id]
