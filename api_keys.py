from fastapi import Request, Response, HTTPException, status, Security, Header, Depends
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
from os import environ

load_dotenv()


API_KEYS = [
    environ.get("TEST_X_API_KEY"),
    environ.get("PROD_X_API_KEY")
]

_api_key_header = APIKeyHeader(name="x-api-key")


def get_api_key(api_key_header: str = Security(_api_key_header)) -> str:
    if api_key_header in API_KEYS:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )