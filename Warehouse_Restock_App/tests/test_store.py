import pytest  # type: ignore
from warehouse_restock_manifest.store import load_Manifest,FixtureNotFound
from warehouse_restock_manifest.models import Restockitem
from pydantic import ValidationError
from pathlib import Path

@pytest.mark.parametrize("field, value",[("category", "Invalid"),("quantity", 0),("unit_cost", 0)])
def test_invalid_fields(field, value):
    """
        tests invalid sets of data for RestockItem
    """
    data = {
        "sku": "SKU123",
        "warehouse": "WH1",
        "quantity": 10,
        "unit_cost": 25.0,
        "category": "electronics",
    }
    
    data[field] = value

    with pytest.raises(ValidationError):
        Restockitem(**data)

def test_valid_fields():
    """
        tests a valid set of data for RestockItem
    """
    data = {
            "sku": "SKU123",
            "warehouse": "WH1",
            "quantity": 10,
            "unit_cost": 25.0,
            "category": "electronics",
        }
    assert Restockitem(**data) != pytest.raises(ValidationError)

def test_restock_manifest_json():
    """
    tests restock_manifest.json for expected number of valid and invalid tickets
    """
    valid_manifest, error_manifest = load_Manifest()
    assert len(valid_manifest) == 8, "Expected for Valid Restock items to be 8"
    assert len(error_manifest) == 4, "Expected for Invalid RestockItems to be 4"

def test_load_path_json():
    with pytest.raises(FixtureNotFound):
        valid_manifest, error_manifest = load_Manifest(Path("data/non_existant_manifest.json")) 
