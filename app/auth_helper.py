from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Simulated database of valid tokens
VALID_TOKENS = ["tech_admin_token", "valid_token_2"]


# Define a dependency to extract the bearer token from the Authorization header
def get_token(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    if credentials.scheme != "Bearer":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid authentication scheme. Bearer token required",
        )
    if credentials.credentials not in VALID_TOKENS:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )
    return credentials.credentials
