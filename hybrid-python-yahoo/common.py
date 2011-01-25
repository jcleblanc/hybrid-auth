import os

#set oauth consumer key and consumer secret keys
consumer_key = 'dj0yJmk9TWI3cno3UW82TWZkJmQ9WVdrOVFqRjBZMEpOTjJzbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1kYg--'
consumer_secret = '23080401f6af65e7807fa0a9b9727e01a0669e0d'

#oauth access token endpoint (Yahoo!)
oauth_access_token_endpoint = 'https://api.login.yahoo.com/oauth/v2/get_token'

#trust root and return to urls for openid process
trust_root = 'http://%s/' % (os.environ['HTTP_HOST'])
return_to = 'http://%s/complete.py' % (os.environ['HTTP_HOST'])