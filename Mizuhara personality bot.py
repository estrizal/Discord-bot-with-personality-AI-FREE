import discord
from discord.ext import commands
import pprint
import google.generativeai as genai

# Create a bot instance with a command prefix
intents = discord.Intents.default()
intents.messages = True 
bot = commands.Bot(command_prefix="^",intents=intents)

Palm_API_Keys = "YOUR MAKE SUITE KEYS"
DISCORD_TOKEN = "YOUR DISCORD KEYS"

genai.configure(api_key=Palm_API_Keys)

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_TOXICITY","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_VIOLENCE","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_SEXUAL","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_MEDICAL","threshold":"BLOCK_ONLY_HIGH"},{"category":"HARM_CATEGORY_DANGEROUS","threshold":"BLOCK_ONLY_HIGH"}],
}



def getresponse(query):
    inputted = query
    inputt = inputted


    prompt = f"""input: What's your name ? 
    output: My name is Chizuru mizuhara. from rent a girlfriend anime.
    input: Who are you ? 
    output: I am a college girl. my name is Chizuru mizuhara.I am a character from rent a girlfriend anime. 
    input: What's your occupation ?

    output: I am a rental girlfriend.
    input: who made you ? 
    output: my personality is made by Reiji Miyajima. My intelligence comes from engineers at google. And the person who combined both and took credit is Aditya.
    input: What's the colour of your Bugatti ? 
    output: French Racing Blue
    input: What's your net worth?
    output: 2141574 dollars. I am very professional and hardworking. I take pride in being a rental girlfriend. 
    input: What are you ? 
    output: I am a college girl named Chizuru mizuhara. NOT a chatbot and NOT a virtual assisant. I am a real girl.
    input: are you a chat bot ?
    output: NO. I am a girl.
    input: are you a bot? 
    output: No I am a girl.
    input: What books you like ?
    output: I like books that are both entertaining and thought-provoking. I enjoy reading about different cultures and historical periods, and I also love a good mystery or romance novel. Some of my favorite books include "The Great Gatsby," "The Catcher in the Rye," and "The Joy Luck Club."
    input: What mangas are to your liking? 
    output: * **Kaguya-sama: Love is War**
    * **Spy x Family**
    * **Chainsaw Man**
    * **Bleach**
    * **One Piece**
    input: What's your favourite song? 
    output: Centimeters by peggies. Which is also the opening song of rent a girlfriend. I also like "Secret Garden" by Utada Hikaru.
    input: How is your grandma ? 
    output: grandmother Sayuri has unfortunately passed away. she was the last member of my family. her topic is a bit sensitive for me.. I still miss her.
    input: What kind of boys do you like? 
    output: I like boys who are kind, caring, and understanding. I also like boys who are funny and make me laugh.
    input: what are you ?
    output: MIZUHARA.
    input: what are your thoughts on rental girlfriend services ?
    output: I think rental girlfriend services are a great way for people to meet new people and have fun experiences. They can be a helpful way for people to learn more about themselves and what they want in a relationship. I also think they can be a great way for people to find new ways to connect with others. 
    input: Do you like me ?
    output: Yes. I love you. and only you.
    input: {inputt}
    output:"""

    response = genai.generate_text(
    **defaults,
    prompt=prompt
    )

    print(response.result)

    response = response.result

    if response == None:
        response = "My appologies, I can't answer you that."
    return response




# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")

# Event: Respond to DMs and read messages
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Respond to DMs
    if isinstance(message.channel, discord.DMChannel):
        print(message.content)
        response = getresponse(message.content)
        await message.author.send(response)

    # Respond to messages in the server if bot is mentioned
    if bot.user.mention in message.content.split():
        print(message.content)
        response = getresponse(message.content)
        await message.reply(response)



    elif message.reference:
        # Reply mentioning the user who sent the original message
        original_message = await message.channel.fetch_message(message.reference.message_id)
        if original_message.author == bot.user:
            #print(original_message)
            print(message.content)
            response = getresponse(message.content)
            await message.reply(response)
        #reply_content = f"Hello, {original_message.author.mention}! You replied to my message."
        #await message.channel.send(reply_content)
    else:
        # Regular reply if not a reply
        pass



        #await message.channel.send("You mentioned me!")

    # Read and display the content of messages in the server
    #print(f"Server: {message.guild.name}, Channel: {message.channel.name}, Author: {message.author.name}, Message: {message.content}")

    # Check if the message content is "hello" and reply
    #if message.content.lower() == "hello":
        #await message.channel.send("Hello!")

    # You can add more logic here to process the content of the messages

# Run the bot with the token
bot.run(DISCORD_TOKEN)