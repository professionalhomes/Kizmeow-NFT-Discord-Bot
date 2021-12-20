import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
import urllib.request as ur
import urllib.parse
from urllib.error import HTTPError
from datetime import datetime, timezone, timedelta
import json
import qrcode
import asyncio 
import os
import requests
import keep_alive

discord_token = os.environ['discord_token']
etherscan_api_key = os.environ['etherscan_api_key']
#opensea_api_key = os.environ['opensea_api_key']

bot = commands.Bot(command_prefix="k!",
intents=discord.Intents.all(),
help_command=None)
slash = SlashCommand(bot, sync_commands=True) 

@bot.event
async def on_ready():
  print("Ready!")
  while True:
    url1='https://api.etherscan.io/api?module=stats&action=ethprice&apikey='+etherscan_api_key #api url

    site1 = ur.urlopen(url1)
    page1 = site1.read()
    contents1 = page1.decode()
    data1 = json.loads(contents1)

    ethusd = data1['result']['ethusd']
    #####
    url2='https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey='+etherscan_api_key #api url

    site2 = ur.urlopen(url2)
    page2 = site2.read()
    contents2 = page2.decode()
    data2 = json.loads(contents2)

    SafeGasPrice = data2['result']['SafeGasPrice']
    ProposeGasPrice = data2['result']['ProposeGasPrice']
    FastGasPrice = data2['result']['FastGasPrice']

    presence_ctx1 = 'Ξ '+ethusd
    presence_ctx2 = '🚀'+FastGasPrice+'🚗'+ProposeGasPrice+'🚲'+SafeGasPrice

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=presence_ctx1))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=presence_ctx2))
    await asyncio.sleep(10)
################################################################################help
@slash.slash(name="help",description="display help message")
async def help(ctx):
  BUTTONS = ["◀️","0️⃣","1️⃣","2️⃣","3️⃣","4️⃣"]
  embed=discord.Embed(title="**/help**", description="指令列表\n請按emoji選擇分類", color=0xe8006f)

  embed.add_field(name="[返回]", value="◀️", inline=True)
  embed.add_field(name="[bot資訊]", value="0️⃣", inline=True)
  embed.add_field(name="ㅤ", value="ㅤ", inline=True)#弄一行空白 單純排版用
  embed.add_field(name="[系統]", value="1️⃣", inline=True)
  embed.add_field(name="[NFT]", value="2️⃣", inline=True)
  embed.add_field(name="[3(開發中)]", value="3️⃣", inline=True)
  embed.add_field(name="[4（開發中）]", value="4️⃣", inline=True)
  embed.add_field(name="參數說明", value="有些指令需輸入參數方可使用\ne.g. /demi-nft token_id: 824 \n其中`824`就是此指令的參數。若超過2個參數，輸入完第一個後可按鍵盤上的`tab`鍵切換至下一個參數。", inline=False)
  embed.set_footer(text="last update:\n2021.12.17 4:01 p.m.")
  msg = await ctx.send(embed=embed)
  embed0=discord.Embed(title="**[bot資訊]**", description="關於本bot的資訊", color=0xe8006f)
  embed0.add_field(name="bot名稱", value="Kizmeow", inline=False)
  embed0.add_field(name="開發者", value="Xeift", inline=False)
  embed0.add_field(name="頭像繪師", value="姬玥", inline=False)
  embed0.add_field(name="程式語言", value="Python", inline=False)
  embed0.add_field(name="GitHub", value="https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot", inline=False)
  embed0.add_field(name="聯絡資訊", value="Xeift：Xeift#1230\n姬玥：https://www.facebook.com/profile.php?id=100026170072950", inline=False)
  embed0.add_field(name="聲明", value="交易記錄功能調用Etherscan API，OpenSea相關功能調用OpenSea API，所有資料皆合法取得", inline=False)

  embed1=discord.Embed(title="**[系統]**", description="系統類指令", color=0xe8006f)
  embed1.add_field(name="/help", value="顯示幫助訊息", inline=False)
  embed1.add_field(name="/invite", value="取得邀請網址，可將bot邀請至伺服器 `需有該伺服器的管理者權限`", inline=False)
  embed1.add_field(name="/ping", value="顯示機器人的回應延遲時間", inline=False)

  embed2=discord.Embed(title="**[NFT]**", description="查詢關於NFT項目的相關資訊", color=0xe8006f)
  embed2.add_field(name="/demi-human", value="顯示Demi-Human實時價格資訊", inline=False)
  embed2.add_field(name="/demi-human-history", value="顯示Demi-Human歷史價格資訊", inline=False)
  embed2.add_field(name="/demi-nft", value="查詢特定編號的Demi-Human NFT 參數：`token_id`", inline=False)
  embed2.add_field(name="ㅤ", value="ㅤ", inline=True)#弄一行空白 單純排版用
  embed2.add_field(name="/project", value="顯示項目實時價格資訊 參數：`project_name`", inline=False)
  embed2.add_field(name="/project-history", value="顯示項目歷史價格資訊 參數：`project_name`", inline=False)
  embed2.add_field(name="/nft", value="查詢特定項目、特定編號的NFT 參數：`contract_address` `token_id`", inline=False)
  embed2.add_field(name="/txn", value="輸入地址，顯示交易紀錄 參數：`eth_address`", inline=False)
  embed2.add_field(name="/account_info", value="輸入地址，顯示ETH餘額和Demi NFT balance 參數：`eth_address`", inline=False)

  embed3=discord.Embed(title="**[3]**", description="3", color=0xe8006f)
  embed3.add_field(name="3", value="3", inline=False)

  embed4=discord.Embed(title="**[4]**", description="4", color=0xe8006f)
  embed4.add_field(name="4", value="4", inline=False)

  for b in BUTTONS:
    await msg.add_reaction(b)
  
  while True:
    try:
      react, user = await bot.wait_for("reaction_add", timeout=60.0, check=lambda r, u: r.message.id == msg.id and u.id == ctx.author.id and r.emoji in BUTTONS)
      await msg.remove_reaction(react.emoji, user) #user按了以後馬上清掉reaction
    
    except asyncio.TimeoutError:
      pass

    else:
      if react.emoji == BUTTONS[0]:
        await msg.edit(embed=embed)
      if react.emoji == BUTTONS[1]:
        await msg.edit(embed=embed0)
      elif react.emoji == BUTTONS[2]:
        await msg.edit(embed=embed1)
      elif react.emoji == BUTTONS[3]:
        await msg.edit(embed=embed2)
      elif react.emoji == BUTTONS[4]:
        await msg.edit(embed=embed3)
      elif react.emoji == BUTTONS[5]:
        await msg.edit(embed=embed4)

################################################################################ping
@slash.slash(name="ping",description="return bot latency")
async def _ping(ctx):
  await ctx.send(f"pong! ({bot.latency*1000} ms)")
################################################################################invite
@slash.slash(name="invite",description="invite bot to your server")
async def invite(ctx):
  embed=discord.Embed(title="**[Bot邀請連結]**", description="https://discord.com/api/oauth2/authorize?client_id=886198731328868402&permissions=534727097920&scope=bot%20applications.commands", color=0xe8006f)
  await ctx.send(embed = embed)
################################################################################balance
@slash.slash(
name="account_info",
description="get the account info from the ETH address you enter",
options=
[
  create_option
  (
    name="eth_address",
    description="enter wallet address",
    option_type=3,
    required=True
  )
]
)

async def account_info(ctx, eth_address: str):
# await ctx.send(content=f"{eth_address}")
  url1='https://api.etherscan.io/api?module=account&action=balance&address='+eth_address+'&tag=latest&apikey='+etherscan_api_key #api url

  url2='https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0xa6916545a56f75acd43fb6a1527a73a41d2b4081&address='+eth_address+'&tag=latest&apikey='+etherscan_api_key

  site1 = ur.urlopen(url1)
  page1 = site1.read()
  contents1 = page1.decode()
  data1 = json.loads(contents1)

  bal_ori = data1['result']#eth balance
  eth_bal = int(bal_ori)/1000000000000000000

  site2 = ur.urlopen(url2)
  page2 = site2.read()
  contents2 = page2.decode()
  data2 = json.loads(contents2)

  demi_balance = data2['result']

  if(eth_bal != 0):
    embed=discord.Embed(title="[balance]", color=0xe8006f)
    embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Xeift/image-hosting@main//a8eb74eaa4d1148c2b33db119edb9515.gif")
    embed.add_field(name="ETH balance" , value=str(eth_bal)[0:7]+"||"+str(eth_bal)[7:20]+"||"+" ETH", inline=False)
    embed.add_field(name="Demi-Human balance" , value=demi_balance+" Demi", inline=False)
    await ctx.send(embed=embed)
  else:
      await ctx.send("no ETH in this address or you've entered the wrong address")
################################################################################transaction history
@slash.slash(
name="txn",
description="get the transaction history from the ETH address you enter",
options=
[
  create_option
  (
    name="eth_address",
    description="enter wallet address",
    option_type=3,
    required=True
  )
]
)

async def txn(ctx, eth_address: str):
  BUTTONS = ["◀️","▶️"]
  url1='https://api.etherscan.io/api?module=account&action=txlist&address='+eth_address+'&startblock=0&endblock=99999999&page=1&offset=10&sort=dsc&apikey='+etherscan_api_key #api url

  site1 = ur.urlopen(url1)
  page1 = site1.read()
  contents1 = page1.decode()
  data1 = json.loads(contents1)

  index = 9
  blockNumber = data1['result'][index]['blockNumber']
  timeStamp = data1['result'][index]['timeStamp']
  hash = data1['result'][index]['hash']
  nonce = data1['result'][index]['nonce']
  blockHash = data1['result'][index]['blockHash']
  transactionIndex = data1['result'][index]['transactionIndex']
  from1 = data1['result'][index]['from']
  to = data1['result'][index]['to']
  value1 = data1['result'][index]['value']
  gas = data1['result'][index]['gas']
  gasPrice = data1['result'][index]['gasPrice']
  isError = data1['result'][index]['isError']
  txreceipt_status = data1['result'][index]['txreceipt_status']
  input1 = data1['result'][index]['input']
  contractAddress = data1['result'][index]['contractAddress']
  if contractAddress == "":
    contractAddress = "empty"
  cumulativeGasUsed = data1['result'][index]['cumulativeGasUsed']
  gasUsed = data1['result'][index]['gasUsed']
  confirmations = data1['result'][index]['confirmations']

  icount = 10#index count

  embed=discord.Embed(title="[transaction history]", color=0xe8006f)
  embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Xeift/image-hosting@main//a8eb74eaa4d1148c2b33db119edb9515.gif")
  embed.add_field(name="blockNumber" , value=f"{blockNumber}", inline=False)
  embed.add_field(name="timeStamp" , value=f"{timeStamp}", inline=False)
  embed.add_field(name="hash" , value=f"{hash}", inline=False)
  embed.add_field(name="nonce" , value=f"{nonce}", inline=False)
  embed.add_field(name="blockHash" , value=f"{blockHash}", inline=False)
  embed.add_field(name="transactionIndex" , value=f"{transactionIndex}", inline=False)
  embed.add_field(name="from" , value=f"{from1}", inline=False)
  embed.add_field(name="to" , value=f"{to}", inline=False)
  embed.add_field(name="value" , value=f"{value1}", inline=False)
  embed.add_field(name="gas" , value=f"{gas}", inline=False)
  embed.add_field(name="gasPrice" , value=f"{gasPrice}", inline=False)
  embed.add_field(name="isError" , value=f"{isError}", inline=False)
  embed.add_field(name="txreceipt_status" , value=f"{txreceipt_status}", inline=False)
  embed.add_field(name="input" , value=f"{input1}", inline=False)
  embed.add_field(name="contractAddress" , value=f"{contractAddress}", inline=False)
  embed.add_field(name="cumulativeGasUsed" , value=f"{cumulativeGasUsed}", inline=False)
  embed.add_field(name="gasUsed" , value=f"{gasUsed}", inline=False)
  embed.add_field(name="confirmations" , value=f"{confirmations}", inline=False)

  progresse = "◇" * icount 
  replacement = "◆"
  progresse2 = progresse[:9-index] + replacement + progresse[-index:]
  embed.add_field(name=f"{progresse2}" , value=f"頁數：{10-index}/{icount}", inline=False)
  msg = await ctx.send(embed=embed)

  for b in BUTTONS:
    await msg.add_reaction(b)

  while True:
    try:
      react, user = await bot.wait_for("reaction_add", timeout=60.0, check=lambda r, u: r.message.id == msg.id and u.id == ctx.author.id and r.emoji in BUTTONS)
      await msg.remove_reaction(react.emoji, user) #clear reaction when user add reaction
    
    except asyncio.TimeoutError:
      pass

    else:
      if react.emoji == BUTTONS[0] and index < 9: 
        index += 1#
      elif react.emoji == BUTTONS[1] and index > 1: 
        index -= 1

      blockNumber = data1['result'][index]['blockNumber']
      timeStamp = data1['result'][index]['timeStamp']
      hash = data1['result'][index]['hash']
      nonce = data1['result'][index]['nonce']
      blockHash = data1['result'][index]['blockHash']
      transactionIndex = data1['result'][index]['transactionIndex']
      from1 = data1['result'][index]['from']
      to = data1['result'][index]['to']
      value1 = data1['result'][index]['value']
      gas = data1['result'][index]['gas']
      gasPrice = data1['result'][index]['gasPrice']
      isError = data1['result'][index]['isError']
      txreceipt_status = data1['result'][index]['txreceipt_status']
      input1 = data1['result'][index]['input']
      contractAddress = data1['result'][index]['contractAddress']

      if contractAddress == "":
        contractAddress = "empty"
      cumulativeGasUsed = data1['result'][index]['cumulativeGasUsed']
      gasUsed = data1['result'][index]['gasUsed']
      confirmations = data1['result'][index]['confirmations']

      embed=discord.Embed(title="[transaction history]", color=0xe8006f)
      embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Xeift/image-hosting@main//a8eb74eaa4d1148c2b33db119edb9515.gif")
      embed.add_field(name="blockNumber" , value=f"{blockNumber}", inline=False)
      embed.add_field(name="timeStamp" , value=f"{timeStamp}", inline=False)
      embed.add_field(name="hash" , value=f"{hash}", inline=False)
      embed.add_field(name="nonce" , value=f"{nonce}", inline=False)
      embed.add_field(name="blockHash" , value=f"{blockHash}", inline=False)
      embed.add_field(name="transactionIndex" , value=f"{transactionIndex}", inline=False)
      embed.add_field(name="from" , value=f"{from1}", inline=False)
      embed.add_field(name="to" , value=f"{to}", inline=False)
      embed.add_field(name="value" , value=f"{value1}", inline=False)
      embed.add_field(name="gas" , value=f"{gas}", inline=False)
      embed.add_field(name="gasPrice" , value=f"{gasPrice}", inline=False)
      embed.add_field(name="isError" , value=f"{isError}", inline=False)
      embed.add_field(name="txreceipt_status" , value=f"{txreceipt_status}", inline=False)
      embed.add_field(name="input" , value=f"{input1}", inline=False)
      embed.add_field(name="contractAddress" , value=f"{contractAddress}", inline=False)
      embed.add_field(name="cumulativeGasUsed" , value=f"{cumulativeGasUsed}", inline=False)
      embed.add_field(name="gasUsed" , value=f"{gasUsed}", inline=False)
      embed.add_field(name="confirmations" , value=f"{confirmations}", inline=False)

      progresse = "◇" * icount 
      replacement = "◆"
      progresse2 = progresse[:9-index] + replacement + progresse[-index:]
      embed.add_field(name=f"{progresse2}" , value=f"頁數：{10-index}/{icount}", inline=False)
      await msg.edit(embed = embed)

################################################################################demi_pass
#@slash.slash(name="demi_pass",description="generate a qrcode for verification if you have demi-pass")
@bot.command()
async def demi_pass(ctx,message=None):
  role = discord.utils.get(ctx.guild.roles, name="DemiPASS")


  if role in ctx.message.author.roles:
    userid = ctx.message.author.id
    tz = timezone(timedelta(hours=+8))
    t_qr = datetime.now(tz).isoformat(timespec="seconds")
    date_qr = t_qr[:10]
    hour_qr = t_qr[11:13]
    minute_qr = t_qr[14:16]
    second_qr = t_qr[17:19]
    if int(minute_qr) >=50 :
      minute_qr2 = str(int(minute_qr)+10-60)
      if int(hour_qr) == 23 :
        hour_qr = str(int(hour_qr)+1-24)
    else:
      minute_qr2 =  str(int(minute_qr)+10)

    verifyctx = "[Demi-Pass]\n["+str(userid)+"]\n[創建時間："+date_qr+" "+hour_qr+":"+minute_qr+":"+second_qr+"]\n[失效時間："+date_qr+" "+hour_qr+":"+minute_qr2+":"+second_qr+"]\n[有效時間：10分鐘]"
    img = qrcode.make(verifyctx)
    type(img)  
    img.save("qr_temp/qrcodeimg.png")
    qrpic = discord.File("qr_temp/qrcodeimg.png")
    msg = await ctx.send(file = qrpic)
    os.remove("qr_temp/qrcodeimg.png")
  else:
    msg = await ctx.send("你還沒有DemiPASS唷，可以去https://opensea.io/collection/demihuman ||花10ETH||買一個Demi Human NFT")
    
  BUTTONS = ["✅"]
  for b in BUTTONS:
    await msg.add_reaction(b)
  
  while True:
    try:
      react, user = await bot.wait_for("reaction_add", timeout=60.0, check=lambda r, u: r.message.id == msg.id and u.id == ctx.author.id and r.emoji in BUTTONS)
      await msg.remove_reaction(react.emoji, user) #user按了以後馬上清掉reaction
    
    except asyncio.TimeoutError:
      pass

    else:
      if react.emoji == BUTTONS[0]:
        await msg.delete()
        await ctx.send("交易完成")
################################################################################history volume
@slash.slash(name="Demi-Human-History",description="return some useful hidtory information from OpenSea API")

async def Demi_Human_History(ctx):
  url1='https://api.opensea.io/api/v1/collection/demihuman/stats?format=json' #api url
  site1 = ur.urlopen(url1)
  page1 = site1.read()
  contents1 = page1.decode()
  data1 = json.loads(contents1)

  one_day_volume = str(data1['stats']['one_day_volume'])[:5]#one_day_volume
  one_day_change = str(data1['stats']['one_day_change'])[:5]
  one_day_sales = str(data1['stats']['one_day_sales'])[:5]
  one_day_average_price = str(data1['stats']['one_day_average_price'])[:5]
  seven_day_volume = str(data1['stats']['seven_day_volume'])[:5]
  seven_day_change = str(data1['stats']['seven_day_change'])[:5]
  seven_day_sales = str(data1['stats']['seven_day_sales'])[:5]
  seven_day_average_price = str(data1['stats']['seven_day_average_price'])[:5]
  thirty_day_volume = str(data1['stats']['thirty_day_volume'])[:5]
  thirty_day_change = str(data1['stats']['thirty_day_change'])[:5]
  thirty_day_sales = str(data1['stats']['thirty_day_sales'])[:5]
  thirty_day_average_price = str(data1['stats']['thirty_day_average_price'])[:5]

  if(one_day_volume != 0):
    embed=discord.Embed(title="[歷史價格]", color=0xe8006f)
    embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Xeift/image-hosting@main//1c0e140d3293a88391abaaa1e02f8e0e.png")
    embed.add_field(name="1日總交易價格" , value=one_day_volume+" ETH", inline=False) 
    embed.add_field(name="1日交易價格變化" , value=one_day_change+" ETH", inline=False) 
    embed.add_field(name="1日交易數量" , value=one_day_sales+" Demi Human NFT", inline=False)
    embed.add_field(name="1日平均交易價格" , value=one_day_average_price+"ETH\n ㅤ", inline=False) 
    embed.add_field(name="7日總交易價格" , value=seven_day_volume+" ETH", inline=False) 
    embed.add_field(name="7日交易價格變化" , value=seven_day_change+" ETH", inline=False) 
    embed.add_field(name="7日交易數量" , value=seven_day_sales+" Demi Human NFT", inline=False)
    embed.add_field(name="7日平均交易價格" , value=seven_day_average_price+" ETH\n ㅤ", inline=False) 
    embed.add_field(name="30日總交易價格" , value=thirty_day_volume+" ETH", inline=False)
    embed.add_field(name="30日交易價格變化" , value=thirty_day_change+" ETH", inline=False)
    embed.add_field(name="30日交易數量" , value=thirty_day_sales+" Demi Human NFT", inline=False)
    embed.add_field(name="30日平均交易價格" , value=thirty_day_average_price+" ETH", inline=False)        
    await ctx.send(embed=embed)
  else:
      await ctx.send("錯誤")
################################################################################project realtime stats
@slash.slash(name="Demi-Human",description="return some useful realtime information from OpenSea API")

async def Demi_Human(ctx):
  url1='https://api.opensea.io/api/v1/collection/demihuman/stats?format=json' #api url
  site1 = ur.urlopen(url1)
  page1 = site1.read()
  contents1 = page1.decode()
  data1 = json.loads(contents1)

  total_volume = str(float(round(data1['stats']['total_volume'],3)))
  total_sales = str(float(round(data1['stats']['total_sales'],3)))
  total_supply = str(float(round(data1['stats']['total_supply'],3)))
  num_owners = str(float(round(data1['stats']['num_owners'],3)))
  average_price = str(float(round(data1['stats']['average_price'],3)))
  num_reports = str(float(round(data1['stats']['num_reports'],3)))
  market_cap = str(float(round(data1['stats']['market_cap'],3)))
  floor_price = str(float(round(data1['stats']['floor_price'],3)))

  if(total_volume != 0):
    embed=discord.Embed(title="[實時數據]", color=0xe8006f)
    embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Xeift/image-hosting@main//1c0e140d3293a88391abaaa1e02f8e0e.png")
    embed.add_field(name="總量" , value=total_supply+"/10000 Demi Human NFT", inline=False) 
    embed.add_field(name="總持有者" , value=num_owners+" 位", inline=False)     
    embed.add_field(name="地板價" , value=floor_price+" ETH", inline=False) 
    embed.add_field(name="總交易價格" , value=total_volume+" ETH", inline=False) 
    embed.add_field(name="總交易數量" , value=total_sales+" Demi Human NFT", inline=False)
    embed.add_field(name="平均交易價格" , value=average_price+"ETH", inline=False) 
    embed.add_field(name="被檢舉次數" , value=num_reports+" 次", inline=False) 
    embed.add_field(name="總市值" , value=market_cap+" ETH", inline=False) 
    
    await ctx.send(embed=embed)
  else:
      await ctx.send("錯誤")
################################################################################project history volume
@slash.slash(name="project-history",
description="return some useful history information from the project name you entered from OpenSea API",
options=
[
  create_option
  (
    name="project_name",
    description="enter the project name which is at the end of OpenSea url",
    option_type=3,
    required=True
  )
]
)

async def project_history(ctx,project_name):
  url1='https://api.opensea.io/api/v1/collection/'+project_name+'/stats?format=json' #api url
  site1 = ur.urlopen(url1)
  page1 = site1.read()
  contents1 = page1.decode()
  data1 = json.loads(contents1)

  one_day_volume = str(data1['stats']['one_day_volume'],3)#one_day_volume
  one_day_change = str(data1['stats']['one_day_change'],3)
  one_day_sales = str(data1['stats']['one_day_sales'],3)
  one_day_average_price = str(data1['stats']['one_day_average_price'],3)
  seven_day_volume = str(data1['stats']['seven_day_volume'],3)
  seven_day_change = str(data1['stats']['seven_day_change'],3)
  seven_day_sales = str(data1['stats']['seven_day_sales'],3)
  seven_day_average_price = str(data1['stats']['seven_day_average_price'],3)
  thirty_day_volume = str(data1['stats']['thirty_day_volume'],3)
  thirty_day_change = str(data1['stats']['thirty_day_change'],3)
  thirty_day_sales = str(data1['stats']['thirty_day_sales'],3)
  thirty_day_average_price = str(data1['stats']['thirty_day_average_price'],3)

  if(one_day_volume != 0):
    embed=discord.Embed(title="["+project_name+"歷史價格]", color=0xe8006f)
    embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Xeift/image-hosting@main//1c0e140d3293a88391abaaa1e02f8e0e.png")
    embed.add_field(name="1日總交易價格" , value=one_day_volume+" ETH", inline=False) 
    embed.add_field(name="1日交易價格變化" , value=one_day_change+" ETH", inline=False) 
    embed.add_field(name="1日交易數量" , value=one_day_sales+" Demi Human NFT", inline=False)
    embed.add_field(name="1日平均交易價格" , value=one_day_average_price+"ETH\n ㅤ", inline=False) 
    embed.add_field(name="7日總交易價格" , value=seven_day_volume+" ETH", inline=False) 
    embed.add_field(name="7日交易價格變化" , value=seven_day_change+" ETH", inline=False) 
    embed.add_field(name="7日交易數量" , value=seven_day_sales+" Demi Human NFT", inline=False)
    embed.add_field(name="7日平均交易價格" , value=seven_day_average_price+" ETH\n ㅤ", inline=False) 
    embed.add_field(name="30日總交易價格" , value=thirty_day_volume+" ETH", inline=False)
    embed.add_field(name="30日交易價格變化" , value=thirty_day_change+" ETH", inline=False)
    embed.add_field(name="30日交易數量" , value=thirty_day_sales+" Demi Human NFT", inline=False)
    embed.add_field(name="30日平均交易價格" , value=thirty_day_average_price+" ETH", inline=False)        
    await ctx.send(embed=embed)
  else:
      await ctx.send("錯誤")
################################################################################project
@slash.slash(name="project",
description="return some useful realtime information from the project name you entered from OpenSea API",
options=
[
  create_option
  (
    name="project_name",
    description="enter the project name which is at the end of OpenSea url",
    option_type=3,
    required=True
  )
]
)

async def project(ctx,project_name):
  url1='https://api.opensea.io/api/v1/collection/'+project_name+'/stats?format=json' #api url
  site1 = ur.urlopen(url1)
  page1 = site1.read()
  contents1 = page1.decode()
  data1 = json.loads(contents1)

  total_volume = str(float(round(data1['stats']['total_volume'],3)))
  total_sales = str(float(round(data1['stats']['total_sales'],3)))
  total_supply = str(float(round(data1['stats']['total_supply'],3)))
  num_owners = str(float(round(data1['stats']['num_owners'],3)))
  average_price = str(float(round(data1['stats']['average_price'],3)))
  num_reports = str(float(round(data1['stats']['num_reports'],3)))
  market_cap = str(float(round(data1['stats']['market_cap'],3)))
  floor_price = str(float(round(data1['stats']['floor_price'],3)))

  if(total_volume != 0):
    embed=discord.Embed(title="["+project_name+"實時數據]", color=0xe8006f)
    embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Xeift/image-hosting@main//1c0e140d3293a88391abaaa1e02f8e0e.png")
    embed.add_field(name="總量" , value=total_supply+"  個NFT", inline=False) 
    embed.add_field(name="總持有者" , value=num_owners+" 位", inline=False)     
    embed.add_field(name="地板價" , value=floor_price+" ETH", inline=False) 
    embed.add_field(name="總交易價格" , value=total_volume+" ETH", inline=False) 
    embed.add_field(name="總交易數量" , value=total_sales+"  個NFT", inline=False)
    embed.add_field(name="平均交易價格" , value=average_price+"ETH", inline=False) 
    embed.add_field(name="被檢舉次數" , value=num_reports+" 次", inline=False) 
    embed.add_field(name="總市值" , value=market_cap+" ETH", inline=False) 
    
    await ctx.send(embed=embed)
  else:
      await ctx.send("錯誤")
################################################################################NFT
@slash.slash(name="nft",
description="return some useful information about your NFT from the contract address and token id you entered",
options=
[
  create_option
  (
    name="contract_address",
    description="enter the contract address of yor NFT",
    option_type=3,
    required=True
  ),
  create_option
  (
    name="token_id",
    description="enter the token id of your NFT",
    option_type=3,
    required=True
  )
],
)

async def nft(ctx,contract_address,token_id):
  url1='https://api.opensea.io/api/v1/asset/'+contract_address+'/'+token_id+'/?format=json' #api url
  site1 = ur.urlopen(url1)
  page1 = site1.read()
  contents1 = page1.decode()
  data1 = json.loads(contents1)

  name = str(data1['name'])
  image_original_url = str(data1['image_original_url'])
  top_ownerships = str(data1['top_ownerships'][0]['owner']['user']['username'])
  description = str(data1['description'])
  external_link = str(data1['collection']['primary_asset_contracts'][0]['external_link'])
  schema_name = str(data1['collection']['primary_asset_contracts'][0]['schema_name'])
  token_id1 = str(data1['token_id'])
  permalink = str(data1['permalink'])

  if name == "None":
    name = "no data"
  if image_original_url == "None":
    image_original_url = "no data"
  if top_ownerships == "None":
    top_ownerships = "no data"   
  if description == "None":
    description = "no data"
  if external_link == "None":
    external_link = "no data"
  if schema_name == "None":
    schema_name = "no data" 
  if token_id1 == "None":
    token_id1 = "no data"
  if permalink == "None":
    permalink = "no data"

  embed=discord.Embed(title="["+name+"]", color=0xe8006f)
  embed.set_thumbnail(url=image_original_url)
  embed.add_field(name="NFT編號" , value=token_id1, inline=False) 
  embed.add_field(name="簡介" , value=description, inline=False)     
  embed.add_field(name="官網" , value=external_link, inline=False) 
  embed.add_field(name="NFT類型" , value=schema_name, inline=False) 
  embed.add_field(name="擁有者" , value=top_ownerships, inline=False)
  embed.add_field(name="OpenSea" , value=permalink, inline=False)
  embed.add_field(name="原始畫質圖片" , value=image_original_url, inline=False)

  await ctx.send(embed=embed)
################################################################################NFT
@slash.slash(name="demi_nft",
description="return some useful information about your Demi Human NFT from the token id you entered",
options=
[
  create_option
  (
    name="token_id",
    description="enter the token id of your NFT",
    option_type=3,
    required=True
  )
],
)

async def demi_nft(ctx,token_id):
  url1='https://api.opensea.io/api/v1/asset/0xa6916545A56f75ACD43fb6A1527A73a41d2b4081/'+token_id+'/?format=json' #api url
  site1 = ur.urlopen(url1)
  page1 = site1.read()
  contents1 = page1.decode()
  data1 = json.loads(contents1)

  name = str(data1['name'])
  image_original_url = str(data1['image_original_url'])
  top_ownerships = str(data1['top_ownerships'][0]['owner']['user']['username'])
  description = str(data1['description'])
  external_link = str(data1['collection']['primary_asset_contracts'][0]['external_link'])
  schema_name = str(data1['collection']['primary_asset_contracts'][0]['schema_name'])
  token_id1 = str(data1['token_id'])
  permalink = str(data1['permalink'])

  if name == "None":
    name = "no data"
  if image_original_url == "None":
    image_original_url = "no data"
  if top_ownerships == "None":
    top_ownerships = "no data"   
  if description == "None":
    description = "no data"
  if external_link == "None":
    external_link = "no data"
  if schema_name == "None":
    schema_name = "no data" 
  if token_id1 == "None":
    token_id1 = "no data"
  if permalink == "None":
    permalink = "no data"

  embed=discord.Embed(title="["+name+"]", color=0xe8006f)
  embed.set_thumbnail(url=image_original_url)
  embed.add_field(name="NFT編號" , value=token_id1, inline=False) 
  embed.add_field(name="簡介" , value=description, inline=False)     
  embed.add_field(name="官網" , value=external_link, inline=False) 
  embed.add_field(name="NFT類型" , value=schema_name, inline=False) 
  embed.add_field(name="擁有者" , value=top_ownerships, inline=False)
  embed.add_field(name="OpenSea" , value=permalink, inline=False)
  embed.add_field(name="原始畫質圖片" , value=image_original_url, inline=False)

  await ctx.send(embed=embed)
################################################################################
keep_alive.keep_alive()
bot.run(discord_token)