from io import StringIO
import pandas as pd
import googledrive
import mailchimp
from dotenv import set_key, load_dotenv
import os


def reformat_csv(file_contents, last_user_id):
    """Takes the content from the google file, cleans it and puts it into a formatted dataframe"""
    data = str(file_contents, 'utf-8')
    data = StringIO(data)
    df = pd.read_csv(data)
    df = df.sort_values("id", axis=0)
    df = df.loc[df['id'] > last_user_id, ['id', 'provider', 'username', 'email', 'first_name', 'last_name']].reset_index(drop=True)
    return df

def subscribe_and_tag(df, mailchimp_client):
    """Pulls data from the dataframe and sends it to the tag/subscribe functions"""
    subscribers = []
    emails = []
    count = 0
    for row in range(len(df.index)):
        if count == 499:
            mailchimp.bulk_subscribe(subscribers, mailchimp_client)
            count = 0
            subscribers = []
        member = {
            "email_address": df["email"][row],
            "status": "subscribed",
            "merge_fields": {
            "FNAME": df["first_name"][row],
            "LNAME": df["last_name"][row],
            "MMERGE3": df["id"][row],  # user id
            "MMERGE6": df["provider"][row],  # provider
            "MMERGE8": df["username"][row]  # username
            }
        }
        subscribers.append(member)
        emails.append(df["email"][row])
        count += 1
    mailchimp.bulk_subscribe(subscribers, mailchimp_client)
    mailchimp.bulk_tag(emails, mailchimp_client)


def set_last_user_id(df):
    last_id = str(df['id'].max())
    set_key(".env", "LAST_USER_ID", last_id)


if __name__ == '__main__':
    
    # get environment variables
    load_dotenv()

    # name of file to be used
    file_id = "1zeYWzL1hsJsEbT9IeKoE7MrJ7bhpOgc1"

    # get google drive connection
    googledrive_service = googledrive.get_service()

    # read file contents
    file_contents = googledrive.print_file_content(googledrive_service, file_id)

    # extract important data from file contents to df using pandas
    df = reformat_csv(file_contents)

    mailchimp_client = mailchimp.get_client(os.getenv("MAILCHIMP_API"), os.getenv("MAILCHIMP_SERVER"))

    # reformat said data for mailchimp and then subscribe/tag the new subscribers
    last_user_id = int(os.getenv("LAST_USER_ID"))
    subscribe_and_tag(df, mailchimp_client)

    # update id of last user imported in .env file
    set_last_user_id(df)
