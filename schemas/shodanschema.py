from typing import List, Any

from pydantic import BaseModel

class ShodansSchema(BaseModel):
    total: int
    data: Any
