import os
import discord
import asyncio

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
RADIO_STREAM_URL = "https://mars.streamerr.co:7140/stream"
VOICE_CHANNEL_NAME = "mmf radio"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def play_radio(channel):
    try:
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(RADIO_STREAM_URL), after=lambda e: print("🔁 Stream ended" if not e else f"❌ Error: {e}"))
        print("✅ Streaming MMF Radio...")
    except Exception as e:
        print(f"❌ Could not play radio: {e}")

@client.event
async def on_ready():
    print("✅ MMF-RadioBot is ready to stream MMF Radio!")
    guild = client.get_guild(GUILD_ID)
    if not guild:
        print("❌ Bot is not in the specified guild.")
        return
    channel = discord.utils.get(guild.voice_channels, name=VOICE_CHANNEL_NAME)
    if channel:
        await play_radio(channel)
    else:
        print(f"❌ Voice channel '{VOICE_CHANNEL_NAME}' not found.")

client.run(TOKEN)
