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


def test_get_authors(client, sample_data):
    response = client.get('/api/v1/messages')
    response_data = response.get_json()
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data['success'] is True
    assert len(response_data['data'])

