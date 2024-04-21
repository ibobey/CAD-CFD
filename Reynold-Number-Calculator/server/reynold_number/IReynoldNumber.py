from typing import Protocol
from reynold_number.FluidAttributes import FluidAttributes


class IReynoldNumber(Protocol):
    u: float
    L: float
    _p: float | None
    _mu: float | None
    _nu: float | None
    fluid_attributes: FluidAttributes

    def _setup(self) -> None: ...

    def calculate_reynold_number(self) -> float: ...

    def predict_flow_type(self) -> str:  ...
