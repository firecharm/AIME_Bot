import tweepy
import logging
from config import *
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def main():
    api = construct_api()
    time_0 = 0
    
    while True:
        dm_list = api.list_direct_messages()
        timestamp_list = []
        for i in dm_list:
            timestamp_list.append(i.created_timestamp)
        time_1 = int(max(timestamp_list))

        logger.info("Waiting...")
        time.sleep(60)
        if time_1 != time_0:
            print('Found a new message!')
            time_0 = time_1

            new_sender = int(dm_list[0].message_create['sender_id'])
            new_message = dm_list[0].message_create['message_data']['text']

            if new_sender == int(ACCESS_KEY[:19]):
                continue

            if new_message == 'hello':
                api.send_direct_message(new_sender,'Hello, how are you?')
            elif new_message == 'fine, how are you?':
                api.send_direct_message(new_sender,'I am great!')
            else:
                api.send_direct_message(new_sender,'HEY HOW ARE YOU HUMAN, WRONG INPUT')

        else:
            continue

if __name__ == "__main__":
    main()