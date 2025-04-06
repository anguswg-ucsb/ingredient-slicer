from dataclasses import dataclass, field
from typing import Union, Dict, Any

from ingredient_slicer.models.quantity_unit_data import QuantityUnitData

@dataclass
class ParsedIngredientData:
    ingredient: str = ""
    standardized_ingredient: str = ""
    food: str = ""

    quantity: Union[str, None] = None
    unit: Union[str, None] = None
    standardized_unit: Union[str, None] = None

    secondary_quantity: Union[str, None] = None
    secondary_unit: Union[str, None] = None
    standardized_secondary_unit: Union[str, None] = None

    gram_weight: Union[str, None] = None
    max_gram_weight: Union[str, None] = None
    min_gram_weight: Union[str, None] = None
    densities: dict[str, Union[int, float]] = field(default_factory=dict)

    prep: list[str] = field(default_factory=list)
    size_modifiers: list[str] = field(default_factory=list)
    dimensions: list[str] = field(default_factory=list)

    is_required: bool = True
    parenthesis_content: list[str] = field(default_factory=list)

    def merge_quantity_unit_data(self, data: QuantityUnitData):
        self.quantity = data.quantity
        self.unit = data.unit
        self.standardized_unit = data.standardized_unit

        self.secondary_quantity = data.secondary_quantity
        self.secondary_unit = data.secondary_unit
        self.standardized_secondary_unit = data.standardized_secondary_unit

    def to_json(self) -> Dict[str, Any]:
            return {
                "ingredient": self.ingredient,                                # "2 1/2 large cups of sugar lightly packed (about 40 tbsp of sugar)"
                "standardized_ingredient": self.standardized_ingredient,          # "2.5 cups of sugar"
            
                "food" : self.food,                                           # "sugar"

                "quantity": self.quantity,                                    # "2.5"
                "unit": self.unit,                                            # "cups"
                "standardized_unit": self.standardized_unit,                      # "cup"

                "secondary_quantity": self.secondary_quantity,                # "40"
                "secondary_unit": self.secondary_unit,                        # "tbsp"
                "standardized_secondary_unit": self.standardized_secondary_unit,  # "tablespoon"
                "density": self.densities.get("density"),                     # 0.95

                "gram_weight": self.gram_weight,                              # "113.4 grams

                "prep": self.prep,                                            # ["lightly", "packed"]
                "size_modifiers": self.size_modifiers,                        # ["large"]
                "dimensions": self.dimensions,                                # ["2 inches"]
                "is_required": self.is_required,                              # True

                # NOTE: drop these at some point
                "parenthesis_content": self.parenthesis_content               # ["(about 40 tbsp of sugar)"]
            }