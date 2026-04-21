import os
import hmac
import hashlib
import time
import requests
from urllib.parse import urlencode
from bot.logging_config import logger

class BinanceFuturesClient:
    BASE_URL = "https://testnet.binancefuture.com"

    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = requests.Session()
        self.session.headers.update({
            "X-MBX-APIKEY": self.api_key
        })

    def _generate_signature(self, query_string: str) -> str:
        return hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

    def _dispatch_request(self, method: str, endpoint: str, **params) -> dict:
        # Add timestamp
        params["timestamp"] = int(time.time() * 1000)
        
        # Build query string
        query_string = urlencode(params)
        
        # Generate signature
        signature = self._generate_signature(query_string)
        
        # Final URL
        url = f"{self.BASE_URL}{endpoint}?{query_string}&signature={signature}"
        
        # Remove sensitive signature from logging if desired, but for debugging testnet we keep it simple
        logger.info(f"API Request: {method} {endpoint} params: {params}")
        
        try:
            response = self.session.request(method, url)
            data = response.json()
            
            # Binance errors usually have a "code" or "msg"
            if response.status_code != 200:
                logger.error(f"API Error: HTTP {response.status_code} - {data}")
                response.raise_for_status()
                
            logger.info("API Response Success")
            return data
            
        except requests.exceptions.HTTPError as e:
            logger.error("HTTP Error during API request")
            raise Exception(f"Binance API returned an error: {data.get('msg', str(e))} (Code: {data.get('code', 'N/A')})")
        except requests.exceptions.RequestException as e:
            logger.error("Network Error during API request")
            raise Exception(f"Network failure: {str(e)}")
        except ValueError:
            # JSON parsing error
            logger.error(f"Failed to parse JSON response: {response.text}")
            raise Exception("Invalid response from Binance API")

    def post(self, endpoint: str, **params) -> dict:
        return self._dispatch_request("POST", endpoint, **params)

    def get(self, endpoint: str, **params) -> dict:
        return self._dispatch_request("GET", endpoint, **params)
