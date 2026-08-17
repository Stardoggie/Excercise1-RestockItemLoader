import json
from pathlib import Path
from pydantic import ValidationError
from warehouse_restock_manifest.config import AppSettings
from warehouse_restock_manifest.models import Restockitem



class ManifestStoreError(Exception):
    """base exception for all errors in this module"""

class FixtureNotFound(ManifestStoreError):
    """raise when the Manifest fixture file does not exist"""
class InvalidFixtureFormat(ManifestStoreError):
    """raise when Manifest data cannot be loaded in due to format issues"""


def load_Manifest(path : Path |None = None) -> tuple[list[Restockitem],list[dict[str, list[str]]]]:
    """
        loads restock manifests as a Restockitem class from a .json file and sorts it into valid and invalid tickets with error handling
    """
    #print(f"---FUNCTION NAME: {load_Manifest.__name__}---")
    resolved_path = path if path is not None else AppSettings().data_path
    try:
        raw_text = resolved_path.read_text(encoding="utf-8")
    except FileNotFoundError as e:
        #raise ... from ...
        # raise one exception into another exception
        raise FixtureNotFound(f"No ticket fixture at {resolved_path}") from e

    #will turn json into Python Object. if data isn't in json format, you can get issues
    try:
        rows = json.loads(raw_text)
    except json.JSONDecodeError as e:
        raise InvalidFixtureFormat(f"Tickets data could not be loaded in from {resolved_path}") from e

    valid_Manifest: list[Restockitem] = []
    error_Manifest: list[dict[str, list[str]]] = []
    for row in rows:
        try:
            valid_Manifest.append(Restockitem.model_validate(row))
        except ValidationError as e:
            err_msgs = [f"{e['loc']} : {e['msg']}" for e in e.errors()]
            error_Manifest.append({"id": row.get("sku","<no sku>"), "errors" : err_msgs})
    return valid_Manifest, error_Manifest
