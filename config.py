import tweepy
import os

CONSUMER_KEY = 'xarSajZ3FDflrxiqLNcFdsp7S'
CONSUMER_SECRET = 'y1Va3uhQswGdhKZJW8gX623cKVhTSR1wsX19OpvpGe9znnkeMN'
ACCESS_KEY = '1138560738702823425-5h8yX8xCLxGwVrlJxLJGvsDeQIuZr3'
ACCESS_SECRET = 'OoI2eHMUB0Cym1eyuYOmQVZVcyBxoH31PCSMMCYAD5hn4'
def construct_api():


    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    # api.verify_credentials()
    return api
