from core.client import HttpClient
from core.config import HttpConfig

config = HttpConfig(timeout = 60, verify_ssl = True, retries = 3)
client = HttpClient(config)

response = client.get("https://google.es")

print(response.status_code)
print(response.text)
