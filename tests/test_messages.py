import pytest


def test_get_messages_no_records(client):
    response = client.get('/api/v1/messages')
    expected_result = {
        'success': True,
        'data': [],
        'number_of_records': 0
    }
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.get_json() == expected_result


def test_get_messages(client, sample_data):
    response = client.get('/api/v1/messages')
    response_data = response.get_json()
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data['success'] is True
    assert len(response_data['data'])


def test_get_single_message(client, sample_data):
    response = client.get('/api/v1/messages/1')
    response_data = response.get_json()
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data['success'] is True
    assert response_data['data']['receiver'] == 'Lou'
    assert response_data['data']['date'] == '25-10-2020'
    assert response_data['data']['text'] == 'Hey Lou, its Jon! Loved connecting with you. Enjoy Vegas!'
    assert response_data['data']['sender'] == 'John'


def test_get_single_message_not_found(client, sample_data):
    response = client.get('/api/v1/messages/25')
    response_data = response.get_json()
    assert response.status_code == 404
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data['success'] is False
    assert 'data' not in response_data


def test_create_message(client, token, message):
    response = client.post('/api/v1/messages',
                           json=message,
                           headers={
                               'Authorization': f'Bearer {token}'
                           })
    response_data = response.get_json()
    expected_result = {
        'success': True,
        'data': {
            **message,
            'id': 1,
        }
    }
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data == expected_result

    response = client.get('/api/v1/messages/1')
    response_data = response.get_json()
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data == expected_result


@pytest.mark.parametrize(
    'data,missing_field',
    [
        ({'receiver': 'Lou', 'date': '25-10-2020', 'text': 'Hey Lou, its Jon! Loved connecting with you. Enjoy Vegas!'},
         'sender'),
        ({'date': '25-10-2020', 'text': 'Hey Lou, its Jon! Loved connecting with you. Enjoy Vegas!', 'sender': 'John'},
         'receiver'),
        ({'receiver': 'Lou', 'text': 'Hey Lou, its Jon! Loved connecting with you. Enjoy Vegas!', 'sender': 'John'},
         'date'),
        ({'receiver': 'Lou', 'date': '25-10-2020', 'sender': 'John'},
         'text'),
    ]
)
def test_create_message_ivalid_data(client, token, data, missing_field):
    response = client.post('/api/v1/messages',
                           json=data,
                           headers={
                               'Authorization': f'Bearer {token}'
                           })
    response_data = response.get_json()
    assert response.status_code == 400
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data['success'] is False
    assert 'data' not in response_data
    assert missing_field in response_data['message']
    assert 'Missing data for required field.' in response_data['message'][missing_field]


def test_create_message_ivalid_content_type(client, token, message):
    response = client.post('/api/v1/messages',
                           data=message,
                           headers={
                               'Authorization': f'Bearer {token}'
                           })
    response_data = response.get_json()
    assert response.status_code == 415
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data['success'] is False
    assert 'data' not in response_data
