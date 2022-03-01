# remove_lambda_versions

Serverless Frameworkを長年使ってると溜まりがちな、古いバージョンのLambdaを一掃するスクリプトです。

- アクセス可能なLambda関数のバージョンを削除
- $LATESTは例外として削除しない


## 前提条件
- 作業端末にpipenvがインストール済みであること
- Lambdaに対してフル権限があること。

## 実行方法

```bash
# 初期インストール
export PIPENV_VENV_IN_PROJECT=true
pipenv install

pipenv shell
python remove_versions.py

```
