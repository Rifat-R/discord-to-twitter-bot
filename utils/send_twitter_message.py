import tweepy
from settings import config
from dotenv import load_dotenv

load_dotenv()

# Authenticate access

client = tweepy.Client(config.BEARER_TOKEN, config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
auth = tweepy.OAuth1UserHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)




def send_tweet(message:str=None, image_locations=None):
    if message == None and image_locations == None:
        raise  Exception("Cannot send a tweet without message and an image.")

    # media = api.media_upload(filename=image_locations)
    media_ids = []

    if image_locations != None:
        for image_location in image_locations:
            media = api.media_upload(filename=image_location)
            media_ids.append(media.media_id)

    else:
        media_ids = None


    client.create_tweet(text = message, media_ids = media_ids)
    print("Sent message to twitter!")

