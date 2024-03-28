"""
    Rouets related to common informations like constants, etc.,
"""

from typing import List, Optional, Tuple, cast
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# import starlette.status as status

# from app.database.models.spinning_production_constant import models
from app.database.database import get_db
from app.auth_helper import get_token

router = APIRouter(prefix="/common", tags=["common"])


@router.get("/spinning_production_constants", response_model=List[dict])
def get_spinning_production_constants(
    db: Session = Depends(get_db),
    token: str = Depends(get_token),
    skip: int = 0,
    limit: int = 100,
) -> List[dict]:
    """
    Retrieve spinning production constants
    """
    raw_materials = db.query(models).offset
    return raw_materials.limit(limit).all()


@router.get("/count_wise_fourties_conversion", response_model=List[dict])
def get_count_wise_fourties_conversion(
    token: str = Depends(get_token),
) -> List[dict]:
    """
    Retrieve count wise fourties conversion
    """
    return []


@router.get("/machine_wise_spindle", response_model=List[dict])
def get_machine_wise_spindle(
    token: str = Depends(get_token),
) -> List[dict]:
    """
    Retrieve machine wise spindle
    """
    return []
