from pydantic import BaseModel

class ColumnStruct(BaseModel):
    col_name: str