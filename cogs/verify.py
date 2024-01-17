import discord
from discord import app_commands
from discord.ext import commands


class verify(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @app_commands.command(name="verify", description="Verifys users leetcode account")
    async def verify(self, interaction: discord.Interaction):
        user: discord.member.Member = interaction.user
        user_id = interaction.user.id

        await interaction.response.send_message(
            content=f"Verification in process: <@{user_id}> please check your DM "
        )

        try:
            await user.send("Please proceed to your leetcode profile")
        except discord.Forbidden:
            print(
                f"Failed to send a direct message to {user.name}#{user.discriminator}. Make sure the user allows direct messages from this server."
            )
            await interaction.response.send_message(
                content=f"Failed to send a direct message to <@{user_id}>. Make sure the user allows direct messages from this server."
            )
        except Exception as e:
            print(f"An error occurred while sending a direct message: {e}")


async def setup(client: commands.Bot) -> None:
    await client.add_cog(verify(client))
