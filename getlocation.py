import requests, json
import pandas as pd
import time


def get_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    headers = {"Authorization": "KakaooAK 여기에 개인키 입력"}
    api_json = json.loads(str(requests.get(url,headers=headers).text))
    return api_json


get_location("부산 금정구 부산대학로63번길 2")