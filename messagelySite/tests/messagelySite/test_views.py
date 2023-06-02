def test_index_ok(client):
    response = client.get('/')
    #should be 200
    assert response.status_code == 404