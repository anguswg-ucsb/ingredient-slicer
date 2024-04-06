ingredient-slicer
------

Python 📦 package for extracting quantities, units, and food words from unstructured recipe ingredients text. 

`ingredient-slicer` works by standardizing the input text and then applying a set of rules and heuristic methods to parse out quantities, units, and food words from unstructured recipe ingredients text.
`ingredient-slicer` was designed to provide a robust and lightweight method for parsing recipe ingredients 
text *without* relying on any external dependencies or NLP/ML models.
That being said, it is not perfect and can always be improved upon. 


Table of Contents:
-----------------------
- [Installation](#installation)
- [Usage](#usage)

<br>

Installation:
-----------------------
`ingredient_slicer` can be downloaded from PyPI via `pip` like so:

``` shell
pip install ingredient-slicer
```

Usage:
-----------------------

Provide a string to the `IngredientSlicer` class and thats it. Invoke the `to_json()` method to return the parsed ingredient.

```pycon

import ingredient_slicer

slicer = ingredient_slicer.IngredientSlicer("2 (15-ounces) cans chickpeas, rinsed and drained")

slicer.to_json()

{
    'standardized_ingredient': '2 cans chickpeas, rinsed and drained', 
    'food': 'chickpeas', 

    # primary units
    'quantity': '30', 
    'unit': 'ounces', 
    'standardized_unit': 'ounce', 

    # any other secondary units found in the string
    'secondary_quantity': '2', 
    'secondary_unit': 'cans', 
    'standardized_secondary_unit': 'can', 

    'gram_weight': '850.49', 
    'prep': ['drained', 'rinsed'], 
    'size_modifiers': [], 
    'dimensions': [], 
    'is_required': True, 
    'parenthesis_content': ['15 ounce']
}
```

Individual ingredient components can also be found using methods like `food()`, `quantity()`, or `unit()`

```pycon

import ingredient_slicer

slicer = ingredient_slicer.IngredientSlicer("3 tbsp unsalted butter, softened at room temperature")

slicer.food() 
>>> 'unsalted butter'

slicer.quantity() 
>>> '3' 

slicer.unit() 
>>> 'tbsp'

slicer.standardized_unit() 
>>> 'tablespoon'

slicer.prep() 
>>> ['room temperature', 'softened']
```

Contributing/Issues:
-----------------------
If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.