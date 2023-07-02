import datetime
from settings import config
from sqlitedict import SqliteDict

db = SqliteDict(config.DATABASE_NAME)



class TweetMessage:
    def __init__(self, send_time:datetime.datetime, message=None, image_locations:list[str]=None, image_urls:list[str]=None):
        self.message = message
        self.image_locations:list[str] = image_locations
        self.image_urls:list[str] = image_urls
        self.send_time = send_time

    def set_send_time(self, datetime):
        self.send_time = datetime


class TweetData:
    def __init__(self):
        self.initialise()
        self.queue:list[TweetMessage] = db["tweet_queue"]


    def initialise(self):
        if db.get("tweet_queue") == None:
            db["tweet_queue"] = []
            db.commit()


    def add_to_queue(self, message:str=None, image_locations:list[str] = None, image_urls:list[str] = None):
        if message == None and image_locations == None:
            raise Exception("Cannot store empty tweet in queue.")

        if len(self.queue) == 0:
            one_hour_later_dt = datetime.datetime.now() + datetime.timedelta(hours = 1)
        else:
            last_queue_tweet_message = self.queue[-1]
            one_hour_later_dt = last_queue_tweet_message.send_time + datetime.timedelta(hours = 1)

        tweet_message = TweetMessage(one_hour_later_dt, message, image_locations, image_urls)
        self.queue.append(tweet_message)
        db["tweet_queue"] = self.queue
        db.commit()
        return tweet_message

    def get_queue(self):
        return self.queue

    def remove_from_queue(self, index):
        self.queue.pop(index)
        db["tweet_queue"] = self.queue
        db.commit()

    def shift_send_time(self, dt):
        # Shifts queue up by how much time bot has been offline
        if len(self.queue) == None:
            return

        print(dt)

        new_queue = []
        for tweet_message in self.queue:
            print("Before: ", tweet_message.send_time)
            tweet_message.send_time += dt
            print("After: ", tweet_message.send_time)
            new_queue.append(tweet_message)

        db["tweet_queue"] = new_queue
        db.commit()

    def swap_queue_places(self, first_element, second_element):
        self.queue[first_element], self.queue[second_element] = self.queue[second_element], self.queue[first_element]
        first_element_sendtime = self.queue[first_element].send_time
        second_element_sendtime = self.queue[second_element].send_time
        self.queue[first_element].send_time = second_element_sendtime
        self.queue[second_element].send_time = first_element_sendtime
        db["tweet_queue"] = self.queue
        db.commit()





    def set_last_online_dt(self, dt:datetime.datetime):
        db["last_online_dt"] = dt
        db.commit()

    def get_last_online_dt(self):
        return db.get("last_online_dt")




