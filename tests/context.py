import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

# Import the required classes and functions
# pylint: disable=unused-import,wrong-import-position
from geojson_validator import (
    main,
    geometry_utils,
    checks_invalid,
    checks_problematic,
    fixes_invalid,
    validation_utils,
    schema_validation,
)
