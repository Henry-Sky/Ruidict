import json
import requests
import pandas as pd
from utils.AuthV3Util import addAuthParams

lang_from = "auto"  # 源语言语种
lang_to = "zh-CHS"  # 目标语言语种


def init():
    keys = pd.read_csv("keys.csv")
    key = keys.where(keys["name"] == "youdao")
    app_key = key.at[0, "appkey"]
    app_secret = key.at[0, "appsecret"]
    return app_key, app_secret


def pack(word, app_key, app_secret):
    global lang_from
    global lang_to
    data = {'q': word, 'from': lang_from, 'to': lang_to}
    addAuthParams(app_key, app_secret, data)
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    return header, data


def docall(url, header, params, method):
    if 'get' == method:
        return requests.get(url, params)
    elif 'post' == method:
        return requests.post(url, params, header)


def translate(word):
    app_key, app_secret = init()
    header, data = pack(word, app_key, app_secret)
    res = docall('https://openapi.youdao.com/api', header, data, 'post')
    res = res.content.decode("utf-8")
    res = json.loads(res)
    return res


def get_explains(word):
    res = translate(word)
    basic = dict(res["basic"])
    return basic["explains"]