from endpoint_type import Cryptocurrency
from requester import Requester

class ApiUrl:
    BASE_URL = 'https://pro-api.coinmarketcap.com'
    SANDBOX_URL = 'https://sandbox-api.coinmarketcap.com'

class CoinMarketCap:
    
    def __init__(self, url, api_key):
        self.requester = Requester(
            base_url=url, 
            api_key=api_key)
        self.cryptocurrency = Cryptocurrency(
            requester=self.requester)