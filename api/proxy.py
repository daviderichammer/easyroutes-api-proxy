from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

EASYROUTES_API_BASE = "https://easyroutes.roundtrip.ai/api/2024-07"

@app.route('/')
def home():
    return jsonify({
        "service": "EasyRoutes API Proxy",
        "status": "running",
        "endpoints": [
            "/api/proxy/authenticate",
            "/api/proxy/routes",
            "/api/proxy/routes/<route_id>"
        ]
    })

@app.route('/api/proxy/authenticate', methods=['POST'])
def proxy_authenticate():
    """Proxy authentication requests to EasyRoutes API"""
    try:
        data = request.get_json()
        
        response = requests.post(
            f"{EASYROUTES_API_BASE}/authenticate",
            json=data,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "application/json",
                "Accept-Language": "en-US,en;q=0.9"
            },
            timeout=30
        )
        
        return response.json(), response.status_code
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/proxy/routes', methods=['GET'])
def proxy_routes():
    """Proxy routes list requests"""
    try:
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({"error": "Authorization header required"}), 401
        
        response = requests.get(
            f"{EASYROUTES_API_BASE}/routes",
            headers={
                "Authorization": auth_header,
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "application/json"
            },
            params=request.args.to_dict(),
            timeout=30
        )
        
        return response.json(), response.status_code
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/proxy/routes/<route_id>', methods=['GET'])
def proxy_route_detail(route_id):
    """Proxy route detail requests"""
    try:
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({"error": "Authorization header required"}), 401
        
        response = requests.get(
            f"{EASYROUTES_API_BASE}/routes/{route_id}",
            headers={
                "Authorization": auth_header,
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "application/json"
            },
            timeout=30
        )
        
        return response.json(), response.status_code
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
