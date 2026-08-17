from warehouse_restock_manifest.store import load_Manifest
from warehouse_restock_manifest.config import AppSettings
import logging
logging.basicConfig(level = AppSettings().log_level, format= "%(levelname)s %(name)s: %(message)s")
print(AppSettings().data_path)
valid_manifest, error_manifest = load_Manifest()
print("--- Valid Manifests ---")
print(valid_manifest)
print(len(valid_manifest))
print("--- Error Manifests ---")
print(error_manifest)
print(len(error_manifest))