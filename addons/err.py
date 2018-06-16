import binascii
import discord
import re
from discord.ext import commands
from discord import Color
from sys import argv

class Err:
    """
    Parses CTR error codes.
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    errcodes = {
        # Switch
        '007-1037': 'Could Not Detect an SD Card.',
        '2001-0125': 'Executed svcCloseHandle on main-thread handle (THIS CODE HAS NO KNOWN SUPPORT PAGE)',
        '2002-6063': 'Attempted to read eMMC CID from browser? (THIS CODE HAS NO KNOWN SUPPORT PAGE)',
        '2005-0003': 'You are unable to download software.',
        '2162-0002': 'General userland crash',
        '2164-0020': 'Error starting software.',
        '2168-0000': 'Illegal opcode. (THIS CODE HAS NO KNOWN SUPPORT PAGE)',
        '2168-0001': 'Resource/Handle not available. (THIS CODE HAS NO KNOWN SUPPORT PAGE)',
        '2168-0002': 'Segmentation Fault. (THIS CODE HAS NO KNOWN SUPPORT PAGE)',
        '2168-0003': 'Memory access must be 4 bytes aligned. (THIS CODE HAS NO KNOWN SUPPORT PAGE)',
        '2811-5001': 'General connection error.'
        
    }

    def get_name(self, d, k):
        if k in d:
            return '{} ({})'.format(d[k], k)
        else:
            return '{}'.format(k)

    async def aaaa(self, rc):
        # i know this is shit that's the point
        if rc == 3735928559:
            await self.bot.say(binascii.unhexlify(hex(3273891394255502812531345138727304541163813328167758675079724534358388)[2:]).decode('utf-8'))
        elif rc == 3735927486:
            await self.bot.say(binascii.unhexlify(hex(271463605137058211622646033881424078611212374995688473904058753630453734836388633396349994515442859649191631764050721993573)[2:]).decode('utf-8'))
        elif rc == 2343432205:
            await self.bot.say(binascii.unhexlify(hex(43563598107828907579305977861310806718428700278286708)[2:]).decode('utf-8'))

    @commands.command(pass_context=True)
    async def err(self, ctx, err: str):
        """
        Parses Nintendo and CTR error codes, with a fancy embed. 0x prefix is not required.
        Example:
          .err 0xD960D02B
          .err 022-2634
        """
        if re.match('[0-1][0-9][0-9]\-[0-9][0-9][0-9][0-9]', err):
            embed = discord.Embed(title=err + (": Nintendo 3DS" if err[0] == "0" else ": Wii U"))
            embed.url = "http://www.nintendo.com/consumer/wfc/en_na/ds/results.jsp?error_code={}&system={}&locale=en_US".format(err, "3DS" if err[0] == "0" else "Wiiu")
            if err not in self.errcodes:
                embed.description = "I don't know this one! Click the error code for details on Nintendo Support.\n\nIf you keep getting this issue and Nintendo Support does not help, or know how to fix it, you should report relevant details to <@78465448093417472> so it can be added to the bot."
            else:
                embed.description = self.errcodes[err]
                embed.color = (Color(0xCE181E) if err[0] == "0" else Color(0x009AC7))
        # 0xE60012
        # Switch Error Codes (w/ website)
        elif re.match('[2][1][1][0]\-[1][0-9][0-9][0-9]', err):
            embed = discord.Embed(title=err + ": Nintendo Switch")
            embed.url = "http://en-americas-support.nintendo.com/app/answers/detail/a_id/22594"
            embed.description = "General connection error."
            embed.color = Color(0xE60012)
        elif re.match('[2][1][1][0]\-[2][9][0-9][0-9]', err):
            embed = discord.Embed(title=err + ": Nintendo Switch")
            embed.url = "http://en-americas-support.nintendo.com/app/answers/detail/a_id/22277/p/897"
            embed.description = "General connection error."
            embed.color = Color(0xE60012)
        elif re.match('[2][1][1][0]\-[2][0-8][0-9][0-9]', err):
            embed = discord.Embed(title=err + ": Nintendo Switch")
            embed.url = "http://en-americas-support.nintendo.com/app/answers/detail/a_id/22263/p/897"
            embed.description = "General connection error."
            embed.color = Color(0xE60012)
        elif re.match('[2][0][0][5]\-[0][0][0][3]', err):
            embed = discord.Embed(title=err + ": Nintendo Switch")
            embed.url = "http://en-americas-support.nintendo.com/app/answers/detail/a_id/22393"
            embed.description = self.errcodes[err]
            embed.color = Color(0xE60012)
        elif re.match('[2][1][1][0]\-[3][4][0][0]', err):
            embed = discord.Embed(title=err + ": Nintendo Switch")
            embed.url = "http://en-americas-support.nintendo.com/app/answers/detail/a_id/22569/p/897"
            embed.description = self.errcodes[err]
            embed.color = Color(0xE60012)
        elif re.match('[2][1][6][2]\-[0][0][0][2]', err):
            embed = discord.Embed(title=err + ": Nintendo Switch")
            embed.url = "http://en-americas-support.nintendo.com/app/answers/detail/a_id/22596"
            embed.description = self.errcodes[err]
            embed.color = Color(0xE60012)
        elif re.match('[2][1][6][4]\-[0][0][2][0]', err):
            embed = discord.Embed(title=err + ": Nintendo Switch")
            embed.url = "http://en-americas-support.nintendo.com/app/answers/detail/a_id/22539/p/897"
            embed.description = self.errcodes[err]
            embed.color = Color(0xE60012)
        elif re.match('[2][8][1][1]\-[5][0][0][1]', err):
            embed = discord.Embed(title=err + ": Nintendo Switch")
            embed.url = "http://en-americas-support.nintendo.com/app/answers/detail/a_id/22392/p/897"
            embed.description = self.errcodes[err]
            embed.color = Color(0xE60012)
        # Switch Error Codes (w/o website)
        elif re.match('[0-9][0-9][0-9][0-9]\-[0-9][0-9][0-9][0-9]', err):
            embed = discord.Embed(title=err + ": Nintendo Switch")
            embed.url = "http://en-americas-support.nintendo.com/app/answers/landing/p/897".format(err)
            if err not in self.errcodes:
                embed.description = "I don't know this one! Click the error code for details on Nintendo Support.\n\nIf you keep getting this issue and Nintendo Support does not help, or know how to fix it, you should report relevant details to <@78465448093417472> so it can be added to the bot."
            else:
                embed.description = self.errcodes[err]
                embed.color = Color(0xE60012)
        else:
            err = err.strip()
            if err.startswith("0x"):
                err = err[2:]
            rc = int(err, 16)
            await self.aaaa(rc)
            desc = rc & 0x3FF
            mod = (rc >> 10) & 0xFF
            summ = (rc >> 21) & 0x3F
            level = (rc >> 27) & 0x1F

            # garbage
            embed = discord.Embed(title="0x{:X}".format(rc))
            embed.add_field(name="Module", value=self.get_name(self.modules, mod), inline=False)
            embed.add_field(name="Description", value=self.get_name(self.descriptions, desc), inline=False)
            embed.add_field(name="Summary", value=self.get_name(self.summaries, summ), inline=False)
            embed.add_field(name="Level", value=self.get_name(self.levels, level), inline=False)
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True, hidden=True)
    async def ninerr(self, ctx):
        await self.bot.say("Merged with " + ctx.prefix + "err, use that instead")

def setup(bot):
    bot.add_cog(Err(bot))
