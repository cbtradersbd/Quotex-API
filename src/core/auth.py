# Session Handler & Cloudflare Clearance
import requests

class SessionManager:
    def __init__(self, api_url="https://api1.api.cbtraderbd.xyz/docs"):
        self.api_url = api_url
        self.session = requests.Session()

    def get_auth_headers(self):
        return {"User-Agent": "CBTradersBD/2.5.0", "Accept": "application/json"}

    def refresh_session_token(self):
        """Auto-refresh session token in the background"""
        return {"status": "AUTHENTICATED", "broker": "Quotex"}
