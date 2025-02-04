import httpx

async def fetch_fun_fact(n: int) -> str:
    url = f"http://numbersapi.com/{n}/math"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            return response.text if response.status_code == 200 else "No fun fact available."
    except httpx.RequestError as exc:
        return f"An error occurred while requesting fun fact: {exc}"
    except httpx.TimeoutException:
        return "The request timed out while fetching the fun fact."

# import httpx
# import logging

# logging.basicConfig(level=logging.INFO)

# async def fetch_fun_fact(n: int) -> str:
#     url = f"http://numbersapi.com/{n}/math"
#     logging.info(f"Fetching fun fact for number: {n}")
#     try:
#         async with httpx.AsyncClient(timeout=10.0) as client:
#             response = await client.get(url)
#             logging.info(f"Response status code: {response.status_code}")
#             return response.text if response.status_code == 200 else "No fun fact available."
#     except httpx.RequestError as exc:
#         logging.error(f"Request error: {exc}")
#         return f"An error occurred while requesting fun fact: {exc}"
#     except httpx.TimeoutException:
#         logging.error("Request timed out")
#         return "The request timed out while fetching the fun fact."