import requests

# curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
url = 'http://localhost:9000/2015-03-31/functions/function/invocations'

# Create the event with the URL of the image
event = {'url': 'https://www.toyotanation.com/attachments/received_252542826473517-jpeg.343498'}

# Send POST request using requests module
response = requests.post(url, json=event)
# Print the response
print(response.text)