# Module: Code Function

import discord
import urllib.parse
import re
import json

c = json.loads(open('말.json', encoding='utf-8').read())

color_preset = {
    'weather' : [0x6BC6FF, 0x78FFEB, 0x6BFF95, 0xE4FFA3, 0xFFF6B0, 0xFFE2A3, 0xFFB682, 0xFFDDD1, 0xFFA5A3],
    'tier' : {
        'iron' : 0x32373a, 
        'bronze' : 0xac9d85, 
        'silver' : 0x97a0a6, 
        'gold' : 0xffa905, 
        'platinum' : 0x05c58e, 
        'diamond' : 0x1b9ff6, 
        'sky' : 0xff6c81
    },
    'search' : [0xDBF7FF, 0xE88D84, 0xFFEA9E]
}

def getcontent(content = ''):
    spltd = content.split()
    content = ''
    for i in range(len(spltd)):
        if i != 0:
            if i != 1:
                content += ' '
            content += spltd[i]
    return content

def get_fancy(dic):
    if dic['__init__'] == 'calculate':
        embed = discord.Embed(
            title = dic['variable']
        )
        if dic['calced']:
            embed.description = '{}={}'.format(dic['variable'], dic['value'])
        else:
            embed.description = dic['display']
    if dic['__init__'] == 'weather':
        lv_sum = dic['detail']['dust']['level'] + dic['detail']['smalldust']['level'] + dic['detail']['ozon']['level'] - 3
        embed = discord.Embed(
            title = '현재 온도: {}℃'.format(dic['degree']['now']),
            description = '최저: {}℃ / 최고: {}℃'.format(dic['degree']['min'], dic['degree']['max']),
            url = 'https://search.naver.com/search.naver?query={}'.format(urllib.parse.quote('날씨')),
            color = color_preset['weather'][lv_sum]
        )
        embed.add_field(name='미세먼지: {}'.format(dic['detail']['dust']['evel']), value=dic['detail']['dust']['degree'], inline=True)
        embed.add_field(name='초미세먼지: {}'.format(dic['detail']['smalldust']['evel']), value=dic['detail']['smalldust']['degree'], inline=True)
        embed.add_field(name='오존: {}'.format(dic['detail']['ozon']['evel']), value=dic['detail']['ozon']['degree'], inline=True)
        embed.set_footer(text="제공: 기상청")
    if dic['__init__'] == 'op.gg-lol':
        if dic['queryok']:
            tier = re.sub(r'.[0-9]', '', dic['tierrank']).lower()
            if tier == 'master' or tier == 'grandmaster' or tier == 'challenger':
                tier = 'sky'
            if tier == 'unranked':
                tier = 'iron'
            embed=discord.Embed(
                title = dic['username'],
                description = '솔로 랭크: {}'.format(dic['tierrank']),
                color = color_preset['tier'][tier]
            )
            embed.set_author(name=dic['username'], icon_url=dic['profile_image'])
            embed.set_thumbnail(url=dic['tiermedal'])
            embed.set_footer(text='제공: OP.GG')
        else:
            embed=discord.Embed(
                title = dic['username'], 
                description = c['전적검색 소환사 못찾음'],
                color = color_preset['tier']['iron']
            )
            embed.set_thumbnail(url='https://opgg-static.akamaized.net/images/medals/default.png')
            embed.set_author(name=dic['username'])
    if dic['__init__'] == 'naver':
        embed = discord.Embed(
            title = '검색 결과: {}'.format(dic['search_content']),
            description = '네이버 검색 결과'
        )
        if dic['status'] == 200:
            if len(dic['items']) == 0:
                embed.color = color_preset['search'][2]
                embed.add_field(name=c['네이버 검색 결과 없음'], value=c['네이버 검색 결과 없음 설명'], inline=False)
            else:
                embed.color = color_preset['search'][0]
                for i in range(len(dic['items'])):
                    embed.add_field(name=dic['items'][i]['title'], value='{}\n{}'.format(dic['items'][i]['link'], dic['items'][i]['description']), inline=False)
                    if i == 2:
                        break
        else:
            embed.color = color_preset['search'][1]
            embed.add_field(name=c['네이버 검색 문제 발생'], value=c['네이버 검색 문제 발생 설명'], inline=False)
    return embed

if __name__ == '__main__':
    print(getcontent('안녕 세상아 ㅎㅎ'))