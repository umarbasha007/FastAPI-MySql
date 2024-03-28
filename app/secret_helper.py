from typing import Any
import jwt

SECRET = "secret"


def encode(payload: Any) -> str:
    return jwt.encode(payload, SECRET, algorithm="HS256")


def decode(token: str) -> Any:
    return jwt.decode(token, SECRET, algorithms=["HS256"])
