def test_index_ok(client):
    #Make a get request to /and store the response object
    #using the Django test client
    response = client.get('/')
    #Assert that the status_code s 200 (OK)
    assert response.status_code == 200