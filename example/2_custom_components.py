import numpy as np

from hydreservoir.water_balance.v2.hydraulic_component import BaseFreeSpillway, BaseGatedSpillway, BaseCircularCulvert, \
    BaseBoxCulvert, SimpleDischarge
from hydreservoir.water_balance.v2.hydraulic_component.core import Core


class CustomFromScratch(Core):

    def provide_discharge(self, water_level: np.ndarray[float], capacity: np.ndarray[float]) -> np.ndarray[float]:
        return np.zeros(len(water_level))


class CustomFreeSpillway(BaseFreeSpillway):
    def calculate_free_spillway_discharge(self, water_level: float, capacity: float) -> float:
        m = self._spillway_discharge_coefficient
        g = self._gravitational_acceleration
        _B = self._dimension
        _H = water_level - self._elevation
        # do something ...
        return 0


class CustomGatedSpillway(BaseGatedSpillway):
    def calculate_gated_spillway_discharge(self, water_level: float, capacity: float, opening: float) -> float:
        # access properties
        # do something ...
        return 0


class CustomCircularCulvert(BaseCircularCulvert):
    def calculate_circular_culvert_discharge(self, water_level: float, capacity: float, opening: float) -> float:
        # access properties
        # do something ...
        return 0


class CustomBoxCulvert(BaseBoxCulvert):
    def calculate_box_culvert_discharge(self, water_level: float, capacity: float, opening: float) -> float:
        # access properties
        # do something ...
        return 0


class CustomPump(SimpleDischarge):
    def provide_discharge(
            self, water_level: np.ndarray[float], capacity: np.ndarray[float]
    ) -> np.ndarray[float]:
        return self._discharge
