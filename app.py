import discord
import asyncio
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Bot

num = 0
num1 = 0
num_1 = 10

call = '닉네임'
token = "token"
userID = "ID"

bot = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')    

@bot.event
async def on_message(message):
    if message.author.bot:
        return None

    global call,num,num_1,num1,userID
    user_id = message.author.id
    channel = message.channel
    
    if message.content.startswith("!"+call+"?"):
        for i in range(num_1):
            print("맨션이 정상적으로 처리가 되었습니다!")
            print("맨션",num,"개 처리 완료 되었습니다")
            await message.channel.send("<@"+userID+">")
            num += 1

        if num == num_1:
            print("최종적으로 맨션을 종료 하였습니다")
            embed = Embed(title="맨션",description="최종적으로 맨션을 종료 하였습니다", color=0x00aaaa)
            embed.add_field(name="맨션 사용자", value = user_id , inline=False,)
            embed.add_field(name="맨션 사용위치", value = message.channel ,inline=False,)
            embed.add_field(name="맨션 최종 사용량", value = num ,inline=False,)
            embed.add_field(name="맨션 제사용 방법", value = "!미르! 하여 초기화을 해주십시오" ,inline=False,)
            msg = await message.channel.send(embed=embed)
            print(num)
            num == 0 
            
    elif message.content.startswith("!"+call+"!"):
        print("맨션이 정상적으로 처리가 되었습니다!")
        print("맨션",num,"개 처리 완료 되었습니다")
        await message.channel.send("미르 콜 초기화 하었습니다")
        num = 0 
        num1 = 0
    
    elif message.content.startswith("!도움!"):
        embed = Embed(title="맨션 도배 봇",description="주의 사항 작성 안함", color=0x00aaaa)
        embed.add_field(name="!"+call+"?", value = call+"을 부르기 위한 커멘드 입니다" , inline=False,)
        embed.add_field(name="!"+call+"!", value ="재사용을 하기위해서는 반드시 !"+call+"!을 하시고 사용해주십시오" ,inline=False,)
        msg = await message.channel.send(embed=embed)

bot.run(token)
