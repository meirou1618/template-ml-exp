# 🧪 DDD-based ML Experiment Template

このテンプレートは、**ドメイン駆動設計（DDD）** の原則に従って構築された、機械学習モデルの実験管理用Pythonコードです。  
MLモデルのライフサイクルや実験履歴を明確なドメインモデルで表現することで、拡張性と保守性を高めることを目的としています。

---

## 📦 構成概要
```
src/ 
├── domain/
    ├── model.py # モデルエンティティ（Model）
    ├── ml_model.py # MLモデルの抽象クラス（MLModel） 
    ├── experiment.py # アグリゲートルート（Experiment） 
    ├── domain_services.py # ドメインサービス（Trainer, Predictor） 
    ├── data.py # 入力データの構造（TemplateTrainData）
├── application/
    ├── aplication_service.py # アプリケーションサービスの実行
    ├── template_service.py # 各種アプリケーションサービス（TemplateService）
├── infrastracture/
    ├── repository.py # 永続化インターフェース（TemplateModelRepository, TemplateDataRepository）
└── cli.py # 実行コマンド
```

---

## 🧠 コンセプト

| ドメインオブジェクト | 説明 |
|------------------|------|
| **Model** | ハイパーパラメータやMLモデル状態を保持するエンティティ |
| **MLModel** | 機械学習モデル（Scikit-learn、torchのモデル、など）のラッパー。値オブジェクトとして扱う |
| **Experiment** | モデル、データ概要、作成者などを包括するアグリゲートルート |
| **ModelTrainer** | モデルの訓練処理を担うドメインサービス |
| **ModelPredictor** | モデルの推論処理を担うドメインサービス |

| アプリケーションオブジェクト | 説明 |
|------------------|------|
| **ApplicationService** | アプリケーションサービスの抽象クラス |
| **ApplicationServiceHndler** | アプリケーションサービスの実行クラス |
| **TemplateService** | アプリケーションサービスの実装クラス |

| インフラストラクチャオブジェクト | 説明 |
|------------------|------|
| **ModelRepository** | モデルの永続化、読み込みを行うリポジトリ |
| **DataRepository** | データの読み込みを行うリポジトリ |


---



## 事前準備
1. uvのインストール
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    - [参考](https://zenn.dev/tabayashi/articles/52389e0d6c353a)

2. 仮想環境を作成する：
    
    uvのパッケージ管理を利用する。
    pyproject.tomlに記載されているパッケージより環境を作成する。
    ```bash
    uv sync
    ```

## 🚀 使い方
### 全般
- コマンド一覧の確認
    ```bash
    uv run python cli.py
    ```

### コマンド（例）
- 実行
    ```bash
    uv run python cli.py template-command
    ```


## 🛠 拡張例
- 評価サービス ModelEvaluator の追加（精度, F1など）
- 複数モデルサポート（LightGBM, XGBoostなどをファクトリで切替）
- MLflowやDVCと連携したリポジトリ実装
- Web UI や CLI インターフェースの構築
- 本番用モデル管理と区別したライフサイクル設計

## 🙋‍♂️ 作者・貢献

このテンプレートは、個人的な勉強のため、DDDを用いてML実験環境を整理したい人のために作りました。
Pull Request や Issue 歓迎です。
