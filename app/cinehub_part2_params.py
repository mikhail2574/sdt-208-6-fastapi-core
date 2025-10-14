from fastapi import APIRouter, Query

params_router = APIRouter(tags=["Basics & Params"])

@params_router.get(
    "/greet/{name}",
    summary="Greet a user by name",
    description="Returns a friendly greeting using the path parameter `name`."
)
def greet_name(name: str) -> dict:
    return {"message": f"Hello, {name}!"}

@params_router.get(
    "/square",
    summary="Square a number",
    description="Provide a positive integer using the `number` query parameter to get its square."
)
def square(number: int = Query(..., ge=0, description="Non-negative integer to be squared")) -> dict:
    return {"input": number, "square": number * number}
