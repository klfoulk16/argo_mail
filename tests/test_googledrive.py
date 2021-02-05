import pytest
from googledrive import mock_print_file_content, print_file_content, get_service

def test_print_file_content():
    file_id = "1UJQnlz7IxJ27hqvnPYXl4jm-oWjr2Zo4"
    service = get_service()
    assert print_file_content(service, file_id) == mock_print_file_content()
