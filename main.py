from fastapi import FastAPI, HTTPException
from app.api.accounts_route import  accounts_router
from app.core.logging import configure_logger

# Configure logger
logger = configure_logger()

# Create a Fast API
app = FastAPI()

# Include account related routes in accounts_router 
# V1 Routes
app.include_router(accounts_router, prefix="/api/v1")

# V2 Routes
app.include_router(accounts_router, prefix="/api/v2")

@app.get("/")
async def root():
    """Root entry point - Navigate to documentation"""
    return {"message" : "Bank API is running. See /docs for API Documentation"}

@app.get("/health")
async def health_check():
    """Checks the API Health - API is running or have issue"""
    return {"message" : "Bank API is running as expected"}