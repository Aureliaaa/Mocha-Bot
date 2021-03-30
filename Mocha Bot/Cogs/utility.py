import discord
from discord.ext import commands
import time
from random import randint

class UtilityCog(commands.Cog, name="utility commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot   
        
	@commands.command(name = "ping",
					usage="",
					description = "Display the bot's ping.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def ping(self, ctx):
		before = time.monotonic()
		message = await ctx.send("🏓 Pong !")
		ping = (time.monotonic() - before) * 1000
		await message.edit(content=f"🏓 Pong !  `{int(ping)} ms`")

	@commands.command(name = "test",
					usage="",
					description = "Test command.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def pong(self, ctx):
		await ctx.send("It seems like everything is working correctly :D")

def setup(bot:commands.Bot):
    bot.remove_command("help")
    bot.add_cog(UtilityCog(bot))