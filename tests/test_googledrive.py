import pytest
from googledrive import print_file_content, get_service

# deprecated...this uses old token.pickle file which was set to my google drive
@pytest.mark.skip
def test_print_file_content(file_contents):
    """Assert that drive is able to access passed file"""
    file_id = "1HZxhz0ot6FUDD6gDQ29MzE7C73PX30Rt"
    service = get_service()
    assert print_file_content(service, file_id) == file_contents
