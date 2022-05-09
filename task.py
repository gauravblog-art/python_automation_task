# import requests module
import requests
from requests.auth import HTTPBasicAuth

# Making a get request
response = requests.get('https://www.flickr.com/services/api/flickr.blogs.postPhoto.html',
			auth = HTTPBasicAuth('user', 'pass'))

# print request object
print(response)
