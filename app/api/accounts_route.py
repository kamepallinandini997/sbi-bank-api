"""
This module defines API endpoints for account-related operations in the banking system.

Routes included:
- POST /create-account: Create a new customer account.
- POST /fund: Fund an existing customer account.
- POST /withdraw: Withdraw funds from a customer account.

Each route delegates  logic to the account service layer and handles exceptions
gracefully, returning appropriate HTTP responses. Logging is included for monitoring
and debugging purposes.
"""

from fastapi import FastAPI, HTTPException, APIRouter, status

from app.core.exceptions import (
    AccountAlreadyExistsException, 
    AccountNotFoundException, 
    InsufficientBalanceException, 
    account_already_exists_exception, 
    account_not_found_exception, 
    insufficient_balance_exception
)

from app.models.schemas import (
    CreateAccountRequest, 
    FundAccountRequest, 
    WithdrawRequest)

from app.services.account_service import (
    create_customer_account, 
    fund_customer_account, 
    withdraw_from_customer_account
)

import logging

logger = logging.getLogger(__name__)
accounts_router = APIRouter()

@accounts_router.post("/create-account")
async def create_account(data: CreateAccountRequest):
    """
    Create a new customer account with a zero balance.

    Args:
        data (CreateAccountRequest): Request containing the customer_id.

    Returns:
        dict: Success message confirming account creation.

    Raises:
        HTTPException: If the account already exists or on server error.
    """
    try:
        await create_customer_account(data.customer_id)
        logger.info(f"created the customer with customer id {data.customer_id}")
        return {"message": f"Customer {data.customer_id} created with 0.0 Balance"}
    except AccountAlreadyExistsException:
        raise account_already_exists_exception()
    except Exception as e:
        logger.error(f"Something went wrong and details are {str(e)} - data -  {data.customer_id}")
        raise HTTPException(status_code=500, detail="Something went wrong. Please try again.")

@accounts_router.post("/fund")
async def fund_account(data: FundAccountRequest):
    """
    Fund an existing customer account with the specified amount.

    Args:
        data (FundAccountRequest): Request containing customer_id and amount to fund.

    Returns:
        dict: Success message with the updated balance.

    Raises:
        HTTPException: If the account is not found or on server error.
    """
    try:
        balance = await fund_customer_account(data.customer_id, data.amount)
        logger.info(f"Funded customer account with id {data.customer_id} with amount {data.amount} and balance is {balance}")
        return {"message": f"Funded customer account with id {data.customer_id} with amount {data.amount} and balance is {balance}"}
    except AccountNotFoundException:
        raise account_not_found_exception()
    except Exception as e:
        logger.error(f"Error funding account {data.customer_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong. Please try again.")

@accounts_router.post("/withdraw")
async def withdraw_from_account(data: WithdrawRequest):
    """
    Withdraw a specified amount from a customer account.

    Args:
        data (WithdrawRequest): Request containing customer_id and amount to withdraw.

    Returns:
        dict: Success message with the updated balance.

    Raises:
        HTTPException: If balance is insufficient, account not found, or on server error.
    """
    try:
        balance = await withdraw_from_customer_account(data.customer_id, data.amount)
        logger.info(f"Amount of Rs. {data.amount} is withdrawn for customer {data.customer_id} final balance is {balance}")
        return {"message": f"Amount of Rs. {data.amount} is withdrawn for customer {data.customer_id} final balance is {balance}"}
    except InsufficientBalanceException:
        raise insufficient_balance_exception()
    except AccountNotFoundException:
        raise account_not_found_exception()
    except Exception as e:
        logger.error(f"Error withdrawing from account {data.customer_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong. Please try again.")
