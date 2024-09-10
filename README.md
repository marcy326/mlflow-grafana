# Proxy Server with Monitoring

このプロジェクトは、MLflow モデルサーバーへのリクエストをプロキシするサーバーと、Grafana を使ったモニタリングシステムを提供します。

## 機能

- プロキシサーバーは、クライアントからのリクエストを受け取り、MLflow モデルサーバーに転送します。
- リクエストとレスポンスのデータは、Loki に保存されます。
- Grafana ダッシュボードを使って、モデルの予測率などのメトリクスを監視できます。

## 構成

このプロジェクトは、以下のコンポーネントで構成されています:

- `proxy`: Flask ベースのプロキシサーバー
- `inference`: MLflow モデルサーバー
- `loki`: ログ収集システム
- `promtail`: Loki にログを送信するエージェント
- `grafana`: モニタリングダッシュボード

これらのコンポーネントは、Docker Compose を使って起動されます。

## 使い方

1. このリポジトリをクローンします。
2. `docker-compose up -d` を実行して、すべてのコンポーネントを起動します。
3. Grafana にアクセス (http://localhost:3000) し、ログインします (ユーザー名: `admin`, パスワード: `admin`)。
4. ダッシュボードを確認して、モデルの予測率などのメトリクスを監視できます。
5. プロキシサーバーにリクエストを送信するには、`request_example.sh` スクリプトを使用できます。

## 注意事項

- プロキシサーバーのログは、`/app/logs` ディレクトリに保存されます。
- Grafana のダッシュボードとデータソースの設定は、`grafana/` ディレクトリ内のファイルで定義されています。
- Promtail の設定は、`promtail-config.yaml` ファイルで定義されています。

## 今後の拡張

- 複数のモデルをサポートするように拡張する
- モデルの精度や性能に関するより詳細なメトリクスを追加する
- アラート機能を追加する
- 自動スケーリングなどの運用機能を追加する
