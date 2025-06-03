import _asyncio
import logging
from app.core.logging import configure_logger
from app.db.database import accounts

from app.core.exceptions import (
    AccountNotFoundException, 
    InsufficientBalanceException, 
    AccountAlreadyExistsException, 
    InsufficientBalanceException
    )

# logger = configure_logger()
#from app.core.logging import logger
logger = logging.getLogger(__name__)



async def create_customer_account(customer_id: str):
    if customer_id in accounts:
        logger.warning(f"account already exists with customer id {customer_id}")
        raise AccountAlreadyExistsException()
    accounts[customer_id] = 0.0    

async def fund_customer_account( customer_id: str, amount: float):
    if customer_id not in accounts:
        logger.warning(f"account does not exists with customer id {customer_id}")
        raise AccountNotFoundException()
    accounts[customer_id] += amount
    return accounts[customer_id]

async def withdraw_from_customer_account ( customer_id: str, amount: float):
    if customer_id not in accounts:
        logger.warning(f"account does not exists with customer id {customer_id}")
        raise AccountNotFoundException()
    if accounts[customer_id] < amount:
        logger.warning(f"account does not balance for customer id {customer_id}, current balance {accounts[customer_id]}")
        raise InsufficientBalanceException()
    accounts[customer_id] -= amount
    return accounts[customer_id]

    