from reynold_number.IReynoldNumber import IReynoldNumber
from reynold_number.FluidAttributes import FluidAttributes


class ReynoldNumber(IReynoldNumber):
    u: float
    L: float
    _p: float | None
    _mu: float | None
    _nu: float | None
    fluid_attributes: FluidAttributes

    __Re: float | None

    @property
    def Re(self):
        if self.__Re is not None:
            return self.__Re
        return 0

    def __init__(self, u: float, L: float, fluid: FluidAttributes) -> None:
        self.u = u
        self.L = L
        self.fluid_attributes = fluid
        self._setup()

    def __str__(self) -> str:
        return f"Test"

    def __repr__(self) -> str:
        return f"Test"

    def _setup(self) -> None:
        self._p = self.fluid_attributes.p
        self._mu = self.fluid_attributes.mu
        self._nu = self.fluid_attributes.nu
        return None

    def calculate_reynold_number(self) -> float:
        if self._nu is not None:
            re = (self.u * self.L) / self._nu
            self.__Re = re
            return re

        elif self._mu is not None and self._p is not None:
            re = (self._p * self.L * self.L) / self._mu
            self.__Re = re
            return re

        else:
            raise Exception("Some Error Occurred")

    def predict_flow_type(self) -> str:
        if self.__Re < 2000:
            return "The Flow is probably Laminar"

        elif 2000 <= self.__Re <= 4000:
            return "The Flow is probably Transient"

        elif self.__Re > 4000:
            return "The Flow is probably Turbulent"

        else:
            raise Exception("Cannot Calculated")
