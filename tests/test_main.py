"""Tests"""
import pytest
import main


# 3. google file reformating works properly, assert env variable worked properly
def test_reformat_csv(file_contents):
    df = main.reformat_csv(file_contents, 12947)

    # assert that only users with id's greater than 12947 were included
    assert df['id'].min() == 12948

    # make sure columns are correct
    assert list(df.columns) == ['id', 'provider', 'username', 'email', 'first_name', 'last_name']


# emails and subscribe lists are in proper format
def test_subscribe_and_tag_format(df, monkeypatch):
    class test_objects(object):
        batches = []
        emails = None
    
    def fake_bulk_subscribe(subscribers, mailchimp_client):
        test_objects.batches.append(subscribers)

    def fake_bulk_tag(emails, mailchimp_client):
        test_objects.emails = emails

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

    def fake_bulk_tag(emails, mailchimp_client):
        pass

    monkeypatch.setattr('main.mailchimp.bulk_subscribe', fake_bulk_subscribe)
    monkeypatch.setattr('main.mailchimp.bulk_tag', fake_bulk_tag)
    main.subscribe_and_tag(long_df, 'not_a_mailchimp_client')
    assert len(test_objects.batches) == 4
    assert len(test_objects.batches[0]) == 499


# 5. only tries to subscribe users who haven't been subscribed yet (env var)

# Non-code tests:

# 2. ME: that the new users get the new downloaded app emails and such 