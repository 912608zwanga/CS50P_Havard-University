import sys
import requests

# Check for command-line argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Try to convert argument to float early
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command line argument is not a number")

# Query the CoinCap API
# Replace 'YourApiKey' with your actual key if you have one,
# but often for CS50, the public link works for testing.
url = "https://api.coincap.io/v2/assets/bitcoin"

try:
    response = requests.get(url)
    response.raise_for_status() # Check for HTTP errors
    json_response = response.json()

    # CoinCap structure: data -> priceUsd
    # Note: priceUsd is a string in the JSON, so we convert to float
    price_usd = float(json_response['data']['priceUsd'])

    amount = n * price_usd
    print(f"${amount:,.4f}")

except requests.RequestException:
    sys.exit("HTTP request failed")
except (KeyError, TypeError):
    sys.exit("JSON structure not as expected")
