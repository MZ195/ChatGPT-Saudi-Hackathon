from fastapi import APIRouter, HTTPException, status
from models.column_struct import ColumnStruct

from .. import controller

router = APIRouter(prefix="/generate", tags=["generate"])

@router.post("/")
def generate(col: ColumnStruct):
    result, err = controller.generate_dummy(col)
    if err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=err)

    return result

