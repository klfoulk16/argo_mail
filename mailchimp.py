from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import os
from dotenv import load_dotenv


def get_client():
    # Get environment variables
    load_dotenv()

    client = Client()
    client.set_config(
        {"api_key": os.getenv("MAILCHIMP_API"), "server": os.getenv("MAILCHIMP_SERVER")}
    )
    return client

def get_all_account_lists():
    client = get_client()
    try:
        response = client.lists.get_all_lists()
        print(response)
    except ApiClientError as error:
        print(f"Error: {error}")


def get_list_merge_fields():
    client = get_client()
    list_id = "d73bda636d"
    try:
        response = client.lists.get_list_merge_fields(list_id)
        print(response)
    except ApiClientError as error:
        print("Error: {}".format(error.text))


def add_subscriber():
    list_id = "d73bda636d"
    member_info = {
        "email_address": "mock1@mock.com",
        "status": "subscribed",
        "merge_fields": {
          "FNAME": "Prudence",
          "LNAME": "McVankab",
          "MMERGE3": 0,  # user id
          "MMERGE6": "facebook",  # provider
          "MMERGE8": "mock1"  # username
        }
    }
    client = get_client()
    try:
        response = client.lists.add_list_member(list_id, member_info)
        print(f"response: {response}")
    except ApiClientError as error:
        print(f"An exception occurred: {error.text}")

