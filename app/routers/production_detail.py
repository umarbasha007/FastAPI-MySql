"""
    Rouets related to production detail
"""

import datetime
from typing import List, Optional, Tuple, cast
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import starlette.status as status

# from app.database.models.spinning_production_constant import models
from app.database.database import get_db
from app.auth_helper import get_token

router = APIRouter(prefix="/production_detail", tags=["production_detail"])


@router.post("/new_detail", response_model=List[dict])
def submit_new_production_detail(
    date: datetime.date,
    quantity: float,  # In KG
    token: str = Depends(get_token),
    db: Session = Depends(get_db),
) -> dict:
    """
    Submit a new raw material
    """
    new_raw_material = models.RawMaterial(**new_raw_material)
    db.add(new_raw_material)
    db.commit()
    db.refresh(new_raw_material)
    return new_raw_material.to_dict()
