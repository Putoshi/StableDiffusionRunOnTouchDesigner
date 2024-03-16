

# ComfyUIのAPI機能の参考
https://github.com/comfyanonymous/ComfyUI/tree/master/script_examples


# Setup

## Install Python
TouchDesignerのPythonバージョンに合わせて、環境を用意してね
```
import sys
print(sys.version)
```

## Install ComfyUI Modules
```
$cd ComfyUI/
$pip install -r requirements.txt
```

## Install Client Modules
```
$pip install numpy decode websocket-client pillow
```

## ComfyUIの起動 ※TouchDesignerを立ち上げてから起動する
```
$cd ComfyUI/
$python main.py --cpu

```

### ComfyUIのサーバー設定
#### 1. WebUIをブラウザで開く。=> http://127.0.0.1:8188/
#### 2. 右上の歯車ボタンを押して、設定画面を開く。
#### 3. 「Enable Dev mode Options」をチェック入れて、開発モードにする。
#### 4. 右のメニューのSave(API Format)をクリック。APIをキックする時の設定ファイル(workflow_api.json)をダウンロードする。
#### 5. 上記の設定ファイル(workflow_api.json)を、プロジェクトフォルダ(README.mdと同じフォルダ)にコピー。

### TouchDesignerのPython Modulesの設定
#### 1. メニューバーのTouchDesigner > Settings > Generalを開く。
#### 2. 「Python 64-bit Module Path」のところに使っているPython環境のモジュールのパスを入れる。
(ex. /Users/XXX/opt/anaconda3/envs/touchdesigner/lib/python3.9/site-packages/)
#### 3. 再起動
