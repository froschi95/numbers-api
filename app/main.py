from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import number
from app.exceptions.handler import value_error_handler
from typing import Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"]
)

app.include_router(number.router)

app.add_exception_handler(ValueError, value_error_handler)

@app.get("/")
async def health_check() -> Dict[str, str]:
    """
    Simple health check endpoint to verify API is running.
    
    Returns:
        dict: Status message indicating the API is operational
    """
    return {"status": "healthy"}