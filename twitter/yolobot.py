import tweepy, time
import sys
from credentials import *
auth = tweepy.OAuthHandler(sys.argv[1], sys.argv[2])
auth.set_access_token(sys.argv[3], sys.argv[4])
api = tweepy.API(auth)

api.update_status(sys.argv[5])
