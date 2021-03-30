import discord
from discord.ext import commands
import time


class FunCog(commands.Cog, name="Fun commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "rickRoll",
					aliases= ["rr"],
					usage="",
					description = "Rick rolls the user")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def rickroll(self, ctx):
		 await ctx.send("https://youtu.be/dQw4w9WgXcQ")

def setup(bot:commands.Bot):
	bot.add_cog(FunCog(bot))