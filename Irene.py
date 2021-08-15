#json = [ 수수료봇 모듈 ]
#random = [ 가위바위보 모듈 ]
#string = [ 니트로 생성기 페이크 ]

# 아래를 참조 하세요. #
#client1 = 핀과 제이크 서버 관리 봇 (setting1.json)
#client2 = 망치 server 관리 봇 (setting2.json)
#client3 = 진주잡것들 (setting3.json)

import discord, asyncio, datetime, pytz, json, random, string #모듈

client1 = discord.Client() #핀과 제이크 서버 관리 봇
client2 = discord.Client() # 망치 server 관리 봇
client3 = discord.Client() # 진주 06 관리 봇

@client1.event # 핀과 제이크 관리 봇 시작 알림 (프린트)
async def on_ready(): 
  async def message(games):
    await client1.wait_until_ready()
    while not client1.is_closed():
        for g in games:
            await client1.change_presence(status = discord.Status.online, activity = discord.Game(g))
            await asyncio.sleep(6) #상태메세지 바뀌는 초 {현재는 6초로 설정되어있습니다.}
  print("\n=============================================")
  print(("""[ 정보 ]\n이름 : {}#2628 \nBot 아이디 : {}""").format(client1.user.name, client1.user.id))
  print("=============================================")
  print(("\n[ 알림 ] {}이 실행되었습니다.\n\nSYSTEM 안내 메세지 :\n채팅 청소 기능 시작 완료!..\n공지 기능 시작 완료!..\n명령어 가이드 시스템 시작 완료!..\n디스코드 서버 모든 유저 언밴 시스템 시작 완료!..\n메세지 삭제/수정 로그 시스템 시작 완료!..\n가위바위보 게임 시작완료!..\n인증 시스템 로딩완료..!\n채널 폭파 기능 로딩완료..!\n\n등록 된 서버\n[ 핀과 제이크와 어드벤처 타임 ]\n[ FIVEM 버닝 서버 ]\n[ 자료실 ]\n[ 망치 서버 ]\n[ 진주잡것들 ]\n\n만든 사람 : 아이린(Irene)\n\n봇 라이센스가 정상적으로 인식되었습니다.\n\n라이센스 키 : WJSM23-23SDXA-SDS-S1658\n\n본 라이센스키는 유출을 절때 금지합니다.").format(client1.user.name))
  #print(("""[ 정보 ]\n[1] Bot Name : {} \n[2] Bot ID : {}""").format(client.user.name, client.user.id))
  await message(['관리 봇 점검 끝','디스코드 관리'])
  #await client1.change_presence(status=discord.Status.online, activity=discord.Game("핀과 제이크 디스코드 관리"))

@client2.event # 망치 server 관리 봇 시작 알림 (프린트)
async def on_ready(): 
  async def message(games):
    await client2.wait_until_ready()

    while not client2.is_closed():
        for g in games:
            await client2.change_presence(status = discord.Status.online, activity = discord.Game(g))
            await asyncio.sleep(6) #상태메세지 바뀌는 초 {현재는 6초로 설정되어있습니다.}
  print("\n=============================================")
  print(("""[ 정보 ]\n이름 : {}#1362 \nBot 아이디 : {}""").format(client2.user.name, client2.user.id))
  print("=============================================")
  print(("\n[ 알림 ] {}이 실행되었습니다.\n\nSYSTEM 안내 메세지 :\n채팅 청소 기능 시작 완료!..\n공지 기능 시작 완료!..\n명령어 가이드 시스템 시작 완료!..\n디스코드 서버 모든 유저 언밴 시스템 시작 완료!..\n메세지 삭제/수정 로그 시스템 시작 완료!..\n\n등록 된 서버\n[ 핀과 제이크와 어드벤처 타임 ]\n[ FIVEM 버닝 서버 ]\n[ 자료실 ]\n[ 망치 서버 ]\n[ 진주잡것들 ]\n\n만든 사람 : 아이린(Irene)").format(client2.user.name))
  #print(("""[ 정보 ]\n[1] Bot Name : {} \n[2] Bot ID : {}""").format(client.user.name, client.user.id))
  await client2.change_presence(status=discord.Status.online, activity=discord.Game("망치 서버 관리"))

@client3.event # 진주 관리 봇 시작 알림 (프린트)
async def on_ready(): 
  async def message(games):
    await client3.wait_until_ready()

    while not client3.is_closed():
        for g in games:
            await client3.change_presence(status = discord.Status.online, activity = discord.Game(g))
            await asyncio.sleep(8) #상태메세지 바뀌는 초 {현재는 6초로 설정되어있습니다.}
  print("\n=============================================")
  print(("""[ 정보 ]\n이름 : {}#1688 \nBot 아이디 : {}""").format(client3.user.name, client3.user.id))
  print("=============================================")
  print(("\n[ 알림 ] {}이 실행되었습니다.\n\nSYSTEM 안내 메세지 :\n채팅 청소 기능 시작 완료!..\n공지 기능 시작 완료!..\n명령어 가이드 시스템 시작 완료!..\n디스코드 서버 모든 유저 언밴 시스템 시작 완료!..\n메세지 삭제/수정 로그 시스템 시작 완료!..\n\n등록 된 서버\n[ 핀과 제이크와 어드벤처 타임 ]\n[ FIVEM 버닝 서버 ]\n[ 자료실 ]\n[ 망치 서버 ]\n[ 진주잡것들 ]\n\n만든 사람 : 아이린(Irene)").format(client3.user.name))
  #print(("""[ 정보 ]\n[1] Bot Name : {} \n[2] Bot ID : {}""").format(client.user.name, client.user.id))
  await message(['!인증 @멘션','만든사람 이원준이다'])    

@client1.event #[ 핀과 제이크 서버 관리 ] 메세지 삭제 로그 봇 소스
async def on_message_delete(message):
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    h = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    bot_logs = '870003755200966707'
    embed = discord.Embed(title='메시지 삭제 알림', colour=discord.Colour.orange())
    embed.add_field(name='사용자', value=f'<@{message.author.id}>({message.author})')
    embed.add_field(name='채널', value=f'<#{message.channel.id}>')
    embed.add_field(name='내용', value=message.content, inline=False)
    embed.add_field(name='사용자 ID • 메시지 ID', value=f"{message.author.id} • {message.id}", inline=False)
    embed.set_footer(text=f"처리 일시 : {y}년 {m}월 {d}일 {h}시 {min}분 • 만든 사람 : ! 아이린#4573", icon_url="https://blog.kakaocdn.net/dn/CCuuf/btqJ4HXd1c1/bCZz9KVs6A79GeXWrTM2u0/img.gif")
    await client1.get_channel(int(bot_logs)).send(embed=embed)    

@client2.event # [ 망치 관리 ] 메세지 삭제 로그 봇 소스
async def on_message_delete(message):
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    h = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    bot_logs = '872898717710155868'
    embed = discord.Embed(title='메시지 삭제 알림', colour=discord.Colour.orange())
    embed.add_field(name='사용자', value=f'<@{message.author.id}>({message.author})')
    embed.add_field(name='채널', value=f'<#{message.channel.id}>')
    embed.add_field(name='내용', value=message.content, inline=False)
    embed.add_field(name='사용자 ID • 메시지 ID', value=f"{message.author.id} • {message.id}", inline=False)
    embed.set_footer(text=f"처리 일시 : {y}년 {m}월 {d}일 {h}시 {min}분 • 만든 사람 : ! 아이린#4573", icon_url="https://blog.kakaocdn.net/dn/CCuuf/btqJ4HXd1c1/bCZz9KVs6A79GeXWrTM2u0/img.gif")  
    await client2.get_channel(int(bot_logs)).send(embed=embed)

@client3.event # [ 진주 관리 ] 메세지 삭제 로그 봇 소스
async def on_message_delete(message):
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    h = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    bot_logs = '875249096473063424'
    embed = discord.Embed(title='메시지 삭제 알림', colour=discord.Colour.orange())
    embed.add_field(name='사용자', value=f'<@{message.author.id}>({message.author})')
    embed.add_field(name='채널', value=f'<#{message.channel.id}>')
    embed.add_field(name='내용', value=message.content, inline=False)
    embed.add_field(name='사용자 ID • 메시지 ID', value=f"{message.author.id} • {message.id}", inline=False)
    embed.set_footer(text=f"처리 일시 : {y}년 {m}월 {d}일 {h}시 {min}분 • 만든 사람 : ! 아이린#4573", icon_url="https://blog.kakaocdn.net/dn/CCuuf/btqJ4HXd1c1/bCZz9KVs6A79GeXWrTM2u0/img.gif")  
    await client3.get_channel(int(bot_logs)).send(embed=embed)        

@client1.event
async def on_connect():
    with open('./setting1.json', 'r') as boo:
        data = json.load(boo)
    setting = data['percent']

    if not setting.isdecimal() or int(setting) > 100: #오류가 나면 콘솔알림 코드 
        print(f'[ 수수료 봇 오류 알림 ] 현재 설정된 수수료가 잘못 되었습니다! 클라이언트 1 코드에서 문제가 발생 하였습니다, {setting}은/는 불가능한 설정 값 입니다.\n[ 수수료 봇 오류 알림 ] Irene Bot 파일에서 setting1.json 파일을 수정해주세요!!\n[ 수수료 봇 오류 알림 ] 최고 설정값은 100% 입니다. 아래에 오류 메세지가 전송됩니다.\n[알림] 오류가 없는 봇은 정상 실행이 됩니다.')
        time.sleep(3)
        await client1.logout()
        sys.exit()
    print(f"\n[ 수수료 BOT ] 수수료 봇 시스템이 정상적으로 시작이 되었습니다!\n현재 설정된 수수료는 {setting}% 입니다.(핀과 제이크 디스코드)") #정 상 실 행

@client2.event
async def on_connect():
    with open('./setting2.json', 'r') as boo:
        data = json.load(boo)
    setting = data['percent']

    if not setting.isdecimal() or int(setting) > 100: #오류가 나면 콘솔알림 코드 
        print(f'[ 수수료 봇 오류 알림 ] 현재 설정된 수수료가 잘못 되었습니다! 클라이언트 2 코드에서 문제가 발생 하였습니다, {setting}은/는 불가능한 설정 값 입니다.\n[ 수수료 봇 오류 알림 ] Irene Bot 파일에서 setting2.json 파일을 수정해주세요!!\n[ 수수료 봇 오류 알림 ] 최고 설정값은 100% 입니다. 아래에 오류 메세지가 전송됩니다.\n[알림] 오류가 없는 봇은 정상 실행이 됩니다.')
        time.sleep(3)
        await client2.logout()
        sys.exit()
    print(f"\n[ 수수료 BOT ] 수수료 봇 시스템이 정상적으로 시작이 되었습니다!\n현재 설정된 수수료는 {setting}% 입니다.(망치 SERVER 디스코드)") #정 상 실 행

@client3.event
async def on_connect():
    with open('./setting3.json', 'r') as boo:
        data = json.load(boo)
    setting = data['percent']

    if not setting.isdecimal() or int(setting) > 100: #오류가 나면 콘솔알림 코드 
        print(f'[ 수수료 봇 오류 알림 ] 현재 설정된 수수료가 잘못 되었습니다! 클라이언트 3 코드에서 문제가 발생 하였습니다, {setting}은/는 불가능한 설정 값 입니다.\n[ 수수료 봇 오류 알림 ] Irene Bot 파일에서 setting3.json 파일을 수정해주세요!!\n[ 수수료 봇 오류 알림 ] 최고 설정값은 100% 입니다. 아래에 오류 메세지가 전송됩니다.\n[알림] 오류가 없는 봇은 정상 실행이 됩니다.')
        time.sleep(3)
        await client3.logout()
        sys.exit()
    print(f"\n[ 수수료 BOT ] 수수료 봇 시스템이 정상적으로 시작이 되었습니다!\n현재 설정된 수수료는 {setting}% 입니다.(진주 잡것들 디스코드)") #정 상 실 행            

@client1.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="오류!!", description="오류가 발생했습니다.", color=0xFF0000)
    embed.add_field(name="상세", value=f"{error}")
    
    await ctx.send(embed=embed)

@client2.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="오류!!", description="오류가 발생했습니다.", color=0xFF0000)
    embed.add_field(name="상세", value=f"{error}")
    
    await ctx.send(embed=embed)

@client3.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="오류!!", description="오류가 발생했습니다.", color=0xFF0000)
    embed.add_field(name="상세", value=f"{error}")
    
    await ctx.send(embed=embed)

@client1.event
async def on_message(message):
    if message.content.startswith ("!공지"): # 명령어,공지사항 코드
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client1.get_channel(857613103256698880) # 공지 올라갈 채널 아이디
            embed = discord.Embed(title="**⭐ 핀과 제이크 서버 공지사항 ⭐**", description="공지사항이 등록되었습니다! 확인해주세요.\n━━━━━━━━━━━━━━━━━━━\n{}\n\n".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xf80909)
            embed.set_footer(text="Made by : ! 아이린#4573 | 담당 관리자 : {}".format(message.author), icon_url="https://i.imgur.com/3QPa9gQ.gif")
            embed.set_thumbnail(url="https://i.imgur.com/3QPa9gQ.gif")
            await channel.send ("@everyone", embed=embed)
            #await message.author.send("**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 응 아니야 ,공지 띄울려 하지마 ㅋ (관리자 권한만 사용 가능합니다.) ㅣ [ 공지를 시도 하였습니다. 해당 메세지는 관리자 방에 로그로 전송됩니다. ]".format(message.author.mention))
    
    if message.content.startswith('!니트로'):
        ranNitro = ""
        for i in range(0, 16):
            ranNitro += str(random.choice(string.ascii_letters))
            NitroEmbed = discord.Embed(title='니트로 생성기', description='https://discord.gift/' + ranNitro)
            embed = discord.Embed(title='니트로 생성 시스템', description='응 구라야!~ 그걸 속냐! ㅋ')
        await message.author.send(embed=embed)
        await message.author.send(embed=NitroEmbed)
        await message.channel.send("개인DM을 확인해주세요.")

    if message.content.startswith('!폭파'):
        if message.author.guild_permissions.ban_members:
            aposition = message.channel.position
            new = await message.channel.clone()
            await message.channel.delete()
            await new.edit(position=aposition)

            embed = discord.Embed(title='알림 : 해당 채널의 채팅이 모두 폭파 되었습니다.', colour=discord.Colour.red())
            embed.set_image(url='https://media.giphy.com/media/HhTXt43pk1I1W/giphy.gif')
            await new.send(embed=embed)
        else:
            await message.channel.send('**[ 알림 ]**\n**```당신은 채팅 폭파 명령어 사용권한이 없습니다.```**')
    
    if message.content.startswith ("!청소"): #청소 기능 코드
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="**```디스코드 채팅 {}개가 관리자 {}님의 요청으로 인해 삭제 처리가 되었습니다.```**".format(amount, message.author), color=0xf80909)
            embed.set_footer(text="Made by : ! 아이린#4573", icon_url="https://i.imgur.com/3QPa9gQ.gif")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 응 안돼 ,채팅 삭제 할려 하지마 ㅋ (관리자 권한만 사용 가능합니다.) ㅣ Made by : ! 아이린#4573".format(message.author.mention))  

    if message.content.startswith ("!인증 "):
        #if message.author.guild_permissions.administrator:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xA566FF)
            embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            #embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="Bot Made by : ! 아이린#4573", icon_url="https://i.imgur.com/3QPa9gQ.gif")
            await message.channel.send (embed=embed)
            await message.author.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '【🧡】ㅣ유저')
            await user.add_roles(role)

        #else:
            #await message.delete()
            #await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))

    if message.content == "!명령어": # 해당 명령어를 치면 아래의 임베드 코드를 불러옵니다.
        await message.delete() # 명령어를 사용하면 입력한 명령어가 제거 되고 아래의 코드를 불러옵니다.
        if not message.author.guild_permissions.administrator: return

        embed = discord.Embed(title="핀과 제이크 관리 봇 명령어 안내 입니다.", description="명령어 분류 : 디스코드 사용 안내",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xFF9436)
        
        embed.add_field(name="디스코드 공지사항 시스템 (관리자 전용)[!공지 할말]", value="**```!공지 할말 을 입력하시면 공지사항 채널에 공지가 올라옵니다.```**", inline=False)
        embed.add_field(name="채팅 청소 시스템 (관리자 전용)[!청소 갯수]", value="**```!청소 갯수를 입력 하시면 됩니다.\n예를 들어 !청소 10 하면 해당 채널의 채팅을 10개 제거합니다.```**", inline=False)
        
        embed.add_field(name="디스코드 모든유저 차단 해제 시스템 (관리자 전용)[!언밴]", value="```diff\n!언밴 명령어를 치시면 디스코드 모든 유저를 차단 해제 합니다.\n- 해당 명령어를 바로 치면 즉시 모든유저 차단이 풀리므로 절때 장난 치시면 안됩니다.!```", inline=False)
        embed.add_field(name="!수수료 숫자 (관리자 전용) [!수수료]", value="```!수수료를 치시면 저장되어 있는 수수료의 값을 제외한 값이 나옵니다.```", inline=False)
        
        embed.add_field(name="!수수료 수정 또는 !수정 (관리자 전용) [!수수료 수정,!수정]", value="```!수수료 수정이나 !수정을 입력하시면 수수료 값이 변경됩니다. ex)!수정 20 또는 !수수료 수정 30```", inline=False)
        embed.add_field(name="!폭파 (관리자 전용)", value="```!폭파를 입력하시면 해당 채널의 채팅이 모두 삭제됩니다.```", inline=False)

        #embed.add_field(name="인게임 데이터베이스 봇 도움 명령어 (서버 관리)", value="```~명령어```", inline=False)
        #embed.add_field(name="관리 봇 도움 명령어 (서버 관리)", value="```#명령어```", inline=False)

        #embed.add_field(name="서버 리붓 명령어 (서버 관리)", value="```!리붓 사유 를 적으시면 서버 리붓이 됩니다.```", inline=False)

        embed.add_field(name="\n\n안내", value="```diff\n- 해당 봇 소스는 FIVEM BURNING서버 , 핀과 제이크와 어드벤처 서버, 망치 server 에만 소유 중임을 알립니다.```", inline=False)
        embed.set_footer(text="Copyright © Wonjun. All rights reserved ㅣ 사용해주셔서 감사합니다!", icon_url="https://i.imgur.com/3QPa9gQ.gif")
        embed.set_thumbnail(url="https://i.imgur.com/3QPa9gQ.gif")

        await message.channel.send (embed=embed)

    if message.content == '!언밴': #디코서버 모든유저 차단 해제 코드
        if not message.author.guild_permissions.administrator:
            return
        bans = await message.guild.bans()
        lists = ["{0.id}".format(entry.user) for entry in bans]

        for i in lists:
            a = await client1.fetch_user(i)
            await message.guild.unban(a)
            print(f"[ 차단 해제 알림 ] {a} 님이 핀과 제이크 서버의 차단 해제가 정상적으로 완료되었습니다.")
            await message.channel.send(f"** [ 알림 ] ** ```{a} 님이 언밴 시스템에 의해 정상적으로 차단이 해제 되었습니다.```")

    if message.content == "정순교": # 메세지 감지
        await message.channel.send ("<@771651270435405824> 병신 새끼 급발진 장인에다가 찬희 짱친임")
    if message.content == "/디스코드1": # 메세지 감지
        await message.channel.send ("핀과 제이크와 어드벤처 타임 서버 영구주소 입니다. ㅣ discord.gg/cuDeSxu9GK")
    if message.content == "/디스코드": # 메세지 감지
        await message.channel.send ("{} ㅣ 핀과 제이크와 어드벤처 타임 서버 영구주소 입니다. ㅣ discord.gg/cuDeSxu9GK".format(message.author.mention))        
    if message.content == "정재준": # 메세지 감지
        await message.channel.send ("<@515525168165158943> PC방 구석탱이에서 사타구니 벅벅 긁으면서 누네띠네 먹을려는데 누네띠네 살 돈이 없어서 친구한테 돈 보내달라고 한새끼ㅋ")    
    if message.content == "이렐리아": # 메세지 감지
        await message.channel.send ("{} ㅣ 이렐리아 정보 입니다. (선호하는 라인 : 미드,탑) https://www.op.gg/champion/irelia/statistics/top/build (출처 : OP.GG)".format(message.author.mention))
    if message.content == "제드": # 메세지 감지
        await message.channel.send ("제드의 정보를 전송 하였습니다. 개인 디엠을 확인 해주세요.")
    if message.content == "제드": # 메세지 감지
        await message.author.send ("{} ㅣ 제드 정보 입니다. (선호하는 라인 : 미드) https://www.op.gg/champion/zed/statistics/mid/build (출처 : OP.GG)".format(message.author.mention))    
    if message.content == "야스오": # 메세지 감지
        await message.channel.send ("{} ㅣ 야스오 정보 입니다. (선호하는 라인 : 모든 라인) https://www.op.gg/champion/yasuo/statistics/mid/build (출처 : OP.GG)".format(message.author.mention))
    if message.content == "아칼리": # 메세지 감지
        await message.channel.send ("{} ㅣ 아칼리 챔피언 정보 입니다. (선호하는 라인 : 미드,탑) https://www.op.gg/champion/akali/statistics/mid/build (출처 : OP.GG)".format(message.author.mention))    
    if message.content == "야릇한 야스오": # 메세지 감지
        await message.channel.send ("{} ㅣ [리그 오브 레전드] 야릇한 야스오 플레이어의 인게임 정보 입니다.https://www.op.gg/summoner/userName=%EC%95%BC%EB%A6%87%ED%95%9C+%EC%95%BC%EC%8A%A4%EC%98%A4 (출처 : OP.GG)".format(message.author.mention))
    if message.content == "야릇한 루시안": # 메세지 감지
        await message.channel.send ("{} ㅣ [리그 오브 레전드] 야릇한 루시안 플레이어의 인게임 정보 입니다. https://www.op.gg/summoner/userName=%EC%95%BC%EB%A6%87%ED%95%9C+%EB%A3%A8%EC%8B%9C%EC%95%88 (출처 : OP.GG)".format(message.author.mention))                 
    if message.content == "다원카이저": # 메세지 감지
        await message.channel.send ("{} ㅣ [리그 오브 레전드] 다원카이저 플레이어의 인게임 정보 입니다. https://www.op.gg/summoner/userName=%EB%8B%A4%EC%9B%90%EC%B9%B4%EC%9D%B4%EC%A0%80 (출처 : OP.GG)".format(message.author.mention))  
    if message.content == "야릇한 클레드": # 메세지 감지
        await message.channel.send ("{} ㅣ [리그 오브 레전드] 야릇한 클레드 플레이어의 인게임 정보 입니다. https://www.op.gg/summoner/userName=%EC%95%BC%EB%A6%87%ED%95%9C+%ED%81%B4%EB%A0%88%EB%93%9C (출처 : OP.GG)".format(message.author.mention))
        
    if message.content.startswith("!수수료") and not message.content.startswith("!수수료수정"):
        await message.delete() # 명령어를 사용하면 입력한 명령어가 제거 되고 아래의 코드를 불러옵니다.
        with open('./setting1.json', 'r') as boo:
            data = json.load(boo)
        setting = data['percent']

        try:
            amount = message.content.split(" ")[1]
        except IndexError:
            await message.channel.send(f'{message.author.mention} 값이 설정되지 않았습니다')
            return

        if not amount.isdecimal():
            await message.channel.send(f'{message.author.mention} 값은 숫자가 아닙니다')
            return

        result = int(amount) * (100-int(setting)) / 100
        result = round(result)
        await message.channel.send(f'{message.author.mention}, **```cs\n{amount}원의 수수료 {setting}% 를 제외한 값은 {result}원입니다.\n```**\n**[ 현재 수수료 저장되어 있는 값은 {setting}% 입니다. ]**')

    if message.content.startswith('!수수료 수정') or message.content.startswith('!수정'):
        if message.author.guild_permissions.manage_messages:
            try:
                edit_amount = message.content.split(" ")[1]
            except:
                embed = discord.Embed(title='!수수료수정 [숫자]', description='EX)!수수료수정 20')
                await message.channel.send(embed=embed)
                return

            if not edit_amount.isdecimal() or int(edit_amount) > 100:
                embed = discord.Embed(title='!수수료수정 [숫자]', description='EX)!수수료수정 20')
                await message.channel.send(embed=embed)
                return

            with open('./setting1.json', 'r') as boo:
                data = json.load(boo)
            data['percent'] = edit_amount
            with open('./setting1.json', 'w', encoding='utf-8') as making:
                json.dump(data, making, indent="\t")
            s = data['percent']
            await message.channel.send(f'수수료가 {s}%로 수정/저장되었습니다')

    if message.content == "!핑":
        la = client1.latency
        await message.channel.send(f'{message.author.mention}님ㅣ🏓현재 {client1.user.name}의 SERVER 핑은 `{str(round(la * 1000))}ms`입니다. ㅣ **해당 명령어는 !핑 입니다.**')

    if message.content == "/가위" or message.content == "/바위" or message.content == "/보" or message.content == "/찌" or message.content == "/묵" or message.content == "/빠": #가위바위보 기능
        bot_response = random.randint(1, 3)
        if bot_response == 1:
            if message.content == "가위":
                await message.channel.send(embed=discord.Embed(title="아쉽게도 이번판은 비겼습니다..", colour=discord.Color.yellow()))
            elif message.content == "바위":
                await message.channel.send(embed=discord.Embed(title="제가 졌습니다, 당신이 승리 하였습니다!", colour=discord.Color.green()))
            else:
                await message.channel.send(embed=discord.Embed(title="제가 이겼습니다, 당신은 패배 하였습니다.ㅋ", colour=discord.Color.red()))

        elif bot_response == 2:
            if message.content == "가위":
                await message.channel.send(embed=discord.Embed(title="제가 이겼습니다, 당신은 패배 하였습니다.", colour=discord.Color.red()))
            elif message.content == "바위":
                await message.channel.send(embed=discord.Embed(title="아쉽게도 이번판은 비겼습니다.", colour=discord.Color.yellow()))
            else:
                await message.channel.send(embed=discord.Embed(title="제가 졌습니다, 당신이 승리하였습니다!", colour=discord.Color.green()))

        elif bot_response == 3:
            if message.content == "가위":
                await message.channel.send(embed=discord.Embed(title="제가 졌습니다, 당신이 승리하였습니다!", colour=discord.Color.green()))
            elif message.content == "바위":
                await message.channel.send(embed=discord.Embed(title="제가 이겼습니다, 당신은 패배 하였습니다. ㅋ", colour=discord.Color.red()))
            else:
                await message.channel.send(embed=discord.Embed(title="아쉽게도 이번판은 비겼습니다..", colour=discord.Color.yellow()))

    #if message.content in "<@!715474124851511337>" or message.content in "<@715474124851511337>": #! 아이린#4573
            #await message.channel.send("**[ ! 아이린#4573 알림 ]** ㅣ {} 왜 멘션하는거야 태그 하지마 셰키야!".format(message.author.mention))
@client2.event
async def on_message(message):
    if message.content.startswith ("!공지"): # 명령어,공지사항 코드
        await message.delete()
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client2.get_channel(872587833242681434) # 공지 올라갈 채널 아이디
            embed = discord.Embed(title="**⭐ 망치 서버 공지사항 ⭐**", description="공지사항이 등록되었습니다! 확인해주세요.\n━━━━━━━━━━━━━━━━━━━\n{}\n\n".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xf80909)
            embed.set_footer(text="Made by : ! 아이린#4573 | 담당 관리자 : {}".format(message.author), icon_url="https://i.imgur.com/3QPa9gQ.gif")
            embed.set_thumbnail(url="https://i.imgur.com/3QPa9gQ.gif")
            await channel.send ("@everyone", embed=embed)
            #await message.author.send("**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 응 아니야 ,공지 띄울려 하지마 ㅋ (관리자 권한만 사용 가능합니다.) ㅣ Made by : ! 아이린#4573".format(message.author.mention))
    
    if message.content.startswith ("!청소"): #청소 기능 코드
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="디스코드 채팅 {}개가\n 관리자 {}님의 요청으로 인해 삭제 처리가 되었습니다.".format(amount, message.author), color=0xf80909)
            embed.set_footer(text="Made by : ! 아이린#4573", icon_url="https://i.imgur.com/3QPa9gQ.gif")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 응 안돼 ,채팅 삭제 할려 하지마 ㅋ (관리자 권한만 사용 가능합니다.) ㅣ Made by : ! 아이린#4573".format(message.author.mention))

    if message.content.startswith ("!인증 "):
        #if message.author.guild_permissions.administrator:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xA566FF)
            embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            #embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="디스코드 인증 시스템", icon_url="https://i.imgur.com/3QPa9gQ.gif")
            await message.channel.send (embed=embed)
            await message.author.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '⭐ㆍUSER')
            await user.add_roles(role)

        #else:
            #await message.delete()
            #await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))

    if message.content == "!명령어": # 해당 명령어를 치면 아래의 임베드 코드를 불러옵니다.
        await message.delete() # 명령어를 사용하면 입력한 명령어가 제거 되고 아래의 코드를 불러옵니다.
        if not message.author.guild_permissions.administrator: return #관리자 권한 아닌사람이 입력하면 자동으로 입력한 글 사라지는 코드 입니다.
        embed = discord.Embed(title="망치 서버 관리 봇 명령어 안내 입니다.", description="명령어 분류 : 디스코드 사용 안내",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xFF9436)

        embed.add_field(name="디스코드 공지사항 시스템 (관리자 전용)[!공지 할말]", value="**```!공지 할말 을 입력하시면 공지사항 채널에 공지가 올라옵니다.```**", inline=False)
        embed.add_field(name="채팅 청소 시스템 (관리자 전용)[!청소 갯수]", value="**```!청소 갯수를 입력 하시면 됩니다.\n예를 들어 !청소 10 하면 해당 채널의 채팅을 10개 제거합니다.```**", inline=False)
        embed.add_field(name="디스코드 모든유저 차단 해제 시스템 (관리자 전용)[!언밴]", value="```diff\n!언밴 명령어를 치시면 디스코드 모든 유저를 차단 해제 합니다.\n- 해당 명령어를 바로 치면 즉시 모든유저 차단이 풀리므로 절때 장난 치시면 안됩니다.!```", inline=False)

        embed.add_field(name="!수수료 숫자 (관리자 전용) [!수수료]", value="```!수수료를 치시면 저장되어 있는 수수료의 값을 제외한 값이 나옵니다.```", inline=False)
        embed.add_field(name="!수수료 수정 또는 !수정 (관리자 전용) [!수수료 수정,!수정]", value="```!수수료 수정이나 !수정을 입력하시면 수수료 값이 변경됩니다. ex)!수정 20 또는 !수수료 수정 30```", inline=False)
        #embed.add_field(name="서버 점검/오프 디스코드 알림 (관리자 전용) [?!서버점검]", value="```?!서버점검 을 치면 서버 점검/오프 알림을 해당 채널에 점검/오프 알림이 뜹니다.```", inline=False)

        #embed.add_field(name="인게임 데이터베이스 봇 도움 명령어 (서버 관리)", value="```~명령어```", inline=False)
        #embed.add_field(name="관리 봇 도움 명령어 (서버 관리)", value="```#명령어```", inline=False)

        #embed.add_field(name="서버 리붓 명령어 (서버 관리)", value="```!리붓 사유 를 적으시면 서버 리붓이 됩니다.```", inline=False)

        embed.add_field(name="\n\n안내", value="```diff\n- 해당 봇 소스는 FIVEM BURNING서버 , 핀과 제이크와 어드벤처 서버 , 망치 Server에 소유 중임을 알립니다.```", inline=False)

        embed.set_footer(text="Made by : ! 스톤#4573 ㅣ Copyright © Wonjun. All rights reserved ㅣ 사용해주셔서 감사합니다!", icon_url="https://i.imgur.com/3QPa9gQ.gif")
        embed.set_thumbnail(url="https://i.imgur.com/3QPa9gQ.gif")

        await message.channel.send (embed=embed)

    if message.content == "!핑":
        la = client1.latency
        await message.channel.send(f'{message.author.mention}님ㅣ🏓현재 관리 봇의 SERVER 핑은 `{str(round(la * 1000))}ms`입니다. ㅣ **해당 명령어는 !핑 입니다.**')

    if message.content == "/가위" or message.content == "/바위" or message.content == "/보" or message.content == "/찌" or message.content == "/묵" or message.content == "/빠": #가위바위보 기능
        bot_response = random.randint(1, 3)
        if bot_response == 1:
            if message.content == "가위":
                await message.channel.send(embed=discord.Embed(title="아쉽게도 이번판은 비겼습니다..", colour=discord.Color.yellow()))
            elif message.content == "바위":
                await message.channel.send(embed=discord.Embed(title="제가 졌습니다, 당신이 승리 하였습니다!", colour=discord.Color.green()))
            else:
                await message.channel.send(embed=discord.Embed(title="제가 이겼습니다, 당신은 패배 하였습니다.ㅋ", colour=discord.Color.red()))

        elif bot_response == 2:
            if message.content == "가위":
                await message.channel.send(embed=discord.Embed(title="제가 이겼습니다, 당신은 패배 하였습니다.", colour=discord.Color.red()))
            elif message.content == "바위":
                await message.channel.send(embed=discord.Embed(title="아쉽게도 이번판은 비겼습니다.", colour=discord.Color.yellow()))
            else:
                await message.channel.send(embed=discord.Embed(title="제가 졌습니다, 당신이 승리하였습니다!", colour=discord.Color.green()))

        elif bot_response == 3:
            if message.content == "가위":
                await message.channel.send(embed=discord.Embed(title="제가 졌습니다, 당신이 승리하였습니다!", colour=discord.Color.green()))
            elif message.content == "바위":
                await message.channel.send(embed=discord.Embed(title="제가 이겼습니다, 당신은 패배 하였습니다. ㅋ", colour=discord.Color.red()))
            else:
                await message.channel.send(embed=discord.Embed(title="아쉽게도 이번판은 비겼습니다..", colour=discord.Color.yellow()))

    if message.content == '!언밴': #디코서버 모든유저 차단 해제 코드
        if not message.author.guild_permissions.administrator:
            return
        bans = await message.guild.bans()
        lists = ["{0.id}".format(entry.user) for entry in bans]

        for i in lists:
            a = await client2.fetch_user(i)
            await message.guild.unban(a)
            print(f"[ 차단 해제 알림 ] {a} 님이 망치 서버의 차단 해제가 정상적으로 완료되었습니다.")
            await message.channel.send(f"** [ 알림 ] ** ```{a} 님이 언밴 시스템에 의해 정상적으로 차단이 해제 되었습니다.```")
        
    if message.content.startswith("!수수료") and not message.content.startswith("!수수료수정"):
        await message.delete() # 명령어를 사용하면 입력한 명령어가 제거 되고 아래의 코드를 불러옵니다.
        with open('./setting2.json', 'r') as boo:
            data = json.load(boo)
        setting = data['percent']

        try:
            amount = message.content.split(" ")[1]
        except IndexError:
            await message.channel.send(f'{message.author.mention} 값이 설정되지 않았습니다')
            return

        if not amount.isdecimal():
            await message.channel.send(f'{message.author.mention} 값은 숫자가 아닙니다')
            return
        result = int(amount) * (100-int(setting)) / 100
        result = round(result)
        await message.channel.send(f'{message.author.mention}, **```cs\n{amount}원의 수수료 {setting}% 를 제외한 값은 {result}원입니다.\n```**\n**[ 현재 수수료 저장되어 있는 값은 {setting}% 입니다. ]**')

    if message.content.startswith('!수수료 수정') or message.content.startswith('!수정'):
        if message.author.guild_permissions.manage_messages:
            try:
                edit_amount = message.content.split(" ")[1]
            except:
                embed = discord.Embed(title='!수수료수정 [숫자]', description='')
                await message.channel.send(embed=embed)
                return

            if not edit_amount.isdecimal() or int(edit_amount) > 100:
                embed = discord.Embed(title='!수수료수정 [숫자]', description='')
                await message.channel.send(embed=embed)
                return

            with open('./setting2.json', 'r') as boo:
                data = json.load(boo)
            data['percent'] = edit_amount
            with open('./setting2.json', 'w', encoding='utf-8') as making:
                json.dump(data, making, indent="\t")
            s = data['percent']
            await message.channel.send(f'수수료가 {s}%로 수정/저장되었습니다')

    if message.content == "!핑":
        await message.delete() # 명령어를 사용하면 입력한 명령어가 제거 되고 아래의 코드를 불러옵니다.
        la = client2.latency
        await message.channel.send(f'{message.author.mention}님ㅣ🏓{client2.user.name}의 SERVER 핑은 `{str(round(la * 1000))}ms`입니다. ㅣ **해당 명령어는 !핑 입니다.**')

@client3.event
async def on_message(message):
    if message.content.startswith ("!공지"): # 명령어,공지사항 코드
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client3.get_channel(847158495819989022) # 공지 올라갈 채널 아이디
            embed = discord.Embed(title="**⭐ 진주 잡것들 서버 공지사항 ⭐**", description="공지사항이 등록되었습니다! 확인해주세요.\n━━━━━━━━━━━━━━━━━━━\n{}\n\n".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xf80909)
            embed.set_footer(text="Made by : ! 아이린#4573 | 담당 관리자 : {}".format(message.author), icon_url="https://i.imgur.com/3QPa9gQ.gif")
            embed.set_thumbnail(url="https://i.imgur.com/3QPa9gQ.gif")
            await channel.send ("@everyone", embed=embed)
            #await message.author.send("**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 응 아니야 ,공지 띄울려 하지마 ㅋ (관리자 권한만 사용 가능합니다.) ㅣ [ 공지를 시도 하였습니다. 해당 메세지는 관리자 방에 로그로 전송됩니다. ]".format(message.author.mention))
    
    if message.content.startswith ("!청소"): #청소 기능 코드
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="**```디스코드 채팅 {}개가 관리자 {}님의 요청으로 인해 삭제 처리가 되었습니다.```**".format(amount, message.author), color=0xf80909)
            embed.set_footer(text="Made by : ! 아이린#4573", icon_url="https://i.imgur.com/3QPa9gQ.gif")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 응 안돼 ,채팅 삭제 할려 하지마 ㅋ (관리자 권한만 사용 가능합니다.) ㅣ Made by : ! 아이린#4573".format(message.author.mention))  

    if message.content.startswith ("!인증 "):
        #if message.author.guild_permissions.administrator:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            #embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="Bot Made by : ! 아이린#4573", icon_url="https://i.imgur.com/3QPa9gQ.gif")
            await message.channel.send (embed=embed)
            await message.author.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '진주잡것들')
            await user.add_roles(role)

        #else:
            #await message.delete()
            #await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))

    if message.content == "!명령어": # 해당 명령어를 치면 아래의 임베드 코드를 불러옵니다.
        await message.delete() # 명령어를 사용하면 입력한 명령어가 제거 되고 아래의 코드를 불러옵니다.
        if not message.author.guild_permissions.administrator: return #관리자 권한 아닌사람이 입력하면 자동으로 입력한 글 사라지는 코드 입니다.
        embed = discord.Embed(title="진주 관리 봇 명령어 안내 입니다.", description="명령어 분류 : 디스코드 사용 안내",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xFF9436)

        embed.add_field(name="디스코드 공지사항 시스템 (관리자 전용)[!공지 할말]", value="**```!공지 할말 을 입력하시면 공지사항 채널에 공지가 올라옵니다.```**", inline=False)
        embed.add_field(name="채팅 청소 시스템 (관리자 전용)[!청소 갯수]", value="**```!청소 갯수를 입력 하시면 됩니다.\n예를 들어 !청소 10 하면 해당 채널의 채팅을 10개 제거합니다.```**", inline=False)
        embed.add_field(name="디스코드 모든유저 차단 해제 시스템 (관리자 전용)[!언밴]", value="```diff\n!언밴 명령어를 치시면 디스코드 모든 유저를 차단 해제 합니다.\n- 해당 명령어를 바로 치면 즉시 모든유저 차단이 풀리므로 절때 장난 치시면 안됩니다.!```", inline=False)

        embed.add_field(name="!수수료 숫자 (관리자 전용) [!수수료]", value="```!수수료를 치시면 저장되어 있는 수수료의 값을 제외한 값이 나옵니다.```", inline=False)
        embed.add_field(name="!수수료 수정 또는 !수정 (관리자 전용) [!수수료 수정,!수정]", value="```!수수료 수정이나 !수정을 입력하시면 수수료 값이 변경됩니다. ex)!수정 20 또는 !수수료 수정 30```", inline=False)
        #embed.add_field(name="서버 점검/오프 디스코드 알림 (관리자 전용) [?!서버점검]", value="```?!서버점검 을 치면 서버 점검/오프 알림을 해당 채널에 점검/오프 알림이 뜹니다.```", inline=False)

        #embed.add_field(name="인게임 데이터베이스 봇 도움 명령어 (서버 관리)", value="```~명령어```", inline=False)
        #embed.add_field(name="관리 봇 도움 명령어 (서버 관리)", value="```#명령어```", inline=False)

        #embed.add_field(name="서버 리붓 명령어 (서버 관리)", value="```!리붓 사유 를 적으시면 서버 리붓이 됩니다.```", inline=False)

        embed.add_field(name="\n\n안내", value="```diff\n- 해당 봇 소스는 FIVEM BURNING서버 , 핀과 제이크와 어드벤처 서버, 망치 server, 진주잡것들 서버에만 소유 중임을 알립니다.```", inline=False)

        embed.set_footer(text="Copyright © Wonjun. All rights reserved ㅣ 사용해 주셔서 감사합니다!", icon_url="https://i.imgur.com/3QPa9gQ.gif")
        embed.set_thumbnail(url="https://i.imgur.com/3QPa9gQ.gif")

        await message.channel.send (embed=embed)

    if message.content == '!언밴': #디코서버 모든유저 차단 해제 코드
        if not message.author.guild_permissions.administrator:
            return
        bans = await message.guild.bans()
        lists = ["{0.id}".format(entry.user) for entry in bans]

        for i in lists:
            a = await client3.fetch_user(i)
            await message.guild.unban(a)
            print(f"[ 차단 해제 알림 ] {a} 님이 진주잡것들 서버의 차단 해제가 정상적으로 완료되었습니다.")
            await message.channel.send(f"** [ 알림 ] ** ```{a} 님이 언밴 시스템에 의해 정상적으로 차단이 해제 되었습니다.```")
        
    if message.content.startswith("!수수료") and not message.content.startswith("!수수료수정"):
        await message.delete() # 명령어를 사용하면 입력한 명령어가 제거 되고 아래의 코드를 불러옵니다.
        with open('./setting3.json', 'r') as boo:
            data = json.load(boo)
        setting = data['percent']

        try:
            amount = message.content.split(" ")[1]
        except IndexError:
            await message.channel.send(f'{message.author.mention} 값이 설정되지 않았습니다')
            return

        if not amount.isdecimal():
            await message.channel.send(f'{message.author.mention} 값은 숫자가 아닙니다')
            return

        result = int(amount) * (100-int(setting)) / 100
        result = round(result)
        await message.channel.send(f'{message.author.mention}, **```cs\n{amount}원의 수수료 {setting}% 를 제외한 값은 {result}원입니다.\n```**\n**[ 현재 수수료 저장되어 있는 값은 {setting}% 입니다. ]**')

    if message.content.startswith('!수수료 수정') or message.content.startswith('!수정'):
        if message.author.guild_permissions.manage_messages:
            try:
                edit_amount = message.content.split(" ")[1]
            except:
                embed = discord.Embed(title='!수수료수정 [숫자]', description='')
                await message.channel.send(embed=embed)
                return

            if not edit_amount.isdecimal() or int(edit_amount) > 100:
                embed = discord.Embed(title='!수수료수정 [숫자]', description='')
                await message.channel.send(embed=embed)
                return

            with open('./setting3.json', 'r') as boo:
                data = json.load(boo)
            data['percent'] = edit_amount
            with open('./setting3.json', 'w', encoding='utf-8') as making:
                json.dump(data, making, indent="\t")
            s = data['percent']
            await message.channel.send(f'수수료가 {s}%로 수정/저장되었습니다')

    if message.content == "!핑":
        la = client1.latency
        await message.channel.send(f'{message.author.mention}님ㅣ🏓현재 {client3.user.name}의 SERVER 핑은 `{str(round(la * 1000))}ms`입니다. ㅣ **해당 명령어는 !핑 입니다.**')

    if message.content == "/가위" or message.content == "/바위" or message.content == "/보" or message.content == "/찌" or message.content == "/묵" or message.content == "/빠": #가위바위보 기능
        bot_response = random.randint(1, 3)
        if bot_response == 1:
            if message.content == "가위":
                await message.channel.send(embed=discord.Embed(title="아쉽게도 이번판은 비겼습니다..", colour=discord.Color.yellow()))
            elif message.content == "바위":
                await message.channel.send(embed=discord.Embed(title="제가 졌습니다, 당신이 승리 하였습니다!", colour=discord.Color.green()))
            else:
                await message.channel.send(embed=discord.Embed(title="제가 이겼습니다, 당신은 패배 하였습니다.ㅋ", colour=discord.Color.red()))

        elif bot_response == 2:
            if message.content == "가위":
                await message.channel.send(embed=discord.Embed(title="제가 이겼습니다, 당신은 패배 하였습니다.", colour=discord.Color.red()))
            elif message.content == "바위":
                await message.channel.send(embed=discord.Embed(title="아쉽게도 이번판은 비겼습니다.", colour=discord.Color.yellow()))
            else:
                await message.channel.send(embed=discord.Embed(title="제가 졌습니다, 당신이 승리하였습니다!", colour=discord.Color.green()))

        elif bot_response == 3:
            if message.content == "가위":
                await message.channel.send(embed=discord.Embed(title="제가 졌습니다, 당신이 승리하였습니다!", colour=discord.Color.green()))
            elif message.content == "바위":
                await message.channel.send(embed=discord.Embed(title="제가 이겼습니다, 당신은 패배 하였습니다. ㅋ", colour=discord.Color.red()))
            else:
                await message.channel.send(embed=discord.Embed(title="아쉽게도 이번판은 비겼습니다..", colour=discord.Color.yellow()))                    


# 봇을 실행시키려면 아래의 토큰을 입력 [3개 클라이언트 (client1,client2,client3)로 나눠져 있습니다.]
loop = asyncio.get_event_loop() 
loop.create_task(client1.start('ODMxODYwNjUwNjI0MDI0NjI3.YHbYmg.vVIpiXNcEDGXDp9u96f8ncfHq4o'))  # 핀과 제이크 관리봇 : ODMxODYwNjUwNjI0MDI0NjI3.YHbYmg.vVIpiXNcEDGXDp9u96f8ncfHq4o
loop.create_task(client2.start('ODcyOTA1Nzg5OTQwMDUyMDIx.YQwq3g.cxzutC8bTYvWPITzTQIdLvc0t1o')) # 망치봇 : ODcyOTA1Nzg5OTQwMDUyMDIx.YQwq3g.cxzutC8bTYvWPITzTQIdLvc0t1o
loop.create_task(client3.start('ODUyNzE4MjY2NzczNTM2ODE4.YMK5xQ.WYpHqSVAnaRMcN0KOLwvivjBK-o')) # 진주 06 관리봇 : ODUyNzE4MjY2NzczNTM2ODE4.YMK5xQ.WYpHqSVAnaRMcN0KOLwvivjBK-o
loop.run_forever()