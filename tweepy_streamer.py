"""This file streams tweets based on a set of filetred criteria listed in stream.filter. The access keys/tokens and consumer keys/tokens need
to be setup prior"""

from tweepy.streaming import StreamListener
from tweepy import OathHandler
from tweepy import Stream
import twitter_credentials


class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self,status):
        print(status)

if __name__ == "main.py":
    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_key_secret)
    auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)
    stream = Stream(auth, listener)

    stream.filter(track = ['donald trump', 'hillary clinton', 'barack obama','bernia sanders'])
