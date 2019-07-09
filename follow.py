import tweepy
import logging
from config import construct_api
import time

logging.basicConfig(level=logging.INFO)
logs = logging.getLogger()


def follow(api):
    logs.info("Retrieving and following followers on Twitter")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logs.info(f"Following {follower.name}")
            follower.follow()


def main():
    api = construct_api()
    while True:
        follow(api)
        logs.info("Waiting...")
        time.sleep(15)


if __name__ == "__main__":
    main()
