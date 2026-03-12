import os
import logging
import random

import aiohttp
import discord
from discord.ext import commands

# --- CONFIGURATION ---
BOT_TOKEN = os.environ.get("PLANECHASE_BOT_TOKEN", "")
PREFIX = "!"
SCRYFALL_URL = "https://api.scryfall.com/cards/random?q=(t:plane+or+t:phenomenon)"

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("planechase")

# --- BOT SETUP ---
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)


async def fetch_random_plane():
    """Fetch a random plane/phenomenon card from Scryfall and return a Discord embed."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(SCRYFALL_URL) as response:
                if response.status != 200:
                    log.warning("Scryfall returned status %s", response.status)
                    return None

                data = await response.json()
                card_name = data.get("name", "Unknown Card")
                card_uri = data.get("scryfall_uri", "")

                if "image_uris" in data:
                    image_url = data["image_uris"]["large"]
                elif "card_faces" in data:
                    image_url = data["card_faces"][0]["image_uris"]["large"]
                else:
                    image_url = None

                embed = discord.Embed(title=f"✈️ {card_name}", url=card_uri, color=0x2B2D31)
                if image_url:
                    embed.set_image(url=image_url)
                embed.set_footer(text="Data provided by Scryfall")
                return embed
    except aiohttp.ClientError as e:
        log.error("Failed to fetch plane from Scryfall: %s", e)
        return None


@bot.event
async def on_ready():
    log.info("Planar Die is ready! Logged in as %s", bot.user)


@bot.command(name="roll", help="Rolls the planar die.")
async def roll(ctx):
    """
    Simulates a 6-sided Planar Die:
    - 1 side: Planeswalk (fetch a new plane)
    - 1 side: Chaos (trigger the chaos ability)
    - 4 sides: Blank (nothing happens)
    """
    die_roll = random.randint(1, 6)

    if die_roll == 1:
        await ctx.send(
            "🎲 **You rolled the PLANESWALKER symbol!**\n"
            "🌌 **PLANESWALK!** Finding a new plane..."
        )
        plane_embed = await fetch_random_plane()
        if plane_embed:
            await ctx.send(embed=plane_embed)
        else:
            await ctx.send("❌ Error fetching the new plane.")

    elif die_roll == 6:
        await ctx.send(
            "🎲 **You rolled the CHAOS symbol!**\n"
            "🌀 Trigger the chaos ability!"
        )

    else:
        await ctx.send("🎲 **You rolled a BLANK.**\nNothing happens.")


if __name__ == "__main__":
    if not BOT_TOKEN:
        raise SystemExit("Set PLANECHASE_BOT_TOKEN environment variable before running.")
    bot.run(BOT_TOKEN)
