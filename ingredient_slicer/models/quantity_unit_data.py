from typing import Union
from dataclasses import dataclass, field

@dataclass
class QuantityUnitData:
    quantity: Union[str, None] = None 
    unit: Union[str, None] = None 
    secondary_quantity: Union[str, None] = None
    secondary_unit: Union[str, None] = None
    parenthesis_notes: list[str] = field(default_factory=list)