from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse
from app.services.classification import is_prime, is_perfect, is_armstrong, digit_sum
from app.services.fun_fact import fetch_fun_fact

router = APIRouter()

@router.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="The number to classify")):
    """
    Classify a number based on its properties.
    Args:
        - number (int, optional): The number to classify.
    Returns:
        - JSONResponse: A JSON response containing the classification results.
    """

    properties = []
    if is_armstrong(number):
        properties.append("armstrong")

    properties.append("odd" if number % 2 else "even")

    return JSONResponse(
        status_code = status.HTTP_200_OK,
        content = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": digit_sum(number),
            "fun_fact": await fetch_fun_fact(number)
            }
        )