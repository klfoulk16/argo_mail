""""The heart of the project - downloads csv and pushes new users to mailchimp"""

from io import StringIO
import pandas as pd
import googledrive
import mailchimp
from dotenv import set_key, load_dotenv
import os
import datetime
import mail_logs


def reformat_csv(file_contents, last_user_id):
    """Takes the content from the google file, cleans it and puts it into a formatted dataframe
    
    Args:
    file_contents: Byte string of file contents
    last_user_id: Int, id of last user imported to milchimp.
    
    Returns:
    Dataframe of the users that haven't yet been imported with only the values that are needed."""
    data = str(file_contents, 'utf-8')
    data = StringIO(data)
    df = pd.read_csv(data, keep_default_na=False)
    df = df.sort_values("id", axis=0)
    df = df.loc[df['id'] > last_user_id, ['id', 'provider', 'username', 'email', 'first_name', 'last_name', 'current_sign_in_at']].reset_index(drop=True)
    return df


def subscribe_and_tag(df, mailchimp_client):
    """Pulls data from the dataframe, sends it to the tag/subscribe functions and prints results.

    Args:
    df: Dataframe of users to be subscribed to mailchimp with proper info.
    mailchimp_client: Mailchimp client
    """
    subscribers = []
    emails = []
    not_logged_in_emails = []
    count = 0
    tagged = 0
    count_not_logged_in = 0
    mailchimp_created = 0
    mailchimp_updated = 0
    mailchimp_error_count = 0
    mailchimp_errors = []
    for row in range(len(df.index)):
        if count == 499:
            created, updated, error_count, errors = mailchimp.bulk_subscribe(subscribers, mailchimp_client)
            tagged += mailchimp.bulk_tag(emails, mailchimp_client, 649346)
            mailchimp_created += created
            mailchimp_updated += updated
            mailchimp_error_count += error_count
            for error in errors:
                mailchimp_errors.append(error)
            count = 0
            subscribers = []
            emails = []
        member = {
            "email_address": df["email"][row],
            "status": "subscribed",
            "merge_fields": {
            "FNAME": df["first_name"][row],
            "LNAME": df["last_name"][row],
            "MMERGE3": int(df["id"][row]),  # user id
            "MMERGE6": df["provider"][row],  # provider
            "MMERGE8": df["username"][row]  # username
            }
        }
        if not df["current_sign_in_at"][row]:
            not_logged_in_emails.append(df["email"][row])
        subscribers.append(member)
        emails.append(df["email"][row])
        count += 1
    created, updated, error_count, errors = mailchimp.bulk_subscribe(subscribers, mailchimp_client)
    tagged += mailchimp.bulk_tag(emails, mailchimp_client, "649346")
    count_not_logged_in += mailchimp.bulk_tag(not_logged_in_emails, mailchimp_client, "1619729")
    mailchimp_created += created
    mailchimp_updated += updated
    mailchimp_error_count += error_count
    for error in errors:
        mailchimp_errors.append(error)
    mail_logs.new_imports_log(mailchimp_created, mailchimp_updated, mailchimp_error_count, errors, tagged, count_not_logged_in)


def set_last_user_id(df):
    """Set the value of LAST_USER_ID in our .env file to be the highest id we imported today.
    
    Args:
    df: Dataframe of users that were imported to mailchimp."""
    last_id = str(df['id'].max())
    print(f"Users added through {last_id}")
    set_key(".env", "LAST_USER_ID", last_id)


def main():
    """Downloads file of all users from GoogleDrive, pulls information for the new users,
    subscribes them to mailchimp and tags them 'Downloaded app'"""

    # for the cron logs
    print(datetime.datetime.now())
    
    # get environment variables
    load_dotenv()

    # name of file to be used
    # test: 1zeYWzL1hsJsEbT9IeKoE7MrJ7bhpOgc1
    file_id = os.getenv("FILE_ID")

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

        try:
            # reformat said data for mailchimp and then subscribe/tag the new subscribers
            subscribe_and_tag(df, mailchimp_client)
            # update id of last user imported in .env file
            set_last_user_id(df)
        except Exception as e:
            message = f"There was an error during subscribe and tag:\n {e}"
            print(message)
            mail_logs.other_news_log("Error", message)

    else:
        # email myself that there were no imports today
        mail_logs.other_news_log("Argo Email: No New Users", "No new Argo users to import today.")


if __name__ == '__main__':
    main()
