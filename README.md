# EasyRoutes API Proxy

A simple proxy service to bypass WAF blocking for EasyRoutes API requests.

## Purpose

This proxy service forwards API requests to the EasyRoutes API, bypassing IP-based blocking that may occur on certain hosting providers (like Hetzner).

## Endpoints

- `GET /` - Service status and available endpoints
- `POST /proxy/authenticate` - Proxy for EasyRoutes authentication
- `GET /proxy/routes` - Proxy for listing routes
- `GET /proxy/routes/<route_id>` - Proxy for getting route details

## Deployment

### Render.com
1. Create a new Web Service
2. Connect this repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `gunicorn app:app`

### Railway.app
1. Create a new project
2. Deploy from GitHub
3. Railway will auto-detect Flask app

### Fly.io
1. Install flyctl
2. Run `fly launch`
3. Deploy with `fly deploy`

## Usage

Replace `https://easyroutes.roundtrip.ai/api/2024-07` with your proxy URL in your application.

Example:
```python
# Instead of:
response = requests.post('https://easyroutes.roundtrip.ai/api/2024-07/authenticate', ...)

# Use:
response = requests.post('https://your-proxy.onrender.com/proxy/authenticate', ...)
```
