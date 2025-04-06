from abc import ABC, abstractmethod

# from .models.quantity_unit_data import QuantityUnitData
from ingredient_slicer.models.quantity_unit_data import QuantityUnitData

class ParenthesisHandler(ABC):
    @abstractmethod
    def handle(self, parenthesis: str, data: QuantityUnitData) -> QuantityUnitData:
        pass