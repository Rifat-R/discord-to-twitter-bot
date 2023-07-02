import disnake
from settings import config

def created_tweet(tweet_message):
    embed = disnake.Embed(title = f"Created tweet! Added to queue.", color = config.EMBED_COLOUR)
    scheduled_time = tweet_message.send_time
    epoch_time = round(scheduled_time.timestamp())
    message = tweet_message.message
    image_urls = tweet_message.image_urls
    embed.add_field(name = "Tweet message", value = message, inline=False)
    embed.add_field(name = "Scheduled Time", value = f"<t:{epoch_time}>", inline=False)
    if image_urls == None:
        embed.add_field(name = "Images", value = "None", inline=False)
    else:
        images_field_value = ""
        for index, url in enumerate(image_urls):
            images_field_value += f"[Image {index+1}]({url})\n"
        embed.add_field(name = "Images", value = images_field_value, inline=False)

    return embed


def tweet_info(tweet_message):
    embed = disnake.Embed(title = f"Tweet info", color = config.EMBED_COLOUR)
    scheduled_time = tweet_message.send_time
    epoch_time = round(scheduled_time.timestamp())
    message = tweet_message.message
    image_urls = tweet_message.image_urls
    embed.add_field(name = "Tweet message", value = message, inline=False)
    embed.add_field(name = "Scheduled Time", value = f"<t:{epoch_time}>", inline=False)
    if image_urls == None:
        embed.add_field(name = "Images", value = "None", inline=False)
    else:
        images_field_value = ""
        for index, url in enumerate(image_urls):
            images_field_value += f"[Image {index+1}]({url})\n"
        embed.add_field(name = "Images", value = images_field_value, inline=False)


    return embed

def sent_tweet(tweet_message):
    embed = disnake.Embed(title = f"Sent tweet!", color = disnake.Color.green())
    scheduled_time = tweet_message.send_time
    epoch_time = round(scheduled_time.timestamp())
    message = tweet_message.message
    image_urls = tweet_message.image_urls
    embed.add_field(name = "Tweet message", value = message, inline=False)
    embed.add_field(name = "Send time", value = f"<t:{epoch_time}>", inline=False)
    if image_urls == None:
        embed.add_field(name = "Images", value = "None", inline=False)
    else:
        images_field_value = ""
        for index, url in enumerate(image_urls):
            images_field_value += f"[Image {index+1}]({url})\n"
        embed.add_field(name = "Images", value = images_field_value, inline=False)


    return embed
