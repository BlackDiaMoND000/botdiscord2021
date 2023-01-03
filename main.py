import openai
import discord
from discord.ext import commands
openai.api_key = "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"
model = "text-davinci-002"

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith(".s"):
            query = message.content[8:]
            completions = openai.Completion.create(engine=model, prompt=query, max_tokens=1024, n=1,stop=None,temperature=0.5)
            response = completions.choices[0].text
            channel = client.get_channel(1059731612922826773)
            await message.channel.send(response)
        else:
            prompt = message.content
            completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)
            response = completions.choices[0].text
            channel = client.get_channel(1059731612922826773)
            await message.channel.send(response)

client.run("NTE3MzM4MjMxMzQ4Mzk2MDMy.GZBqam.kajwZruq-gynIpim1iJ5qy8lipF9SGvmgWbmWk")
