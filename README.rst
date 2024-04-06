ingredient-slicer
------

Python 📦 package for extracting quantities, units, and food words from unstructured recipe ingredients text

Unlike many other recipe ingredient parsers out there, `ingredient-slicer` does not make use of any NLP models or machine learning,
but rather follows a set of rules to parse out quantities, units, and food words from unstructured recipe ingredients text.
`ingredient-slicer` was designed with the intent of providing a robust and lightweight method for parsing recipe ingredients 
text without relying on any external dependencies.
That being said, it is not perfect. 

Table of Contents:
-----------------------
- [Installation](#installation)

<br>

Installation:
-----------------------
`ingredient_slicer` can be downloaded from PyPI via `pip` like so:

.. code:: shell

    pip install ingredient-slicer

then:

.. code:: python

    import ingredient_slicer

    slicer = ingredient_slicer.IngredientSlicer("2 (15-ounces) cans chickpeas, rinsed and drained")

    slicer.to_json()
    {
        'standardized_ingredient': '2 cans chickpeas, rinsed and drained', 
        'food': 'chickpeas', 
        'quantity': '30', 
        'unit': 'ounces', 
        'standardized_unit': 'ounce', 
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

Contributing:
-----------------------
If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.