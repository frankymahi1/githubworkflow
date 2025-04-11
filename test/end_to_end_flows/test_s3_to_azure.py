import pytest
from config_loader import load_config
config = load_config()

# Parametrize the test case for nas_to_azure

# Parametrize the test case for s3_to_azure
@pytest.mark.parametrize("transfer", config['s3_to_azure'])
def test_s3_to_azure_transfer(transfer):
    file_type = transfer['file_type']
    raw_source_path = transfer['raw_source_path']
    dest_path = transfer['dest_path']
    transformation_flag = transfer.get('transformation_flag', False)

    # Example assertions or operations for s3_to_azure
    assert isinstance(file_type, str), "File type should be a string"
    assert isinstance(raw_source_path, str), "Raw source path should be a string"
    assert isinstance(dest_path, str), "Destination path should be a string"
    assert isinstance(transformation_flag, bool), "Transformation flag should be a boolean"

    # Additional logic to simulate file transfer can be added here
    print(f"Testing S3 to Azure transfer of {file_type} from {raw_source_path} to {dest_path} with transformation: {transformation_flag}")


