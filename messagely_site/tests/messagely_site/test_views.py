"""tests for views"""
def test_index_ok(client):
    """test if website runs properly"""
    response = client.get('/')
    assert response.status_code == 404
    