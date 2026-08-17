
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class AppSettings(BaseSettings) :
    """
    BaseSettings gives you the Pydantic checks, but for CONFIGURATION rather than data
    maps env rars to class properties.
        ex; RESTOCK_MANIFEST_DATA_PATH -> data path
    env_file - the exact name of your .env file to look in
    env_prefix - the prefix for all the env vars to look for
    extra - decides how to contain env file vvars that dont have mappings in the class
    """

    model_config = SettingsConfigDict(env_file=[".env",".env.prod"], env_prefix="RESTOCK_MANIFEST_", extra= "ignore")
    # giving default values means this class can still be instantiated withou an .env file
    data_path: Path = Path("data/restock_manifest.json")
    default_page_size: int = 5
    log_level: str = "DEBUG"
