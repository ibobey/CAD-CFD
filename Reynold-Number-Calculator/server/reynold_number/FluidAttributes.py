from pydantic import BaseModel
from typing import Optional


class FluidAttributes(BaseModel):
    p: Optional[float]
    nu: Optional[float]
    mu: Optional[float]
