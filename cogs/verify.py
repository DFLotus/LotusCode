import discord
from discord import app_commands
from discord.ext import commands
import requests


class verify(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @app_commands.command(name="verify", description="Verifys users leetcode account")
    async def verify(self, interaction: discord.Interaction, *, user_input: str):
        user: discord.member.Member = interaction.user
        userId = interaction.user.id
        try:
            await fetchLeetCodeAccount(user_input)
            await interaction.response.send_message(
                content=f"Verification successful found <@{userId}> account: {user_input}"
            )
        except Exception as e:
            print(
                f"An error occurred while attemtping to access leetcode account {user_input}: {e}"
            )
            await self.client.send_message(
                content=f"Verification unsuccessful failed to find account <@{userId}>"
            )


async def fetchLeetCodeAccount(accountName: str) -> None:
    try:
        res = requests.get(
            f"https://leetcode.com/{accountName}/"
        )  # Verifys that the account exisit
    except Exception as e:
        print(f"Error fetching url with error: {e}")


async def setup(client: commands.Bot) -> None:
    await client.add_cog(verify(client))
