# Unicode fractions
UNICODE_FRACTIONS = {
    '¼': "1/4",
    '½': "1/2",
    '¾': "3/4",
    '⅐': "1/7",
    '⅑': "1/9",
    '⅒': "1/10",
    '⅓': "1/3",
    '⅔': "2/3",
    '⅕': "1/5",
    '⅖': "2/5",
    '⅗': "3/5",
    '⅘': "4/5",
    '⅙': "1/6",
    '⅚': "5/6",
    '⅛': "1/8",
    '⅜': "3/8",
    '⅝': "5/8",
    '⅞': "7/8",
    '⅟': "1",
    # "⁄": "/"
    '-¼': "-1/4",
    '-½': "-1/2",
    '-¾': "-3/4",
    '-⅐': "-1/7",
    '-⅑': "-1/9",
    '-⅒': "-1/10",
    '-⅓': "-1/3",
    '-⅔': "-2/3",
    '-⅕': "-1/5",
    '-⅖': "-2/5",
    '-⅗': "-3/5",
    '-⅘': "-4/5",
    '-⅙': "-1/6",
    '-⅚': "-5/6",
    '-⅛': "-1/8",
    '-⅜': "-3/8",
    '-⅝': "-5/8",
    '-⅞': "-7/8",
    '-⅟': "-1"
}

# Numbers represented as words
NUMBER_WORDS = {
    'one': 1, 
    'two': 2,
    'three': 3, 
    'four': 4, 
    'five': 5,
    'six': 6, 
    'seven': 7, 
    'eight': 8, 
    'nine': 9, 
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'dozen': 12,  # 12
    'dozens': 12,  # 12
    'baker\'s dozen': 13,  # 13
    'bakers dozen': 13,  # 13
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'hundreds': 100,
    'thousand': 1000
}

NUMBER_PREFIX_WORDS = {
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'hundreds': 100,
    'thousand': 1000
}

# Fractions words representing a single fraction (i.e. a quarter is equal to 1/4)
FRACTION_WORDS = {
    # singular versions
    "half": ("1/2", "0.5"),
    "quarter": ("1/4", "0.25"),
    "third": ("1/3", "0.333"),
    "fourth": ("1/4", "0.25"),
    "fifth": ("1/5", "0.2"),
    "sixth": ("1/6", "0.166"),
    "seventh": ("1/7", "0.142"),
    "eighth": ("1/8", "0.125"),
    "ninth": ("1/9", "0.111"),
    "tenth": ("1/10", "0.1"),
    "eleventh": ("1/11", "0.0909"),
    "twelfth": ("1/12", "0.0833"),
    
    # plural versions
    "halves": ("1/2", "0.5"),
    "quarters": ("1/4", "0.25"),
    "thirds": ("1/3", "0.333"),
    "fourths": ("1/4", "0.25"),
    "fifths": ("1/5", "0.2"),
    "sixths": ("1/6", "0.166"),
    "sevenths": ("1/7", "0.142"),
    "eighths": ("1/8", "0.125"),
    "ninths": ("1/9", "0.111"),
    "tenths": ("1/10", "0.1"),
    "elevenths": ("1/11", "0.0909"),
    "twelfths": ("1/12", "0.0833")
}

UNITS = {
    "a taste" : ("a taste",),
    'bag': ('bag', 'bags'), 
    'bagful': ('bagful', 'bagfuls'), 
    'bottle': ('bottle', 'bottles'), 
    'bottleful': ('bottleful', 'bottlefuls'), 
    'bowl': ('bowl', 'bowls'), 
    'bowlful': ('bowlful', 'bowlfuls'),
    'box': ('box', 'boxes'), 
    'boxful': ('boxful', 'boxfuls'), 
    'breast': ('breast', 'breasts'), 
    'bulb': ('bulb', 'bulbs'), 
    'bun': ('bun', 'buns'), 
    'bunch': ('bunch', 'bunches'), 
    'can': ('can', 'cans'), 
    'canful': ('canful', 'canfuls'), 
    'cheek': ('cheek', 'cheeks'),
    'carton': ('carton', 'cartons'),
    # 'centimeter': ('centimeter', 'centimeters', 'cm', 'cms'),  # TODO: address dimensions
    'container': ('container', 'containers'), 
    'cube': ('cube', 'cubes'), 
    'cup': ('cup', 'cups', "C", "c"),
    'cupful': ('cupful', 'cupfuls'), 
    'cutlet': ('cutlet', 'cutlets'),
    # "dallop" : ("dallop", "dallops", "dollop", "dollops", "a dallop", "a dollop"),
    # "dash" : ("dash", "dashes", "a dash"),
    # "drop" : ("drop", "drops", "a drop"),
    # "droplet" : ("droplet", "droplets", "a droplet"),
    "dallop" : ("dallop", "dallops", "dollop", "dollops"),
    'dash': ('dash', 'dashes'), 
    "drop" : ("drop", "drops"),

    "droplet" : ("droplet", "droplets"),
    'drumstick': ('drumstick', 'drumsticks'), 
    "dusting" : ("dusting", "dustings"),
    'ear': ('ear', 'ears'), 
    'envelope': ('envelope', 'envelopes'), 
    'filet': ('filet', 'filets'), 
    'fillet': ('fillet', 'fillets'), 
    'fluid ounce': ('fluid ounce', 'fluid ounces', 'fl oz', 'fl ozs', 'fluid oz', 'fluid ozs', 'fluid oz', 'fluid ozs'),
    'floret': ('floret', 'florets'),
    # 'foot': ('foot', 'feet', 'ft', 'fts'), # TODO: address dimensions
    'gallon': ('gallon', 'gallons', 'gals', 'gal'), 
    'glass': ('glass', 'glasses'), 
    'gram': ('gram', 'grams', 'grm', 'grms', 'g'), 
    'giblet' : ('giblet', 'giblets'),

    "handful" : ("handful", "handfuls", "handfull", "handfulls"),
    # "handful" : ("handful", "handfuls", "handfull", "handfulls", "a handful"),
    'head': ('head', 'heads'), 
    # 'inch': ('inch', 'inches', 'ins'), # TODO: Removing unit "in" for now, unit "in" needs to be dealt with separately somehow, 
    #                                    # TODO: "in" is used for both the unit "inch" and the standard usage of the word "in" (i.e. "I am in a house")
    # 'inch': ('inch', 'inches', 'in', 'ins'), # Inches unit including the abbreviation "in"
    'jar': ('jar', 'jars'), 
    'jarful': ('jarful', 'jarfuls'), 
    'kilogram': ('kilogram', 'kilograms', 'kg', 'kgs'), 
    'leg': ('leg', 'legs'), 
    'link': ('link', 'links'), 
    'liter': ('liter', 'liters', 'litre', 'litres', 'l'), 
    'loaf': ('loaf', 'loaves'), 
    # 'meter': ('meter', 'meters', 'm', 'ms'), # TODO: address dimensions
    'milligram': ('milligram', 'milligrams', 'mg', 'mgs'), 
    'milliliter': ('milliliter', 'milliliters', 'millilitre', 'millilitres', 'ml', 'mls'), 
    # 'millimeter': ('millimeter', 'millimeters', 'mm', 'mms'), # TODO: address dimensions
    'ounce': ('ounce', 'ounces', 'oz', 'ozs', 'oz.', 'ozs.', 'onz'), 
    'package': ('package', 'packages', 'pkg', 'pkgs'), 
    'packageful': ('packageful', 'packagefuls'), 
    'packet': ('packet', 'packets'), 
    'patty': ('patty', 'patties'), 
    'piece': ('piece', 'pieces'), 
    "pinch" : ("pinch", "pinches", "pinchful", "pinchfuls", "pinchfull", "pinchfulls"),
    # 'pinch': ('pinch', 'pinches'), 
    'pint': ('pint', 'pints', 'pt', 'pts'), 
    'plate': ('plate', 'plates'), 
    'portion': ('portion', 'portions'), 
    'pound': ('pound', 'pounds', 'lbs', 'lb', 'lb.', 'lbs.'),
    'quart': ('quart', 'quarts', 'qt', 'qts'), 
    'rib': ('rib', 'ribs'),
    'ribeye': ('ribeye', 'ribeyes', 'rib eye', 'rib eyes', 'rib-eye', 'rib-eyes'),
    'rim': ('rim', 'rims'), 
    'roll': ('roll', 'rolls'), 
    'round': ('round', 'rounds'),
    'scoop': ('scoop', 'scoops'), 
    'sheet': ('sheet', 'sheets'), 
    'slice': ('slice', 'slices'), 
    "smidgen" : ("smidgen", "smidgens"),
    "sprinkle" : ("sprinkle", "sprinkles", "springkling", "sprinklings"),
    "spear" : ("spear", "spears"),
    # "smidgen" : ("smidgen", "smidgens", "a smidgen"),
    # "sprinkle" : ("sprinkle", "sprinkles", "springkling", "sprinklings", "a sprinkle", "a sprinkling"),
    'sprig': ('sprig', 'sprigs'), 
    'stalk': ('stalk', 'stalks'), 
    'stick': ('stick', 'sticks'), 
    'strip': ('strip', 'strips'), 

    'tablespoon': ('tablespoon', 'tablespoons', 'tbsp', 'tbsps', "tbsp", "tbsps", "tbsp.", "tbsps.", "tbl", "tbls", "tbl.", "tbls.", "T", "tbs", "tbs."), # 'tablespoon': ('tablespoon', 'tablespoons', 'tbsp', 'tbsps', 'tbsp', 'tbsps'), 
    'tablespoonful': ('tablespoonful', 'tablespoonfuls'), 
    "tad" : ("tad", "tads"),
    # "tad" : ("tad", "tads", "a tad"),
    'teaspoon': ('teaspoon', 'teaspoons', 'tsp', 'tsps', "tsp", "tspn", "tspns", "tspn.", "tspns.", "ts", "t", "t."), # 'teaspoon': ('teaspoon', 'teaspoons', 'tsp', 'tsps', "tsp", "t"),
    'teaspoonful': ('teaspoonful', 'teaspoonfuls'), 
    'tender' : ('tender', 'tenders'),
    'tenderloin': ('tenderloin', 'tenderloins'),
    'thigh': ('thigh', 'thighs'),
    "to taste" : ("to taste",), 
    'tongue': ('tongue', 'tongues'),
    "touch" : ("touch", "touches"),
    # "touch" : ("touch", "touches", "a touch"),
    'tube': ('tube', 'tubes'), 
    'wheel': ('wheel', 'wheels'), 
    'wing': ('wing', 'wings')
}

UNITS_SET = set()

# add all of the keys and values to a Hash set to contain all of the volume units words
for key, pattern in UNITS.items():
    UNITS_SET.add(key)
    for val in pattern:
        UNITS_SET.add(val)

# create a hash map that maps every variation of a unit to the standard unit name
UNIT_TO_STANDARD_UNIT = {}

for key, pattern in UNITS.items():
    # print(f"key: {key}, pattern: {pattern}")
    for val in pattern:
        UNIT_TO_STANDARD_UNIT[val] = key

# Only the core basic imperial and metric units (Excludes the more specific units like "stalk", "fillet", "slices", etc.)
BASIC_UNITS = {
    # Imperial volume units
    'teaspoon': ('teaspoon', 'teaspoons', 'tsp', 'tsps', "tsp", "tspn", "tspns", "tspn.", "tspns." , "ts", "t", "t."), # 'teaspoon': ('teaspoon', 'teaspoons', 'tsp', 'tsps', "tsp", "t"),
    'tablespoon': ('tablespoon', 'tablespoons', 'tbsp', 'tbsps', "tbsp", "tbsps", "tbsp.", "tbsps.", "tbl", "tbls", "tbl.", 
                   "tbls.", "T", "tbs", "tbs."),
    'tablespoonful': ('tablespoonful', 'tablespoonfuls'),
    'teaspoonful': ('teaspoonful', 'teaspoonfuls'),
    'cup': ('cup', 'cups', "C", "c"),
    'pint': ('pint', 'pints', "pt", "pts"),
    'quart': ('quart', 'quarts', "qt", "qts"),
    'gallon': ('gallon', 'gallons', "gals", "gal"),
    'fluid ounce': ('fluid ounce', 'fluid ounces', 'fl oz', 'fl ozs',
                    "fluid oz", "fluid ozs", "fluid oz", "fluid ozs"),

    # Metric volume units
    'milliliter': ('milliliter', 'milliliters', 'millilitre', 'millilitres', 'ml', 'mls'), 
    'liter': ('liter', 'liters', 'litre', 'litres', 'l'), 

    # Imperial weight units
    'ounce': ('ounce', 'ounces', 'oz', 'ozs', 'oz.', 'ozs.', 'onz'), 
    'pound': ('pound', 'pounds', 'lbs', 'lb', 'lb.', 'lbs.'),

    # Metric weight units
    'milligram': ('milligram', 'milligrams', 'mg', 'mgs'),
    'gram': ('gram', 'grams', 'grm', 'grms', 'g'),
    'kilogram': ('kilogram', 'kilograms', 'kg', 'kgs'),
}

BASIC_UNITS_SET = set()

# add all of the keys and values to a Hash set to contain all of the basic units words
for key, pattern in BASIC_UNITS.items():
    BASIC_UNITS_SET.add(key)
    for val in pattern:
        BASIC_UNITS_SET.add(val)

# create a non basic units set by subtracting the basic units set from the units set
NON_BASIC_UNITS_SET = UNITS_SET - BASIC_UNITS_SET

# volume units dictionary, things like "cup", "fluid ounce", "gallon", etc.
VOLUME_UNITS = {
    'cup': ('cup', 'cups', "C", "c"),
    'fluid ounce': ('fluid ounce', 'fluid ounces', 'fl oz', 'fl ozs', "fluid oz", "fluid ozs", "fluid oz", "fluid ozs"),
    'gallon': ('gallon', 'gallons', "gals", "gal"),
    'liter': ('liter', 'liters', 'litre', 'litres', 'l'), 
    'milliliter': ('milliliter', 'milliliters', 'millilitre', 'millilitres', 'ml', 'mls'), 
    # 'ounce': ('ounce', 'ounces', 'oz', 'ozs', "oz", "ozs"),
    'pint': ('pint', 'pints', "pt", "pts"),
    'quart': ('quart', 'quarts', "qt", "qts"),
    'tablespoon': ('tablespoon', 'tablespoons', 'tbsp', 'tbsps', "tbsp", "tbsps", "tbsp.", "tbsps.", "tbl", "tbls", "tbl.", "tbls.", "T", "tbs", "tbs."),
    'teaspoon': ('teaspoon', 'teaspoons', 'tsp', 'tsps', "tsp.")
}

VOLUME_UNITS_SET = set()

# add all of the keys and values to a Hash set to contain all of the volume units words
for key, pattern in VOLUME_UNITS.items():
    VOLUME_UNITS_SET.add(key)
    for val in pattern:
        VOLUME_UNITS_SET.add(val)

VOLUME_UNIT_TO_STANDARD_VOLUME_UNIT = {}
for key, pattern in VOLUME_UNITS.items():
    for val in pattern:
        VOLUME_UNIT_TO_STANDARD_VOLUME_UNIT[val] = key

MILLILITER_CONVERSION_FACTORS = {
    'cup': 236.588,          # 1 cup = 236.588 milliliters
    'fluid ounce': 29.5735,  # 1 fluid ounce = 29.5735 milliliters
    'gallon': 3785.41,       # 1 gallon = 3785.41 milliliters
    'liter': 1000,           # 1 liter = 1000 milliliters
    'milliliter': 1,         # 1 milliliter = 1 milliliter
    # 'ounce': 29.5735,        # 1 ounce = 29.5735 milliliters
    'pint': 473.176,         # 1 pint = 473.176 milliliters
    'quart': 946.353,         # 1 quart = 946.353 milliliters
    'tablespoon': 14.7868,   # 1 tablespoon = 14.7868 milliliters
    'teaspoon': 4.92892      # 1 teaspoon = 4.92892 milliliters
}

# dry weight units dictionary, things like "ounce", "pound", "gram", etc.
WEIGHT_UNITS = {
    'ounce': ('ounce', 'ounces', 'oz', 'ozs', 'oz.', 'ozs.', 'onz'), 
    'pound': ('pound', 'pounds', 'lbs', 'lb', 'lb.', 'lbs.'),
    'gram': ('gram', 'grams', 'grm', 'grms', 'g'),
    'kilogram': ('kilogram', 'kilograms', 'kg', 'kgs'),
    'milligram': ('milligram', 'milligrams', 'mg', 'mgs'),
    'microgram': ('microgram', 'micrograms', 'µg', 'mcg', 'mcgs')
}

WEIGHT_UNITS_SET = set()

# add all of the keys and values to a Hash set to contain all of the weight units words
for key, pattern in WEIGHT_UNITS.items():
    WEIGHT_UNITS_SET.add(key)
    for val in pattern:
        WEIGHT_UNITS_SET.add(val)

# create a hash map that maps every variation weight units to the standard weight unit name
WEIGHT_UNIT_TO_STANDARD_WEIGHT_UNIT = {}

for key, pattern in WEIGHT_UNITS.items():
    # print(f"key: {key}, pattern: {pattern}")
    for val in pattern:
        WEIGHT_UNIT_TO_STANDARD_WEIGHT_UNIT[val] = key

GRAM_CONVERSION_FACTORS = {
    'ounce': 28.3495,        # 1 ounce = 28.3495 grams
    'pound': 453.592,        # 1 pound = 453.592 grams
    'gram': 1,               # 1 gram = 1 gram
    'kilogram': 1000,        # 1 kilogram = 1000 grams
    'milligram': 0.001,      # 1 milligram = 0.001 grams
    'microgram': 0.000001    # 1 microgram = 0.000001 grams
}

# dimensions dictioanry, things like "feet", "inches", "centimeters", etc.
DIMENSION_UNITS = {
    'centimeter': ('centimeter', 'centimeters', 'centimetre', 'centimetres', 'cm', 'cms'),
    'foot': ('foot', 'feet', 'ft', 'fts'),
    'inch': ('inch', 'inches'), # TODO: Removing unit "in" for now, unit "in" needs to be dealt with separately somehow, "in" is used for both the unit "inch" and the standard usage of the word "in" (i.e. "I am in a house")
    # 'inch': ('inch', 'inches', 'in', 'ins'),
    # 'inch': ('inch', 'inches', 'ins'), 
    'meter': ('meter', 'meters', 'metre', 'metres', 'm', 'ms'),
    'millimeter': ('millimeter', 'millimeters', 'millimetre', 'millimetres', 'mm', 'mms')
}

DIMENSION_UNITS_SET = set()
for key, pattern in DIMENSION_UNITS.items():
    DIMENSION_UNITS_SET.add(key)
    for val in pattern:
        DIMENSION_UNITS_SET.add(val)

# terms used to describe vague quantities
CASUAL_QUANTITIES = {
    # 'a' : 1,
    # 'an': 1,
    'couple': 2,
    'few': 3,
    'a couple': 2,
    'a few': 3,
}

CASUAL_QUANTITIES_SET = set()
for key, pattern in CASUAL_QUANTITIES.items():
    CASUAL_QUANTITIES_SET.add(key)


# # terms used to describe vague quantities
# CASUAL_QUANTITIES = {
#     # 'a' : 1,
#     # 'an': 1,
#     'couple': 2,
#     'few': 3,
#     'bit': 1,
#     'tiny bit': 1,
#     'handful': 5,
#     'pinch': 1,
#     'dash': 1,
#     'dallop': 1,
#     'drop': 1,
#     "tad": 1,
#     "smidgen": 1,
#     "touch": 1,
#     "to taste": 1,
# }

# terms that are sometimes used as units (i.e. "a pinch of salt")
CASUAL_UNITS = {
    "a taste" : ("a taste",),
    "dash" : ("dash", "dashes"),
    "dallop" : ("dallop", "dallops", "dollop", "dollops"),
    "dusting" : ("dusting", "dustings"),
    "drop" : ("drop", "drops"),
    "droplet" : ("droplet", "droplets"),
    "handful" : ("handful", "handfuls", "handfull", "handfulls"),
    "pinch" : ("pinch", "pinches", "pinchful", "pinchfuls", "pinchfull", "pinchfulls"),
    "tad" : ("tad", "tads"),
    "smidgen" : ("smidgen", "smidgens"),
    "sprinkle" : ("sprinkle", "sprinkles", "springkling", "sprinklings"),
    "to taste" : ("to taste",),
    "touch" : ("touch", "touches"),
    # # NOTE: going back on forth on using units prefixed with "a " or not, for now I'm NOT using them
    # "a taste" : ("a taste"),
    # "bit" : ("bit", "bits"),
    # "dash" : ("dash", "dashes", "a dash"),
    # "dallop" : ("dallop", "dallops", "dollop", "dollops", "a dallop", "a dollop"),
    # "dusting" : ("dusting", "dustings"),
    # "drop" : ("drop", "drops", "a drop"),
    # "droplet" : ("droplet", "droplets", "a droplet"),
    # "handful" : ("handful", "handfuls", "handfull", "handfulls", "a handful"),
    # "pinch" : ("pinch", "pinches", "pinchful", "pinchfuls", "pinchfull", "pinchfulls", "a pinch"),
    # "tad" : ("tad", "tads", "a tad"),
    # "smidgen" : ("smidgen", "smidgens", "a smidgen"),
    # "sprinkle" : ("sprinkle", "sprinkles", "springkling", "sprinklings", "a sprinkle", "a sprinkling"),
    # "touch" : ("touch", "touches", "a touch")
}

CASUAL_UNITS_SET = set()
for key, pattern in CASUAL_UNITS.items():
    CASUAL_UNITS_SET.add(key)
    for val in pattern:
        CASUAL_UNITS_SET.add(val)

# set of units in UNITS that are meat related cuts / portions (i.e. "breast", "cutlet", "drumstick", "filet", "fillet", "leg", "rib", "ribeye", "tenderloin", "thigh", "tongue", "wing"
ANIMAL_PROTEIN_UNITS = { 
    "breast", 
    "cutlet", 
    "drumstick", 
    "filet", 
    "fillet", 
    "giblet", 
    "leg", 
    "patty", 
    "rib", 
    "ribeye", 
    "round", 
    "strip", 
    "tender", 
    "tenderloin", 
    "thigh", 
    "tongue", 
    "wing"
    }

ANIMAL_PROTEIN_UNITS = {
    "breast": ("breast", "breasts"),
    "cutlet": ("cutlet", "cutlets"),
    "drumstick": ("drumstick", "drumsticks"),
    "filet": ("filet", "filets"),
    "fillet": ("fillet", "fillets"),
    "giblet": ("giblet", "giblets"),
    "leg": ("leg", "legs"),
    "patty": ("patty", "patties"),
    "rib": ("rib", "ribs"),
    "ribeye": ("ribeye", "ribeyes", "rib eye", "rib eyes", "rib-eye", "rib-eyes"),
    "round": ("round", "rounds"),
    "strip": ("strip", "strips"),
    "tender": ("tender", "tenders"),
    "tenderloin": ("tenderloin", "tenderloins"),
    "thigh": ("thigh", "thighs"),
    "tongue": ("tongue", "tongues"),
    "wing": ("wing", "wings")
}

ANIMAL_PROTEIN_UNITS_SET = set()

# add all of the keys and values to a Hash set to contain all of the weight units words
for key, pattern in ANIMAL_PROTEIN_UNITS.items():
    ANIMAL_PROTEIN_UNITS_SET.add(key)
    for val in pattern:
        ANIMAL_PROTEIN_UNITS_SET.add(val)

ANIMAL_PROTEIN_UNIT_TO_STANDARD_ANIMAL_PROTEIN_UNIT = {}
for key, pattern in ANIMAL_PROTEIN_UNITS.items():
    for val in pattern:
        ANIMAL_PROTEIN_UNIT_TO_STANDARD_ANIMAL_PROTEIN_UNIT[val] = key

ANIMAL_PROTEIN_UNITS_SET = set()
for key in ANIMAL_PROTEIN_UNITS:
    # print(f"key: {key}")
    ANIMAL_PROTEIN_UNITS_SET.add(key)
    unit_variations = UNITS.get(key, None)
    if unit_variations:
        for unit in unit_variations:
            ANIMAL_PROTEIN_UNITS_SET.add(unit) 

ANIMAL_PROTEIN_UNITS_TO_GRAMS = {
    "breast": 170.1,
    "cutlet": 85.05,
    "drumstick": 113.4,
    "filet": 170.1,
    "fillet": 170.1,
    "giblet": 28.35,
    "leg": 113.4,
    "patty": 113.4,
    "rib": 42.5,
    "ribeye": 226.8,
    "round": 170.1,
    "strip": 85.05,
    "tender": 56.699,
    "tenderloin": 56.699,
    "thigh":  113.4,
    "tongue": 453.592,
    "wing": 56.699
}

# Units that if they appear in a string and there are no "real" units, then these strings might be units
# (i.e. "2 small carrots" -> "quantity: 2, unit: small, ingredient: carrots")
# (i.e. "medium carrot" -> "quantity: 1, unit: medium, ingredient: carrot")
SIZE_MODIFIERS_SET = set((
    "extra small",
    "extra-small",
    "small",
    "smallish",
    "small-ish",
    "medium",
    "mediumish",
    "medium-ish",
    "large",
    "largeish",
    "large-ish",
    # "sm",
    # "med",
    # "lrg",
    "extra large",
    "extra-large",
    "big", 
    "bigish",
    "big-ish",
    "tiny",
    "modest",
    "huge",
    "giant",
    "gigantic"
    ))

PREP_WORDS = {
    'baked',
    'batonnet',
    'batonnetted',
    'beaten',
    'beating',
    'beat',
    'blended',
    'blending',
    'blend',
    'blanch',
    'blanched',
    'blistered',
    'boil',
    'boiled',
    'broil',
    'broiled',
    "chilled",
    'chopped',
    'chopping',
    'cored',
    'cracked',
    'cracking',
    'cooked',
    'crumbled',
    'crushed',
    'cubed',
    'cut',
    'cutting',
    'crisped',
    'deboned',
    'deveined',
    'decored',
    'diced',
    'divided',
    'drained',
    'drenched',
    'dressed',
    'emulsified',
    "even",
    "firm",
    "firmly",
    'flaked',
    'flattened',
    # TODO: not sure if i should have "fresh" and "freshly" in this set, 
    # TODO: they are used in a lot of recipes but they are not really prep words
    'fresh', 
    'freshly', 
    'fried',
    'generous',
    'grated',
    'grilled',
    'ground',
    'grounded',
    'halved',
    'hardened',
    "heaping",
    "heaped",
    "heavy",
    "heavily",
    "hefty",
    'julienned',
    'juiced',
    "level",
    "leveled",
    "light",
    "lightly",
    "lightly packed",
    'mashed',
    "matchstick",
    "matchsticks",
    "matchsticked",
    'melted',
    'minced',
    'packed',
    'peeled',
    'pitted',
    'poached',
    # 'pounded',
    'pressed',
    'pureed',
    'quartered',
    'refrigerate',
    'refrigerated',
    'rinsed',
    'roasted',
    "roughly",
    "round",
    "rounded",
    "room temp",
    "room temperature",
    "scant",
    'scramble',
    'scrambled',
    'scrambling',
    'scrambles',
    'seeded',
    'shredded',
    'sifted',
    'sliced',
    'slivered',
    "smooth",
    "smoothed",
    'smoothly',
    'softened',
    'squeezed',
    'squeeze',
    'squished',
    'steamed',
    'stewed',
    'stirred',
    'stirring',
    'stir',
    'tenderized',
    'thickened',
    "tightly",
    'toasted',
    'trimmed',
    "unsifted",
    'zested'
}

# specific words that are used to describe something about a unit (i.e. "packed cup", "level tablespoon")
# TODO: Probably something to remove at some point, I've split/consilidated values in this set into PREP_WORDS and SIZE_MODIFIERS_SET
UNIT_MODIFIERS = set((
    "round",
    "rounded",
    "level",
    "leveled",
    "heaping",
    "heaped",
    "scant",
    "even",
    "generous",
    "packed",
    "sifted",
    "unsifted",
    "light",
    "lightly",
    "lightly packed",
    "heavy",
    "heavily",
    "firm",
    "firmly",
    "tightly",
    "smooth",
    "hefty",
    "roughly",
    
    "small",
    "medium",
    "large",
    "extra large",
    "extra-large",
    "big", 
    "tiny",
    "modest",
    "huge",
    "giant",
    "gigantic"
))

# specific words that are used to describe something about a unit (i.e. "packed cup", "level tablespoon")
APPROXIMATE_STRINGS = set((
    "about",
    "bout",
    "around",
    "approximately",
    "approx",
    "approx.",
    "appx",
    "appx.",
    "nearly",
    "almost",
    "roughly",
    "estimated",
    "estimate",
    "est.",
    "est",
    "estim", 
    "estim."
))

# phrases that are used to specify the amount of quantity per unit (i.e. "4 lbs each", "about 2 ounces each")
QUANTITY_PER_UNIT_STRINGS = set((
    "each",
    "per",
    "apiece",
    "a piece",
    "per each"
))

# sets of all dashes and hyphens, and sets of dashes that should be removed
DASH_SYMBOLS = set(("-", "‐" "−", "–", "—"))
REMOVABLE_DASH_SYMBOLS = set(("‐" "−", "–", "—"))

TEMPERATURE_UNITS = {
    "celsius": ("celsius", "degree celsius", "degrees celsius", "°C"),
    "fahrenheit": ("fahrenheit", "degree fahrenheit", "degrees fahrenheit", "°F")
}

# ---- Common stop words ----
# - NOTE: Add more as other stop words become known

# generic list of stop words that are not useful for parsing and should be removed from the string
STOP_WORDS = set((
    "0o", "0s", "3a", "3b", "3d", "6b", "6o",
    "a", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst", 
    "ac", "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af", 
    "affected", "affecting", "affects", "after", "afterwards", "ag", "again", "against", "ah", "ain", "ain't", "aj", 
    "al", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", 
    "amongst", "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", 
    "anyone", "anything", "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appear", "appreciate", 
    "appropriate", "approximately", "ar", "are", "aren", "arent", "aren't", "arise", "around", "as", "a's", "aside", 
    "ask", "asking", "associated", "at", "au", "auth", "av", "available", "aw", "away", "awfully", "ax", "ay", "az", 
    
    "b", "b1", "b2", "b3", "ba", "back", "bc", "bd", "be", "became", "because", "become", "becomes", "becoming", 
    "been", "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", 
    "below", "beside", "besides", "best", "better", "between", "beyond", "bi", "bill", "biol", "bj", "bk", "bl", 
    "bn", "both", "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu", "but", "bx", "by", 
    "bitesized", "bitesize", "bite-sized", "bite-size",
    # "c",  "cm",
    "c1", "c2", 
    "c3", "ca", "call", "came", "can", "cannot", "cant", "can't", "cause", "causes", "cc", "cd", "ce", "certain", 
    "certainly", "cf", "cg", "ch", "changes", "ci", "cit", "cj", "cl", "clearly",
    "c'mon", "cn", "co", "com", "come", "comes", "con", "concerning", "consequently", "consider", "considering", "contain", "containing", 
    "contains", "corresponding", "could", "couldn", "couldnt", "couldn't", "course", "cp", "cq", "cr", "cry", "cs", 
    "c's", "ct", "cu", "currently", "cv", "cx", "cy", "cz",
    "d", "d2", "da", "date", "dc", "dd", "de", "definitely", 
    "describe", "described", "despite", "detail", "df", "di", "dia", "diameter", "did", "didn", "didn't", "different", "dj", "dk", "dl", 
    "do", "does", "doesn", "doesn't", "doing", "don", "done", "don't", "down", "downwards", "dp", "dr", "ds", "dt", 
    "du", "due", "during", "dx", "dy", 
    "e", "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee", "ef", "effect", "eg", "ei", "eight", "eighty", "either", 
    "ej", "el", "eleven", "else", "elsewhere", "em", "empty", "en", "end", "ending", "enough", "entirely", "eo", 
    "ep", "eq", "er", "es", "especially", "est", "et", "et-al", "etc", "eu", "ev", "even", "ever", "every", 
    "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "ey", 
    "farmraised", "farm-raised", "farm", "raised",
    "f", "f2", 
    "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire", "first", "five", 
    "fix", "fj", "fl", "fn", "fo", "followed", "following", "follows", "for", "former", "formerly", "forth", 
    "forty", "found", "four", "fr", "from", "front", "frozen", "further", "furthermore", 
    "fs", "ft", "fu", "full", "further", "furthermore", "fy", 
    # "g",
    "ga", "gave", "ge", "get", "gets", "getting", "gi", "give", "given", "gives", "giving", "gj", "gl", 
    "go", "goes", "going", "gone", "got", "gotten", "gr", "greetings", "gs", "gy",
    "h", "h2", "h3", "had", 
    "hadn", "hadn't", "happens", "hardly", "has", "hasn", "hasnt", "hasn't", "have", "haven", "haven't", "having", 
    "he", "hed", "he'd", "he'll", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", 
    "here's", "hereupon", "hers", "herself", "hes", "he's", "hh", "hi", "hid", "him", "himself", "his", "hither", 
    "hj", "ho", "home", "hopefully", "how", "howbeit", "however", "how's", "hr", "hs", "http", "hu", "hundred", "hy",

    "i", "i2", "i3", "i4", "i6", "i7", "i8", "ia", "ib", "ibid", "ic", "id", "i'd", "ie", "if", "ig", "ignored", 
    "ih", "ii", "ij", "il", "i'll", "im", "i'm", "immediate", "immediately", "importance", "important", "in", 
    "inasmuch", "inc", "indeed", "index", "indicate", "indicated", "indicates", "information", "inner", "insofar", 
    "instead", "interest", "into", "invention", "inward", "io", "ip", "iq", "ir", "is", "isn", "isn't", "it", "itd", 
    "it'd", "it'll", "its", "it's", "itself", "iv", "i've", "ix", "iy", "iz", "j", "jj", "jr", "js", "jt", "ju", 
    "just", "k", "ke", "keep", "keeps", "kept", "kg", "kj", "km", "know", "known", "knows", "ko", 
    
    # "l",
    "l2", "la", "largely", "last", "lately", "later", "latter", "latterly", 
    # "lb", 
    "lc", "le", "least", "les", "less", "lest", "lengthwise", "length",
    "let", "lets", "let's", "lf", "like", "liked", "likely", "line", "little", "lj", "ll", "ln", "lo", "lol", "look", 
    "looking", "looks", "los", "lr", "ls", "long", "love", "loved", "loving", "lovingly",
    # "lt", # "ltd", 
    "m2", "ma", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "mean", "means", "meantime", 
    "meanwhile", "merely", "mg", "might", "mightn", "mightn't", 
    "mill", "million", "mine", "miss", 
    "mn", "mo", "more", "moreover", "most", "mostly", "move", "mr", "mrs", 
    "mt", "mu", "much", 
    # "m", "ml",  "ms","mug", 
    "must", "mustn", "mustn't", "my", "myself", 

    "n", "n2", "na", "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "necessary",
    "need", "needn", "needn't", "needs","needed", "neither", "never", "nevertheless", "new", "next", "ng", "ni", "nine", "ninety",
    "nj", "nl", "nn", "no", "nobody", "non", "none", "nonetheless", "noone",  "nor", "normally",
    "nos", "not", "noted", "nothing", "novel", "now", "nowhere", "nr", "ns", "nt", "ny", 

    "o", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often", "og", "oh", "oi", "oj", "ok", 
    "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only", "onto", "oo", "op", "oq", "or", "ord", 
    "os", "ot", "other", "others", "otherwise", "ou", "ought", "our", "ours", "ourselves", "out", "outside", "over", 
    "overall", "ow", "owing", "own", "ox", "oz", 

    "p1", "p2", "p3", "page", "pagecount", "pages", "par", "part", 
    "particular", "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", 
    "pl", "placed", "please", "plus", "pm", "pn", "po", "poorly", "possible", "possibly", "potentially", "pp", "pq", 
    "pr", "predominantly", "present", "presumably", "previously", "primarily", "probably", "promptly", "proud", 
    "provides", "ps", "pt", "pu", "put", "purpose", "purposes", "py",

    "q", "qj", "qu", "que", "quickly", "quite", "qv", 

    "r", "r2", "ra", 
    "ran", "rather", "rc", "rd", "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs", 
    "regarding", "regardless", "regards", "related", "relatively", "research", "research-articl", "respectively", 
    "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", 
    "rt", "ru", "run", "rv", "ry", 
    "s", 
    "s2", "sa", "said", "same", "saw", "say", "saying", "says", "sc", "sd", 
    "se", "sec", "second", "secondly", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", 
    "self", "selves", "sensible", "sent", "serious", "seriously", "served", "serving", "servings", "serves", "serve", "seven", "several", "sf", "shall", "shan", 
    "shan't", "she", "shed", "she'd", "she'll", "shes", "she's", "should", "shouldn", "shouldn't", "should've", 
    "show", "showed", "shown", "showns", "shows", "si", "side", "significant", "significantly", "similar", "similarly", 
    "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so", "some", "somebody", "somehow", 
    "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", 
    "specifically", "specified", "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", 
    "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sum", "summary", 
    "sure", "sy", "system", "sz",

    # "t", 
    "t1", "t2", "t3", "take", "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th", 
    "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "that've", "thaw", "thawed", 
    "the", "their", "theirs", 
    "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", 
    "there'll", "thereof", "therere", "theres", "there's", "thereto", "thereupon", "there've", "these", "they", 
    "theyd", "they'd", "they'll", "theyre", "they're", "they've", "thickv", "thin", "think", "third", "this", 
    "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three", "throug", "through", 
    "throughout", "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together", "too", "took", 
    "top", "topping", "toward", "towards", "tp", "tq", "tr", "tried", "tries", "truly", "try", "trying", 
    # "ts",
    "t's", "tt", "tv", "twelve", "twenty", "twice", "two", "tx", 
    "u", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under", "unfortunately", "unless", 
    "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur", "us", "use", 
    "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "ut", 
    # "v", 
    "va", "value", "various", "vd", "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", 
    # "w", 
    "wa", "want", "wants", "was", "wasn", "wasnt", "wasn't", "way", "we", "wed", "we'd", "welcome", "well", "we'll", 
    "well-b", "went", "were", "we're", "weren", "werent", "weren't", "we've", "what", "whatever", "what'll", 
    "whats", "what's", "when", "whence", "whenever", "when's", "where", "whereafter", "whereas", "whereby", 
    "wherein", "wheres", "where's", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", 
    "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos", "who's", "whose", "why", "why's", "wi", 
    "widely", "will", "willing", "wish", "with", "within", "without", "wo", 
    "won", 
    "wonder", "wont", "won't", 
    "words", "world", "would", "wouldn", "wouldnt", "wouldn't", "www", 
    "x", "x1", "x2", "x3", "xf", "xi", "xj", 
    "xk", "xl", "xn", "xo", "xox", "xoxo", "xs", "xt", "xv", "xx",
    "y", "y2", "yall", "ya'll", "y'all", "yes", "yet", "yj", "yl", "you", "youd", "you'd", 
    "you'll", "your", "youre", "you're", "yours", "yourself", "yourselves", "you've", "yr", "ys", "yt", 
    "z", "zero", "zi", "zz", "zip", "zips", "zipped", "zipping", "zipper"
))

# -----------------------------------------------------------------------------------------------------
# ---- Map of common foods to a primary and secondary food category ----
# - this is a somewhat exhaustive list, this could always be added to more 
# - Key-value format:
#      "food" : ("primary_category", "secondary_category")
# -----------------------------------------------------------------------------------------------------

FOOD_CATALOG = {

            # -------------------------------------------------------------------------------------------------------
            # ----- Vegetables ("vegetables") -----
            # -------------------------------------------------------------------------------------------------------

            # VEGETABLES
            "onion": ("vegetables", "bulb"),
            "onions": ("vegetables", "bulb"),
            "shallot": ("vegetables", "bulb"),
            "shallots": ("vegetables", "bulb"),
            "green onion": ("vegetables", "bulb"),
            "green onions": ("vegetables", "bulb"),
            "red onion": ("vegetables", "bulb"),
            "red onions": ("vegetables", "bulb"),
            "yellow onion": ("vegetables", "bulb"),
            "yellow onions": ("vegetables", "bulb"),
            "white onion": ("vegetables", "bulb"),
            "white onions": ("vegetables", "bulb"),
            "sweet onion": ("vegetables", "bulb"),
            "sweet onions": ("vegetables", "bulb"),
            "pearl onion": ("vegetables", "bulb"),
            "pearl onions": ("vegetables", "bulb"),
            "cipollini onion": ("vegetables", "bulb"),
            "cipollini onions": ("vegetables", "bulb"),
            "leek": ("vegetables", "bulb"),
            "leeks": ("vegetables", "bulb"),
            "scallion": ("vegetables", "bulb"),
            "scallions": ("vegetables", "bulb"),
            "garlic": ("vegetables", "bulb"),
            "celery": ("vegetables", "stem"),
            "tomato": ("vegetables", "fruit"),
            "tomatoes": ("vegetables", "fruit"),
            "tomato paste": ("vegetables", "fruit"),
            "cherry tomato": ("vegetables", "fruit"),
            "cherry tomatoes": ("vegetables", "fruit"),
            "asparagus": ("vegetables", "stem"),
            "kale": ("vegetables", "leafy"),
            "spinach": ("vegetables", "leafy"),
            "broccoli": ("vegetables", "cruciferous"),
            "broccolini": ("vegetables", "cruciferous"),
            "broccolis": ("vegetables", "cruciferous"),
            "broccolinis": ("vegetables", "cruciferous"),
            "broccoli rabe": ("vegetables", "cruciferous"),
            "broccoli raab": ("vegetables", "cruciferous"),
            "cauliflower": ("vegetables", "cruciferous"),
            "cauliflower rice": ("vegetables", "cruciferous"),
            "brussel sprout": ("vegetables", "cruciferous"),
            "brussel sprouts": ("vegetables", "cruciferous"),
            "brussels sprouts": ("vegetables", "cruciferous"),
            "brussel sprouts": ("vegetables", "cruciferous"),
            "lettuce": ("vegetables", "leafy"),
            "romaine lettuce": ("vegetables", "leafy"),
            "iceberg lettuce": ("vegetables", "leafy"),
            "butter lettuce": ("vegetables", "leafy"),
            "boston lettuce": ("vegetables", "leafy"),
            "bibb lettuce": ("vegetables", "leafy"),
            "butter head lettuce": ("vegetables", "leafy"),
            "mixed greens": ("vegetables", "leafy"),
            "arugula": ("vegetables", "leafy"),
            "endive": ("vegetables", "leafy"),
            "endives": ("vegetables", "leafy"),
            "radicchio": ("vegetables", "leafy"),
            "radish": ("vegetables", "root"),
            "radishes": ("vegetables", "root"),
            "turnip": ("vegetables", "root"),
            "turnips": ("vegetables", "root"),
            "artichoke": ("vegetables", "flower"),
            "artichokes": ("vegetables", "flower"),
            "cabbage": ("vegetables", "cruciferous"),
            "serrano chiles" : ("vegetables", "fruit"),
            "jalapeno chiles" : ("vegetables", "fruit"),
            "poblano chiles" : ("vegetables", "fruit"),
            "habanero chiles" : ("vegetables", "fruit"),
            "serrano pepper" : ("vegetables", "fruit"),
            "jalapeno pepper" : ("vegetables", "fruit"),
            "poblano pepper" : ("vegetables", "fruit"),
            "habanero pepper" : ("vegetables", "fruit"),
            "bell pepper": ("vegetables", "fruit"),
            "bell peppers": ("vegetables", "fruit"),
            "yellow bell pepper": ("vegetables", "fruit"),
            "yellow bell peppers": ("vegetables", "fruit"),
            "red bell pepper": ("vegetables", "fruit"),
            "red bell peppers": ("vegetables", "fruit"),
            "green bell pepper": ("vegetables", "fruit"),
            "green bell peppers": ("vegetables", "fruit"),
            "jalapeno": ("vegetables", "fruit"),
            "jalapenos": ("vegetables", "fruit"),
            "poblano": ("vegetables", "fruit"),
            "poblanos": ("vegetables", "fruit"),
            "habanero": ("vegetables", "fruit"),
            "habaneros": ("vegetables", "fruit"),
            "serrano": ("vegetables", "fruit"),
            "serranos": ("vegetables", "fruit"),
            "cucumber": ("vegetables", "fruit"),
            "cucumbers": ("vegetables", "fruit"),
            "ghost pepper": ("vegetables", "fruit"),
            "ghost peppers": ("vegetables", "fruit"),
            "carolina reaper": ("vegetables", "fruit"),
            "carolina reapers": ("vegetables", "fruit"),
            "mushroom": ("vegetables", "fungi"),
            "mushrooms": ("vegetables", "fungi"),
            "cremini mushroom": ("vegetables", "fungi"),
            "cremini mushrooms": ("vegetables", "fungi"),
            "portobello mushroom": ("vegetables", "fungi"),
            "portobello mushrooms": ("vegetables", "fungi"),
            "shiitake mushroom": ("vegetables", "fungi"),
            "shiitake mushrooms": ("vegetables", "fungi"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Tubers & products ("tubers_and_products") -----
            # -------------------------------------------------------------------------------------------------------

            # Tubers and products
            "potato": ("tubers_and_products", "tuber"),
            "potatoes": ("tubers_and_products", "tuber"),
            "potatoe": ("tubers_and_products", "tuber"),
            "potatos": ("tubers_and_products", "tuber"),
            "russet potato": ("tubers_and_products", "tuber"),
            "russet potatoes": ("tubers_and_products", "tuber"),
            "russet potatos": ("tubers_and_products", "tuber"),
            "yukon gold potato": ("tubers_and_products", "tuber"),
            "yukon gold potatoes": ("tubers_and_products", "tuber"),
            "yukon gold potatos": ("tubers_and_products", "tuber"),
            "fingerling potato": ("tubers_and_products", "tuber"),
            "fingerling potatoes": ("tubers_and_products", "tuber"),
            "fingerling potatos": ("tubers_and_products", "tuber"),
            "sweet potato": ("tubers_and_products", "tuber"),
            "sweet potatoes": ("tubers_and_products", "tuber"),
            "sweet potatos": ("tubers_and_products", "tuber"),
            "yam": ("tubers_and_products", "tuber"),
            "yams": ("tubers_and_products", "tuber"),
            "cassava": ("tubers_and_products", "tuber"),
            "cassavas": ("tubers_and_products", "tuber"),
            "beet": ("tubers_and_products", "root"),
            "beets": ("tubers_and_products", "root"),
            "carrot": ("tubers_and_products", "root"),
            "carrots": ("tubers_and_products", "root"),
            "baby carrot": ("tubers_and_products", "root"),
            "baby carrots": ("tubers_and_products", "root"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Legumes ("legumes") -----
            # -------------------------------------------------------------------------------------------------------

            # LEGUMES
            "bean": ("legumes", "bean"),
            "beans": ("legumes", "bean"),
            "black bean": ("legumes", "bean"),
            "black beans": ("legumes", "bean"),
            "kidney bean": ("legumes", "bean"),
            "kidney beans": ("legumes", "bean"),
            "pinto bean": ("legumes", "bean"),
            "pinto beans": ("legumes", "bean"),
            "cannellini bean": ("legumes", "bean"),
            "cannellini beans": ("legumes", "bean"),
            "refried bean": ("legumes", "bean"),
            "refried beans": ("legumes", "bean"),
            "white bean": ("legumes", "bean"),
            "white beans": ("legumes", "bean"),
            "fava bean": ("legumes", "bean"),
            "fava beans": ("legumes", "bean"),
            "navy bean": ("legumes", "bean"),
            "navy beans": ("legumes", "bean"),
            "lima bean": ("legumes", "bean"),
            "lima beans": ("legumes", "bean"),
            "soybean": ("legumes", "bean"),
            "soybeans": ("legumes", "bean"),
            "edamame": ("legumes", "bean"),
            "edamames": ("legumes", "bean"),

            "lentil": ("legumes", "lentil"),
            "lentils": ("legumes", "lentil"),
            "red lentil": ("legumes", "lentil"),
            "red lentils": ("legumes", "lentil"),
            "green lentil": ("legumes", "lentil"),
            "green lentils": ("legumes", "lentil"),
            "brown lentil": ("legumes", "lentil"),
            "brown lentils": ("legumes", "lentil"),
            "yellow lentil": ("legumes", "lentil"),
            "yellow lentils": ("legumes", "lentil"),
            "black lentil": ("legumes", "lentil"),
            "black lentils": ("legumes", "lentil"),
            "french lentil": ("legumes", "lentil"),
            "french lentils": ("legumes", "lentil"),
            "puy lentil": ("legumes", "lentil"),
            "puy lentils": ("legumes", "lentil"),
            "canned lentil": ("legumes", "lentil"),
            "canned lentils": ("legumes", "lentil"),

            "peas": ("legumes", "peas"),
            "green pea": ("legumes", "pea"),
            "green peas": ("legumes", "pea"),
            "split pea": ("legumes", "pea"),
            "split peas": ("legumes", "pea"),
            "black-eyed pea": ("legumes", "pea"),
            "black-eyed peas": ("legumes", "pea"),
            "black eyed pea": ("legumes", "pea"),
            "black eyed peas": ("legumes", "pea"),
            "blackeyed peas": ("legumes", "pea"),
            "blackeyed pea": ("legumes", "pea"),

            "chickpea": ("legumes", "pea"),
            "chickpeas": ("legumes", "pea"),
            "garbanzo": ("legumes", "bean"),
            "garbanzos": ("legumes", "bean"),
            "garbanzo bean": ("legumes", "pea"),
            "garbanzo beans": ("legumes", "pea"), 
            "can of chickpea": ("legumes", "pea"),
            "can of chickpeas": ("legumes", "pea"),
            "canned chickpea": ("legumes", "pea"),
            "canned chickpeas": ("legumes", "pea"),
            "canned garbanzo": ("legumes", "pea"),
            "canned garbanzos": ("legumes", "pea"),
            "can of garbanzo": ("legumes", "pea"),
            "can of garbanzos": ("legumes", "pea"),
            "can of garbanzo bean": ("legumes", "pea"),
            "can of garbanzo beans": ("legumes", "pea"),
            "canned garbanzo bean": ("legumes", "pea"),
            "canned garbanzo beans": ("legumes", "pea"),
            "snow pea": ("legumes", "pea"),
            "snow peas": ("legumes", "pea"),
            "snowpea": ("legumes", "pea"),
            "snowpeas": ("legumes", "pea"),
            "sugar snap pea": ("legumes", "pea"),
            "sugar snap peas": ("legumes", "pea"),
            "snap pea": ("legumes", "pea"),
            "snap peas": ("legumes", "pea"),
            "field pea": ("legumes", "pea"),
            "field peas": ("legumes", "pea"),
            "cowpea": ("legumes", "pea"),
            "cowpeas": ("legumes", "pea"),
            "yellow pea": ("legumes", "pea"),
            "yellow peas": ("legumes", "pea"),
            "garden pea": ("legumes", "pea"),
            "garden peas": ("legumes", "pea"),
            "pea shoot": ("legumes", "pea"),
            "pea shoots": ("legumes", "pea"),
            "green bean": ("legumes", "bean"),
            "green beans": ("legumes", "bean"),
            "green-bean": ("legumes", "bean"),
            "green-beans": ("legumes", "bean"),
            
            # -------------------------------------------------------------------------------------------------------
            # ----- Meat & meat products ("meat_and_meat_products") -----
            # -------------------------------------------------------------------------------------------------------

            # MEATS
            "chicken": ("meat_and_meat_products", "poultry"),
            "skinless boneless chicken": ("meat_and_meat_products", "poultry"),
            "skinless chicken": ("meat_and_meat_products", "poultry"),
            "boneless chicken": ("meat_and_meat_products", "poultry"),
            "chicken skinless": ("meat_and_meat_products", "poultry"),
            "chicken boneless": ("meat_and_meat_products", "poultry"),
            "chicken skinless boneless": ("meat_and_meat_products", "poultry"),
            "chicken breast": ("meat_and_meat_products", "poultry"),
            "chicken breasts": ("meat_and_meat_products", "poultry"),
            "chicken thigh": ("meat_and_meat_products", "poultry"),
            "chicken thighs": ("meat_and_meat_products", "poultry"),
            "chicken leg": ("meat_and_meat_products", "poultry"),
            "chicken legs": ("meat_and_meat_products", "poultry"),
            "chicken wing": ("meat_and_meat_products", "poultry"),
            "chicken wings": ("meat_and_meat_products", "poultry"),
            "turkey": ("meat_and_meat_products", "poultry"),
            "turkey breast": ("meat_and_meat_products", "poultry"),
            "turkey breasts": ("meat_and_meat_products", "poultry"),
            "turkey thigh": ("meat_and_meat_products", "poultry"),
            "turkey thighs": ("meat_and_meat_products", "poultry"),
            "turkey leg": ("meat_and_meat_products", "poultry"),
            "turkey legs": ("meat_and_meat_products", "poultry"),
            "turkey wing": ("meat_and_meat_products", "poultry"),
            "turkey wings": ("meat_and_meat_products", "poultry"),
            "turkey bacon": ("meat_and_meat_products", "poultry"),
            "turkey sausage": ("meat_and_meat_products", "poultry"),
            "duck": ("meat_and_meat_products", "poultry"),
            "duck breast": ("meat_and_meat_products", "poultry"),
            "duck breasts": ("meat_and_meat_products", "poultry"),
            "duck thigh": ("meat_and_meat_products", "poultry"),
            "duck thighs": ("meat_and_meat_products", "poultry"),
            "duck leg": ("meat_and_meat_products", "poultry"),
            "duck legs": ("meat_and_meat_products", "poultry"),
            "duck wing": ("meat_and_meat_products", "poultry"),
            "duck wings": ("meat_and_meat_products", "poultry"),
            "duck bacon": ("meat_and_meat_products", "poultry"),
            "duck sausage": ("meat_and_meat_products", "poultry"),
            "quail": ("meat_and_meat_products", "poultry"),
            "quail breast": ("meat_and_meat_products", "poultry"),
            "quail breasts": ("meat_and_meat_products", "poultry"),
            "quail thigh": ("meat_and_meat_products", "poultry"),
            "quail thighs": ("meat_and_meat_products", "poultry"),
            "quail leg": ("meat_and_meat_products", "poultry"),
            "quail legs": ("meat_and_meat_products", "poultry"),
            "quail wing": ("meat_and_meat_products", "poultry"),
            "quail wings": ("meat_and_meat_products", "poultry"),

            "beef": ("meat_and_meat_products", "beef"),
            "grass-fed beef": ("meat_and_meat_products", "beef"),
            "grassfed beef": ("meat_and_meat_products", "beef"),
            "grass fed beef": ("meat_and_meat_products", "beef"),
            "ground beef": ("meat_and_meat_products", "beef"),
            "grass-fed ground beef": ("meat_and_meat_products", "beef"),
            "grassfed ground beef": ("meat_and_meat_products", "beef"),
            "grass fed ground beef": ("meat_and_meat_products", "beef"),
            "hamburger": ("meat_and_meat_products", "beef"),
            "hamburgers": ("meat_and_meat_products", "beef"),
            "hamburger patty": ("meat_and_meat_products", "beef"),
            "hamburger patties": ("meat_and_meat_products", "beef"),
            "steak": ("meat_and_meat_products", "beef"),
            "steaks": ("meat_and_meat_products", "beef"),
            "beef chuck": ("meat_and_meat_products", "beef"),
            "beef brisket": ("meat_and_meat_products", "beef"),
            "beef shank": ("meat_and_meat_products", "beef"),
            "beef sirloin": ("meat_and_meat_products", "beef"),
            "beef tenderloin": ("meat_and_meat_products", "beef"),
            "beef loin": ("meat_and_meat_products", "beef"),
            "beef short loin": ("meat_and_meat_products", "beef"),
            "beef ribeye": ("meat_and_meat_products", "beef"),
            "beef ribeyes": ("meat_and_meat_products", "beef"),
            "beef liver": ("meat_and_meat_products", "beef"),
            "beef tongue": ("meat_and_meat_products", "beef"),
            "beef round": ("meat_and_meat_products", "beef"),
            "beef rib": ("meat_and_meat_products", "beef"),
            "beef ribs": ("meat_and_meat_products", "beef"),
            "beef cheek": ("meat_and_meat_products", "beef"),
            "beef cheeks": ("meat_and_meat_products", "beef"),
            "t-bone steak": ("meat_and_meat_products", "beef"),
            "T-bone steaks": ("meat_and_meat_products", "beef"),
            "filet mignon": ("meat_and_meat_products", "beef"),
            "filet mignons": ("meat_and_meat_products", "beef"),
            "new york strip": ("meat_and_meat_products", "beef"),
            "new york strips": ("meat_and_meat_products", "beef"),
            "ribeye steak": ("meat_and_meat_products", "beef"),
            "ribeye steaks": ("meat_and_meat_products", "beef"),
            "sirloin steak": ("meat_and_meat_products", "beef"),
            "sirloin steaks": ("meat_and_meat_products", "beef"),
            "flank steak": ("meat_and_meat_products", "beef"),
            "flank steaks": ("meat_and_meat_products", "beef"),
            "skirt steak": ("meat_and_meat_products", "beef"),
            "skirt steaks": ("meat_and_meat_products", "beef"),
            "hanger steak": ("meat_and_meat_products", "beef"),
            "hanger steaks": ("meat_and_meat_products", "beef"),
            "porterhouse steak": ("meat_and_meat_products", "beef"),
            "porterhouse steaks": ("meat_and_meat_products", "beef"),
            "chuck steak": ("meat_and_meat_products", "beef"),
            "chuck steaks": ("meat_and_meat_products", "beef"),
            "brisket": ("meat_and_meat_products", "beef"),

            "bacon": ("meat_and_meat_products", "pork"),
            "bacon strips": ("meat_and_meat_products", "pork"),
            "bacon slice": ("meat_and_meat_products", "pork"),
            "bacon bits": ("meat_and_meat_products", "pork"),
            "pork": ("meat_and_meat_products", "pork"),
            "pork chop": ("meat_and_meat_products", "pork"),
            "pork chops": ("meat_and_meat_products", "pork"),
            "pork tenderloin": ("meat_and_meat_products", "pork"),
            "pork tenderloins": ("meat_and_meat_products", "pork"),
            "pork loin": ("meat_and_meat_products", "pork"),
            "pork loins": ("meat_and_meat_products", "pork"),
            "pork shoulder": ("meat_and_meat_products", "pork"),
            "pork shoulders": ("meat_and_meat_products", "pork"),
            "pork belly": ("meat_and_meat_products", "pork"),
            "pork bellies": ("meat_and_meat_products", "pork"),
            "pork butt": ("meat_and_meat_products", "pork"),
            "pork butts": ("meat_and_meat_products", "pork"),
            "pork rib": ("meat_and_meat_products", "pork"),
            "pork ribs": ("meat_and_meat_products", "pork"),
            "pork sausage": ("meat_and_meat_products", "pork"),
            "pork sausages": ("meat_and_meat_products", "pork"),
            
            "lamb": ("meat_and_meat_products", "lamb"),
            "lamb chop": ("meat_and_meat_products", "lamb"),
            "lamb chops": ("meat_and_meat_products", "lamb"),
            "lamb shank": ("meat_and_meat_products", "lamb"),
            "lamb shanks": ("meat_and_meat_products", "lamb"),
            "lamb cutlet": ("meat_and_meat_products", "lamb"),
            "lamb cutlets": ("meat_and_meat_products", "lamb"),
            "lamb leg": ("meat_and_meat_products", "lamb"),
            "lamb legs": ("meat_and_meat_products", "lamb"),

            "venison": ("meat_and_meat_products", "venison"),
            "venison chop": ("meat_and_meat_products", "venison"),
            "venison chops": ("meat_and_meat_products", "venison"),
            "venison shank": ("meat_and_meat_products", "venison"),
            "venison shanks": ("meat_and_meat_products", "venison"),
            "venison loin": ("meat_and_meat_products", "venison"),
            "venison loins": ("meat_and_meat_products", "venison"),
            "venison tenderloin": ("meat_and_meat_products", "venison"),
            "venison tenderloins": ("meat_and_meat_products", "venison"),
            "venison shoulder": ("meat_and_meat_products", "venison"),
            "venison shoulders": ("meat_and_meat_products", "venison"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Meat substitutes, classified as misc. ("legumes") -----
            # -------------------------------------------------------------------------------------------------------

            # TODO: Meat substitutes (not sure how to handle this as it relates to density groups)
            "tofu": ("legumes", "meat substitute"),
            "tofus": ("legumes", "meat substitute"),
            "tofu block": ("legumes", "meat substitute"),
            "tofu blocks": ("legumes", "meat substitute"),
            "tofu burger": ("legumes", "meat substitute"),
            "tofu burgers": ("legumes", "meat substitute"),
            "tofu bacon": ("legumes", "meat substitute"),
            "tempeh": ("legumes", "meat substitute"),
            "seitan": ("legumes", "meat substitute"),
            "soy protein": ("legumes", "meat substitute"),
            "soy protein powder": ("legumes", "meat substitute"),
            "soy protein isolate": ("legumes", "meat substitute"),
            "pea protein": ("legumes", "meat substitute"),
            "tofurkey": ("legumes", "meat substitute"),
            "tofurkey sausage": ("legumes", "meat substitute"),
            "tofurkey sausages": ("legumes", "meat substitute"),
            "impossible burger": ("legumes", "meat substitute"),
            "impossible burgers": ("legumes", "meat substitute"),
            "impossible meat": ("legumes", "meat substitute"),
            "impossible meats": ("legumes", "meat substitute"),
            "impossible sausage": ("legumes", "meat substitute"),
            "impossible sausages": ("legumes", "meat substitute"),
            "beyond burger": ("legumes", "meat substitute"),
            "beyond burgers": ("legumes", "meat substitute"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Fish & Fish products ("fish_and_fish_products") -----
            # -------------------------------------------------------------------------------------------------------

            # SEAFOOD
            "salmon": ("fish_and_fish_products", "fish"),
            "swordfish": ("fish_and_fish_products", "fish"),
            "shark": ("fish_and_fish_products", "fish"),
            "sea bass": ("fish_and_fish_products", "fish"),
            "catfish": ("fish_and_fish_products", "fish"),
            "halibut": ("fish_and_fish_products", "fish"),
            "cod": ("fish_and_fish_products", "fish"),
            "tuna": ("fish_and_fish_products", "fish"),
            "trout": ("fish_and_fish_products", "fish"),
            "snapper": ("fish_and_fish_products", "fish"),
            "mahi mahi": ("fish_and_fish_products", "fish"),
            "mackerel": ("fish_and_fish_products", "fish"),
            "sardine": ("fish_and_fish_products", "fish"),
            "sardines": ("fish_and_fish_products", "fish"),
            "anchovy": ("fish_and_fish_products", "fish"),
            "anchovies": ("fish_and_fish_products", "fish"),
            "herring": ("fish_and_fish_products", "fish"),
            "carp": ("fish_and_fish_products", "fish"),
            "tilapia": ("fish_and_fish_products", "fish"),
            "can of tuna": ("fish_and_fish_products", "fish"),
            "canned tuna": ("fish_and_fish_products", "fish"),
            "can of salmon": ("fish_and_fish_products", "fish"),
            "canned salmon": ("fish_and_fish_products", "fish"),
            "clam": ("fish_and_fish_products", "shellfish"),
            "clams": ("fish_and_fish_products", "shellfish"),
            "mussels": ("fish_and_fish_products", "shellfish"),
            "shrimp": ("fish_and_fish_products", "shellfish"),
            "lobster": ("fish_and_fish_products", "shellfish"),
            "lobsters": ("fish_and_fish_products", "shellfish"),
            "crab": ("fish_and_fish_products", "shellfish"),
            "crabs": ("fish_and_fish_products", "shellfish"),
            "imitation crab": ("fish_and_fish_products", "shellfish"),
            "oyster": ("fish_and_fish_products", "shellfish"),
            "oysters": ("fish_and_fish_products", "shellfish"),
            "scallop": ("fish_and_fish_products", "shellfish"),
            "scallops": ("fish_and_fish_products", "shellfish"),
            # # Old shellfish group
            # "clam": ("meat_and_meat_products", "shellfish"),
            # "clams": ("meat_and_meat_products", "shellfish"),
            # "mussels": ("meat_and_meat_products", "shellfish"),
            # "shrimp": ("meat_and_meat_products", "shellfish"),
            # "lobster": ("meat_and_meat_products", "shellfish"),
            # "lobsters": ("meat_and_meat_products", "shellfish"),
            # "crab": ("meat_and_meat_products", "shellfish"),
            # "crabs": ("meat_and_meat_products", "shellfish"),
            # "imitation crab": ("meat_and_meat_products", "shellfish"),
            # "oyster": ("meat_and_meat_products", "shellfish"),
            # "oysters": ("meat_and_meat_products", "shellfish"),
            # "scallop": ("meat_and_meat_products", "shellfish"),
            # "scallops": ("meat_and_meat_products", "shellfish"),
            # # Old egg group
            # "egg": ("meat_and_meat_products", "egg"),
            # "eggs": ("meat_and_meat_products", "egg"),
            # "egg yolk": ("meat_and_meat_products", "egg"),
            # "egg yolks": ("meat_and_meat_products", "egg"),
            # "egg white": ("meat_and_meat_products", "egg"),
            # "egg whites": ("meat_and_meat_products", "egg"),
            # "chicken egg": ("meat_and_meat_products", "egg"),
            # "chicken eggs": ("meat_and_meat_products", "egg"),
            # "duck egg": ("meat_and_meat_products", "egg"),
            # "duck eggs": ("meat_and_meat_products", "egg"),
            # "quail egg": ("meat_and_meat_products", "egg"),
            # "quail eggs": ("meat_and_meat_products", "egg"),


            # -------------------------------------------------------------------------------------------------------
            # ----- Egg & egg products ("egg_and_egg_products") -----
            # -------------------------------------------------------------------------------------------------------

            # EGG PRODUCTS
            "egg": ("egg_and_egg_products", "egg"),
            "eggs": ("egg_and_egg_products", "egg"),
            "egg yolk": ("egg_and_egg_products", "egg"),
            "egg yolks": ("egg_and_egg_products", "egg"),
            "egg white": ("egg_and_egg_products", "egg"),
            "egg whites": ("egg_and_egg_products", "egg"),
            "chicken egg": ("egg_and_egg_products", "egg"),
            "chicken eggs": ("egg_and_egg_products", "egg"),
            "duck egg": ("egg_and_egg_products", "egg"),
            "duck eggs": ("egg_and_egg_products", "egg"),
            "quail egg": ("egg_and_egg_products", "egg"),
            "quail eggs": ("egg_and_egg_products", "egg"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Milk ("milk") -----
            # -------------------------------------------------------------------------------------------------------

            # MILK
            "milk": ("milk", "milk"),
            "whole milk": ("milk", "milk"),
            "skim milk": ("milk", "milk"),
            "nonfat milk": ("milk", "milk"),
            "2% milk": ("milk", "milk"),
            "1% milk": ("milk", "milk"),

            # MILK ALTERNATIVES
            "almond milk": ("milk", "milk substitute"),
            "unsweetened almond milk": ("milk", "milk substitute"),
            "sweetened almond milk": ("milk", "milk substitute"),
            "unsweetened vanilla almond milk": ("milk", "milk substitute"),
            "sweetened vanilla almond milk": ("milk", "milk substitute"),
            "cashew milk": ("milk", "milk substitute"),
            "unsweetened cashew milk": ("milk", "milk substitute"),
            "sweetened cashew milk": ("milk", "milk substitute"),
            "unsweetened vanilla cashew milk": ("milk", "milk substitute"),
            "sweetened vanilla cashew milk": ("milk", "milk substitute"),
            "rice milk": ("milk", "milk substitute"),
            "soy milk": ("milk", "milk substitute"),
            "coconut milk": ("milk", "milk substitute"),
            "oat milk": ("milk", "milk substitute"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Dairy ("dairy_products") -----
            # -------------------------------------------------------------------------------------------------------

            # DAIRY
            "butter": ("dairy_products", "butter"),
            "clarified butter": ("dairy_products", "butter"),
            "unsalted butter": ("dairy_products", "butter"),
            "salted butter": ("dairy_products", "butter"),
            "heavy whipping cream": ("dairy_products", "cream"),
            "half and half": ("dairy_products", "cream"),
            "half & half": ("dairy_products", "cream"),
            "half n half": ("dairy_products", "cream"),
            "halfnhalf": ("dairy_products", "cream"),
            "half-and-half": ("dairy_products", "cream"),
            "half-n-half": ("dairy_products", "cream"),
            "half and half cream": ("dairy_products", "cream"),
            "whipped cream": ("dairy_products", "cream"),
            "light whipped cream": ("dairy_products", "cream"),
            "lowfat whipped cream": ("dairy_products", "cream"),
            "margarine": ("dairy_products", "butter"),
            "cheese": ("dairy_products", "cheese"),
            "crumbled cheese": ("dairy_products", "cheese"),
            "shredded cheese": ("dairy_products", "cheese"),
            "bleu cheese": ("dairy_products", "cheese"),
            "parmesan cheese": ("dairy_products", "cheese"),
            "shredded parmesan cheese": ("dairy_products", "cheese"),
            "cheddar cheese": ("dairy_products", "cheese"),
            "shredded cheddar cheese": ("dairy_products", "cheese"),
            "mozzarella cheese": ("dairy_products", "cheese"),
            "shredded mozzarella cheese": ("dairy_products", "cheese"),
            "feta cheese": ("dairy_products", "cheese"),
            "goat cheese": ("dairy_products", "cheese"),
            "gorgonzola cheese": ("dairy_products", "cheese"),
            "provolone cheese": ("dairy_products", "cheese"),
            "swiss cheese": ("dairy_products", "cheese"),
            "american cheese": ("dairy_products", "cheese"),
            "pepper jack cheese": ("dairy_products", "cheese"),
            "monterey jack cheese": ("dairy_products", "cheese"),
            "colby cheese": ("dairy_products", "cheese"),
            "muenster cheese": ("dairy_products", "cheese"),
            "havarti cheese": ("dairy_products", "cheese"),
            "brie cheese": ("dairy_products", "cheese"),
            "camembert cheese": ("dairy_products", "cheese"),
            "cream cheese": ("dairy_products", "cheese"),
            "light cream cheese": ("dairy_products", "cheese"),
            "lowfat cream cheese": ("dairy_products", "cheese"),
            "cottage cheese": ("dairy_products", "cheese"),
            "lowfat cottage cheese": ("dairy_products", "cheese"),
            "yogurt": ("dairy_products", "yogurt"),
            "nonfat yogurt": ("dairy_products", "yogurt"),
            "lowfat yogurt": ("dairy_products", "yogurt"),
            "greek yogurt": ("dairy_products", "yogurt"),
            "nonfat greek yogurt": ("dairy_products", "yogurt"),
            "lowfat greek yogurt": ("dairy_products", "yogurt"),
            "sour cream": ("dairy_products", "sour cream"),
            "light sour cream": ("dairy_products", "sour cream"),
            "heavy cream": ("dairy_products", "cream"),
            "ice cream": ("dairy_products", "ice cream"),
            "vanilla ice cream": ("dairy_products", "ice cream"),
            "chocolate ice cream": ("dairy_products", "ice cream"),

            # -------------------------------------------------------------------------------------------------------
            # ----- GRAINS ("cereal_and_cereal_products") -----
            # -------------------------------------------------------------------------------------------------------

            # Rices
            "rice": ("cereal_and_cereal_products", "rice"),
            "white rice": ("cereal_and_cereal_products", "rice"),
            "brown rice": ("cereal_and_cereal_products", "rice"),
            "basmati rice": ("cereal_and_cereal_products", "rice"),
            "long grain rice": ("cereal_and_cereal_products", "rice"),
            "short grain rice": ("cereal_and_cereal_products", "rice"),
            "jasmine rice": ("cereal_and_cereal_products", "rice"),
            "wild rice": ("cereal_and_cereal_products", "rice"),
            "wild rice blend": ("cereal_and_cereal_products", "rice"),
            "fried rice": ("cereal_and_cereal_products", "rice"),
            # Pastas
            "pasta": ("cereal_and_cereal_products", "pasta"),
            "pastas": ("cereal_and_cereal_products", "pasta"),
            "whole wheat pasta": ("cereal_and_cereal_products", "pasta"),
            "whole wheat pastas": ("cereal_and_cereal_products", "pasta"),
            "whole grain pasta": ("cereal_and_cereal_products", "pasta"),
            "whole grain pastas": ("cereal_and_cereal_products", "pasta"),
            "gluten free pasta": ("cereal_and_cereal_products", "pasta"),
            "gluten free pastas": ("cereal_and_cereal_products", "pasta"),
            "gluten-free pasta": ("cereal_and_cereal_products", "pasta"),
            "angel hair pasta": ("cereal_and_cereal_products", "pasta"),
            "fettuccine pasta": ("cereal_and_cereal_products", "pasta"),
            "penne pasta": ("cereal_and_cereal_products", "pasta"),
            "spaghetti pasta": ("cereal_and_cereal_products", "pasta"),
            "linguine pasta": ("cereal_and_cereal_products", "pasta"),
            "rotini pasta": ("cereal_and_cereal_products", "pasta"),
            "macaroni pasta": ("cereal_and_cereal_products", "pasta"),
            "elbow pasta": ("cereal_and_cereal_products", "pasta"),
            "penne" : ("cereal_and_cereal_products", "pasta"),
            "spaghetti" : ("cereal_and_cereal_products", "pasta"),
            "linguine" : ("cereal_and_cereal_products", "pasta"),
            "rotini" : ("cereal_and_cereal_products", "pasta"),
            "macaroni" : ("cereal_and_cereal_products", "pasta"),
            "elbow" : ("cereal_and_cereal_products", "pasta"),
            "lasagna noodle": ("cereal_and_cereal_products", "pasta"),
            "lasagna noodles": ("cereal_and_cereal_products", "pasta"),
            "lasagna sheet": ("cereal_and_cereal_products", "pasta"),
            "lasagna sheets": ("cereal_and_cereal_products", "pasta"),
            "lasagna": ("cereal_and_cereal_products", "pasta"),

            # Breads
            "bread": ("cereal_and_cereal_products", "bread"),
            "baguette": ("cereal_and_cereal_products", "bread"),
            "french bread": ("cereal_and_cereal_products", "bread"),
            "french baguette": ("cereal_and_cereal_products", "bread"),
            "french roll": ("cereal_and_cereal_products", "bread"),
            "french rolls": ("cereal_and_cereal_products", "bread"),
            "sourdough": ("cereal_and_cereal_products", "bread"),
            "sourdough bread": ("cereal_and_cereal_products", "bread"),
            "whole wheat bread": ("cereal_and_cereal_products", "bread"),
            "white bread": ("cereal_and_cereal_products", "bread"),
            "multigrain bread": ("cereal_and_cereal_products", "bread"),
            "rye bread": ("cereal_and_cereal_products", "bread"),
            "oat bread": ("cereal_and_cereal_products", "bread"),
            "egg bread": ("cereal_and_cereal_products", "bread"),
            "potato bread": ("cereal_and_cereal_products", "bread"),
            "cornbread": ("cereal_and_cereal_products", "bread"),
            "corn bread": ("cereal_and_cereal_products", "bread"),
            "croissant": ("cereal_and_cereal_products", "bread"),
            "croissants": ("cereal_and_cereal_products", "bread"),
            "biscuit": ("cereal_and_cereal_products", "bread"),
            "biscuits": ("cereal_and_cereal_products", "bread"),
            "english muffin": ("cereal_and_cereal_products", "bread"),
            "english muffins": ("cereal_and_cereal_products", "bread"),
            "bagel": ("cereal_and_cereal_products", "bread"),
            "bagels": ("cereal_and_cereal_products", "bread"),
            "tortilla": ("cereal_and_cereal_products", "tortilla"),
            "tortillas": ("cereal_and_cereal_products", "tortilla"),
            "corn tortilla": ("cereal_and_cereal_products", "tortilla"),
            "corn tortillas": ("cereal_and_cereal_products", "tortilla"),
            "flour tortilla": ("cereal_and_cereal_products", "tortilla"),
            "flour tortillas": ("cereal_and_cereal_products", "tortilla"),
            "flatbread": ("cereal_and_cereal_products", "bread"),
            "flatbreads": ("cereal_and_cereal_products", "bread"),
            "pita": ("cereal_and_cereal_products", "bread"),
            "pitas": ("cereal_and_cereal_products", "bread"),
            "naan": ("cereal_and_cereal_products", "bread"),
            "naans": ("cereal_and_cereal_products", "bread"),
            "whole wheat naan": ("cereal_and_cereal_products", "bread"),
            "hamburger bun": ("cereal_and_cereal_products", "bread"),
            "hamburger buns": ("cereal_and_cereal_products", "bread"),
            "hot dog bun": ("cereal_and_cereal_products", "bread"),
            "hot dog buns": ("cereal_and_cereal_products", "bread"),
            "hawaiian roll": ("cereal_and_cereal_products", "bread"),
            "hawaiian rolls": ("cereal_and_cereal_products", "bread"),
            "english roll": ("cereal_and_cereal_products", "bread"),
            "english rolls": ("cereal_and_cereal_products", "bread"),
            "foccacia": ("cereal_and_cereal_products", "bread"),
            "foccacia bread": ("cereal_and_cereal_products", "bread"),
            "foccacia roll": ("cereal_and_cereal_products", "bread"),
            "foccacia rolls": ("cereal_and_cereal_products", "bread"),

            # Noodles
            "egg noodle": ("cereal_and_cereal_products", "pasta"),
            "egg noodles": ("cereal_and_cereal_products", "pasta"),
            "glass noodle": ("cereal_and_cereal_products", "pasta"),
            "glass noodles": ("cereal_and_cereal_products", "pasta"),
            "ramen noodle": ("cereal_and_cereal_products", "pasta"),
            "ramen noodles": ("cereal_and_cereal_products", "pasta"),
            "rice noodle": ("cereal_and_cereal_products", "pasta"),
            "rice noodles": ("cereal_and_cereal_products", "pasta"),
            "soba noodle": ("cereal_and_cereal_products", "pasta"),
            "soba noodles": ("cereal_and_cereal_products", "pasta"),
            "udon noodle": ("cereal_and_cereal_products", "pasta"),
            "udon noodles": ("cereal_and_cereal_products", "pasta"),

            # OATS
            "oatmeal": ("cereal_and_cereal_products", "oat"),
            "rolled oats": ("cereal_and_cereal_products", "oat"),
            "steel cut oats": ("cereal_and_cereal_products", "oat"),
            "rolled oatmeal": ("cereal_and_cereal_products", "oat"),
            "steel cut oatmeal": ("cereal_and_cereal_products", "oat"),
            "corn": ("cereal_and_cereal_products", "corn"),
            "quinoa": ("cereal_and_cereal_products", "grain"),
            "barley": ("cereal_and_cereal_products", "grain"),
            "rye": ("cereal_and_cereal_products", "grain"),
            "couscous": ("cereal_and_cereal_products", "grain"),
            "millet": ("cereal_and_cereal_products", "grain"),

            # Flours
            "flour": ("cereal_and_cereal_products", "flour"),
            "white flour": ("cereal_and_cereal_products", "flour"),
            "all-purpose flour": ("cereal_and_cereal_products", "flour"),
            "whole wheat flour": ("cereal_and_cereal_products", "flour"),
            "whole wheat white flour": ("cereal_and_cereal_products", "flour"),
            "whole grain flour": ("cereal_and_cereal_products", "flour"),
            "bread flour": ("cereal_and_cereal_products", "flour"),
            "semolina flour": ("cereal_and_cereal_products", "flour"),
            "semolina": ("cereal_and_cereal_products", "flour"),
            "cake flour": ("cereal_and_cereal_products", "flour"),
            "self-rising flour": ("cereal_and_cereal_products", "flour"),
            "cornstarch": ("cereal_and_cereal_products", "flour"),
            "corn starch": ("cereal_and_cereal_products", "flour"),
            "cornmeal": ("cereal_and_cereal_products", "flour"),
            "corn meal": ("cereal_and_cereal_products", "flour"),
            "oat flour": ("cereal_and_cereal_products", "flour"),
            "oat bran": ("cereal_and_cereal_products", "flour"),
            "almond flour": ("cereal_and_cereal_products", "flour"),
            # "cake": ("cereal_and_cereal_products", "flour"), # TODO: moved to baked_goods
            "cake mix": ("cereal_and_cereal_products", "flour"),
            "dough": ("cereal_and_cereal_products", "flour"),
            "dough mix": ("cereal_and_cereal_products", "flour"),
            "toast": ("cereal_and_cereal_products", "bread"),
            "toasts" : ("cereal_and_cereal_products", "bread"),
            "toasts bread": ("cereal_and_cereal_products", "bread"),
            "toasted bread": ("cereal_and_cereal_products", "bread"),
            "cracker" : ("cereal_and_cereal_products", "cracker"),
            "crackers" : ("cereal_and_cereal_products", "cracker"),
            # -------------------------------------------------------------------------------------------------------
            # ----- Nuts and Seeds ("nuts_and_seeds") -----
            # -------------------------------------------------------------------------------------------------------

            # NUTS
            "almond": ("nuts_and_seeds", "nut"),
            "almonds": ("nuts_and_seeds", "nut"),
            "roasted almond": ("nuts_and_seeds", "nut"),
            "roasted almonds": ("nuts_and_seeds", "nut"),
            "peanut": ("nuts_and_seeds", "nut"),
            "peanuts": ("nuts_and_seeds", "nut"),
            "roasted peanut": ("nuts_and_seeds", "nut"),
            "roasted peanuts": ("nuts_and_seeds", "nut"),
            "unsalted peanut": ("nuts_and_seeds", "nut"),
            "unsalted peanuts": ("nuts_and_seeds", "nut"),
            "salted peanut": ("nuts_and_seeds", "nut"),
            "salted peanuts": ("nuts_and_seeds", "nut"),
            "cashew": ("nuts_and_seeds", "nut"),
            "cashews": ("nuts_and_seeds", "nut"),
            "pisatchio": ("nuts_and_seeds", "nut"),
            "pistachios": ("nuts_and_seeds", "nut"),
            "macadamia": ("nuts_and_seeds", "nut"),
            "macadamia nut": ("nuts_and_seeds", "nut"),
            "macadamia nuts": ("nuts_and_seeds", "nut"),
            "hazelnut": ("nuts_and_seeds", "nut"),
            "hazelnuts": ("nuts_and_seeds", "nut"),
            "chestnut": ("nuts_and_seeds", "nut"),
            "chestnuts": ("nuts_and_seeds", "nut"),
            "pine nut": ("nuts_and_seeds", "nut"),
            "pine nuts": ("nuts_and_seeds", "nut"),
            "brazil nut": ("nuts_and_seeds", "nut"),
            "brazil nuts": ("nuts_and_seeds", "nut"),
            "walnut": ("nuts_and_seeds", "nut"),
            "walnuts": ("nuts_and_seeds", "nut"),
            "pecan": ("nuts_and_seeds", "nut"),
            "pecans": ("nuts_and_seeds", "nut"),
            "peanut butter": ("nuts_and_seeds", "nut butter"),
            "almond butter": ("nuts_and_seeds", "nut butter"),
            "cashew butter": ("nuts_and_seeds", "nut butter"),
            "pumpkin seed": ("nuts_and_seeds", "seed"),
            "pumpkin seeds": ("nuts_and_seeds", "seed"),
            "sunflower seed": ("nuts_and_seeds", "seed"),
            "sunflower seeds": ("nuts_and_seeds", "seed"),
            "sesame seed": ("nuts_and_seeds", "seed"),
            "sesame seeds": ("nuts_and_seeds", "seed"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Oils ("oils") -----
            # -------------------------------------------------------------------------------------------------------

            # OILS
            "vegetable oil": ("oils", "vegetable_based"),
            "sesame oil": ("oils", "seed_based"),
            "sunflower oil": ("oils", "seed_based"),
            "canola oil": ("oils", "seed_based"),
            "olive oil": ("oils", "vegetable_based"),
            "coconut oil": ("oils", "vegetable_based"),
            "avocado oil": ("oils", "vegetable_based"),
            "extra virgin olive oil": ("oils", "vegetable_based"),
            "peanut oil": ("oils", "seed_based"),
            "truffle oil": ("oils", "vegetable_based"),
            "chili oil": ("oils", "vegetable_based"),
            "salmon oil": ("oils", "animal_based"),
            "wild alaskan salmon oil": ("oils", "animal_based"),
            "cod liver oil": ("oils", "animal_based"),
            "omega-3 oil": ("oils", "animal_based"),
            "fish oil": ("oils", "animal_based"),
            "omega-3 fish oil": ("oils", "animal_based"),
            "cooking spray": ("oils", "cooking spray"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Fats ("fats_and_other") -----
            # -------------------------------------------------------------------------------------------------------

            "lard": ("fats_and_other", "animal_based"),
            "duck fat": ("fats_and_other", "animal_based"),
            "goose fat": ("fats_and_other", "animal_based"),
            "tallow": ("fats_and_other", "animal_based"),
            "beef tallow": ("fats_and_other", "animal_based"),
            "chicken fat": ("fats_and_other", "animal_based"),
            "ghee": ("fats_and_other", "animal_based"),
            "suet": ("fats_and_other", "animal_based"),
            "grass-fed ghee": ("fats_and_other", "animal_based"),
            "grassfed ghee": ("fats_and_other", "animal_based"),
            "grass fed ghee": ("fats_and_other", "animal_based"),
            "mayonnaise": ("fats_and_other", "condiment_sauce"),
            "light mayonnaise": ("fats_and_other", "condiment_sauce"),
            "lowfat mayonnaise": ("fats_and_other", "condiment_sauce"),
            "low-fat mayonnaise": ("fats_and_other", "condiment_sauce"),
            "low fat mayonnaise": ("fats_and_other", "condiment_sauce"),
            "fat-free mayonnaise": ("fats_and_other", "condiment_sauce"),
            "fat free mayonnaise": ("fats_and_other", "condiment_sauce"),
            "mayo": ("fats_and_other", "condiment_sauce"),
            "light mayo": ("fats_and_other", "condiment_sauce"),
            "lowfat mayo": ("fats_and_other", "condiment_sauce"),
            "low-fat mayo": ("fats_and_other", "condiment_sauce"),
            "low fat mayo": ("fats_and_other", "condiment_sauce"),
            "fat-free mayo": ("fats_and_other", "condiment_sauce"),
            "fat free mayo": ("fats_and_other", "condiment_sauce"),
            "miracle whip": ("fats_and_other", "condiment_sauce"),
            "miracle whip light": ("fats_and_other", "condiment_sauce"),
            "miracle whip fat-free": ("fats_and_other", "condiment_sauce"),
            "miracle whip lowfat": ("fats_and_other", "condiment_sauce"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Herbs & Spices ("herbes_and_spices") -----
            # -------------------------------------------------------------------------------------------------------

            # SPICES
            "salt": ("herbes_and_spices", "salt"),
            "Kosher salt": ("herbes_and_spices", "salt"),
            "kosher salt": ("herbes_and_spices", "salt"),
            "table salt": ("herbes_and_spices", "salt"),
            "sea salt": ("herbes_and_spices", "salt"),
            "iodized salt": ("herbes_and_spices", "salt"),
            "black salt": ("herbes_and_spices", "salt"),
            "himilayan salt": ("herbes_and_spices", "salt"),
            "pink salt": ("herbes_and_spices", "salt"),
            "garlic salt": ("herbes_and_spices", "salt"),
            "onion salt": ("herbes_and_spices", "salt"),
            "cinnamon": ("herbes_and_spices", "bark"),
            "cinnamon stick": ("herbes_and_spices", "bark"),
            "cinnamon sticks": ("herbes_and_spices", "bark"),
            "cinnamon powder": ("herbes_and_spices", "bark"),
            "ground cinnamon": ("herbes_and_spices", "bark"),
            "cumin": ("herbes_and_spices", "spice"),
            "coriander": ("herbes_and_spices", "spice"),
            "paprika": ("herbes_and_spices", "spice"),
            "cayenne": ("herbes_and_spices", "spice"),
            "chili powder": ("herbes_and_spices", "spice"),
            "curry powder": ("herbes_and_spices", "spice"),
            "turmeric": ("herbes_and_spices", "spice"),
            "ginger": ("herbes_and_spices", "herb"),
            "nutmeg": ("herbes_and_spices", "spice"),
            "cloves": ("herbes_and_spices", "spice"),
            "allspice": ("herbes_and_spices", "spice"),
            "cardamom": ("herbes_and_spices", "spice"),
            "oregano": ("herbes_and_spices", "herb"),
            "thyme": ("herbes_and_spices", "herb"),
            "rosemary": ("herbes_and_spices", "herb"),
            "sage": ("herbes_and_spices", "herb"),
            "basil": ("herbes_and_spices", "herb"),
            "fresh basil": ("herbes_and_spices", "herb"),
            "dried basil": ("herbes_and_spices", "herb"),
            "basil leaf": ("herbes_and_spices", "herb"),
            "basil leaves": ("herbes_and_spices", "herb"),
            "fresh basil leaf": ("herbes_and_spices", "herb"),
            "fresh basil leaves": ("herbes_and_spices", "herb"),
            "mint": ("herbes_and_spices", "herb"),
            "mint leaf": ("herbes_and_spices", "herb"),
            "mint leaves": ("herbes_and_spices", "herb"),
            "parsley": ("herbes_and_spices", "herb"),
            "cilantro": ("herbes_and_spices", "herb"),
            "dill": ("herbes_and_spices", "herb"),
            "tarragon": ("herbes_and_spices", "herb"),
            "garlic powder": ("herbes_and_spices", "spice"),
            "onion powder": ("herbes_and_spices", "spice"),
            "cayenne pepper": ("herbes_and_spices", "pepper"),
            "lemon pepper": ("herbes_and_spices", "pepper"),
            "fresh tarragon": ("herbes_and_spices", "herb"),
            "pepper": ("herbes_and_spices", "pepper"),
            "ground pepper": ("herbes_and_spices", "pepper"),
            "black pepper": ("herbes_and_spices", "pepper"),
            "ground black pepper": ("herbes_and_spices", "pepper"),
            "peppercorns": ("herbes_and_spices", "seed"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Fruits ("fruits") -----
            # -------------------------------------------------------------------------------------------------------

            # FRUITS
            "avocado": ("fruits", "berry"),
            "avocados": ("fruits", "berry"),
            "hass avocado": ("fruits", "berry"),
            "hass avocados": ("fruits", "berry"),
            "grapefruit": ("fruits", "citrus"),
            "grapefruits": ("fruits", "citrus"),
            "lime": ("fruits", "citrus"),
            "limes": ("fruits", "citrus"),
            "lemon": ("fruits", "citrus"),
            "lemons": ("fruits", "citrus"),
            "strawberry": ("fruits", "berry"),
            "strawberries": ("fruits", "berry"),
            "blueberry": ("fruits", "berry"),
            "blueberries": ("fruits", "berry"),
            "blackberry": ("fruits", "berry"),
            "blackberries": ("fruits", "berry"),
            "raspberry": ("fruits", "berry"),
            "raspberries": ("fruits", "berry"),
            "banana": ("fruits", "tropical"),
            "bananas": ("fruits", "tropical"),
            "apple": ("fruits", "pome"),
            "apples": ("fruits", "pome"),
            "granny smith apple": ("fruits", "pome"),
            "granny smith apples": ("fruits", "pome"),
            "fuji apple": ("fruits", "pome"),
            "fuji apples": ("fruits", "pome"),
            "red delicious apple": ("fruits", "pome"),
            "red delicious apples": ("fruits", "pome"),
            "golden delicious apple": ("fruits", "pome"),
            "golden delicious apples": ("fruits", "pome"),
            "honeycrisp apple": ("fruits", "pome"),
            "honeycrisp apples": ("fruits", "pome"),
            "macintosh apple": ("fruits", "pome"),
            "macintosh apples": ("fruits", "pome"),
            "orange": ("fruits", "citrus"),
            "oranges": ("fruits", "citrus"),
            "pear": ("fruits", "pome"),
            "pears": ("fruits", "pome"),
            "grape": ("fruits", "berry"),
            "grapes": ("fruits", "berry"),
            "watermelon": ("fruits", "melon"),
            "watermelons": ("fruits", "melon"),
            "cantaloupe": ("fruits", "melon"),
            "cantaloupes": ("fruits", "melon"),
            "honeydew": ("fruits", "melon"),
            "honeydews": ("fruits", "melon"),
            "kiwi": ("fruits", "tropical"),
            "kiwis": ("fruits", "tropical"),
            "mango": ("fruits", "tropical"),
            "mangos": ("fruits", "tropical"),
            "pineapple": ("fruits", "tropical"),
            "pineapples": ("fruits", "tropical"),
            "peach": ("fruits", "stone"),
            "peaches": ("fruits", "stone"),
            "plum": ("fruits", "stone"),
            "plums": ("fruits", "stone"),
            "apricot": ("fruits", "stone"),
            "apricots": ("fruits", "stone"),
            "cherry": ("fruits", "stone"),
            "cherries": ("fruits", "stone"),
            "fig": ("fruits", "fig"),
            "figs": ("fruits", "fig"),
            "date": ("fruits", "date"),
            "dates": ("fruits", "date"),
            "pomegranate": ("fruits", "tropical"),
            "pomegranates": ("fruits", "tropical"),
            "coconut": ("fruits", "drupe"),
            "coconuts": ("fruits", "drupe"),
            "passion fruit": ("fruits", "tropical"),
            "passion fruits": ("fruits", "tropical"),
            "dragon fruit": ("fruits", "tropical"),
            "dragon fruits": ("fruits", "tropical"),
            "guava": ("fruits", "tropical"),
            "guavas": ("fruits", "tropical"),
            "star fruit": ("fruits", "tropical"),
            "star fruits": ("fruits", "tropical"),
            "lychee": ("fruits", "tropical"),
            "lychees": ("fruits", "tropical"),
            "persimmon": ("fruits", "berry"),
            "persimmons": ("fruits", "berry"),
            "papaya": ("fruits", "tropical"),
            "papayas": ("fruits", "tropical"),
            "cranberry": ("fruits", "berry"),
            "cranberries": ("fruits", "berry"),
            "raisin": ("fruits", "grape"),
            "raisins": ("fruits", "grape"),
            "prune": ("fruits", "drupe"),
            "prunes": ("fruits", "drupe"),
            "currant": ("fruits", "berry"),
            "currants": ("fruits", "berry"),
            "elderberry": ("fruits", "berry"),
            "elderberries": ("fruits", "berry"),
            "goji berry": ("fruits", "berry"),
            "goji berries": ("fruits", "berry"),
            "acai": ("fruits", "berry"),
            "acai berry": ("fruits", "berry"),
            "acai berries": ("fruits", "berry"),
            "boysenberry": ("fruits", "berry"),
            "boysenberries": ("fruits", "berry"),
            "zucchini": ("fruits", "squash"),
            "zucchinis": ("fruits", "squash"),

            # BEVERAGES

            # -------------------------------------------------------------------------------------------------------
            # ----- Coffee, Tea, drink powders ("tea_cacao_coffee_and_drinking_powders") -----
            # -------------------------------------------------------------------------------------------------------


            # Coffee/Teas/Powders
            "coffee": ("tea_cacao_coffee_and_drinking_powders", "coffee"),
            "decaf coffee": ("tea_cacao_coffee_and_drinking_powders", "coffee"),
            "espresso": ("tea_cacao_coffee_and_drinking_powders", "espresso"),
            "tea": ("tea_cacao_coffee_and_drinking_powders", "tea"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Bevarages, no alcohol ("beverages_non_alcoholic_including_soft_drinks_and_juices") -----
            # -------------------------------------------------------------------------------------------------------

            # Non alcohlic beverages
            "water": ("beverages_non_alcoholic_including_soft_drinks_and_juices", "water"),
            "soda": ("beverages_non_alcoholic_including_soft_drinks_and_juices", "soda"),
            "orange juice": ("beverages_non_alcoholic_including_soft_drinks_and_juices", "juice"),
            "apple juice": ("beverages_non_alcoholic_including_soft_drinks_and_juices", "juice"),
            "grape juice": ("beverages_non_alcoholic_including_soft_drinks_and_juices", "juice"),
            "mango juice": ("beverages_non_alcoholic_including_soft_drinks_and_juices", "juice"),
            "pineapple juice": ("beverages_non_alcoholic_including_soft_drinks_and_juices", "juice"),
            "lime juice": ("beverages_non_alcoholic_including_soft_drinks_and_juices", "juice"),
            "lemon juice": ("beverages_non_alcoholic_including_soft_drinks_and_juices", "juice"),
            "lemonade": ("beverages_non_alcoholic_including_soft_drinks_and_juices", "juice"),
            "limeade": ("beverages_non_alcoholic_including_soft_drinks_and_juices", "juice"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Beers ("beer") -----
            # -------------------------------------------------------------------------------------------------------

            # Beers
            "beer": ("beer", "beer"),
            "light beer": ("beer", "beer"),
            "dark beer": ("beer", "beer"),
            "ale": ("beer", "beer"),
            "lager": ("beer", "beer"),
            "stout": ("beer", "beer"),
            "pilsner": ("beer", "beer"),
            "porter": ("beer", "beer"),
            "IPA": ("beer", "beer"),
            "india pale ale": ("beer", "beer"),
            "ipa": ("beer", "beer"),
            
            # -------------------------------------------------------------------------------------------------------
            # ----- Spirits and Liquers ("spirits_and_liqueurs") -----
            # -------------------------------------------------------------------------------------------------------

            # Spirits/Liqueurs
            "vodka": ("spirits_and_liqueurs", "spirits"),
            "whiskey": ("spirits_and_liqueurs", "spirits"),
            "bourbon": ("spirits_and_liqueurs", "spirits"),
            "rum": ("spirits_and_liqueurs", "spirits"),
            "gin": ("spirits_and_liqueurs", "spirits"),
            "tequila": ("spirits_and_liqueurs", "spirits"),
            "brandy": ("spirits_and_liqueurs", "spirits"),
            "cognac": ("spirits_and_liqueurs", "spirits"),
            "scotch": ("spirits_and_liqueurs", "spirits"),
            "sake": ("spirits_and_liqueurs", "spirits"),

            "liqueur": ("spirits_and_liqueurs", "liqueur"),
            "amaretto": ("spirits_and_liqueurs", "liqueurs"),
            "kahlua": ("spirits_and_liqueurs", "liqueurs"),
            "baileys": ("spirits_and_liqueurs", "liqueurs"),
            "irish cream": ("spirits_and_liqueurs", "liqueurs"),
            "schnapps": ("spirits_and_liqueurs", "liqueurs"),
            # -------------------------------------------------------------------------------------------------------
            # ----- Wine & Cider ("wine_and_cider") -----
            # -------------------------------------------------------------------------------------------------------

            # Wine/Cider
            "wine": ("wine_and_cider", "wine"),
            "white wine": ("wine_and_cider", "wine"),
            "red wine": ("wine_and_cider", "wine"),
            "pinot noir": ("wine_and_cider", "wine"),
            "chardonnay": ("wine_and_cider", "wine"),
            "sauvignon blanc": ("wine_and_cider", "wine"),
            "merlot": ("wine_and_cider", "wine"),
            "cabernet sauvignon": ("wine_and_cider", "wine"),
            "rosé": ("wine_and_cider", "wine"),
            "rose": ("wine_and_cider", "wine"),
            "ruby port": ("wine_and_cider", "wine"),
            "tawny port": ("wine_and_cider", "wine"),
            "port": ("wine_and_cider", "wine"),
            "ports": ("wine_and_cider", "wine"),
            "port wine": ("wine_and_cider", "wine"),
            "rose wine" : ("wine_and_cider", "wine"),
            "champagne": ("wine_and_cider", "wine"),
            "sparkling wine": ("wine_and_cider", "wine"),
            "dessert wine": ("wine_and_cider", "wine"),
            "cooking wine": ("wine_and_cider", "wine"),
            "creme de cassis": ("wine_and_cider", "wine"),
            "crème de cassis": ("wine_and_cider", "wine"),
            "cassis": ("wine_and_cider", "wine"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Soup, broth, stock ("soups") -----
            # -------------------------------------------------------------------------------------------------------

            # SOUPS
            "broth": ("soups", "soup"),
            "stock": ("soups", "soup"),
            "chicken broth": ("soups", "soup"),
            "beef broth": ("soups", "soup"),
            "vegetable broth": ("soups", "soup"),
            "chicken stock": ("soups", "soup"),
            "beef stock": ("soups", "soup"),
            "vegetable stock": ("soups", "soup"),
            "miso soup": ("soups", "soup"),
            "tomato soup": ("soups", "soup"),
            "tomato bisque": ("soups", "soup"),
            "bouillon": ("soups", "soup"),
            "beef bouillon": ("soups", "soup"),
            "chicken bouillon": ("soups", "soup"),
            "chicken noodle soup": ("soups", "soup"),
            "cream of mushroom soup": ("soups", "soup"),
            "cream of chicken soup": ("soups", "soup"),
            "cream of celery soup": ("soups", "soup"),
            "cream of broccoli soup": ("soups", "soup"),
            "cream of potato soup": ("soups", "soup"),
            "cream of tomato soup": ("soups", "soup"),
            "cream of asparagus soup": ("soups", "soup"),
            "cream of spinach soup": ("soups", "soup"),
            "cream of corn soup": ("soups", "soup"),
            "cream of carrot soup": ("soups", "soup"),
            "cream of squash soup": ("soups", "soup"),
            "cream of pumpkin soup": ("soups", "soup"),
            "cream of sweet potato soup": ("soups", "soup"),
            "cream of zucchini soup": ("soups", "soup"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Misc foods, condiments, sauces ("miscellaneous_foods") -----
            # -------------------------------------------------------------------------------------------------------

            # miscellaneous_foods 
            # CONDIMENTS/SAUCES
            "vinegar": ("sauces_and_gravies", "vinegar"),
            "white wine vinegar": ("sauces_and_gravies", "vinegar"),
            "balsamic vinegar": ("sauces_and_gravies", "vinegar"),
            "red wine vinegar": ("sauces_and_gravies", "vinegar"),
            "apple cider vinegar": ("sauces_and_gravies", "vinegar"),
            "distilled vinegar": ("sauces_and_gravies", "vinegar"),
            "rice vinegar": ("sauces_and_gravies", "vinegar"),
            "white vinegar": ("sauces_and_gravies", "vinegar"),
            "fish sauce": ("sauces_and_gravies", "condiment_sauce"),
            "ketchup": ("sauces_and_gravies", "condiment_sauce"),
            "reduced-sugar ketchup": ("sauces_and_gravies", "condiment_sauce"),
            "reduced sugar ketchup": ("sauces_and_gravies", "condiment_sauce"),
            "low-sugar ketchup": ("sauces_and_gravies", "condiment_sauce"),
            "low sugar ketchup": ("sauces_and_gravies", "condiment_sauce"),
            "sugar-free ketchup": ("sauces_and_gravies", "condiment_sauce"),
            "sugar free ketchup": ("sauces_and_gravies", "condiment_sauce"),
            "low-sodium ketchup": ("sauces_and_gravies", "condiment_sauce"),
            "low sodium ketchup": ("sauces_and_gravies", "condiment_sauce"),
            "sodium-free ketchup": ("sauces_and_gravies", "condiment_sauce"),
            "sodium free ketchup": ("sauces_and_gravies", "condiment_sauce"),
            "relish": ("sauces_and_gravies", "condiment_sauce"),
            "mustard": ("sauces_and_gravies", "condiment_sauce"),
            "dijon mustard": ("sauces_and_gravies", "condiment_sauce"),
            "yellow mustard": ("sauces_and_gravies", "condiment_sauce"),
            "honey mustard": ("sauces_and_gravies", "condiment_sauce"),
            "soy sauce": ("sauces_and_gravies", "condiment_sauce"),
            "BBQ sauce": ("sauces_and_gravies", "condiment_sauce"),
            "bbq sauce": ("sauces_and_gravies", "condiment_sauce"),
            "barbecue sauce": ("sauces_and_gravies", "condiment_sauce"),
            "hot sauce": ("sauces_and_gravies", "condiment_sauce"),
            "sriracha": ("sauces_and_gravies", "condiment_sauce"),
            "gochujang" : ("sauces_and_gravies", "condiment_sauce"),
            "gochujang sauce" : ("sauces_and_gravies", "condiment_sauce"),
            "gochujang paste" : ("sauces_and_gravies", "condiment_sauce"),
            "chilli paste" : ("sauces_and_gravies", "condiment_sauce"),
            "salsa": ("sauces_and_gravies", "condiment_sauce"),
            "pesto": ("sauces_and_gravies", "condiment_sauce"),
            "basil pesto": ("sauces_and_gravies", "condiment_sauce"),
            "pesto spread": ("sauces_and_gravies", "condiment_sauce"),
            "black olive spread": ("sauces_and_gravies", "condiment_sauce"),
            
            # Salad dressing 
            "ranch": ("fats_and_other", "salad dressing"),
            "ranch dressing": ("fats_and_other", "salad dressing"),
            "caesar dressing": ("fats_and_other", "salad dressing"),
            "thousand island dressing": ("fats_and_other", "salad dressing"),
            "blue cheese dressing": ("fats_and_other", "salad dressing"),
            "italian dressing": ("fats_and_other", "salad dressing"),
            "vinaigrette": ("fats_and_other", "salad dressing"),
            "vinaigrette dressing": ("fats_and_other", "salad dressing"),
            "sesame dressing": ("fats_and_other", "salad dressing"),
            "honey mustard dressing": ("fats_and_other", "salad dressing"),
            "balsamic dressing": ("fats_and_other", "salad dressing"),
            "balsamic vinaigrette": ("fats_and_other", "salad dressing"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Sweets, sugars ("sweets") -----
            # -------------------------------------------------------------------------------------------------------

            # SWEETENERS
            "sugar": ("sweets", "sugar"),
            "brown sugar": ("sweets", "sugar"),
            "powdered sugar": ("sweets", "sugar"),
            "cane sugar": ("sweets", "sugar"),
            "granulated sugar": ("sweets", "sugar"),
            "confectioners' sugar": ("sweets", "sugar"),
            "confectioners sugar": ("sweets", "sugar"),
            "confectioner's sugar": ("sweets", "sugar"),
            "coconut palm sugar": ("sweets", "sugar"),
            "coconut sugar": ("sweets", "sugar"),
            "date sugar": ("sweets", "sugar"),
            "stevia": ("sweets", "sugar substitute"),
            "Sweet'n Low": ("sweets", "sugar substitute"),
            "sweet'n low": ("sweets", "sugar substitute"),
            "splenda": ("sweets", "sugar substitute"),
            "Splenda": ("sweets", "sugar substitute"),
            "truvia": ("sweets", "sugar substitute"),
            "Xylitol": ("sweets", "sugar alcohol"),
            "Erythritol": ("sweets", "sugar alcohol"),
            "Sorbitol": ("sweets", "sugar alcohol"),
            "Maltitol": ("sweets", "sugar alcohol"),
            "xylitol": ("sweets", "sugar alcohol"),
            "erythritol": ("sweets", "sugar alcohol"),
            "sorbitol": ("sweets", "sugar alcohol"),
            "maltitol": ("sweets", "sugar alcohol"),
            "chocolate chips": ("sweets", "chocolate"),
            "chocolate": ("sweets", "chocolate"),
            "white chocolate": ("sweets", "chocolate"),
            "dark chocolate": ("sweets", "chocolate"),
            "milk chocolate": ("sweets", "chocolate"),
            "baking chocolate": ("sweets", "chocolate"),
            "cocoa": ("sweets", "chocolate"),
            "ladyfinger": ("sweets", "cookie"),
            "ladysfingers": ("sweets", "cookie"),
            "ladyfingers": ("sweets", "cookie"),


            # -------------------------------------------------------------------------------------------------------
            # ----- SYRUPS ("syrups") -----
            # -------------------------------------------------------------------------------------------------------

            "corn syrup": ("syrups", "syrup"),
            "high fructose corn syrup": ("syrups", "syrup"),
            "honey": ("syrups", "honey"),
            "organic honey": ("syrups", "honey"),
            "maple syrup": ("syrups", "syrup"),
            "maple sugar": ("syrups", "sugar"),
            "agave": ("syrups", "nectar"),
            "agave nectar": ("syrups", "nectar"),
            "fruit syrup": ("syrups", "syrup"),
            "molasses" : ("syrups", "sugar"),
            "pancake syrup": ("syrups", "syrup"),
            "light corn syrup": ("syrups", "syrup"),
            "grenadine syrup": ("syrups", "syrup"),
            "strawberry syrup": ("syrups", "syrup"),
            "chocolate syrup": ("syrups", "syrup"),
            "caramel syrup": ("syrups", "syrup"),
            "simple syrup": ("syrups", "syrup"),
            "vanilla syrup": ("syrups", "syrup"),
            "raspberry syrup": ("syrups", "syrup"),
            "blueberry syrup": ("syrups", "syrup"),
            "blackberry syrup": ("syrups", "syrup"),
            "peach syrup": ("syrups", "syrup"),

            # Jam/jelly/preserve
            "jam" : ("syrups", "syrup"),
            "jams" : ("syrups", "syrup"),
            "strawberry jam" : ("syrups", "syrup"),
            "blueberry jam" : ("syrups", "syrup"),
            "blackberry jam" : ("syrups", "syrup"),
            "peach jam" : ("syrups", "syrup"),
            "raspberry jam" : ("syrups", "syrup"),
            "jelly" : ("syrups", "syrup"),
            "jellies" : ("syrups", "syrup"),
            "strawberry jelly" : ("syrups", "syrup"),
            "blueberry jelly" : ("syrups", "syrup"),
            "blackberry jelly" : ("syrups", "syrup"),
            "peach jelly" : ("syrups", "syrup"),
            "raspberry jelly" : ("syrups", "syrup"),
            "preserves" : ("syrups", "syrup"),
            "preserve" : ("syrups", "syrup"),
            "strawberry preserves" : ("syrups", "syrup"),
            "blueberry preserves" : ("syrups", "syrup"),
            "blackberry preserves" : ("syrups", "syrup"),
            "peach preserves" : ("syrups", "syrup"),
            "raspberry preserves" : ("syrups", "syrup"),
            "marmalades" : ("syrups", "syrup"),
            "marmalade" : ("syrups", "syrup"),
            "orange marmalade" : ("syrups", "syrup"),
            "strawberry marmalade" : ("syrups", "syrup"),
            "blueberry marmalade" : ("syrups", "syrup"),
            "blackberry marmalade" : ("syrups", "syrup"),
            "peach marmalade" : ("syrups", "syrup"),
            "raspberry marmalade" : ("syrups", "syrup"),
            "fruit preserves" : ("syrups", "syrup"),

            # -------------------------------------------------------------------------------------------------------
            # ----- SNACKS ("snacks") -----
            # -------------------------------------------------------------------------------------------------------
            # SNACKS
            "potato chip": ("snacks", "chip"),
            "potato chips": ("snacks", "chip"),
            "puff chip": ("snacks", "chip"),
            "puff chips": ("snacks", "chip"),
            "tortilla chip": ("snacks", "chip"),
            "tortilla chips": ("snacks", "chip"),
            "corn chip": ("snacks", "chip"),
            "corn chips": ("snacks", "chip"),
            "wonton" : ("snacks", "chip"),
            "wontons" : ("snacks", "chip"),
            "wonton chip": ("snacks", "chip"),
            "wonton chips": ("snacks", "chip"),
            "pretzel stick": ("snacks", "chip"),
            "pretzel sticks": ("snacks", "chip"),
            "pretzel": ("snacks", "chip"),
            "pretzels": ("snacks", "chip"),
            "popcorn": ("snacks", "chip"),
            "popcorn kernel": ("snacks", "chip"),
            "popcorn kernels": ("snacks", "chip"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Mixed dishes ("mixed_dishes") -----
            # -------------------------------------------------------------------------------------------------------
            
            # Mixed dishes
            "pizza": ("mixed_dishes", "mixed_dish"),

            # -------------------------------------------------------------------------------------------------------
            # ----- Baked goods ("baked_goods") -----
            # -------------------------------------------------------------------------------------------------------
            
            # Baked goods
            "muffin" : ("baked_goods", "pastry"),
            "muffins" : ("baked_goods", "pastry"),
            "croissant" : ("baked_goods", "pastry"),
            "croissants" : ("baked_goods", "pastry"),
            "almond croissant" : ("baked_goods", "pastry"),
            "almond croissants" : ("baked_goods", "pastry"),
            "chocolate croissant" : ("baked_goods", "pastry"),
            "chocolate croissants" : ("baked_goods", "pastry"),
            "bear claw" : ("baked_goods", "pastry"),
            "bear claws" : ("baked_goods", "pastry"),
            "cinnamon roll" : ("baked_goods", "pastry"),
            "cinnamon rolls" : ("baked_goods", "pastry"),
            "cinammon bun" : ("baked_goods", "pastry"),
            "cinammon buns" : ("baked_goods", "pastry"),
            "danish" : ("baked_goods", "pastry"),
            "danishes" : ("baked_goods", "pastry"),
            "scone" : ("baked_goods", "pastry"),
            "scones" : ("baked_goods", "pastry"),
            "donut" : ("baked_goods", "pastry"),
            "donuts" : ("baked_goods", "pastry"),
            "donut hole" : ("baked_goods", "pastry"),
            "donut holes" : ("baked_goods", "pastry"),
            "doughnut" : ("baked_goods", "pastry"),
            "doughnuts" : ("baked_goods", "pastry"),
            "doughnut hole" : ("baked_goods", "pastry"),
            "doughnut holes" : ("baked_goods", "pastry"),

            "cookie" : ("baked_goods", "cookie"),
            "cookies" : ("baked_goods", "cookie"),
            "molasses cookie" : ("baked_goods", "cookie"),
            "molasses cookies" : ("baked_goods", "cookie"),
            "chocolate chip cookie" : ("baked_goods", "cookie"),
            "chocolate chip cookies" : ("baked_goods", "cookie"),
            "sugar cookie" : ("baked_goods", "cookie"),
            "sugar cookies" : ("baked_goods", "cookie"),
            "oatmeal cookie" : ("baked_goods", "cookie"),
            "oatmeal cookies" : ("baked_goods", "cookie"),
            "peanut butter cookie" : ("baked_goods", "cookie"),
            "peanut butter cookies" : ("baked_goods", "cookie"),
            "snickerdoodle" : ("baked_goods", "cookie"),
            "snickerdoodles" : ("baked_goods", "cookie"),
            "gingerbread cookie" : ("baked_goods", "cookie"),
            "gingerbread cookies" : ("baked_goods", "cookie"),
            "shortbread cookie" : ("baked_goods", "cookie"),
            "shortbread cookies" : ("baked_goods", "cookie"),
            "macaroon" : ("baked_goods", "cookie"),
            "macaroons" : ("baked_goods", "cookie"),
            "macaron" : ("baked_goods", "cookie"),
            "macarons" : ("baked_goods", "cookie"),
            "biscotti" : ("baked_goods", "cookie"),
            "biscottis" : ("baked_goods", "cookie"),
            "oatmeal raisin cookie" : ("baked_goods", "cookie"),
            "oatmeal raisin cookies" : ("baked_goods", "cookie"),
            "peanut butter chocolate chip cookie" : ("baked_goods", "cookie"),
            "peanut butter chocolate chip cookies" : ("baked_goods", "cookie"),
            "peanut butter oatmeal cookie" : ("baked_goods", "cookie"),
            "peanut butter oatmeal cookies" : ("baked_goods", "cookie"),
            "peanut butter oatmeal chocolate chip cookie" : ("baked_goods", "cookie"),
            "peanut butter oatmeal chocolate chip cookies" : ("baked_goods", "cookie"),
            "brownie" : ("baked_goods", "brownie"),
            "brownies" : ("baked_goods", "brownie"),
            "blondie" : ("baked_goods", "brownie"),
            "blondies" : ("baked_goods", "brownie"),

            "cake" : ("baked_goods", "cake"),
            "pound cake" : ("baked_goods", "cake"),
            "pound cakes" : ("baked_goods", "cake"),
            "angel food cake" : ("baked_goods", "cake"),
            "angel food cakes" : ("baked_goods", "cake"),
            "bundt cake" : ("baked_goods", "cake"),
            "bundt cakes" : ("baked_goods", "cake"),
            "cupcake" : ("baked_goods", "cake"),
            "cupcakes" : ("baked_goods", "cake"),
            "birthday cake" : ("baked_goods", "cake"),
            "birthday cakes" : ("baked_goods", "cake"),
            "sheet cake" : ("baked_goods", "cake"),
            "sheet cakes" : ("baked_goods", "cake"),

            "baking sheets": ("baked_goods", "baking"), # TODO: why? 
            "baking powder": ("baked_goods", "baking"),
            "baking soda": ("baked_goods", "baking"),
            "yeast": ("baked_goods", "baking"),
            "baking yeast": ("baked_goods", "baking"),
            "active dry yeast": ("baked_goods", "baking"),
            "instant yeast": ("baked_goods", "baking")
            }

# ---- Map of all of the subcategories in each primary category in the FOOD_CATALOG ----

# From the FOOD_CATALOG, generate new food categories dictionary with the major categories as keys and the minor categories as tuple values
FOOD_CATEGORIES = {}

# go through all of the foods and get all of the major and minor categories from the dictionary value lists
for key, val in FOOD_CATALOG.items():
    primary_category, secondary_category = val
    
    current_set = FOOD_CATEGORIES.get(primary_category, set())
    current_set.add(secondary_category)

    # Update the major category key with the new updated set of minory categories
    FOOD_CATEGORIES[primary_category] = current_set
    # FOOD_CATEGORIES[primary_category] = FOOD_CATEGORIES.get(primary_category, set()).add(secondary_category)

# Convert each set to a list
for key, val in FOOD_CATEGORIES.items():
    # This is hacky, but to keep "miscellaneous_foods" at the end of the list if "miscellaneous_foods" is a category
    if "miscellaneous_foods" not in val:
        FOOD_CATEGORIES[key] = list(val)
    else:
        FOOD_CATEGORIES[key].remove("miscellaneous_foods")
        FOOD_CATEGORIES[key] = list(val)
        FOOD_CATEGORIES[key].append("miscellaneous_foods")

# then convert the lists to tuples 
for key in FOOD_CATEGORIES:
    FOOD_CATEGORIES[key] = tuple(FOOD_CATEGORIES[key])

# -----------------------------------------------------------------------------------------------------
# ---- Map with a list of foods within each category ----
# -----------------------------------------------------------------------------------------------------

# Go through the food catalog and make a set for each category and subcategory

FOODS_BY_CATEGORY = {}

for key, val in FOOD_CATALOG.items():
    primary_category, secondary_category = val
    if primary_category in FOODS_BY_CATEGORY:
        FOODS_BY_CATEGORY[primary_category].add(key)
    else: 
        FOODS_BY_CATEGORY[primary_category] = set([key])

    if secondary_category in FOODS_BY_CATEGORY:
        FOODS_BY_CATEGORY[secondary_category].add(key)
    else: 
        FOODS_BY_CATEGORY[secondary_category] = set([key])

PRIMARY_CATEGORIES = tuple(FOOD_CATEGORIES.keys())

SECONDARY_CATEGORIES = set()
for key, value in FOOD_CATEGORIES.items():
    for val in value:
        SECONDARY_CATEGORIES.add(val)

SECONDARY_CATEGORIES = tuple(SECONDARY_CATEGORIES)

# -----------------------------------------------------------------------------------------------------
# ---- Approximate food densities for food groups ----
# -----------------------------------------------------------------------------------------------------

# Specific food densities derived from the FAO/INFOODS Density Database version 2.0 (2012). 
# The following categories are derived values for each group in the Density Database table
# Credit: 
    # FAO/INFOODS Density Database
    # Version 2.0 (2012)
    # Prepared by: U. Ruth Charrondiere, David Haytowitz and Barbara Stadlmayr
FOOD_DENSITY_BY_GROUP = {
    "water" : {   # NOTE: manually added this category to use a default
       "category": "water",
       "density_g_per_ml": 1.0,
       "min_density_g_per_ml": 1.0,
       "max_density_g_per_ml": 1.0
       },
     "syrups" : {   # NOTE: manually added this category for syrups which are not in the Density Database categories
       "category": "syrups",
       "density_g_per_ml": 1.2,
       "min_density_g_per_ml": 1.2,
       "max_density_g_per_ml": 1.2
       },
    "beverages_non_alcoholic_including_soft_drinks_and_juices" : {
       "category": "beverages_non_alcoholic_including_soft_drinks_and_juices",
       "density_g_per_ml": 1.0419,
        "min_density_g_per_ml": 0.916,
        "max_density_g_per_ml": 1.2372
       },
       # TODO: Just commented this out, the categories here should be a 1:1 mapping with 
       # TODO: the FOOD_CATALOG (i.e. all of these categories should be represented in the FOOD_CATALOG)
    # "miscellaneous_foods": {
    #     "category": "miscellaneous_foods",
    #     "density_g_per_ml": 1.0379,
    #     "min_density_g_per_ml": 0.26,
    #     "max_density_g_per_ml": 2.2
    # },
    "sauces_and_gravies": {
        "category": "sauces_and_gravies",
        "density_g_per_ml": 1.0379,
        "min_density_g_per_ml": 0.26,
        "max_density_g_per_ml": 2.2
    },
    
    "soups": {
        "category": "soups",
        "density_g_per_ml": 1.0321,
        "min_density_g_per_ml": 0.99,
        "max_density_g_per_ml": 1.09
    },
    "wine_and_cider": {
        "category": "wine_and_cider",
        "density_g_per_ml": 0.9957,
        "min_density_g_per_ml": 0.9888,
        "max_density_g_per_ml": 1.0384
    },
    "beer": {
        "category": "beer",
        "density_g_per_ml": 0.9951,
        "min_density_g_per_ml": 0.96,
        "max_density_g_per_ml": 1.008
    },
    "mixed_dishes": {
        "category": "mixed_dishes",
        "density_g_per_ml": 0.9652,
        "min_density_g_per_ml": 0.6,
        "max_density_g_per_ml": 1.33
    },
    "sweets": {
        "category": "sweets",
        "density_g_per_ml": 0.9553,
        "min_density_g_per_ml": 0.4,
        "max_density_g_per_ml": 1.43
    },
    "milk": {
        "category": "milk",
        "density_g_per_ml": 0.9351,
        "min_density_g_per_ml": 0.21,
        "max_density_g_per_ml": 1.08
    },
    "oils": {
        "category": "oils",
        "density_g_per_ml": 0.9108,
        "min_density_g_per_ml": 0.88,
        "max_density_g_per_ml": 0.96
    },
    "spirits_and_liqueurs": {
        "category": "spirits_and_liqueurs",
        "density_g_per_ml": 0.8715,
        "min_density_g_per_ml": 0.789,
        "max_density_g_per_ml": 0.939
    },
    "dairy_products": {
        "category": "dairy_products",
        "density_g_per_ml": 0.827,
        "min_density_g_per_ml": 0.34,
        "max_density_g_per_ml": 1.08
    },
    "fats_and_other": {
        "category": "fats_and_other",
        "density_g_per_ml": 0.7998,
        "min_density_g_per_ml": 0.6,
        "max_density_g_per_ml": 1
    },
    "tea_cacao_coffee_and_drinking_powders": {
        "category": "tea_cacao_coffee_and_drinking_powders",
        "density_g_per_ml": 0.7806,
        "min_density_g_per_ml": 0.23,
        "max_density_g_per_ml": 1.06
    },
    "meat_and_meat_products": {
        "category": "meat_and_meat_products",
        "density_g_per_ml": 0.7425,
        "min_density_g_per_ml": 0.48,
        "max_density_g_per_ml": 0.97
    },
    "legumes": {
        "category": "legumes",
        "density_g_per_ml": 0.7411,
        "min_density_g_per_ml": 0.4,
        "max_density_g_per_ml": 0.96
    },
    "fish_and_fish_products": {
        "category": "fish_and_fish_products",
        "density_g_per_ml": 0.675,
        "min_density_g_per_ml": 0.58,
        "max_density_g_per_ml": 0.77
    },
    "nuts_and_seeds": {
        "category": "nuts_and_seeds",
        "density_g_per_ml": 0.6142,
        "min_density_g_per_ml": 0.46,
        "max_density_g_per_ml": 0.77
    },
    "tubers_and_products": {
        "category": "tubers_and_products",
        "density_g_per_ml": 0.5819,
        "min_density_g_per_ml": 0.21,
        "max_density_g_per_ml": 0.79
    },
    "cereal_and_cereal_products": {
        "category": "cereal_and_cereal_products",
        "density_g_per_ml": 0.5781,
        "min_density_g_per_ml": 0.35,
        "max_density_g_per_ml": 1.07
    },
    "baked_goods": {
        "category": "baked_goods",
        "density_g_per_ml": 0.5781,
        "min_density_g_per_ml": 0.35,
        "max_density_g_per_ml": 1.07
    },
    "herbes_and_spices": {
        "category": "herbes_and_spices",
        "density_g_per_ml": 0.5062,
        "min_density_g_per_ml": 0.29,
        "max_density_g_per_ml": 0.77
    },
    "fruits": {
        "category": "fruits",
        "density_g_per_ml": 0.4667,
        "min_density_g_per_ml": 0.24,
        "max_density_g_per_ml": 0.6
    },
    "vegetables": {
        "category": "vegetables",
        "density_g_per_ml": 0.4546,
        "min_density_g_per_ml": 0.06,
        "max_density_g_per_ml": 1.046
    },
    "egg_and_egg_products": {
        "category": "egg_and_egg_products",
        "density_g_per_ml": 0.44,
        "min_density_g_per_ml": 0.35,
        "max_density_g_per_ml": 0.6
    },
    "snacks": {
        "category": "snacks",
        "density_g_per_ml": 0.1067,
        "min_density_g_per_ml": 0.09,
        "max_density_g_per_ml": 0.12
    }
}

# A default set of density values, with the main value being the density of water
DEFAULT_DENSITY_MAP = {
    "category": "default",
    "density_g_per_ml" : 1.0,
    "min_density_g_per_ml" : 0.9,
    "max_density_g_per_ml" : 1.1
    }
# These approximate food density values are taken from the following paper:
# Credit: 
    # "Using database values to determine food density" by Phyllis J. Stumbo a, Rick Weiss b
    # DOI: https://doi.org/10.1016/j.jfca.2011.04.008        
    # URL: https://www.sciencedirect.com/science/article/abs/pii/S0889157511001141

# syrup (density 1.2)
# water or fully hydrated foods (density 1.0)
# pure fat (density 0.8) or
# highly aerated (density 0.5)
FOOD_DENSITY = {
    "syrup": 1.2,
    "water": 1.0,
    "fat": 0.8,
    "aerated": 0.5
}

# ---- Strings that obviously point to a food being a specific category ----

# Words that are so obviously pointing to a specific category that they can be used to determine the category of a food
# (i.e. if a food contains the word "flour", it is most likely a cereal product)
INDICATOR_STRINGS_MAP = {
    "flour" : "cereal_and_cereal_products",
    "flours" : "cereal_and_cereal_products",
    "bread" : "cereal_and_cereal_products",
    "breads" : "cereal_and_cereal_products",
    "bouillon" : "soups",
    "oil" : "oils",
    "oils" : "oils",
    "milk" : "milk",
    "milks" : "milk",
    "syrup" : "syrups",
    "syrups" : "syrups",
    "sugar" : "sweets",
    "sugars" : "sweets",
    "egg" : "egg_and_egg_products",
    "eggs" : "egg_and_egg_products",
    "wine" : "wine_and_cider",
    "wines" : "wine_and_cider",
    "beer" : "beer",
    "beers" : "beer"
}

# A map of common food items and their weight in grams (i.e. 1 egg is approximately 56.7 grams, 1 apple is approximately 195 grams, etc.)
SINGLE_ITEM_FOOD_WEIGHTS = {
    'egg': '56.7',
    'eggs': '56.7',
    'whole egg' : '56.7',
    'whole eggs' : '56.7',
    # NOTE: general rule of thumb for egg / egg white / egg yolk weights:
        # egg yolk   = 30% of egg weight
        # egg white  = 60% of egg weight
        # Source: https://cooking.stackexchange.com/questions/77802/how-much-do-egg-yolks-and-whites-weigh-in-grams
    'egg yolk': '17', 
    'egg yolks': '17',
    'eggs yolk': '17',
    'eggs yolks': '17',
    'egg white': '34',
    'egg whites': '34',
    'eggs white': '34',
    'eggs whites': '34',
    'apple': '195',
    'apples': '195',
    'apricot': '35',
    'apricots': '35',
    'avocado': '170',
    'avocados': '170',
    'banana': '120',
    'bananas': '120',
    'blackberry': '2.45',
    'blackberries': '2.45',
    'blueberry': '0.5',
    'blueberries': '0.5',
    'cherry': '5',
    'cherries': '5',
    'coconut': '680',
    'cocunuts': '680',
    'cranberry': '1.13',
    'cranberries': '1.13',
    'date': '8',
    'dates': '8',
    'medjool date': '8',
    'medjool dates': '8',
    'fig': '25',
    'figs': '25',
    'grapefruit': '246',
    'grapefruits': '246',
    'grape': '5',
    'grapes': '5',
    'guava': '200',
    'jackfruit': '6800',
    'durian': '6800',
    'kiwi': '50',
    'kiwis' : '50',
    'kiwifruit': '50',
    'lemon': '55',
    'lemons': '55',
    'lime': '50',
    'limes': '50',
    'mango': '200',
    'mangos': '200',
    'cantaloupe': '1360',
    'cantaloupes': '1360',
    'honeydew': '1800',
    'honeydew melon': '1800',
    'honeydew melons': '1800',
    'melon': '1500',
    'melons' : '1500',
    'nectarine': '150',
    'olive': '5',
    'olives': '5',
    'orange': '130',
    'papaya': '450',
    'peach': '150',
    'peaches': '150',
    'pear': '180',
    'pears': '180',
    'pineapple': '1590',
    'pineapples': '1590',
    'plum': '50',
    'plums': '50',
    'pomegranate': '255',
    'pumpkin': '4500',
    'raspberry': '5',
    'raspberries': '5',
    'strawberry': '10',
    'strawberries': '10',
    'watermelon': '9000',
    'artichoke': '368',
    'artichokes': '368',
    'asparagus': '22',
    'asparaguses': '22',
    'eggplant': '453.5',
    'eggplants': '453.5',
    'garlic': '5',
    'green beans': '5',
    'beet' : '113',
    'beets': '113',
    'bell pepper': '170',
    'broccoli': '225',
    'broccolini' : '16',
    'brussel sprouts': '14',
    'cabbage': '9070',
    'carrots': '60',
    'cauliflower': '500',
    'celery': '450',
    'corn': '180',
    'corns': '180',
    'cucumber': '250',
    'kale': '198',
    'kales': '198',
    'lettuce': '650',
    'mushrooms': '15',
    'onion': '160',
    'parsnip': '115',
    'pea': '0.2',
    'peas': '0.2',
    'potato': '184',
    'potatoes': '184',
    'snow pea': '2.5',
    'snow peas': '2.5',
    'spinach': '30',
    'squash': '200',
    'butternut squash': '1100',
    'sweet potato': '113',
    'tomato': '170',
    'zucchini': '200'
}

# Maps and sets for common foods that don't have a "real" unit but instead have the food name as the unit (i.e. "1 egg", "1 apple", "4 corn tortillas" etc.)
FOOD_UNITS = {
    "egg": ("eggs",),
    # "egg": ("eggs", "whole egg", "whole eggs", "egg yolk", "egg yolks", 
            # "eggs yolk", "eggs yolks", "egg white", "egg whites", "eggs white", "eggs whites"),
    "anchovy": ("anchovies",),
    "sardine": ("sardines",),
    "gizzard": ("gizzards",),
    "giblet": ("giblets",),
    "liver": ("livers",),
    "heart": ("hearts",),
    "tongue": ("tongues",),
    "gumdrop": ("gumdrops",),
    "raisin": ("raisins",),
    "waterchestnut": ("waterchestnuts",),
    "triscuit": ("triscuits",),
    "saltine": ("saltines",),
    
    "yam": ("yams",),
    "breadstick": ("breadsticks",),
    "crouton": ("croutons",),
    "ravioli": ("raviolis",),
    "tortellini": ("tortellinis",),
    "pierogi": ("pierogis",),
    "hush puppy": ("hush puppies",),
    "prune": ("prunes",),
    "pita": ("pitas",),
    "naan": ("naans",),
    "baguette": ("baguettes",),
    "scone": ("scones",),
    "pickle": ("pickles",),
    "waxgourd": ("waxgourds",),
    "donette": ("donettes",),
    "donut": ("donuts",),
    "doughnut": ("doughnuts",),

    "shrimp": ("shrimps",),
    "prawn": ("prawns",),
    "lobster": ("lobsters",),
    "crab": ("crabs",),
    "clam": ("clams",),
    "mussel": ("mussels",),
    "oyster": ("oysters",),
    "scallop": ("scallops",),
    "sausage": ("sausages",),
    "peanut": ("peanuts",),
    "nut": ("nuts",),
    "almond": ("almonds",),

    "tortilla": ("tortillas",),
    "rack": ("racks",),
    "bagel": ("bagels",),
    "cake": ("cakes",),
    "bar": ("bars",),
    "biscuit": ("biscuits",),
    "pancake": ("pancakes",),
    "wedge": ("wedges",),
    "steak": ("steaks",),
    "roast": ("roasts",),  # Assuming there might be a plural form
    "taco": ("tacos",),
    "hotdog": ("hotdogs",),
    "frankfurter": ("frankfurters",),
    "tomato": ("tomatoes",),
    "pastry": ("pastries",),
    "patty": ("patties",),
    "hambuger": ("hamburgers",),  # Assuming there might be a plural form
    "burger": ("burgers",),
    "pepper": ("peppers",),
    "onion": ("onions",),
    "bun": ("buns",),
    "banana": ("bananas",),
    "lemon": ("lemons",),
    "lime": ("limes",),
    "waffle": ("waffles",),
    "wafer": ("wafers",),
    "cracker": ("crackers",),
    "apple": ("apples",),
    "apricot": ("apricots",),
    "avocado": ("avocados",),
    "berry" : ("berries",),
    "blackberry": ("blackberries",),
    "blueberry": ("blueberries",),
    "cherry": ("cherries",),
    "coconut": ("coconuts",),
    "cranberry": ("cranberries",),
    "date": ("dates", "medjool", "medjools"),
    "fig": ("figs",),
    "grapefruit": ("grapefruits",),
    "grape": ("grapes",),
    "guava": ("guavas",),
    "jackfruit": ("jackfruits",),
    "durian": ("durians",),
    "kiwi": ("kiwis", "kiwifruit", "kiwifruits"),
    "cantaloupe": ("cantaloupes",),
    "honeydew": ("honeydew", "honeydews"),
    "melon": ("melons",),
    "nectarine": ("nectarines",),
    "olive": ("olives",),
    "orange": ("oranges",),
    "papaya": ("papayas",),
    "peach": ("peaches",),
    "pear": ("pears",),
    "pineapple": ("pineapples",),
    "plum": ("plums",),
    "pomegranate": ("pomegranates",),
    "pumpkin": ("pumpkins",),
    "raspberry": ("raspberries",),
    "strawberry": ("strawberries",),
    "watermelon": ("watermelons",),
    "artichoke": ("artichokes",),
    "asparagus": ("asparaguses",),
    "eggplant": ("eggplants",),

    "clove": ("cloves",),
    # "garlic": ("garlics",),

    # "green bean": ("green beans",),
    "beet": ("beets",),
    # "bell pepper": ("bell peppers",),
    "broccoli": ("broccolis",),
    "broccolini": ("broccolinis",),

    "brussel sprout": ("brussel sprouts",),
    
    "sprout": ("sprouts",),
    
    "cabbage": ("cabbages",),
    "carrot": ("carrots",),
    "cauliflower": ("cauliflowers",),
    "celery": ("celeries",),
    "corn": ("corns",),
    "cucumber": ("cucumbers",),
    "kale": ("kales",),
    "lettuce": ("lettuces",),
    "mushroom": ("mushrooms",),
    "parsnip": ("parsnips",),
    "pea": ("peas", "snowpea", "snowpeas"),
    "potato": ("potatoes",),
    "spinach": ("spinaches",),
    "squash": ("squashes", "butternutsquash"),
    
    # "sweet potato": ("sweet potatoes",),

    "sweetpotato": ("sweetpotatoes",),
    "zucchini": ("zucchinis",)
}

# Create a set of all the food units
FOOD_UNITS_SET = set()

for key, pattern in FOOD_UNITS.items():
    FOOD_UNITS_SET.add(key)
    for val in pattern:
        FOOD_UNITS_SET.add(val)

FOOD_UNIT_TO_STANDARD_FOOD_UNIT = {}

for key, pattern in FOOD_UNITS.items():
    for val in pattern:
        FOOD_UNIT_TO_STANDARD_FOOD_UNIT[val] = key
    FOOD_UNIT_TO_STANDARD_FOOD_UNIT[key] = key

# ANIMAL_PROTEIN_UNIT_TO_GRAMS = {
#     "chicken" : {
#         "breast"  : 170.097,
#         "boneless breast" : 170.097,
#         "bone-in breast" : 283.495,
#         "cutlet" : 85.046,
#         "tender" : 56.699,
#         "tenderloin" : 56.699,
#         "thigh" : 141.748,
#         "drumstick" : 113.398,
#         "drum" : 113.398,
#         "leg" : 113.398,
#         "wing" :  56.699,
#         "giblet" : 28.35,
#         "gizzard" : 28.35
#     },
#      "beef" : {
#         "steak" : 227,
#         "ground beef" : 113,
#         "ribeye" : 340,
#         "sirloin" : 227,
#         "tenderloin" : 170,
#         "brisket" : 453,
#         "short ribs" : 340,
#         "chuck roast" : 453
#     },
#     "pork" : {
#         "chop" : 170,
#         "tenderloin" : 113,
#         "shoulder" : 227,
#         "loin" : 227,
#         "ribs" : 340,
#         "belly" : 227,
#         "ham" : 453,
#         "ground pork" : 113
#     },
#     "turkey" : {
#         "breast" : 227,
#         "thigh" : 170,
#         "drumstick" : 113,
#         "wing" : 85,
#         "ground turkey" : 113,
#         "tenderloin" : 113
#     },
#     "veal" : {
#         "cutlet" : 85,
#         "chop" : 170,
#         "shank" : 227,
#         "tenderloin" : 113,
#         "rib" : 170,
#         "ground veal" : 113
#     },
#     "lamb" : {
#         "chop" : 113,
#         "leg" : 340,
#         "shank" : 227,
#         "rib" : 113,
#         "shoulder" : 227,
#         "ground lamb" : 113
#     }
# }

# MEAT_FOODS = set([
#     "beef",
#     "pork",
#     "chicken",
#     "turkey",
#     "duck",
#     "goose",
#     "lamb",
#     "veal",
#     "sausage",
#     "salmon",
#     "tuna",
#     "trout",
#     "cod",
#     "haddock",
#     "halibut",
#     "mackerel",
#     "sardine",
#     "anchovy",
#     "herring",
#     "swordfish",
#     "snapper",
#     "bass",
#     "catfish",
#     "tilapia",
#     "perch",
#     "pollock",
#     "shark",
#     "shrimp",
#     "prawn",
#     "bison",
#     "buffalo",
#     "rabbit",
#     "quail",
#     "pheasant",
#     "venison",
#     "elk",
#     "moose",
#     "boar",
#     "wild boar",
#     "emu",
#     "ostrich",
#     "alligator",
#     "crocodile",
#     "snake"
# ])

# ---- Unused constants ----

# TODO: Probably can delete the constants below, they've been replaced/deprecated by other constants

# # Fractions words representing the denominator of a fraction
# DENOMINATOR_WORDS = {
#     "half": "/2",
#     "halves": "/2",

#     "quarter": "/4",
#     "quarters": "/4",
#     "fourth": "/4",
#     "fourths": "/4",

#     "third": "/3",
#     "thirds": "/3",

#     "fifth": "/5",
#     "fifths": "/5",

#     "sixth": "/6",
#     "sixths": "/6",

#     "seventh": "/7",
#     "sevenths": "/7",

#     "eighth": "/8",
#     "eighths": "/8",

#     "ninth": "/9",
#     "ninths": "/9",

#     "tenth": "/10",
#     "tenths": "/10",

#     "eleventh": "/11",
#     "elevenths": "/11",

#     "twelfth": "/12",
#     "twelfths": "/12"
# }

# # Fractions represented as multiple words (or numbers) and words
# MULTI_FRACTION_WORDS = {
#     # amount with fraction words
#     "one half": "1/2",
#     "1 half": "1/2",
#     "two halves": "1",

#     "one quarter": "1/4",
#     "1 quarter": "1/4",
#     "two quarters": "1/2",
#     "three quarters": "3/4",
#     "3 quarters": "3/4",
#     "three quarter": "3/4",
#     "3 quarter": "3/4",

#     "one fourth": "1/4",
#     "1 fourth": "1/4",
#     "two fourths": "1/2",
#     "three fourths": "3/4",
#     "3 fourths": "3/4",

#     "one third": "1/3",
#     "1 third": "1/3",
#     "two thirds": "2/3",
#     "two thirds": "2/3",
#     "2 thirds": "2/3",
#     "2 third": "2/3",

#     "one fifth": "1/5",
#     "1 fifth": "1/5",
#     "two fifths": "2/5",
#     "2 fifths": "2/5",
#     "three fifths": "3/5",
#     "3 fifths": "3/5",
#     "four fifths": "4/5",
#     "4 fifths": "4/5",

#     "one sixth": "1/6",
#     "1 sixth": "1/6",
#     "two sixths": "1/3",
#     "three sixths": "1/2",
#     "4 sixths": "2/3",
#     "four sixths": "2/3",
#     "five sixths": "5/6",
#     "5 sixths": "5/6",

#     "one seventh": "1/7",
#     "1 seventh": "1/7",
#     "two sevenths": "2/7",
#     "2 sevenths": "2/7",
#     "three sevenths": "3/7",
#     "3 sevenths": "3/7",
#     "four sevenths": "4/7",
#     "4 sevenths": "4/7",
#     "five sevenths": "5/7",
#     "5 sevenths": "5/7",
#     "six sevenths": "6/7",
#     "6 sevenths": "6/7",

#     "one eighth": "1/8",
#     "1 eighth": "1/8",
#     "two eighths": "1/4",
#     "2 eighths": "1/4",
#     "three eighths": "3/8",
#     "3 eighths": "3/8",
#     "four eighths": "1/2",
#     "five eighths": "5/8",
#     "six eighths": "3/4",
#     "seven eighths": "7/8",

#     "one ninth": "1/9",
#     "two ninths": "2/9",
#     "one tenth": "1/10",
#     "two tenths": "1/5",

#     "one eleventh": "1/11",
#     "two elevenths": "2/11",

#     "one twelfth": "1/12",
#     "two twelfths": "1/6",
#     "eleven twelfths": "11/12",


#     "two thirds": "2/3",
#     "two fourths": "1/2",
#     "two fifths": "2/5",
#     "two sixths": "1/3",
#     "two sevenths": "2/7",
#     "two eighths": "1/4",
#     "two ninths": "2/9",
#     "two tenths": "1/5",
#     "two elevenths": "2/11",
#     "two twelfths": "1/6",

#     "three fourths": "3/4",
#     "three fifths": "3/5",
#     "three sixths": "1/2",
#     "three sevenths": "3/7",
#     "three eighths": "3/8",
#     "three ninths": "1/3",
#     "three tenths": "3/10",
#     "three elevenths": "3/11",
#     "three twelfths": "1/4",
#     "four fifths": "4/5",
#     "four sixths": "2/3",
#     "four sevenths": "4/7",
#     "four eighths": "1/2",
#     "four ninths": "4/9",
#     "four tenths": "2/5",
#     "four elevenths": "4/11",
#     "four twelfths": "1/3",
#     "five sixths": "5/6",
#     "five sevenths": "5/7",
#     "five eighths": "5/8",
#     "five ninths": "5/9",
#     "five tenths": "1/2",
#     "five elevenths": "5/11",
#     "five twelfths": "5/12",
#     "six sevenths": "6/7",
#     "six eighths": "3/4",
#     "six ninths": "2/3",
#     "six tenths": "3/5",
#     "six elevenths": "6/11",
#     "six twelfths": "1/2",
#     "seven eighths": "7/8",
#     "seven ninths": "7/9",
#     "seven tenths": "7/10",
#     "seven elevenths": "7/11",
#     "seven twelfths": "7/12",
#     "eight ninths": "8/9",
#     "eight tenths": "4/5",
#     "eight elevenths": "8/11",
#     "eight twelfths": "2/3",
#     "nine tenths": "9/10",
#     "nine elevenths": "9/11",
#     "nine twelfths": "3/4",
#     "ten elevenths": "10/11",
#     "ten twelfths": "5/6",
#     "eleven twelfths": "11/12"
# }