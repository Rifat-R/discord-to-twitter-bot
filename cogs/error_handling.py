from disnake.ext import commands

class ErrorHandling(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            # Replace MissingRequiredArguments with your error
            await ctx.reply("You do not have the necessary role to use this command.")
        else:
            error:commands.CommandInvokeError = error
            print(error)





def setup(bot):
    bot.add_cog(ErrorHandling(bot))
