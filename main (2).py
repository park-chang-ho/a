# This Python file uses the following encoding: utf-8
from distutils.cmd import Command
import os, sys, discord, random, asyncio, traceback, re, time, requests, pickle, json, datetime, laftel, xmltodict, sqlite3
import xml.etree.ElementTree as ET
from discord import Activity, ActivityType
from discord.ext import commands, tasks
from itertools import cycle
from typing import Union
from emoji import UNICODE_EMOJI
import aiohttp
from urllib.parse import quote
import numpy as np
import pandas as pd
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup
import urllib.request
from seoul import Client
from webdriver import keep_alive
from googleapiclient.discovery import build

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

man = '🀇'
man2 = '🀈'
man3 = '🀉'
man4 = '🀊'
man5 = '🀋'
man6 = '🀌'
man7 = '🀍'
man8 = '🀎'
man9 = '🀏'
tong = '🀙'
tong2 = '🀚'
tong3 = '🀛'
tong4 = '🀜'
tong5 = '🀝'
tong6 = '🀞'
tong7 = '🀟'
tong8 = '🀠'
tong9 = '🀡'
sak = '🀐'
sak2 = '🀑'
sak3 = '🀒'
sak4 = '🀓'
sak5 = '🀔'
sak6 = '🀕'
sak7 = '🀖'
sak8 = '🀗'
sak9 = '🀘'
dong = '🀀'
nam = '🀁'
seo = '🀂'
buck = '🀃'
joong = '🀄'
bal = '🀅'
back = '🀆'

key = "sF36xw%2FgdZjKy5PeTJUh2TGNhc6hYvVBD09VDclye4EjZcWXw4s97ZORxVfdKLRwhkptnpz%2FJxoPK5Os07mNwQ%3D%3D"

#"이 봇의 명령어는 .도움 이라고 예기 ", "이 봇은 학습 ", f"현재 {len(app.guilds)}개의 서버에 참여 중"

intents = discord.Intents.all()

app = commands.Bot(command_prefix='.', intents=intents)
status = cycle(["명령어는 .도움 이라고 얘기", "이 봇은 학습 ", "봇 관련 질문은 카구라히카리#5288로"])

seoul = Client()

blocked_user = [902557582294654987]


def get_random_cat_image_url():
    response = requests.get("https://nekos.life/api/v2/img/neko")
    if response.status_code == 200:
        data = response.json()
        image_url = data["url"]
        return image_url
    else:
        print("Error:", response.status_code)
        return None


@app.event
async def on_ready():
    print("로그인에 성공")
    print(f"{app.user.name}")
    print(f"{app.user.id}")


@tasks.loop(seconds=3)
async def change_status():
    await app.change_presence(activity=discord.Game(next(status)))


@app.event
async def on_reaction_add(reaction, user):
    role = discord.utils.get(user.guild.roles, name="기본")
    await user.add_roles(role)


@app.event
async def on_message(message):
    CHANNEL_ID = 1410751039438852206  #1098261056637370440
    bad2 = ['<@958192042570293288>']
    ALLOWED_USERS = [571950912655065089]
    binz = ['.삭제']
    message_contant = message.content
    if message.guild is None and message.author.id == 736565395300941854:
        # 메시지 내용 저장
        msg_content = message.content

        # 특정 채널에서 메시지 전송
        channel = await app.fetch_channel(CHANNEL_ID)
        await channel.send(msg_content)

    # 명령어 처리
    else:
        await app.process_commands(message)
    for i in bad2:
        if i in message_contant:
            mm = [
                "멘션 금지",
                "뭐하세요?",
                "너 뭐하니?",
                "그만!",
                "멘션하면 큰일(?)나요!",
                "니까짓게 감히 위대한 나를 멘션해?",
                "장난 금지!",
                "심심해?",
                "자~",
                " 조용!",
                "왜 그러니?",
                "뭐가 문제니!",
                "내 도움이 필요하니?",
                "내가 궁금하니? \n .도움을 입력해보렴~",
                "위대하신(?) 카구라 히카리님이 날 만들어 주셨어...",
                "나 가지고 이상한 장난 하지마",
                "안녕? \n 내 이름은 공원봇 (parkbot)! \n 내 이름이 왜 이런지는 제작자(카구라히카리님)도 모른다고 했어...\n 혹시 대충 지어준게 아닐까 하는 생각도 드네...",
            ]
            randomNum = random.randrange(0, len(mm))
            print("랜덤수 값 :" + str(randomNum))
            print(mm[randomNum])
            await message.channel.send(mm[randomNum])
    for i in binz:
        if i in message_contant:
            if message.author.guild_permissions.administrator:
                requester_type = "관리자"
            elif message.author.id in ALLOWED_USERS:
                requester_type = "봇 관리자"
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                embed = discord.Embed(
                    title="메시지 삭제 알림",
                    description=
                    f"최근 디스코드 채팅 {amount}개가\n{requester_type} {message.author.display_name}님의 요청으로 인해 정상 삭제 조치 되었습니다."
                    .format(amount, message.author),
                    color=0x000000)
                embed.set_footer(text=f"{message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                                 icon_url=message.author.display_avatar)
                message = await message.channel.send(embed=embed)
                await asyncio.sleep(5)
                await message.delete()
            else:
                await message.delete()
                embed = discord.Embed(
                    title="메시지 삭제 알림",
                    description=
                    "{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다 \n 관리자에게 문의 바랍니다".format(
                        message.author.mention),
                    color=0x000000)
                embed.set_footer(text=f"{message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                                 icon_url=message.author.display_avatar)
                message = await message.channel.send(embed=embed)
                await asyncio.sleep(5)
                await message.delete()

    if not message.guild or message.author.id == app.user.id:
        return

    server_id_1 = 958313240633434113  # 특정 서버의 ID
    server_id_2 = 715085662373806141

    if message.guild.id == server_id_1 or message.guild.id == server_id_2:
        return

    m = re.match(r"^<a?:[\w]+:([\d]+)>$", message.content)
    if m:
        if message.content.startswith("<a:"):
            ext = "gif"
        else:
            ext = "png"

        embed = discord.Embed(color=message.author.color)
        embed.set_author(name=message.author.name,
                         icon_url=message.author.display_avatar)
        embed.set_image(
            url=f"https://cdn.discordapp.com/emojis/{m.group(1)}.{ext}")
        await message.channel.send(embed=embed)
        await message.delete()


@commands.cooldown(1, 2, commands.BucketType.user)
@app.command(aliases=['도움'])
async def a(ctx):
    if ctx.author.id in blocked_user:
        return
    embed = discord.Embed(title="parkbot",
                          description="명령어 모음",
                          color=0x62c1cc)
    embed.add_field(name=".기본", value="명령어보기")
    embed.add_field(name=".놀이", value="명령어보기")
    embed.add_field(name=".삭제(숫자)", value="관리자 권한 가진 사람만 가능")
    embed.add_field(name="이모티콘을 보내면?", value="크게 되지요~\n(특정 서버 제외)")
    embed.set_image(url="")
    embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                     icon_url=ctx.message.author.display_avatar)
    await ctx.reply(embed=embed)


@app.command(aliases=['기본'])
async def b(ctx):
    if ctx.author.id in blocked_user:
        return
    embed = discord.Embed(title="기본", description="명령어 모음", color=0x62c1cc)
    embed.add_field(name=".핑", value="하루키라는 분이 제공 해주셨습니다#")
    embed.add_field(name=".안녕", value="0")
    embed.add_field(name=".프사", value=".프사 + 프사 보고 싶은 사람 멘션")
    embed.add_field(name=".때리기", value="멘션과 함께")
    embed.add_field(name=".이모지허그", value="멘션과 함께")
    embed.add_field(name=".따라해", value="봇이 널 따라함")
    embed.add_field(name=".유저정보 + 멘션",
                    value="나의 정보와 다른 사람의 정보를 알려드립니다",
                    inline=False)
    embed.add_field(name=".투표", value="예) .투표\n투표 주제 감자 고구마")
    embed.add_field(name="멘션 하지마라", value="뭐가 나올까?")
    embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                     icon_url=ctx.message.author.display_avatar)
    await ctx.reply(embed=embed)


@app.command(aliases=['놀이'])
async def c(ctx):
    if ctx.author.id in blocked_user:
        return
    embed = discord.Embed(title="놀이", description="명령어 모음", color=0x62c1cc)
    embed.add_field(name=".오타쿠", value="명령어 보기")
    embed.add_field(name=".게임", value="명령어 보기")
    embed.add_field(name=".랜덤", value="명령어 보기")
    embed.add_field(name=".교통", value="명령어 보기")
    embed.add_field(name=".멜론검색 + 노래 이름 또는 가수 이름", value="(베타 버전)")
    embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                     icon_url=ctx.message.author.display_avatar)
    await ctx.reply(embed=embed)


@app.command(aliases=['교통'])
async def c1(ctx):
    if ctx.author.id in blocked_user:
        return
    embed = discord.Embed(title="교통", description="명령어 모음", color=0x62c1cc)
    embed.add_field(name=".버스 + (버스번호)",
                    value="예) .버스 370\n(테스트중)\n서울 버스(마을버스 제외)만 가능")
    embed.add_field(
        name=".지하철 + ()호선",
        value=
        "예) .지하철 경의중앙선\n(테스트중)\n검색 가능한 노선 [1호선, 2호선, 3호선, 4호선, 5호선, 6호선, 7호선, 8호선, 9호선, 수인분당선, 신분당선, 경의중앙선, 공항철도, 경춘선, 우이신설선]"
    )
    embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                     icon_url=ctx.message.author.display_avatar)
    await ctx.reply(embed=embed)


@app.command(aliases=['랜덤'])
async def cg(ctx):
    if ctx.author.id in blocked_user:
        return
    embed = discord.Embed(title="랜덤", description="명령어 모음", color=0x62c1cc)
    embed.add_field(name=".유튜브검색 + 검색어", value="예) .유튜브검색 애국가")
    embed.add_field(name=".랜덤이모지", value="이모지가 랜덤으로~")
    embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                     icon_url=ctx.message.author.display_avatar)
    await ctx.reply(embed=embed)


@app.command(aliases=['게임'])
async def cg1(ctx):
    if ctx.author.id in blocked_user:
        return
    embed = discord.Embed(title="게임", description="명령어 모음", color=0x62c1cc)
    #    embed.add_field(name = ".도박", value = "이 게임을 하고 싶다면 일단 #도박장 이라는 체널을 만드세요.\n명령어 보기")
    embed.add_field(name=".랜덤주사위", value="주사위 숫자가 랜덤으로~")
    embed.add_field(name=".짱깸뽀", value="봇과 가위바위보 한판!\n예) .짱깸뽀 가위")
    embed.add_field(name=".명언타자",
                    value="무작위로 나오는 명언들을 20초 안에 빨리 치세요!\n이 봇은 오타를 싫어합니다")
    embed.add_field(name=".아재개그",
                    value="무작위로 나오는 아재개그의 답을 10초 안에 빨리 치세요!\n이 봇은 오타를 싫어합니다")
    embed.add_field(name=".구구단퀴즈",
                    value="무작위로 나오는 구구단 문제!\n여러분도 풀어보세요!4\n이 봇은 오타를 싫어합니다")
    embed.add_field(
        name=".업다운",
        value=
        "봇의 마음을 읽어볼시간~\n1에서 100까지의 랜덤한 숫자들~\n과연 봇은 어떤 숫자를 선택 했을지 여러분들이 한번 맞춰보세요!\n시간은 턴 마다 10초(글자 칠 시간)를 드립니다"
    )
    embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                     icon_url=ctx.message.author.display_avatar)
    await ctx.reply(embed=embed)


@app.command(aliases=['오타쿠'])
async def cz(ctx):
    if ctx.author.id in blocked_user:
        return
    embed = discord.Embed(title="오타쿠", description="명령어 모음", color=0x62c1cc)
    #embed.add_field(name = ".반응", value = "O는 멘션 가능한 명령어, X는 멘션 기능이 없는 명령어\n(명령어 보기)")
    embed.add_field(name=".일러스트", value="인증을 해야 가능(현재는 막아둠)")
    embed.add_field(name=".뱅드림만화", value="뱅드림 만화가 무작위로 나옴")
    embed.add_field(name=".고양이", value="귀여운 고양이(?) 보세요!\n랜덤으로 나와요!")
    embed.add_field(name=".애니검색", value=".애니검색 + 애니이름")
    embed.add_field(name=".보컬로이드", value="랜덤으로 추천 해주는 보컬로이드 노래, 프세카 관련 영상과 음악")
    #embed.add_field(name = ".스타리라", value = "소녀 가극 레뷰 스타라이트 -Re LIVE- 게임 일러스트 관련 명령어를 볼 수 있습니다.\n[현재 저는 바쁜 관계로 이 부분의 업데이트는 힘들것 같습니다.]\n출처는 나무위키이며 나무위키는 나무위키일뿐 정확하지 않을 수 있으니 양해 바랍니다.\n이 명령어 관련 수정을 원하시는 분은 봇 주인 (카구라히카리#5288)으로 DM 주시면 확인후 수정 하겠습니다.")
    embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                     icon_url=ctx.message.author.display_avatar)
    await ctx.reply(embed=embed)


@app.command(name="유저정보")
async def userinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.purple(),
                          timestamp=ctx.message.created_at,
                          title=f"{member}의 정보")
    embed.set_thumbnail(url=member.avatar.url)
    embed.set_footer(text=f"{ctx.author}가 명령어를 사용함.")
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="서버 닉네임:", value=member.display_name)
    embed.add_field(
        name="계정 생성 시간:",
        value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(
        name="서버 입장 시간:",
        value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    roles = [role.mention for role in member.roles if not role.is_default()]
    if roles:
        embed.add_field(name="역할들:", value="".join(roles))
    else:
        embed.add_field(name="역할들:", value="없음")
    embed.add_field(name="최상위 역할:", value=member.top_role.mention)
    embed.add_field(name="봇여부:", value=member.bot)
    await ctx.send(embed=embed)


@app.command(aliases=['안녕'])
async def d(ctx):
    if ctx.author.id in blocked_user:
        return
    ama = [
        "https://ac2-p2.namu.la/20221206sac2/cc3f30c2db20400864a198955da74db3661d371e41a110c997c472260e30c1d6.gif",
        "https://media.tenor.com/XMvXpoXRgIUAAAAi/anko-kitashirakawa-tamako-market.gif",
        "https://media.tenor.com/vJh0VNq-XxYAAAAj/630-%EB%8D%B0%EB%A0%88%EC%8A%A4%ED%85%8C%EC%BF%A8.gif",
        "https://media.tenor.com/kLchf-ekqdAAAAAi/rin-hoshizora-anime.gif",
        "https://media.tenor.com/hh80qwBav_cAAAAi/shiratori-kurumi-d4dj.gif",
        "https://media.tenor.com/KM3VNP5d1FIAAAAC/miku-hello.gif",
        "https://media.tenor.com/DDnp-TLMTWQAAAAC/hello-anime.gif"
    ]
    randomNum = random.randrange(0, len(ama))
    print("랜덤수 값 :" + str(randomNum))
    print(ama[randomNum])
    embed = discord.Embed(title="안녕~",
                          description=f"{ctx.author.mention}님 안녕하세요~",
                          color=0x62c1cc)
    embed.set_image(url=ama[randomNum])
    embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                     icon_url=ctx.message.author.display_avatar)
    await ctx.reply(embed=embed)


#--------------기본--------------
@app.command(aliases=['핑'])
async def ping(ctx):
    if ctx.author.id in blocked_user:
        return
    gcolor = 0x336BFF
    ecolor = 0x00ff56
    ncolor = 0xD9EA33
    omgcolor = 0xFF0000
    errorcolor = 0xC70039
    pings = round(app.latency * 1000)
    if pings < 100:
        pinglevel = '🔵 매우좋다\n(따봉!)'
        color = gcolor
        gif_url = 'https://media.tenor.com/0XDvs2JB8RsAAAAi/meiling-thumbs-up.gif'
    elif pings < 200:
        pinglevel = '🟢 양호하다\n(오케이!)'
        color = ecolor
        gif_url = "https://media.tenor.com/Ts7xLC70LqwAAAAi/menhera-chibi.gif"
    elif pings < 300:
        pinglevel = '🟡 보통이다\n(빙글빙글)'
        color = ncolor
        gif_url = "https://tenor.com/ko/view/ereshkigal-padoru-fate-fate-grand-order-fgo-gif-24820856"
    elif pings < 500:
        pinglevel = '🔴 나쁘다\n(칼가는중)'
        color = errorcolor
        gif_url = "https://tenor.com/ko/view/uni-corn-asasas-azurlane-unicorn-killer-azur-lane-unicorn-bad-mood-gif-13327303"
    else:
        pinglevel = '🔴 매우 나쁘다\n(고쳐저라...[퍽퍽...])'
        color = omgcolor
        gif_url = "https://tenor.com/ko/view/cheshire-azur-lane-bonk-emote-no-horny-gif-21675007"

    embed = discord.Embed(title="🏓 | 현재 나의 핑 상태 이올시다",
                          description=f"{pings}ms\n{pinglevel}",
                          color=color)
    embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1\
                                                                                 소스 제공: 하루키#3801",
                     icon_url=ctx.message.author.display_avatar)
    if gif_url:
        embed.set_image(url=gif_url)
    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/890396367569182813/916185428481150996/IMG_1029.PNG?width=409&height=467"
    )
    await ctx.reply(embed=embed)


@app.command(aliases=['어이없네'])
async def fuk(ctx, member: discord.Member = None):
    if ctx.author.id in blocked_user:
        return
    await ctx.reply(
        "https://media.tenor.com/4prfwLpDBsgAAAAC/park-myeongsu-listening.gif")


@app.command(aliases=['따라해'])
async def f(ctx, *, arg):
    if ctx.author.id in blocked_user:
        return
    await ctx.reply(arg)


@app.command(aliases=['때리기'])
async def fuck(ctx, member: discord.Member = None):
    if ctx.author.id in blocked_user:
        return
    await ctx.reply("그런거 나빠요 하지마세요")


@app.command(aliases=['이모지허그'])
async def hug(ctx, member: discord.Member = None):
    if ctx.author.id in blocked_user:
        return
    ask07 = [
        '<a:a1:969581186798223450>', '<a:a2:969581281123913749>',
        '<a:a3:969581365945327708>', '<a:a4:969581429849731143>'
    ]
    await ctx.send(f"{ctx.author.mention}님이 {member.mention}님을 안아 드렸습니다")
    randomNum = random.randrange(0, len(ask07))
    print("랜덤수 값 :" + str(randomNum))
    print(ask07[randomNum])
    await ctx.reply(ask07[randomNum])


@app.command(aliases=['프사'])
async def avatars(ctx, *, member: discord.Member = None):
    if ctx.author.id in blocked_user:
        return
    if not member:
        member = ctx.message.author
    userAvatar = member.display_avatar
    embed = discord.Embed(
        title="프로필 사진 도둑이다!!!",
        description=f"제가 {member.mention}님의 프로필 사진을 몰래(?) 가지고 왔답니다~\n칭찬 해줘요!",
        color=0x62c1cc)
    embed.set_image(url=userAvatar)
    embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                     icon_url=ctx.message.author.display_avatar)
    await ctx.reply(embed=embed)


@app.command()
async def 투표(ctx, title, *choice):
    if ctx.author.id in blocked_user:
        return
    if title is None and choice == ():
        embed = discord.Embed(title=f'투표 도움말', description=f'개발자: 카구라히카리')
        embed.add_field(name=f'좋아요/싫어요', value=f'!투표 제목')
        embed.add_field(name=f'복수응답(1-9)', value=f'!투표 제목 내용1 내용2 ...')
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title=title)
        if choice == ():

            embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                             icon_url=ctx.message.author.display_avatar)
            message = await ctx.reply(embed=embed)
            await message.add_reaction('👍')
            await message.add_reaction('👎')
        else:

            emoji_list = [
                '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣'
            ]

            s = ''
            emoji = iter(emoji_list)
            for cont in choice:
                try:
                    s += f'{next(emoji)} {cont}\n'
                except ValueError:
                    await ctx.sent('투표 선택지는 9개까지만 가능합니다.')
                    return

            embed.add_field(name=s, value='1은 기본적으로 있음, 중복투표 가능')
            embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                             icon_url=ctx.message.author.display_avatar)
            message = await ctx.reply(embed=embed)

            for i in range(len(choice)):
                await message.add_reaction(emoji_list[i])


#--------------기본--------------


@app.command(aliases=['랜덤이모지'])
async def h(ctx):
    if ctx.author.id in blocked_user:
        return
    emoji = [
        " ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ",
        " ⋌༼ •̀ ⌂ •́ ༽⋋ ", " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ",
        " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ", " ( •́ ̯•̀ ) ",
        " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ",
        " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ", " ´_ゝ` ", " ٩(͡◕_͡◕ ",
        " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
        " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "##╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄",
        "︻╦̵̵͇̿̿̿̿══╤─", " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ",
        " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ", " (///▽///) ", " σ(oдolll) ",
        " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
        " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ", " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ",
        " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "
    ]
    randomNum = random.randrange(0, len(emoji))
    print("랜덤수 값 :" + str(randomNum))
    print(emoji[randomNum])
    await ctx.reply(emoji[randomNum])


@app.command(aliases=['랜덤주사위'])
async def i(ctx):
    if ctx.author.id in blocked_user:
        return
    randomNum = random.randrange(1, 7)  # 1~6까지 랜덤수
    print(randomNum)
    if randomNum == 1:
        await ctx.reply(embed=discord.Embed(description='⚀\n ' + ':one:'))
    if randomNum == 2:
        await ctx.reply(embed=discord.Embed(description='⚁\n ' + ':two:'))
    if randomNum == 3:
        await ctx.reply(embed=discord.Embed(description='⚂\n ' + ':three:'))
    if randomNum == 4:
        await ctx.reply(embed=discord.Embed(description='⚃\n ' + ':four:'))
    if randomNum == 5:
        await ctx.reply(embed=discord.Embed(description='⚄\n ' + ':five:'))
    if randomNum == 6:
        await ctx.reply(embed=discord.Embed(description='⚅\n ' + ':six: '))


@app.command(aliases=['짱깸뽀'])
async def k(ctx, user: str):
    if ctx.author.id in blocked_user:
        return
    rps_table = ['가위', '바위', '보']
    bot = random.choice(rps_table)
    result = rps_table.index(user) - rps_table.index(bot)
    if result == 0:
        await ctx.reply(f'{user} vs {bot}  \n게임결과...\n비겼습니다.')
    elif result == 1 or result == -2:
        await ctx.reply(f'{user} vs {bot}  \n게임결과...\n유저가 이겼습니다.')
    else:
        await ctx.reply(f'{user} vs {bot}  \n게임결과...\n봇이 이겼습니다.')


@app.command()
async def 업다운(ctx):
    if ctx.author.id in blocked_user:
        return
    # 게임 초기화
    number = random.randint(1, 100)
    attempts = 0
    await ctx.send("1에서 100까지의 숫자를 맞춰보세요!\n시간은 10초!")

    # 게임 루프
    while True:
        try:
            message = await app.wait_for("message",
                                         timeout=10,
                                         check=lambda m: m.author == ctx.author
                                         and m.channel == ctx.channel)
        except:
            embed = discord.Embed(title="게임 오버!",
                                  description="시간 초과!",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)
            return

        guess = int(message.content)
        attempts += 1

        if guess < number:
            embed = discord.Embed(title="숫자 맞추기 게임",
                                  description="너무 낮아요!",
                                  color=discord.Color.blue())
            await ctx.send(embed=embed)
        elif guess > number:
            embed = discord.Embed(title="숫자 맞추기 게임",
                                  description="너무 높아요!",
                                  color=discord.Color.blue())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="숫자 맞추기 게임",
                                  description=f"정답입니다! {attempts}번 만에 맞추셨어요!",
                                  color=discord.Color.green())
            await ctx.send(embed=embed)
            return


#--------------교통--------------

@app.command(name="지하철")
async def train(ctx, *, text):
    if ctx.author.id in blocked_user:
        return
    trains = seoul.get_subway_realtime_position(text)
    for train in trains:
        embed = discord.Embed(title="지하철 정보", description="ㅁ", color=0x62c1cc)
        embed.add_field(name="지하철호선명", value=train.subway_name, inline=True)
        embed.add_field(name="지하철역명", value=train.station_name, inline=True)
        embed.add_field(name="열차번호", value=train.number, inline=True)
        embed.add_field(name="종착 지하철역명",
                        value=train.terminal_station_name,
                        inline=True)
        embed.add_field(name="열차 상태 구분 (0:진입 1:도착, 0,1외 나머지는:출발)",
                        value=train.status,
                        inline=True)
        embed.add_field(name="열차 방향", value=train.direction, inline=True)
        embed.add_field(name="급행 여부 (F는 아님 T는 급행)",
                        value=train.express,
                        inline=True)
        embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                         icon_url=ctx.message.author.display_avatar)
        return await ctx.reply(embed=embed)

@app.command()
async def 버스3(ctx, *, bus_number):
    url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey={key}&strSrch={bus_number}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            text = await resp.text()

    # XML 파싱
    root = ET.fromstring(text)

    # itemList 찾기
    items = root.findall(".//itemList")

    # 정확히 일치하는 버스 번호만 필터링
    matches = [item for item in items if item.find("busRouteAbrv").text == bus_number]

    if not matches:
        await ctx.send(f"버스 {bus_number}를 찾을 수 없습니다.")
        return

    for item in matches:
        bus_name = item.find("busRouteNm").text
        start = item.find("stStationNm").text
        end = item.find("edStationNm").text
        corp = item.find("corpNm").text
        first_bus = item.find("firstBusTm").text
        last_bus = item.find("lastBusTm").text
        term = item.find("term").text
        item.find("lastBusTm").text
        busRoute = item.find("busRouteId").text

        # 시간 형식 변환 (YYYYMMDDHHMMSS → HH:MM)
        def format_time(t):
            if t and t.strip():
                return f"{t[8:10]}:{t[10:12]}"
            return "정보 없음"

        embed = discord.Embed(
            title=f"버스 {bus_name}",
            description=f"운행회사: {corp}\n출발: {start}\n도착: {end}\n첫차: {format_time(first_bus)}\n막차: {format_time(last_bus)}\n배차간격: {term}분\n노선도: {busRoute}\n노선도를 보려면 .루트랑 노선도 번호를 같이 쓰세요"
        )
        await ctx.send(embed=embed)

@app.command(name="루트")
async def route(ctx, *, text):
    async def getStationList(routeid):
        html = requests.get(
            'http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?ServiceKey='
            + key + '&busRouteId=' + routeid).text
        root = BeautifulSoup(html, 'html.parser')
        items = root.find_all('itemlist')

        directions = {}
        for j in items:
            direction = j.find("direction").text if j.find("direction") else "알수없음"
            stationnm = j.find("stationnm").text if j.find("stationnm") else "?"
            if direction not in directions:
                directions[direction] = []
            directions[direction].append(stationnm)

        result = []
        for d, stations in directions.items():
            # 모든 정류장을 ' > '로 이어붙이기
            line = " > ".join(stations)
            result.append(f"[{d} 방면]\n{line}")

        return "\n\n".join(result)

    station_list = await getStationList(text)
    await ctx.reply(embed=discord.Embed(
        title="운행방향",
        description=station_list,
        color=0x62c1cc
    ))

#--------------교통--------------

#--------------기본--------------


@app.command(aliases=['명언타자'])
async def type(ctx):
    if ctx.author.id in blocked_user:
        return
    starttime = time.time()
    answer = [
        '동해물과 백두산이 마르고 닳도록', '하나님이 보우하사 우리나라 만세', '무궁화 삼천리 화려강산',
        '상처를 주고 후회를 해도 주워담을 수 없는게 말이다', '인생은 살아있는 동안 몇번이고 새출발할 수 있다',
        '왕은 누구보다 강렬하게 살고 모든이를 매혹 시킨다', '포기하면 그 순간 바로 시합 종료다',
        '자신을 믿지 않는 사람은 노력할 가치도 없다', '꿈은 도망가지 않으며 도망가는 것은 언제나 나 자신이다',
        '우리는 혼자가 아니다', '맑은물에서 살든 시궁창에서 살든 앞으로 헤엄치는 물고기는 아름답게 자라는 법이다',
        '오늘의 특별한 순간들은 내일의 추억이다', '예쁘지 않은 것을 예쁘게 보아주는 것이 사랑이다',
        '우리는 외관이 변하지 않더라도 내면은 끊임없이 변한다', '인생의 선택에 타인의 말은 필요 없다',
        '계획대로 되지 않는게 인생이다', '약한 자일수록 상대를 용서하지 못한다', '용서한다는 것은 강하다는 증거다',
        '할 수 있다고 생각 하니까 할 수 있는 것이다', '평생 행복하고 싶다면 정직하게 살아라'
    ]

    timer = 30.0
    randomNum = random.randrange(0, len(answer))
    print("랜덤수 값 :" + str(randomNum))
    print(answer[randomNum])
    await ctx.reply(f"{timer} 초 안에: {answer[randomNum]} 를 처줘!")

    def is_correct(msg):
        return msg.author == ctx.author

    try:
        guess = await app.wait_for('message', check=is_correct, timeout=timer)
    except asyncio.TimeoutError:
        return await ctx.reply("실패...\n 다시 시도해봐!")

    if guess.content == answer[randomNum]:
        fintime = time.time()
        total = fintime - starttime
        await ctx.reply(f"성공 했습니다!\n{round(total)} 초 걸렸네요")

    else:
        await ctx.reply("아니야...\n내가 원하는건 이게 아니야...\n(종료)")
        return


@app.command(aliases=['아재개그'])
async def gag1(ctx):
    if ctx.author.id in blocked_user:
        return
    starttime = time.time()
    answers = [
        '오리가 얼면?', '동그라미 2개, 별이 2개면?', '딸기가 직장을 잃으면?', '소금의 유통기한은?',
        '세상에서 가장 억울한 도형은?', '우유가 넘어지면?', '아몬드가 죽으면?', '소가 죽으면?', '깨가 죽으면?',
        '토끼가 쓰는 빗은?', '세상에서 가장 쉬운 숫자는?', '비가 1시간 동안 내리면?', '바늘만 가지고 다니는 사람은?',
        '콩 한알을 영어로?', '햄버거는의 색깔은?', '토끼가 강한 이유는?', '가장 정의로운 달은?',
        '항상 미안한 동물은?', '가장 인기있는 벌레는?', '둘리가 다니는 고등학교 이름은?', '삶은?', '이별은?',
        '11월에 뱀이랑 벌이 없는 이유는?', '미소의 반대말은?', '모래가 울면?', '얼음이 죽으면?', '사과가 웃으면?',
        '칼이 정색하면?', '바나나가 웃으면?', '아마존의 창업자는?', '차가 울면?', '무가 울면?',
        '거북이가 소화제를 먹은 이유는?', '피자가 놀라면?', '침묵을 영어로?', '가장 폭력적인 동물은?',
        '독재를 다섯글자로?', '살면서 가장 조심해야 할 개 두마리는?', '스님이 못가는 대학교는?', '소가 이기면?',
        '용이 놀라면?', '다정함의 반대말은?', '아이 추워의 반대말은?', '문제투성이인 것은?', '소가 노래하면?',
        '자가용의 반대말은?', '달에서 쓰는 언어는?', '돌잔치를 영어로?', '말이 화가 나면?', '오이가 무를 치면?',
        '있을 수도 있고 없을 수도 있는 섬은?', '논리적인 사람이 총을 쏘면?', '물고기가 싫어하는 물은?', '해가 울면?',
        '선생님이 좋아하는 피자는?', '다이어리를 쓰면 빨리 죽는 이유는?', '개가 벽을 보고 영어로 한 말은?',
        '미국에 비가 내리면?', '왕이 궁에 들어가기 싫을 때 하는 말은?', '세상에서 제일 예쁜 풀은?'
    ]
    dap = [
        '언덕', '영영이별', '딸기시럽', '천일염', '원통', '아야', '다이아몬드', '다이소', '주근깨', '래빗',
        '190000', '추적 60분', '실 없는 사람', '원빈', '버건디', '깡과 총이 있어서', '악토벌', '오소리',
        '스타벅스', '빙하타고', '계란', '지구', '노뱀벌', '당기소', '흙흙', '다이빙', '풋사과', '검정색',
        '바나나킥', '아마존', '잉카', '무뚝뚝', '속이 거북해서', '피자헛', '노말', '팬다', '나홀로지배',
        '편견과 선입견', '중앙대', '우승', '띠용', '선택장애', '어른 더워', '시험지', '소송', '커용', '문어',
        '락페스티벌', '마리화나', '오이무침', '아마도', '타당 타당', '그물', '해운대', '책피자',
        'Die Early', '월월', 'USB', '궁시렁궁시렁', '뷰티풀'
    ]

    timers = 10.0
    randomNum = random.randrange(0, len(answers))
    print("랜덤수 값 :" + str(randomNum))
    print(answers[randomNum])
    await ctx.reply(f"{answers[randomNum]}\n뭘까요~\n{timers} 초 안에 맞춰봐용!")

    def is_correct(msg):
        return msg.author == ctx.author

    try:
        guess = await app.wait_for('message', check=is_correct, timeout=timers)
    except asyncio.TimeoutError:
        return await ctx.reply(
            f"시간이 지났어요...\n정답은 {dap[randomNum]} 이랍니다~\왜 그런지는 직접 검색 해봐요...")

    if guess.content == dap[randomNum]:
        fintime = time.time()
        total = fintime - starttime
        await ctx.reply(f"성공 했습니다!\n{round(total)} 초 걸렸네요")

    else:
        await ctx.reply(
            f"틀렸어요...\n정답은 {dap[randomNum]} 이랍니다~\n왜 그런지는 직접 검색 해봐요...")
        return


@app.command(name='구구단퀴즈')
async def timeso(ctx):
    if ctx.author.id in blocked_user:
        return
    times_table = random.randint(2, 9)
    first_number = random.randint(2, 9)
    second_number = random.randint(2, 9)
    answer = times_table * first_number

    await ctx.send(f"{times_table} x {first_number}은?")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    user_answer = await app.wait_for('message', check=check)
    user_answer = int(user_answer.content)

    if user_answer == answer:
        await ctx.send("정답!")
    else:
        await ctx.send(f"땡~\n정답은...\n{answer} 입니다.")


@app.command(aliases=['진우야'])
async def ns1(ctx):
    if ctx.author.id in blocked_user:
        return
    msg = await ctx.reply("https://j.gifs.com/nRkB6W.gif")
    await asyncio.sleep(14.0)
    await ctx.reply("진우야?")
    await ctx.reply("진우야?")
    await ctx.reply("진우야?")
    await ctx.reply("어디 감히 그냥...")
    await msg.edit(
        content=
        "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FclqIxY%2FbtqHO0qNj9n%2F3eHvt2XGK0rgOQDrs7u3J0%2Fimg.jpg"
    )
    await ctx.reply("너는 이제 죽었어...")


@app.command(pass_context=True)
async def 유튜브검색(ctx, keyword):
    if ctx.author.id in blocked_user:
        return
    # Use the YouTube API to search for videos with the given keyword
    response = requests.get('https://www.googleapis.com/youtube/v3/search',
                            params={
                                'part': 'snippet',
                                'q': keyword,
                                'type': 'video',
                                'maxResults': 50,
                                'key':
                                'AIzaSyAXWNgsRRAhmeuc8qEQtMHZUxFLH6tyYBU'
                            })
    data = response.json()

    # Check if 'items' exists in the response
    if 'items' not in data:
        await ctx.send('No videos found.')
        return

    videos = data['items']

    # Pick a random video and send its link to Discord
    video = random.choice(videos)
    await ctx.send(f'https://youtube.com/watch?v={video["id"]["videoId"]}')


#---------------오타쿠---------------


@app.command(name="애니검색")
async def anime000(ctx,
                   *,
                   text,
                   text2=None,
                   text3=None,
                   text4=None,
                   text5=None):
    if ctx.author.id in blocked_user:
        return
    embed = discord.Embed(
        title="로딩중...",
        description=
        f"{ctx.message.author.name}님이 얘기한 {text}{text2 or ''}{text3 or ''}{text4 or ''}{text5 or ''}의 정보를 가지고 오는중 입니다.\n이 현상은 라프텔(API)또는 봇이 문제가 생겼을때 나타나는 것으로.\n주요 원인은 서버가 느릴때 발생합니다.\n 차분히 기다려 주시면 결과가 나올거에요!",
        color=discord.Color.purple())
    embed.set_image(
        url=
        "https://cdn.discordapp.com/attachments/571951027482263572/1076795243560714240/1672818747527.gif"
    )
    msg = await ctx.reply(embed=embed)
    delay = random.randint(1, 10)
    await asyncio.sleep(delay)
    data = await laftel.searchAnime(f'{text} {text2} {text3}')
    data = await laftel.getAnimeInfo(data[0].id)

    if len(data.content) > 300:
        content = f'{data.content[:300]}...'
    else:
        content = data.content
    embed = discord.Embed(title=data.name,
                          url=data.url,
                          description=content,
                          color=discord.Color.purple())
    embed.set_thumbnail(url=data.image)
    embed.add_field(name="별점", value=data.avg_rating, inline=True)
    embed.add_field(name="장르",
                    value=", ".join(str(x) for x in data.genres),
                    inline=True)
    embed.add_field(name="방영분기", value=data.air_year_quarter, inline=True)
    embed.add_field(name="등급", value=data.content_rating, inline=True)
    embed.add_field(name="완결 여부 (F는 미완 T는 완)", value=data.ended, inline=True)
    embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                     icon_url=ctx.message.author.display_avatar)
    await msg.edit(embed=embed)


@app.command(name='일러스트')
async def captcha(ctx):
    if ctx.author.id in blocked_user:
        return
    # API 요청을 보내서 CAPTCHA 이미지를 생성합니다.
    captcha_url = "https://api.junseojjang.com/captcha"
    captcha_response = requests.get(captcha_url)

    if captcha_response.status_code == 200:
        # API 응답에서 key와 이미지 URL을 추출합니다.
        captcha_data = captcha_response.json()
        captcha_key = captcha_data['key']
        captcha_image_url = captcha_data['url']

        # 생성된 CAPTCHA 이미지를 Discord Embed에 포함시켜 채팅에 보여줍니다.
        embed = discord.Embed(
            title="CAPTCHA 이미지",
            description="아래 이미지에 보이는 글자를 30초안에 입력하세요\n(소문자로도 가능)",
            color=0x00ff00)
        embed.set_image(url=captcha_image_url)
        await ctx.send(embed=embed)

        # 사용자의 입력을 대기합니다.
        def check(msg):
            return msg.author == ctx.author and msg.content.lower(
            ) == captcha_key.lower()

        try:
            await app.wait_for('message', check=check, timeout=30.0)
            waifu_url = "https://api.waifu.pics/sfw/waifu"
            waifu_response = requests.get(waifu_url)

            if waifu_response.status_code == 200:
                # Waifu API 응답에서 이미지 URL을 추출합니다.
                waifu_data = waifu_response.json()
                waifu_image_url = waifu_data['url']

                # 무작위로 선택한 Waifu 이미지를 Discord Embed에 포함시켜 채팅에 보여줍니다.
                embed = discord.Embed(title="CAPTCHA 검증 성공!", color=0x00ff00)
                embed.set_image(url=waifu_image_url)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Waifu API 요청 실패...",
                                      description="다시 시도해주세요.",
                                      color=0xff0000)
                await ctx.send(embed=embed)
        except asyncio.TimeoutError:
            embed = discord.Embed(title="CAPTCHA 검증 실패...",
                                  description="다시 시도해주세요.",
                                  color=0xff0000)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="CAPTCHA 생성 실패...",
                              description="다시 시도해주세요.",
                              color=0xff0000)
        await ctx.send(embed=embed)


@app.command(name="뱅드림만화")
async def bang(ctx, *, text=None):
    if ctx.author.id in blocked_user:
        return
    url = "http://bandori.party/api/assets/{}/".format(
        str(random.randint(18, 97)))
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        embed = discord.Embed(colour=discord.Colour.green())
        embed.set_image(url=data["korean_image"])
        embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                         icon_url=ctx.message.author.display_avatar)
        await ctx.reply(embed=embed)


@app.command(pass_context=True)
async def 보컬로이드(ctx):
    if ctx.author.id in blocked_user:
        return
    # Use the YouTube API to search for videos with the given keyword
    keyword = random.choice([
        '初音ミク', '鏡音リン', '巡音ルカ', 'MEIKO', 'KAITO', 'VIRTUAL SINGER', 'Leo/need',
        'MORE MORE JUMP!', 'Vivid BAD SQUAD', 'ワンダーランズ×ショウタイム', '25時、ナイトコードで。'
    ])
    response = requests.get('https://www.googleapis.com/youtube/v3/search',
                            params={
                                'part': 'snippet',
                                'q': keyword,
                                'type': 'video',
                                'maxResults': 50,
                                'key':
                                'AIzaSyAXWNgsRRAhmeuc8qEQtMHZUxFLH6tyYBU'
                            })
    data = response.json()

    # Check if 'items' exists in the response
    if 'items' not in data:
        await ctx.send('No videos found.')
        return

    videos = data['items']

    # Pick a random video and send its link to Discord
    video = random.choice(videos)
    await ctx.send(f'https://youtube.com/watch?v={video["id"]["videoId"]}')


#---------------오타쿠---------------


@app.command()
async def 더하기게임(ctx):
    IMAGES = {
        '0': 'https://i.ibb.co/5nvGhrv/image.gif',
        '1': 'https://i.ibb.co/QNFwN4n/1.gif',
        '2': 'https://i.ibb.co/F690D1J/2.gif',
        '3': 'https://i.ibb.co/CHpMqjT/3.gif',
        '4': 'https://i.ibb.co/C2MXNVz/4.gif',
        '5': 'https://i.ibb.co/C53kvry/5.gif',
        '6': 'https://i.ibb.co/yh0W7bX/6.gif',
        '7': 'https://i.ibb.co/PrNg5xh/7.gif',
        '8': 'https://i.ibb.co/WPj1cJ9/8.gif',
        '9': 'https://i.ibb.co/nP66Y5S/9.gif'
    }
    # 두 개의 랜덤한 숫자 생성
    num1 = str(random.randint(0, 999))
    num2 = str(random.randint(0, 999))

    image1 = Image.open(requests.get(IMAGES[num1[0]], stream=True).raw)
    image2 = Image.open(requests.get(IMAGES[num1[1]], stream=True).raw)
    image3 = Image.open(requests.get(IMAGES[num1[2]], stream=True).raw)
    separator1 = Image.open('separator.png')

    image4 = Image.open(requests.get(IMAGES[num2[0]], stream=True).raw)
    image5 = Image.open(requests.get(IMAGES[num2[1]], stream=True).raw)
    image6 = Image.open(requests.get(IMAGES[num2[2]], stream=True).raw)

    result_image = Image.new(
        'RGB', (image1.width + image2.width + image3.width + separator1.width +
                image4.width + image5.width + image6.width, image1.height))

    result_image.paste(image1, (0, 0))
    result_image.paste(image2, (image1.width, 0))
    result_image.paste(image3, (image1.width + image2.width, 0))
    result_image.paste(separator1,
                       (image1.width + image2.width + image3.width, 0))
    result_image.paste(
        image4,
        (image1.width + image2.width + image3.width + separator1.width, 0))
    result_image.paste(image5, (image1.width + image2.width + image3.width +
                                separator1.width + image4.width, 0))
    result_image.paste(image6,
                       (image1.width + image2.width + image3.width +
                        separator1.width + image4.width + image5.width, 0))

    # 디스코드 채팅에 이미지 전송
    with BytesIO() as image_binary:
        result_image.save(image_binary, 'PNG')
        image_binary.seek(0)
        image_file = discord.File(fp=image_binary, filename='addition.png')

    embed = discord.Embed(title="두 숫자의 합을 입력하세요", color=0x00ff00)
    embed.set_image(url="attachment://addition.png")

    # 사용자 입력 대기
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send(embed=embed, file=image_file)

    # 사용자 입력 확인
    try:
        answer = int((await app.wait_for('message', check=check,
                                         timeout=30.0)).content)
    except asyncio.TimeoutError:
        await ctx.send('시간 초과!')
        return

    # 정답 확인 및 결과 embed 생성
    if answer == int(num1) + int(num2):
        result_embed = discord.Embed(title="정답입니다!", color=0x00ff00)
    else:
        result_embed = discord.Embed(title="오답입니다!", color=0xff0000)

    result_embed.set_image(url="attachment://addition.png")
    await ctx.send(embed=result_embed, file=image_file)


@app.command()
async def 승병조직(ctx):
    mages = ["🧙‍♂️", "🧙‍♀️", "🧙"]
    # 사용자 입력 값이 0 이상 500 이하인지 확인
    while True:
        embed = discord.Embed(description="당신은 승병을 조직하려는거 같은데...\n얼마나 하시려고?",
                              color=0xff0000)
        await ctx.send(embed=embed)
        try:
            message = await app.wait_for('message',
                                         check=lambda m: m.author == ctx.author
                                         and m.channel == ctx.channel,
                                         timeout=30.0)
            num_army = int(message.content)
            if 0 <= num_army <= 500:
                army = ''.join(random.choice(mages) for _ in range(num_army))
                embed = discord.Embed(title=f"너는 {num_army}명의 승병을 조직했다\n축하한다",
                                      description=army,
                                      color=0x00ff00)
                await ctx.send(embed=embed)
                break
            elif num_army > 500:
                embed = discord.Embed(description="승병이 너무 많은거 아니오?",
                                      color=0xff0000)
                embed.set_image(
                    url="https://i.ytimg.com/vi/H5Ycj_jdsco/hqdefault.jpg")
                await ctx.send(embed=embed)
                break
        except asyncio.TimeoutError:
            await ctx.send("")


@app.command()
async def 서버인원수(ctx):
    server = ctx.guild
    bot_count = sum(1 for member in server.members if member.bot)
    user_count = sum(1 for member in server.members if not member.bot)
    embed = discord.Embed(
        title=f"{server.name} 정보",
        description=f"서버 멤버 정보 - 봇: {bot_count}, 사용자: {user_count}",
        color=0x00ff00)
    await ctx.send(embed=embed)


@app.command()
async def 멜론검색(ctx, *, query):
    url = "https://www.melon.com/search/keyword/index.json"
    params = {
        'jscallback': "jQuery19105357803934720518_1603168193882",
        'query': query
    }
    headers = {
        "Referer":
        "http://www.melon.com/index.htm",
        "User-Agent":
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
         "(KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36")
    }

    response = requests.get(url, headers=headers, params=params)
    response = response.text

    json_string = response.replace(params['jscallback'] + '(',
                                   '').replace(');', '')
    result_dict = json.loads(json_string)

    count = 0
    for song in result_dict['SONGCONTENTS']:
        title = song['SONGNAME']
        artist = song['ARTISTNAME']
        link = f"https://www.melon.com/song/detail.htm?songId={song['SONGID']}"

        embed = discord.Embed(title=title,
                              description=f"아티스트: {artist}",
                              url=link)
        await ctx.send(embed=embed)

        count += 1
        if count >= 5:
            break


@app.command()
async def 고양이(ctx):
    cat_image_url = get_random_cat_image_url()
    if cat_image_url:
        embed = discord.Embed()
        embed.set_image(url=cat_image_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Failed to fetch cat image.")


@app.command(aliases=['마작역알람'])
async def mahjong(ctx):
    if ctx.author.id in blocked_user:
        return
    embed = discord.Embed(title="마작", description="마작역알람 모음", color=0x62c1cc)
    #    embed.add_field(name = ".도박", value = "이 게임을 하고 싶다면 일단 #도박장 이라는 체널을 만드세요.\n명령어 보기")
    embed.add_field(name=".1판역", value="ㅈㄱㄴ")
    embed.add_field(name=".2판역", value="ㅈㄱㄴ")
    embed.add_field(name=".3판역", value="ㅈㄱㄴ")
    embed.add_field(name=".6판역과만관", value="ㅈㄱㄴ")
    embed.add_field(name=".역만", value="ㅈㄱㄴ")
    embed.add_field(name=".더블역만", value="ㅈㄱㄴ")
    embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                     icon_url=ctx.message.author.display_avatar)
    await ctx.reply(embed=embed)


@app.command(aliases=['1판역'])
async def mahjong1(ctx):
    if ctx.author.id in blocked_user:
        return
    embed = discord.Embed(title="마작", description="마작역알람 모음", color=0x62c1cc)
    #    embed.add_field(name = ".도박", value = "이 게임을 하고 싶다면 일단 #도박장 이라는 체널을 만드세요.\n명령어 보기")
    embed.add_field(name="리치",
                    value="치, 퐁 깡을 안하고 텐파이를 만들면 가능.\n리치 선언을 한 후 화료하면 성립된다.")
    embed.add_field(
        name="탕야요",
        value=
        f"1,9 숫자패와 자패 없이 만들면 성립된다 \n예시) {man2+man2+man5+man5+man5+tong5+tong6+tong7+sak2+sak3+sak4+sak6+sak7} {sak8}\n[2만2만5만5만5만5통6통7통2삭3삭4삭6삭7삭] [8삭]"
    )
    embed.add_field(
        name="멘젠쯔모",
        value="리치랑 비슷하지만 리치 해도 되고 안해도 가능한역... \n 대신에 , 퐁 깡을 안하고 텐파이를 만드세요")
    embed.add_field(name=".6판역과만관", value="ㅈㄱㄴ")
    embed.add_field(name=".역만", value="ㅈㄱㄴ")
    embed.add_field(name=".더블역만", value="ㅈㄱㄴ")
    embed.set_footer(text=f"{ctx.message.author.name}\
                                   parkbot#9826 \
                                                                                 봇 주인 디스코드 서버: https://bit.ly/3LVxAm1",
                     icon_url=ctx.message.author.display_avatar)
    await ctx.reply(embed=embed)


@app.command(aliases=['마작퀴즈'])
async def mahjongquiz(ctx):
    starttime = time.time()
    answers = [
        '오리가 얼면?', '동그라미 2개, 별이 2개면?', '딸기가 직장을 잃으면?', '소금의 유통기한은?',
        '세상에서 가장 억울한 도형은?', '우유가 넘어지면?', '아몬드가 죽으면?', '소가 죽으면?', '깨가 죽으면?',
        '토끼가 쓰는 빗은?', '세상에서 가장 쉬운 숫자는?', '비가 1시간 동안 내리면?', '바늘만 가지고 다니는 사람은?',
        '콩 한알을 영어로?', '햄버거는의 색깔은?', '토끼가 강한 이유는?', '가장 정의로운 달은?',
        '항상 미안한 동물은?', '가장 인기있는 벌레는?', '둘리가 다니는 고등학교 이름은?', '삶은?', '이별은?',
        '11월에 뱀이랑 벌이 없는 이유는?', '미소의 반대말은?', '모래가 울면?', '얼음이 죽으면?', '사과가 웃으면?',
        '칼이 정색하면?', '바나나가 웃으면?', '아마존의 창업자는?', '차가 울면?', '무가 울면?',
        '거북이가 소화제를 먹은 이유는?', '피자가 놀라면?', '침묵을 영어로?', '가장 폭력적인 동물은?',
        '독재를 다섯글자로?', '살면서 가장 조심해야 할 개 두마리는?', '스님이 못가는 대학교는?', '소가 이기면?',
        '용이 놀라면?', '다정함의 반대말은?', '아이 추워의 반대말은?', '문제투성이인 것은?', '소가 노래하면?',
        '자가용의 반대말은?', '달에서 쓰는 언어는?', '돌잔치를 영어로?', '말이 화가 나면?', '오이가 무를 치면?',
        '있을 수도 있고 없을 수도 있는 섬은?', '논리적인 사람이 총을 쏘면?', '물고기가 싫어하는 물은?', '해가 울면?',
        '선생님이 좋아하는 피자는?', '다이어리를 쓰면 빨리 죽는 이유는?', '개가 벽을 보고 영어로 한 말은?',
        '미국에 비가 내리면?', '왕이 궁에 들어가기 싫을 때 하는 말은?', '세상에서 제일 예쁜 풀은?'
    ]
    dap = [['언덕',
            '덕'], ['영영이별',
                   '덕'], '딸기시럽', '천일염', '원통', '아야', '다이아몬드', '다이소', '주근깨',
           '래빗', '190000', '추적 60분', '실 없는 사람', '원빈', '버건디', '깡과 총이 있어서',
           '악토벌', '오소리', '스타벅스', '빙하타고', '계란', '지구', '노뱀벌', '당기소', '흙흙', '다이빙',
           '풋사과', '검정색', '바나나킥', '아마존', '잉카', '무뚝뚝', '속이 거북해서', '피자헛', '노말',
           '팬다', '나홀로지배', '편견과 선입견', '중앙대', '우승', '띠용', '선택장애', '어른 더워', '시험지',
           '소송', '커용', '문어', '락페스티벌', '마리화나', '오이무침', '아마도', '타당 타당', '그물',
           '해운대', '책피자', 'Die Early', '월월', 'USB', '궁시렁궁시렁', '뷰티풀']

    timers = 30.0
    randomNum = random.randrange(0, len(answers))
    print("랜덤수 값 :" + str(randomNum))
    print(answers[randomNum])
    await ctx.reply(f"{answers[randomNum]}\n뭘까요~\n{timers} 초 안에 맞춰봐용!")

    def is_correct(msg):
        return msg.author == ctx.author

    try:
        guess = await app.wait_for('message', check=is_correct, timeout=timers)
    except asyncio.TimeoutError:
        return await ctx.reply(
            f"시간이 지났어요...\n정답은 {', '.join(dap[randomNum])} 이랍니다~\왜 그런지는 직접 검색 해봐요..."
        )

    if guess.content == dap[randomNum]:
        fintime = time.time()
        total = fintime - starttime
        await ctx.reply(f"성공 했습니다!\n{round(total)} 초 걸렸네요")

    else:
        await ctx.reply(
            f"틀렸어요...\n정답은 {', '.join(dap[randomNum])} 이랍니다~\n왜 그런지는 직접 검색 해봐요..."
        )
        return

@app.command(pass_context=True)
async def join(ctx):
    global voice_client
    channel = ctx.message.author.voice.channel
    voice_client = await channel.connect()

app.run('TOKEN')
