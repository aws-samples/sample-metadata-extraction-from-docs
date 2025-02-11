import json
import yaml
import logging
from globals import *
from pathlib import Path
from typing import Union, Dict, Optional

# Create a logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def load_config(config_file: Union[Path, str]) -> Optional[Dict]:
    """
    Load configuration from a local file.

    :param config_file: Path to the local file
    :return: Dictionary with the loaded configuration
    """
    try:
        config_data: Optional[Dict] = None
        logger.info(f"Loading config from local file system: {config_file}")
        content = Path(config_file).read_text()
        config_data = yaml.safe_load(content)
        logger.info(f"Loaded config from local file system: {json.dumps(config_data, indent=2)}")
    except Exception as e:
        logger.error(f"Error loading config from local file system: {e}")
        config_data = None
    return config_data