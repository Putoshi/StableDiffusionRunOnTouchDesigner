import json
from urllib import request, parse
import random

# タスクを処理キューに追加する
def queue_prompt(prompt):
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    req =  request.Request("http://127.0.0.1:8188/prompt", data=data)
    request.urlopen(req)

# プロンプトをjsonファイルから読み込む
with open("./workflow_api.json", "r") as file:
    prompt = json.load(file)


# ⇩ jsonから変更しなくても、この部分を変更することで、生成する画像の内容を変更することもできる
prompt["6"]["inputs"]["text"] = "special masterpiece best quality man"
prompt["3"]["inputs"]["seed"] =  random.randint(1, 10000) # 1から10000の間でランダムな値を生成

# 実行
queue_prompt(prompt)

