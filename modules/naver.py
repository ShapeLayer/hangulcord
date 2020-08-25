# Module: Return NAVER Search Result

import os
import sys
import urllib.request
import urllib.parse
import json
import re

try:
    key = json.loads(open(os.path.dirname(__file__) + '/../key.json').read())
except:
    pass

def get(search_content):
    url = 'https://openapi.naver.com/v1/search/blog?query={}'.format(urllib.parse.quote(search_content))
    request = urllib.request.Request(url)
    request.add_header('X-Naver-Client-Id', key['naver_search_client_id'])
    request.add_header('X-Naver-Client-Secret', key['naver_search_client_secret'])
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        result = json.loads(re.sub('<.+?>', '', response.read().decode('utf-8')))
        result['__init__'] = 'naver'
        result['status'] = 200
        result['search_content'] = search_content
    else:
        result = {
            '__init__' : 'naver',
            'status' : 0,
            'search_content' : search_content
        }
    return result

if __name__ == '__main__':
    key = json.loads(open('key.json').read())
    print(str(get('미러ㅣ뱌ㅕ개ㅑㅐㅓㅡㅏ닝럼나ㅣ여런마ㅣㅓ')))