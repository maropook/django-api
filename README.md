# DRFでAPIを作成する
  __開発環境__

* OS: `macOS Big Sur v11.5.2`
* Python: `Python 3.0.6`
* Django: `3.2.5`

## :horse: Djangoのプロジェクトを作成

  __API実装__

[Django REST Frameworkを使って爆速でAPIを実装する](https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8)

__CORS設定__

DRFを使って、APIエンドポイントをフロントエンドから叩く場合にはCORSの設定が必要

[【drf】django-cors-headersを使ってCORS設定を行う](https://self-methods.com/drf-cors-headers/)


__動作確認__

```bash

# 開発サーバーを起動
$python manage.py runserver

```


http://localhost:8000/admin/
管理画面に入り,EntrysとUsersをいくつか作っておく


-----

<img width="739" alt="スクリーンショット 2021-08-28 9 51 46" src="https://user-images.githubusercontent.com/84751550/131200964-69ea9e5a-1697-48ed-92dd-153927740112.png">

<img width="734" alt="スクリーンショット 2021-08-28 9 52 00" src="https://user-images.githubusercontent.com/84751550/131200967-238bbd44-c0ca-4de0-a146-40f294a856e0.png">



-----

REST APIを作成するには最低限以下の3つを定義する必要があります。

 - Serializer
 - ViewSet
 - URL pattern

ざっくり言うと、Serializerは「Modelをどのようにシリアライズ(・デシリアライズ)するかを決めるためのもの」、ViewSetは「APIのクエリーをどう解釈するかを決めるためのもの」、そしてURL Patternは「DjangoにURLのパターンを教えるためのもの」です。これらをAPI化したいModelに対してそれぞれ定義していきます。

最低限のAPI実装をしたい時には結構手間に感じるかもしれませんが、このように分割することによって高い拡張性とコードの見通しのよさを実現しています。
