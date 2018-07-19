#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API
access_token = "2199229989-p9WPMjaVZ2w9LWgwcmxxaIeHqxElw7ugIzTsdG3"
access_token_secret = "QeNAaNE9meeyCaI9alvbuEUIVgubyTEvqst1q2cHXRWAq"
consumer_key = "2sXB2TyHCzGAWiiWB0xGzPe5E"
consumer_secret = "3LmMUpUI2u1awtTGWCuW0ixGWCJIPModUyCbYJ0sfWxjEfV5Rz"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        decoded = json.loads(data)
        print (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keyword: 'python'
    stream.filter(track=['Mercedes', 'MBUSI'])
