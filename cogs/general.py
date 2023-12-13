from disnake.ext import commands
import disnake
from utils import image_utils, send_twitter_message, embed_utils
from settings import database as db, config

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.has_role(config.TWEET_ROLE_NAME)
    @commands.command()
    async def tweet(self, ctx:commands.Context, *, message:str=None):
        tweet_db = db.TweetData()
        medias = [i for i in ctx.message.attachments]

        if len(medias) == 0:
            if message == None:
                await ctx.reply(f"You cannot send an empty tweet! Please attach an image or message.")
                return

            tweet_message = tweet_db.add_to_queue(message)
            print("Added tweet to queue!")
            embed = embed_utils.created_tweet(tweet_message)
            await ctx.send(embed=embed)
            # send_twitter_message.send_tweet(message)
            return

        image_urls = []
        for media in medias:
            filename = media.filename
            image_extensions = ['jpg', 'jpeg', 'png', 'bmp']
            dot_index = filename.index(".")
            file_type = filename[dot_index+1:]
            print(file_type)
            if file_type not in image_extensions:
                print(f"{media.filename} was not able to be saved.")
                continue
            image_urls.append(media.url)


        image_locations = []
        for url in image_urls:
            image_location = image_utils.save_image(url)
            image_locations.append(image_location)
            if image_location == None:
                print(f"{url} could not be saved...")
                continue

            print(f"Saved {url}")

        print(message)
        tweet_message = tweet_db.add_to_queue(message, image_locations, image_urls)
        embed = embed_utils.created_tweet(tweet_message)
        await ctx.send(embed=embed)


    @commands.has_role(config.TWEET_ROLE_NAME)
    @commands.command()
    async def queue(self, ctx:commands.Context):
        tweet_data = db.TweetData()
        queue:list[db.TweetMessage] = tweet_data.get_queue()
        if len(queue) == 0:
            await ctx.reply(f"No tweets have been queued up!")
            return
        embed = disnake.Embed(title = f"Tweet queue", color = config.EMBED_COLOUR)
        description = ""
        for index, tweet_message in enumerate(queue):
            message = tweet_message.message
            scheduled_time = tweet_message.send_time
            # epoch_time = calendar.timegm(scheduled_time.timetuple())
            epoch_time = round(scheduled_time.timestamp())
            if message == None:
                truncated_message = "No message"
            else:
                truncated_message = message[:25] + (message[25:] and '...')
            description += f"**{index+1})** `{truncated_message}` - <t:{epoch_time}>\n"

        embed.description = description
        await ctx.send(embed=embed)

    @commands.has_role(config.TWEET_ROLE_NAME)
    @commands.command()
    async def info(self, ctx:commands.Context, queue_number):
        try:
            queue_number = int(queue_number)
        except ValueError:
            await ctx.reply(f"Please enter a valid number and try again.")
            return

        tweet_data = db.TweetData()
        queue:list[db.TweetMessage] = tweet_data.get_queue()
        print(len(queue))
        if queue_number > len(queue) or queue_number <= 0:
            await ctx.reply(f"Please enter a queue number that exists within the queue")
            return

        tweet_message = queue[queue_number-1]
        embed = embed_utils.tweet_info(tweet_message)
        await ctx.send(embed=embed)

    @commands.has_role(config.TWEET_ROLE_NAME)
    @commands.command()
    async def swap(self, ctx:commands.Context, first_element, second_element):
        try:
            first_element = int(first_element)
            second_element = int(second_element)
        except ValueError:
            await ctx.reply(f"Please enter a valid number and try again.")
            return

        tweet_data = db.TweetData()
        queue:list[db.TweetMessage] = tweet_data.get_queue()
        print(len(queue))
        if first_element > len(queue) or first_element <= 0:
            await ctx.reply(f"Please enter a queue number that exists within the queue")
            return
        if second_element > len(queue) or second_element <= 0:
            await ctx.reply(f"Please enter a queue number that exists within the queue")
            return

        if first_element == second_element:
            await ctx.reply(f"You cannot swap two of the same tweet messages!")
            return

        tweet_data.swap_queue_places(first_element-1, second_element-1)
        await ctx.reply(f"Swapped tweet message `#{first_element}` with `#{second_element}`")

    @commands.has_role(config.TWEET_ROLE_NAME)
    @commands.command()
    async def push(self, ctx:commands.Context):
        tweet_data = db.TweetData()
        queue:list[db.TweetMessage] = tweet_data.get_queue()
        if len(queue) == 0:
            await ctx.reply(f"No tweets have been queued up!")
            return
        tweet_message = queue[0]
        message = tweet_message.message
        image_locations = tweet_message.image_locations
        send_twitter_message.send_tweet(message, image_locations)
        tweet_data.remove_from_queue(0)


def setup(bot):
    bot.add_cog(General(bot))
