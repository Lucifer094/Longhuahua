# -*- coding: utf-8 -*-

import requests
import random
from hashlib import md5
import time

# Set your own appid/appkey.
appid = 'INPUT_YOUR_APPID'
appkey = 'INPUT_YOUR_APPKEY'


# Translate zh to en, return translate result text.
def trans_zh_en(text):
    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'zh'
    to_lang = 'en'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    # Generate salt and sign
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + text + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': text, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    return result['trans_result'][0]['dst']


# Translate auto to zh, return translate result text.
def trans_auto_zh(text):
    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'auto'
    to_lang = 'zh'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    # Generate salt and sign
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + text + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': text, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    return result['trans_result'][0]['dst']


# Translate auto to fin, return translate result text.
def trans_auto_fin(text):
    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'auto'
    to_lang = 'fin'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    # Generate salt and sign
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + text + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': text, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    return result['trans_result'][0]['dst']


# Translate auto to rom, return translate result text.
def trans_auto_rom(text):
    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'auto'
    to_lang = 'rom'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    # Generate salt and sign
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + text + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': text, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    return result['trans_result'][0]['dst']


# Translate auto to hu, return translate result text.
def trans_auto_hu(text):
    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'auto'
    to_lang = 'hu'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    # Generate salt and sign
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + text + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': text, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    return result['trans_result'][0]['dst']


# ????????????????????????????????????????????????
while True:
    # ???????????????????????????????????????
    originalText = input("=====?????????????????????????????????=====\n")

    # ????????????->?????????
    translation = trans_auto_fin(originalText)
    # print("=====???????????????????????????=====\n%s" % (translation))

    # ??????2S
    time.sleep(2)

    # ????????????->???????????????
    translation = trans_auto_rom(translation)
    # print("=====?????????????????????????????????=====\n%s" % (translation))

    # ??????2S
    time.sleep(2)

    # ????????????->????????????
    translation = trans_auto_hu(translation)
    # print("=====??????????????????????????????=====\n%s" % (translation))

    # ??????2S
    time.sleep(2)

    # ????????????->??????
    translation_zh = trans_auto_zh(translation)
    print("=====????????????????????????=====\n%s" % (translation_zh))
