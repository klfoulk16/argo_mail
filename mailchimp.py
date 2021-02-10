"""Provides all mailchimp api functions."""

from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import hashlib


def get_client(mailchimp_api_key, mailchimp_server):
    """Creates a MailChimp client instance.
    
    Args:
    mailchimp_api_key: Mailchimp api key, you can set this up in your mailchimp account.
    mailchimp_server: Mailchimp server, found in your account url.
    
    Returns:
    client: Mailchimp client"""
    client = Client()
    client.set_config(
        {"api_key": mailchimp_api_key, "server": mailchimp_server}
    )
    return client


def bulk_tag(emails, client):
    """Takes a list of subscribed emails and adds specified mailchimp tag to all emails
    
    Args:
    emails: List of subscribed emails
    client: MailChimp client
    
    Returns:
    If successful: Total number of emails tagged"""
    tag_id = "649346"
    list_id = "d73bda636d"
    try:
        response = client.lists.batch_segment_members(
            {"members_to_add": emails},
            list_id,
            tag_id
        )
        return response['total_added']
    except ApiClientError as error:
        print(f"An exception occurred: {error.text}")
        quit()


def bulk_subscribe(subscribers, client):
    """Subscribes a list of subscribers to mailchimp list.
    
    Args:
    Subscribers: list of dicts formatted like so:
    {
        "email_address": "mock1@mock.com",
        "status": "subscribed",
        "merge_fields": {
          "FNAME": "Prudence",
          "LNAME": "McVankab",
          "MMERGE3": 0,  # user id
          "MMERGE6": "facebook",  # provider
          "MMERGE8": "magicmock10"  # username
        },
    }
    Client: Mailchimp client
    
    Returns:
    If successful: Values from response object dictionary that tell us stats about the upload.
    """
    list_id = "d73bda636d"
    try:
        # can only add up to 500 at a time
        response = client.lists.batch_list_members(list_id, {"members": subscribers, "update_existing":True})
        return (response['total_created'], response['total_updated'], response['error_count'], response['errors'])
    except ApiClientError as error:
        print(f"An exception occurred: {error.text}")
        quit()


def get_all_account_lists(client):
    """Used in Setup: Fetches all lists that are part of the given account.
    
    Args:
    client: Mailchimp client"""
    try:
        response = client.lists.get_all_lists()
        print(response)
    except ApiClientError as error:
        print(f"Error: {error}")


def get_list_merge_fields(client):
    """Used in Setup: Prints out list of merge fields for list hardcoded in list_id.
    
    Args:
    client: Mailchimp client"""
    list_id = "d73bda636d"
    try:
        response = client.lists.get_list_merge_fields(list_id)
        print(response)
    except ApiClientError as error:
        print("Error: {}".format(error.text))


def add_subscriber(client):
    """Used in Setup: Add the subscriber hardcoded in member_info.
    
    Args:
    client: Mailchimp client"""
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
    try:
        response = client.lists.add_list_member(list_id, member_info)
        print(f"response: {response}")
    except ApiClientError as error:
        print(f"An exception occurred: {error.text}")


def add_or_update_subscriber(client):
    """Used in Setup: Add or update the subscriber hardcoded in subscriber_info.
    
    Args:
    client: Mailchimp client"""
    list_id = "d73bda636d"
    email = "mock1@mock.com"
    subscriber_info = {
        "email_address": email,
        "status_if_new": "subscribed",
        "merge_fields": {
            "FNAME": "Prudence",
            "LNAME": "McVankab",
            "MMERGE3": 0,  # user id
            "MMERGE6": "apple",  # provider (changed)
            "MMERGE8": "mock1"  # username
        }
    }
    subscriber_hash = hashlib.md5(email.encode('utf-8')).hexdigest()
    try:
        response = client.lists.set_list_member(
            list_id,
            subscriber_hash,
            subscriber_info
        )
        print(f"response: {response}")
    except ApiClientError as error:
        print(f"An exception occurred: {error.text}")


def view_contacts_tags(client):
    """Used in Setup: View all tags associated with a contact.

    Args:
    client: Mailchimp client"""
    list_id = "d73bda636d"
    email = "klf16@my.fsu.edu"
    subscriber_hash = hashlib.md5(email.encode('utf-8')).hexdigest()
    try:
        response = client.lists.get_list_member_tags(list_id, subscriber_hash)
        print(f"response: {response}")
    except ApiClientError as error:
        print(f"An exception occurred: {error.text}")
