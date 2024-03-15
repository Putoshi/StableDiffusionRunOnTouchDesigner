

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

## ComfyUIの起動
```
$cd ComfyUI/
$python main.py --cpu

```

## ComfyUIの設定
### 1. WebUIをブラウザで開く。=> http://127.0.0.1:8188/
### 2. 右上の歯車ボタンを押して、設定画面を開く。
### 3. 「Enable Dev mode Options」をチェック入れて、開発モードにする。
### 4. 右のメニューのSave(API Format)をクリック。APIをキックする時の設定ファイル(workflow_api.json)をダウンロードする。

## ComfyUIのプログラム実行
### 1. 上記の設定ファイル(workflow_api.json)を、プロジェクトフォルダ(README.mdと同じフォルダ)にコピー。
### 2. 右上の歯車ボタンを押して、設定画面を開く。
### 3. 「Enable Dev mode Options」をチェック入れて、開発モードにする。
### 4. 右のメニューのSave(API Format)をクリック。APIをキックする時の設定ファイルをダウンロードする。


## ComfyUIの起動
```
$cd ComfyUI/
$python main.py

```
