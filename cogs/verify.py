import discord
from discord import app_commands
from discord.ext import commands


class verify(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @app_commands.command(name="verify", description="Verifys users leetcode account")
    async def verify(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="Verification in process")


async def setup(client: commands.Bot) -> None:
    await client.add_cog(verify(client))
