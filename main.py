import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Get token from env
load_dotenv()
TOKEN: str = os.getenv("BOT_TOKEN")


def main() -> None:
    intents = discord.Intents.default()
    client = commands.Bot(command_prefix="!", intents=intents)

    @client.event
    async def on_ready():
        print("-----------------")
        print("Lotus Bot Online")
        print("-----------------")
        await client.change_presence(activity=discord.Game("LeetCode"))

    cog_extensions: list = []
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            cog_extensions.append(
                "cogs." + filename[:-3]
            )  # append the path to the file without the file extension
    for extension in cog_extensions:
        client.load_extension(extension)
    print(cog_extensions)
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()
