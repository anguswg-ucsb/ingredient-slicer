# pytest library
import pytest

import re

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# ---- Test _find_and_remove_hyphens_around_substring() utils function  ----
# -------------------------------------------------------------------------------

def test_remove_casual_quantity_few_dashes_of_salt():
    assert _utils._find_and_replace_casual_quantities("Few dashes of salt") == "3 dashes of salt"
    assert _utils._find_and_replace_casual_quantities("few dashes of salt") == "3 dashes of salt"
    assert _utils._find_and_replace_casual_quantities("a couple dashes of salt") == "2 dashes of salt"

