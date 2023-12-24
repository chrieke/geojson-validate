import geojson

from .context import validate


def test_validate():
    geojson_fp = "./tests/examples_geojson/invalid/polygon_has_duplicate_nodes.geojson"
    with open(geojson_fp) as f:
        json = geojson.load(f)
    result = validate(json)
    assert "duplicate_nodes" in result["invalid"]
