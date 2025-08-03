from flask import Flask, request, jsonify, redirect, abort
from app.models import store
from app.utils import generate_short_code, is_valid_url

app = Flask(__name__)

# Health check: used to verify app is running
@app.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "URL Shortener API"
    })

# API health check
@app.route('/api/health')
def api_health():
    return jsonify({
        "status": "ok",
        "message": "URL Shortener API is running"
    })

#  POST /api/shorten — Takes long URL, returns short one
@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"error": "Missing 'url' in request"}), 400

    original_url = data['url']
    
    # Validate the input URL
    if not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL format"}), 400

    # Generate a unique short code
    short_code = generate_short_code()
    while store.get_url(short_code):
        short_code = generate_short_code()  # Avoid collision

    # Store the mapping
    store.add_url(short_code, original_url)

    # Return the short URL and code
    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}"
    }), 201

#  GET /<short_code> — Redirect to original long URL
@app.route('/<short_code>', methods=['GET'])
def redirect_to_original(short_code):
    data = store.get_url(short_code)
    if not data:
        return abort(404)  # Code not found

    # Track the redirect by increasing click count
    store.increment_click(short_code)

    # Redirect user to original long URL
    return redirect(data['url'])

#  GET /api/stats/<short_code> — Get analytics info
@app.route('/api/stats/<short_code>', methods=['GET'])
def get_stats(short_code):
    data = store.get_stats(short_code)
    if not data:
        return jsonify({"error": "Short code not found"}), 404

    # Return original URL, click count and creation timestamp
    return jsonify({
        "url": data['url'],
        "clicks": data['clicks'],
        "created_at": data['created_at']
    })
