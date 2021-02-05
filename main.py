from io import StringIO
import pandas as pd
import googledrive
import mailchimp
from dotenv import set_key, load_dotenv
import os


def reformat_csv(file_contents):
    """Takes the content from the google file, cleans it and puts it into a formatted dataframe"""
    data = str(file_contents, 'utf-8')
    data = StringIO(data)
    df = pd.read_csv(data)
    df = df.sort_values("id", axis=0)
    df = df.loc[df['id'] > os.getenv("LAST_USER_ID"), ['id', 'provider', 'username', 'email', 'first_name', 'last_name']].reset_index()


def subscribe_and_tag(df):
    """Pulls data from the dataframe and sends it to the tag/subscribe functions"""
    subscribers = []
    emails = []
    count = 0
    for row in range(len(df.index)):
        if count == 499:
            mailchimp.bulk_subscribe(subscribers)
            count = 0
            subscribers = []
        member = {
            "email_address": df["email"][row],
            "status": "subscribed",
            "merge_fields": {
            "FNAME": df["first_name"][row],
            "LNAME": df["last_name"][row],
            "MMERGE3": df.index[row],  # user id
            "MMERGE6": df["provider"][row],  # provider
            "MMERGE8": df["username"][row]  # username
            }
        }
        subscribers.append(member)
        emails.append(df["email"][row])
        count += 1
    mailchimp.bulk_tag(emails)


def set_last_user_id(df):
    last_id = str(df['id'].max())
    set_key(".env", "LAST_USER_ID", last_id)


if __name__ == '__main__':
    
    # get environment variables
    load_dotenv()

    # name of file to be used
    file_id = "1UJQnlz7IxJ27hqvnPYXl4jm-oWjr2Zo4"

    # get google drive connection
    service = googledrive.get_service()

    # read file contents
    file_contents = googledrive.print_file_content(service, file_id)

    # extract important data from file contents to df using pandas
    df = reformat_csv(file_contents)

    # reformat said data for mailchimp and then subscribe/tag the new subscribers
    subscribe_and_tag(df)

    # update id of last user imported in .env file
    set_last_user_id(df)
