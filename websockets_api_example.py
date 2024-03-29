import websocket
import uuid
import json
import urllib.request
import urllib.parse
import random

from PIL import Image
import io

server_address = "127.0.0.1:8188"
client_id = str(uuid.uuid4())

# タスクを処理キューに追加する
def queue_prompt(prompt):
    p = {"prompt": prompt, "client_id": client_id}
    data = json.dumps(p).encode('utf-8')
    req =  urllib.request.Request("http://{}/prompt".format(server_address), data=data)
    return json.loads(urllib.request.urlopen(req).read())

# 画像を取得する
def get_image(filename, subfolder, folder_type):
    data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
    url_values = urllib.parse.urlencode(data)
    with urllib.request.urlopen("http://{}/view?{}".format(server_address, url_values)) as response:
        return response.read()

# タスクの実行履歴を取得する
def get_history(prompt_id):
    with urllib.request.urlopen("http://{}/history/{}".format(server_address, prompt_id)) as response:
        return json.loads(response.read())

# タスクの実行結果を取得する
def get_images(ws, prompt):
    prompt_id = queue_prompt(prompt)['prompt_id']
    output_images = {}
    while True:
        out = ws.recv()
        if isinstance(out, str):
            message = json.loads(out)
            if message['type'] == 'executing':
                data = message['data']
                if data['node'] is None and data['prompt_id'] == prompt_id:
                    break #Execution is done
        else:
            continue #previews are binary data

    history = get_history(prompt_id)[prompt_id]
    for o in history['outputs']:
        for node_id in history['outputs']:
            node_output = history['outputs'][node_id]
            if 'images' in node_output:
                images_output = []
                for image in node_output['images']:
                    image_data = get_image(image['filename'], image['subfolder'], image['type'])
                    images_output.append(image_data)
            output_images[node_id] = images_output

    return output_images


# プロンプトをjsonファイルから読み込む
with open("./workflow_api.json", "r") as file:
  prompt = json.load(file)


# ⇩ jsonから変更しなくても、この部分を変更することで、生成する画像の内容を変更することもできる
prompt["6"]["inputs"]["text"] = "special masterpiece best quality man"
prompt["3"]["inputs"]["seed"] =  random.randint(1, 10000) # 1から10000の間でランダムな値を生成

ws = websocket.WebSocket()
ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))

images = get_images(ws, prompt)

# 実行
for node_id in images:
  for image_data in images[node_id]:
    image = Image.open(io.BytesIO(image_data))
    image.show()
