import pytest
from app.main import app

# Setup for testing Flask app
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Check base health route
def test_health_check(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

# Shorten a URL and redirect test
def test_shorten_and_redirect(client):
    # Send POST request to shorten URL
    response = client.post('/api/shorten', json={'url': 'https://www.google.com'})
    assert response.status_code == 201
    data = response.get_json()
    short_code = data['short_code']

    # Follow the redirect from short code
    response = client.get(f'/{short_code}', follow_redirects=False)
    assert response.status_code == 302  # 302 = redirect
    assert response.headers['Location'] == 'https://www.google.com'

# Invalid URL test
def test_invalid_url(client):
    response = client.post('/api/shorten', json={'url': 'not_a_url'})
    assert response.status_code == 400

# Missing URL field test
def test_missing_url_field(client):
    response = client.post('/api/shorten', json={})
    assert response.status_code == 400

# Check stats (clicks, created_at, url)
def test_stats(client):
    # Shorten a test URL
    response = client.post('/api/shorten', json={'url': 'https://www.example.com'})
    short_code = response.get_json()['short_code']

    # Simulate two clicks
    client.get(f'/{short_code}')
    client.get(f'/{short_code}')

    # Check analytics
    stats_resp = client.get(f'/api/stats/{short_code}')
    stats = stats_resp.get_json()
    assert stats['url'] == 'https://www.example.com'
    assert stats['clicks'] == 2
    assert 'created_at' in stats
