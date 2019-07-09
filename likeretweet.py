import tweepy
import logging
from config import construct_api
import json

logging.basicConfig(level=logging.INFO)
logs = logging.getLogger()


class LikeRetweet(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, mention):
        logs.info(f"The tweet id being processed is {mention.id}")
        if mention.in_reply_to_status_id is not None or mention.user.id == self.me.id:
            return
        try:
            mention.favorite()
            mention.retweet()
        except Exception as e:
            logs.error("Error in favourite and retweet", exc_info=True)

    def on_error(self, status):
        logs.error(status)


def main(keywords):
    api = construct_api()
    tweets_checker = LikeRetweet(api)
    stream = tweepy.Stream(api.auth, tweets_checker)
    stream.filter(track=keywords, languages=["en"])


if __name__ == "__main__":
    main(["#deloitte", "#DeloitteCanada"])
