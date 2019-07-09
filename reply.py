import tweepy
import logging
from config import construct_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for mention in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(mention.id, new_since_id)
        if mention.in_reply_to_status_id is not None:
            continue
        if any(keyword in mention.text.lower() for keyword in keywords):
            logger.info(f"Answering to {mention.user.name}")

            if not mention.user.following:
                mention.user.follow()

            api.update_status ('@' + mention.user.screen_name + 'Hi, please reach me via Direct Message. Thank you!', mention.id)
    return new_since_id

def main():
    api = construct_api()
    since_id = 1
    while True:
        print(since_id)
        since_id = check_mentions(api, ["assist", "chat"], since_id)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()