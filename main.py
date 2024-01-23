import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

# Get token from env
load_dotenv()
TOKEN: str = os.getenv("BOT_TOKEN")


async def loadExt(client: commands.Bot) -> None:
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension("cogs." + filename[:-3])


def main() -> None:
    intents = discord.Intents.all()
    client = commands.Bot(command_prefix="!", intents=intents)

    @client.event
    async def on_ready():
        print("Lotus Bot Online")
        await client.change_presence(activity=discord.Game("LeetCode"))
        try:
            await loadExt(client)
            synced: list = await client.tree.sync()  # used to sync commands to bot and fetch slash commands
            print(f"Synced {len(synced)} commands")
        except Exception as error:
            print(f"Failed to sync with error {error}")

    client.run(token=TOKEN)


if __name__ == "__main__":
    main()
