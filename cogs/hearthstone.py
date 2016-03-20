from discord.ext import commands
import urllib.request
from bs4 import BeautifulSoup

# This cog searches http://www.hearthpwn.com/ for images of Hearthstone cards
#
# Use [p]card [name] to search for regular cards
# Use [p]cardg [name] to search for golden cards

class Hearthstone:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def card(self, *text):
        """Retrieves card art from a hearthpwn search"""
        if len(text) > 0:
            try:
                card = '+'.join([str(x) for x in text]) # convert the text list into a string joined by + characters for use in a web address
                url = "http://www.hearthpwn.com/cards?filter-name="+card #build the web adress
                soupObject = BeautifulSoup(urllib.request.urlopen(url), "html.parser") # get the web page and create a BeautifulSoup4 object
                img = soupObject.find("img")["src"] #find the first image tag and return the source attribute
                await self.bot.say(img)
            except:
                await self.bot.say("`Could not find that card, check your spelling or try another card.`")
        else:
            await self.bot.say("```card [name]\n\nSearches http://www.hearthpwn.com/\nReturns first available card that matches the search text.\nUse \"cardg\" to get gold cards.```")

    @commands.command()
    async def cardg(self, *text):
        """Retrieves golden card art from a hearthpwn search"""
        if len(text) > 0:
            try:
                card = '+'.join([str(x) for x in text])
                url = "http://www.hearthpwn.com/cards?filter-name="+card
                soupObject = BeautifulSoup(urllib.request.urlopen(url), "html.parser")
                img = soupObject.find("img")["data-gifurl"] #find the first image tag and return the data-gifurl attribute
                await self.bot.say(img)
            except:
                await self.bot.say("`Could not find that card, check your spelling or try another card.`")
        else:
            await self.bot.say("```cardg [name]\n\nSearches http://www.hearthpwn.com/\nReturns first available gold card that matches the search text.\nUse \"card\" to get regular cards.```")

def setup(bot):
    bot.add_cog(Hearthstone(bot))