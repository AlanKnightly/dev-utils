import time
import http.client
import sys
import urllib.parse
import json

conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

TARGET_LANG_CODES = [
    {
      "desc":'阿拉伯语',
      "code":'ar'
    },
    { 
      "desc":'德文',
      "code":'de'
    },
    { 
      "desc":'英语',
      "code":'en'
    },
    { 
      "desc":'西班牙语',
      "code":'es'
    },
    { 
      "desc":'法文',
      "code":'fr'
    },
    { 
      "desc":'印尼',
      "code":'id'
    },
    { 
      "desc":'日文',
      "code":'ja'
    },
    { 
      "desc":'韩文',
      "code":'ko'
    },
    { 
      "desc":'泰文',
      "code":'th'
    },
    { 
      "desc":'越南语',
      "code":'vi'
    },
    { 
      "desc":'中文台湾',
      "code":'zh-TW'
    },
]

def ask(input,config):
    payload = "q=" + urllib.parse.quote_plus(input)  + "&target=" + config["code"] +"&source=zh"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'Accept-Encoding': "application/gzip",
        'X-RapidAPI-Key': "cfa34fd3e0mshb712411af16ea65p1e23a8jsn799fee07e325",
        'X-RapidAPI-Host': "google-translate1.p.rapidapi.com"
    }
    conn.request("POST", "/language/translate/v2", payload, headers)
    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")
    j = json.loads(result)
    print(config["desc"], "    ", j["data"]["translations"][0]["translatedText"])



input = sys.argv[1]
for index, config in enumerate(TARGET_LANG_CODES):
    ask(input,config)
    time.sleep(0.5)
    
