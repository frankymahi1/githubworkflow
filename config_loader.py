# config_loader.py

import yaml

def load_config():
    """Load the configuration from the YAML file."""
    file_path= 'C:\RBC\github_actions\githubworkflow\config\parameters_config.yml'
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found at: {file_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")
