from reynold_number.IReynoldNumber import IReynoldNumber
from reynold_number.FluidAttributes import FluidAttributes


class ReynoldNumber(IReynoldNumber):
    u: float
    L: float
    _p: float | None
    _mu: float | None
    _nu: float | None
    fluid_attributes: FluidAttributes

    def __init__(self, fluid: FluidAttributes) -> None:
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def _setup(self) -> None:
        pass

    def calculate_reynold_number(self) -> float:
        pass

    def predict_flow_type(self) -> str:
        pass
