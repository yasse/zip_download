#need pip
#1.
#pip install requests

import webbrowser
import requests
import os

DEFAULT_DOWNLOAD_PATH = "ダウンロード"



#取得するパッケージのダウンロードURLを開く
package_download_URL = ""

download_res = requests.get(package_download_URL)
try:
    download_res.raise_for_status()
except Exception as exc:
    print("ダウンロードに失敗しました...")
    print("ダウンロードURL：package_download_URL")
    print('うーん: {}'.format(exc))

print(download_res.headers['Content-Type'])

#URLから保存ファイル名を生成
filename_zip = os.path.basename(package_download_URL)
print(filename_zip)

#open()の第一引数に指定したファイルパスを第二引数にwbを指定してバイナリ書き込みモードで開く
#responsオブジェクトの中身を開いたファイルに書き込む
with open(DEFAULT_DOWNLOAD_PATH + filename_zip, 'wb') as f:
    f.write(download_res.content)
  