# config_loader.py

import yaml
import os

def load_config(file_path='config/parameters_config.yml'):
    """Load the configuration from the YAML file."""
    global abs_file_path
    try:
        # Ensure the file path is absolute
        abs_file_path = os.path.abspath(file_path)
        with open(abs_file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found at: {abs_file_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")
