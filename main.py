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
    my_total = 0
    mailchimp_created = 0
    mailchimp_updated = 0
    mailchimp_error_count = 0
    for row in range(len(df.index)):
        if count == 499:
            created, updated, error_count, errors = mailchimp.bulk_subscribe(subscribers, mailchimp_client)
            mailchimp_created += created
            mailchimp_updated += updated
            mailchimp_error_count += error_count
            for error in errors:
                print(f"There was an error: {error}")
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
        my_total += 1
    created, updated, error_count, errors = mailchimp.bulk_subscribe(subscribers, mailchimp_client)
    mailchimp_created += created
    mailchimp_updated += updated
    mailchimp_error_count += error_count
    for error in errors:
        print(f"There was an error: {error}")
    print(f"Created: {mailchimp_created}, Updated: {mailchimp_updated}, Errors: {mailchimp_error_count}")
    mailchimp_total = mailchimp_created + mailchimp_updated + mailchimp_error_count
    if my_total == mailchimp_total:
        print("My total matched mailchimp's")
    else:
        print(f"My estimate of users to add ({my_total}) was not the same as the number mailchimp added ({mailchimp_total})")
    tagged = mailchimp.bulk_tag(emails, mailchimp_client)
    print(f"Total tagged: {tagged}")


def set_last_user_id(df):
    last_id = str(df['id'].max())
    set_key(".env", "LAST_USER_ID", last_id)


def main():
    # get environment variables
    load_dotenv()

    # name of file to be used
    file_id = "1zeYWzL1hsJsEbT9IeKoE7MrJ7bhpOgc1"

    # get google drive connection
    googledrive_service = googledrive.get_service()

    # read file contents
    file_contents = googledrive.print_file_content(googledrive_service, file_id)

    # extract important data from file contents to df using pandas
    last_user_id = int(os.getenv("LAST_USER_ID"))
    df = reformat_csv(file_contents, last_user_id)

    # handle case of no new subscribers
    if len(df) > 0:
        mailchimp_client = mailchimp.get_client(os.getenv("MAILCHIMP_API"), os.getenv("MAILCHIMP_SERVER"))

        # reformat said data for mailchimp and then subscribe/tag the new subscribers
        subscribe_and_tag(df, mailchimp_client)

        # update id of last user imported in .env file
        set_last_user_id(df)
    else:
        print("There were no new subscribers")


if __name__ == '__main__':
    main()