import json
import requests
from utils.AuthV3Util import addAuthParams
# API密钥
import key

# 应用密钥
APP_KEY, APP_SECRET = key.get_key()

def docall(url, header, params, method):
    if 'get' == method:
        return requests.get(url, params)
    elif 'post' == method:
        return requests.post(url, params, header)

def translate(word):
    q = word    # 待翻译文本
    lang_from = "auto"  # 源语言语种
    lang_to = "zh-CHS"    # 目标语言语种
    data = {'q': q, 'from': lang_from, 'to': lang_to}
    addAuthParams(APP_KEY, APP_SECRET, data)
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    res = docall('https://openapi.youdao.com/api', header, data, 'post')
    res = res.content.decode("utf-8")
    res = json.loads(res)
    return res

def get_explains(word):
    res = translate(word)
    basic = dict(res["basic"])
    return basic["explains"]

# print(get_explains("deem"))