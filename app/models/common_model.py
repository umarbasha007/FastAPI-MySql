# from pydantic import BaseModels
from enum import Enum


class MaterialType(str, Enum):
    polyster = "polyster"
    viscosc = "viscosc"


# class User(BaseModel):
#     id: int
#     username: str
#     email: str
