import pytest
from mailchimp import get_client
import dotenv
import os

@pytest.mark.skip
def test_setup():
    dotenv.load_dotenv()
    client = get_client(os.getenv("MAILCHIMP_API"), os.getenv("MAILCHIMP_SERVER"))
    response = client.ping.get()
    assert response == {"health_status": "Everything's Chimpy!"}
