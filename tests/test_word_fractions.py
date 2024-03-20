# pytest library
import pytest

import re

from ingredient_slicer import IngredientRegexPatterns, IngredientSlicer

# IngredientSlicer.regex.PREP_WORDS_PATTERN.findall("3 tablespoons unsalted butter, softened at room temperature")
# IngredientSlicer.regex.print_matches("3 tablespoons unsalted butter, softened at room temperature")
# IngredientSlicer.regex.constants["PREP_WORDS"]

# ingredient = "1 and 2thirds cups of milk"
# # parser = IngredientSlicer(ingredient)
# # parser.parse()
# # parsed = parser.to_json()

# IngredientSlicer.regex.constants["FRACTION_WORDS"]

# IngredientSlicer.regex.print_matches(ingredient)