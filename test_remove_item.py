import requests

# Define the URL for removing an item
url = 'http://8000-shagamatula-bluepulseba-ohds842944g.ws-eu106.gitpod.io/bag/remove/22/'

# Define the data to send in the POST request
data = {
    'quantity': 1,  # Adjust the quantity as needed
    'product_size': 'S'  # Adjust the size as needed or omit if not applicable
}

# Send a POST request to the URL
response = requests.post(url, data=data)

# Check the response status code
if response.status_code == 200:
    print('Item removed successfully.')
elif response.status_code == 400:
    print('Invalid quantity. Please adjust the data.')
elif response.status_code == 404:
    print('URL not found. Verify the URL is correct.')
else:
    print('An error occurred. Check your code and view.')

