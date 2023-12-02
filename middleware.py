from fastapi import HTTPException, Depends
from fastapi.security import APIKeyHeader

from config import API_SECRET_KEY

api_key_header = APIKeyHeader(name="X-API-Key")

async def validate_api_key(api_key: str = Depends(api_key_header)):
    """
    Validates an API key by comparing it to a predefined secret key.

    Parameters:
        api_key (str, optional): The API key to be validated. Defaults to the value returned by the `api_key_header` dependency.

    Returns:
        str: The validated API key.

    Raises:
        HTTPException: If the API key is invalid.

    """
    if api_key != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")

    return api_key
