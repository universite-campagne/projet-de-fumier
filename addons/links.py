import discord
from discord.ext import commands
from sys import argv

class Links:
    """
    Commands for easily linking to projects.
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

        
    @commands.command()
    async def builds(self):
        """test"""
        await self.bot.say("http://github.com/thomleg50/Atmosphere/releases")

def setup(bot):
    bot.add_cog(Links(bot))
