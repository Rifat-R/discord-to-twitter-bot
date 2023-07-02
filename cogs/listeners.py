from disnake.ext import commands, tasks
from settings import database as db, config
from utils import send_twitter_message, embed_utils
import datetime

class Listeners(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.check_queue_loop.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot id: {self.bot.user.id}")
        last_online_dt = db.TweetData().get_last_online_dt()
        if last_online_dt == None:
            print(f"There is no last online datetime.")
            return
        else:
            difference_dt = datetime.datetime.now() - last_online_dt
            db.TweetData().shift_send_time(difference_dt)
            print(f"There was interrupted time. Time: {difference_dt}")


    @tasks.loop(seconds=3)
    async def check_queue_loop(self):
        tweet_data = db.TweetData()
        queue:list[db.TweetMessage] = tweet_data.get_queue()
        if len(queue) == 0:
            print(f"Queue is empty.")
            return
        tweet_message = queue[0]
        if datetime.datetime.now() >= tweet_message.send_time:
            channel = self.bot.get_channel(config.ADMIN_CHANNEL_ID)
            embed = embed_utils.sent_tweet(tweet_message)
            message = tweet_message.message
            image_locations = tweet_message.image_locations
            send_twitter_message.send_tweet(message, image_locations)
            tweet_data.remove_from_queue(0)
            await channel.send(embed=embed)
            print("Sent tweet from queue!!!")
        # else:
            # print(f"Checked for queue, not the time yet. {tweet_message.send_time}")



    @check_queue_loop.before_loop
    async def before_printer(self):
        print('Waiting for bot to start up...')
        await self.bot.wait_until_ready()
        print("Bot has started ✔️ Started queue checking loop")





def setup(bot):
    bot.add_cog(Listeners(bot))
