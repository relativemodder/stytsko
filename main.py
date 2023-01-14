import discord
import json
import random



class MyClient(discord.Client):

    cooldownMessages = 3
    countedMessages = 0

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message: discord.Message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        wordsDB:dict = None

        with open("wordsDB.json", "r") as wordsDBfp:
            wordsDB = json.load(wordsDBfp)

            for word in message.content.split(' '):
                wordsDB['words'].append(word)
            
            wordsDBfp.close()
        
            with open("wordsDB.json", "w") as wordsDBfp:
                json.dump(wordsDB, wordsDBfp)

            

        self.countedMessages += 1
        if self.countedMessages == self.cooldownMessages:
            self.countedMessages = 0

            with open("wordsDB.json") as wordsDBfp:
                wordsDB = json.load(wordsDBfp)

                randomPhraseList = []

                for i in range(3):
                    randomPhraseList.append(random.choice(wordsDB['words']))
                
                await message.channel.send(' '.join(randomPhraseList))
            

intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
client.run('MTA1OTkwODE5Mjg2MTE2Nzc2OA.G4b8Py.LJtXHEO8XHulc3-POUmErFsCxxsQdbuQCH9Vd8')