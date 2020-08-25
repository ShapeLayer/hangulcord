dic = {
    'str' : {
        'message_recevied' : 
'''
@client.event
async def on_message(message):
    if message.content == '봇 종료' or message.content == '봇종료':
        await message.channel.send('안녀엉!')
        print('봇 종료됨.')
        exit()
''',

        'if_message' : 'if message.content == "%_variable_%" and client.user.id != message.author.id:',
        'if_startswith' : 'if message.content.startswith("%_variable_%") and client.user.id != message.author.id:',
        'get_content' : 'modules.common.getcontent(message.content)',
        'send_message' : 'await message.channel.send("%_variable_%")',
        'send_result' : 'await message.channel.send("", embed=%_variable_%)',
        'search_naver' : 'modules.common.get_fancy(modules.naver.get(%_variable_%))',
        'calc' : 'modules.common.get_fancy(modules.calc.calc(%_variable_%))',
        'weather' : 'modules.common.get_fancy(modules.weather.get())',
        'opgg' : 'modules.common.get_fancy(modules.opgg.get(%_variable_%))'
    },
    're' : {
        'if_message' : r'(?P<fullmatch>만약\s?메(시|세)지\s?=\s?(?P<content>(.*?))\s?:)',
        'if_startswith' : r'(?P<fullmatch>만약\s?메(시|세)지\s?시작\s?부분\s?=\s?(?P<content>(.*?))\s?:)',
        'get_content' : r'내용\s?가져오기\s?\(\)',
        'send_message' : r'(?P<fullmatch>내용\s?보내기\s?\((?P<content>(.*?))\))',
        'send_result' : r'(?P<fullmatch>결과\s?내용\s?보내기\s?\((?P<content>(.*?))\))',
        'search_naver' : r'(?P<fullmatch>네이버에\s?검색\s?\((?P<content>(.*?))\))',
        'calc' : r'(?P<fullmatch>계산\s?\((?P<content>(.*?))\))',
        'weather' : r'날씨\s?검색(.*?)\(\)',
        'opgg' : r'(?P<fullmatch>(OP\.GG|op\.gg)에\s?검색\s?\((?P<content>.*?)\))'
    }
}