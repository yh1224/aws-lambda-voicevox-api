# aws-voicevox-proxy

AWS Lambda 上で [VOICEVOX](https://voicevox.hiroshiba.jp/) による合成音声を返す Web API を構築します。

## 必要なもの

- [AWS](https://aws.amazon.com/) アカウント
- [AWS CLI](https://aws.amazon.com/jp/cli/) の認証情報が設定済みであること
- [AWS CDK](https://aws.amazon.com/jp/cdk/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## デプロイ

AWS CDK を使ってデプロイします。

```shell
npm install
cdk bootstrap (アカウント/リージョン毎に初回のみ)
cdk deploy
```

## 確認

デプロイが完了すると、以下のように Web API の URL が出力されます。

```
AwsVoicevoxProxyStack.ApiUrl = https://XXXXXXXXXXXXXXXX.lambda-url.ap-northeast-1.on.aws/
```

text パラメーターを指定してこの URL に POST すると、レスポンスとして mp3 データが返ってきます。

```shell
curl -X POST https://XXXXXXXXXXXXXXXX.lambda-url.ap-northeast-1.on.aws \
    -d "text=こんにちは" \
    -o voice.mp3
```

## 注意

- 認証には対応していません。
