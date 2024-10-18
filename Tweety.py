import tweepy

# Replace with Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Authenticate Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Define keyword or hashtag to track
keyword = 'target_keyword'
for tweet in tweepy.Cursor(api.search, q=keyword, lang="en").items(50):
    print(f"User: {tweet.user.screen_name}, Tweet: {tweet.text}")
