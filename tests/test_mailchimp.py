import pytest
from mailchimp import get_client


def test_setup():
    client = get_client()
    response = client.ping.get()
    assert response == {"health_status": "Everything's Chimpy!"}
