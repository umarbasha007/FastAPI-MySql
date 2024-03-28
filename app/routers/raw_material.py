"""
    Rouets related to raw materials
"""

import datetime
from typing import List, Optional, Tuple, cast
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import starlette.status as status

# from app.database.models import models
from app.database.database import get_db
from app.auth_helper import get_token
from app.models.common_model import MaterialType

router = APIRouter(prefix="/raw-materials", tags=["raw-materials"])


@router.get("/{raw_material_id}", response_model=dict)
def get_raw_material(
    raw_material_id: int,
    db: Session = Depends(get_db),
) -> dict:
    """
    Get a raw material by its id
    """
    raw_material = (
        db.query(models.RawMaterial)
        .filter(models.RawMaterial.id == raw_material_id)
        .first()
    )
    if not raw_material:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Raw material with id {raw_material_id} not found",
        )
    return raw_material.to_dict()


@router.get("/", response_model=List[dict])
def get_raw_materials(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> List[dict]:
    """
    Retrieve raw materials
    """
    raw_materials = db.query(models.RawMaterial).offset
    return raw_materials.limit(limit).all()


@router.post("/new_material", response_model=List[dict])
def submit_new_raw_material(
    date: datetime.date,
    material_type: MaterialType,
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
