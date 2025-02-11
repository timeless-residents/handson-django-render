# Django ハンズオン CRUD アプリケーション

Render プラットフォームにデプロイされた、Tailwind CSS を統合した Django CRUD アプリケーションです。

## 技術スタック

- Python
- Django
- Tailwind CSS
- Render (デプロイメントプラットフォーム)

## 機能

- アイテムの作成、読み取り、更新、削除（CRUD操作）
- レスポンシブデザイン（Tailwind CSS）
- モダンでクリーンなUI

## セットアップ手順

1. リポジトリのクローン:
```bash
git clone https://github.com/timeless-residents/handson-django-render.git
cd handson-django-render
```

2. 依存関係のインストール:
```bash
pip install -r requirements.txt
```

3. データベースのマイグレーション:
```bash
python manage.py migrate
```

4. Tailwind CSSのセットアップ:
```bash
cd theme/static_src
npm install
```

5. 開発サーバーの起動:
```bash
python manage.py runserver
```

アプリケーションは http://localhost:8000 で利用可能になります。

## デプロイ

このアプリケーションは Render プラットフォームにデプロイするように設定されています。デプロイの設定は `render.yaml` ファイルで管理されています。
