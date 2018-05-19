# UserImageCreatorRetImage
このプログラムはAWS Lambdaを利用して画像ファイルを生成する処理です。

[ユーザーの初期画像に便利なAPIを作りました \- blog\.beaglesoft\.net](http://blog.beaglesoft.net/entry/2018/05/17/221903)

## 動作方法
以下の通りPythonコマンドを実行することで動作します。


```bash
$ python handler.py

2018-05-19 09:24:01,507 - MainThread - handler:<module>(22) - INFO - Loading function
2018-05-19 09:24:01,507 - MainThread - handler:handle(26) - INFO - event:{'resource': '/create', 'path': '/create', 'httpMethod': 'GET', 'headers': None, 'queryStringParameters': {'s': 'BS'}, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'path': '/create', 'resourceId': 'mmgrks', 'stage': 'test-invoke-stage', 'requestId': 'ae0367fe-5904-11e8-a178-259f37ad7e5e', 'resourcePath': '/create', 'httpMethod': 'GET'}, 'body': None, 'isBase64Encoded': False}
2018-05-19 09:24:01,507 - MainThread - handler:handle(27) - INFO - context:None
2018-05-19 09:24:01,507 - MainThread - handler:handle(37) - INFO - display_str:BS
```

出力された画像は`/tmp`に作成されます。

```bash
$ ls -al /tmp | grep png

# macの場合はこちら
$ ls -al /private/tmp | grep png
-rw-r--r--   1 ymanabe  wheel   2291 May 19 09:24 6a5cae15-ccd5-4e76-bc26-e304545a2b0e.png
```