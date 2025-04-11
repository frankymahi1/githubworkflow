# tests/conftest.py

import pytest
import yaml

@pytest.fixture(scope="session")
def config():
    """Load the configuration from the YAML file."""
    file_path = r'C:\RBC\github_actions\githubworkflow\config\parameters_config.yml'
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found at: {file_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")
