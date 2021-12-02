"""Tests"""
import pytest
import pandas as pd
import main


# 3. google file reformating works properly, assert env variable worked properly
def test_reformat_csv(file_contents):
    df = main.reformat_csv(file_contents, 12947)

    # assert that only users with id's greater than 12947 were included
    assert df['id'].min() == 12948

    # make sure columns are correct
    assert list(df.columns) == ['id', 'provider', 'username', 'email', 'first_name', 'last_name', 'current_sign_in_at']

# deprecated
# def test_empty_dataframe(df, capsys, monkeypatch):
#     """Make sure empty dataframe (aka no new subscribers is handled properly)"""
#     def fake_pass(*argv, **kwargs):
#         pass

#     def fake_reformat_csv(*argv, **kwargs):
#         return df.iloc[0:0]

#     monkeypatch.setattr('main.googledrive.get_service', fake_pass)
#     monkeypatch.setattr('main.googledrive.print_file_content', fake_pass)
#     monkeypatch.setattr('main.reformat_csv', fake_reformat_csv)
#     main.main()
#     out, err = capsys.readouterr()
#     assert out == "There were no new subscribers\n"


# emails and subscribe lists are in proper format
def test_subscribe_and_tag_format(df, monkeypatch):
    class test_objects(object):
        batches = []
        emails = None
        tag_id = 12345
    
    def fake_bulk_subscribe(subscribers, mailchimp_client):
        test_objects.batches.append(subscribers)
        return (1, 2, 0, [])

    def fake_bulk_tag(emails, mailchimp_client, tag_id):
        test_objects.emails = emails
        return 3

    monkeypatch.setattr('main.mailchimp.bulk_subscribe', fake_bulk_subscribe)
    monkeypatch.setattr('main.mailchimp.bulk_tag', fake_bulk_tag)
    main.subscribe_and_tag(df, 'not_a_mailchimp_client')
    assert test_objects.emails == ['magicmock10@mock.com', 'magicmock5@mock.com']
    assert test_objects.batches[0] == [{
            "email_address": 'magicmock10@mock.com',
            "status": "subscribed",
            "merge_fields": {
            "FNAME": 'Craig',
            "LNAME": 'Laudenslager',
            "MMERGE3": 12951,  # user id
            "MMERGE6": "email",  # provider
            "MMERGE8": 'PABoatBoy'  # username
            }
        }, {
            "email_address": 'magicmock5@mock.com',
            "status": "subscribed",
            "merge_fields": {
            "FNAME": 'Brian',
            "LNAME": 'Burrows',
            "MMERGE3": 12952,  # user id
            "MMERGE6": "google",  # provider
            "MMERGE8": 'brian_burrows'  # username
            }
        }]


# batches subscribers if over 499
def test_subscribe_and_tag_batches(long_df, monkeypatch):
    assert len(long_df.index) == 1680

    class test_objects(object):
        batches = []
    
    def fake_bulk_subscribe(subscribers, mailchimp_client):
        test_objects.batches.append(subscribers)
        return (1, 2, 0, [])

    def fake_bulk_tag(emails, mailchimp_client):
        return 3

    monkeypatch.setattr('main.mailchimp.bulk_subscribe', fake_bulk_subscribe)
    monkeypatch.setattr('main.mailchimp.bulk_tag', fake_bulk_tag)
    main.subscribe_and_tag(long_df, 'not_a_mailchimp_client')
    assert len(test_objects.batches) == 4
    assert len(test_objects.batches[0]) == 499


def test_check_na():
    df = pd.read_csv('user_data.csv', keep_default_na=False)
    df = df.sort_values("id", axis=0)
    df = df.loc[df['id'] > 12945, ['id', 'provider', 'username', 'email', 'first_name', 'last_name', 'current_sign_in_at']].reset_index(drop=True)
    print(df)
    assert not df["current_sign_in_at"][0]
    assert df["current_sign_in_at"][3]

