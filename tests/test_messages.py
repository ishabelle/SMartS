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
    assert response_data['data']['date'] == '25-10-2021'
    assert response_data['data']['text'] == 'Hey Lou, its Jon! Loved connecting with you. Enjoy Vegas!'
    assert response_data['data']['sender'] == 'John'


def test_get_single_message_not_found(client, sample_data):
    response = client.get('/api/v1/messages/25')
    response_data = response.get_json()
    assert response.status_code == 404
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data['success'] is False
    assert 'data' not in response_data
