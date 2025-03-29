# アルゴリズム学習プロジェクト 使用ガイド

このガイドでは、Poetryを使用したPythonアルゴリズム学習プロジェクトの使い方を説明します。

## 1. 環境設定

### Poetryのインストール

まだPoetryをインストールしていない場合は、以下のコマンドでインストールします：

```bash
# macOS / Linux / Windowsの場合
curl -sSL https://install.python-poetry.org | python3 -

# または pipを使用して
pip install poetry
```

### プロジェクトのセットアップ

プロジェクトディレクトリに移動し、依存関係をインストールします：

```bash
cd /Users/t_ishikawa/workspace/python_work/algo_study
poetry install
```

これにより、`pyproject.toml`に記載されているすべての依存関係がインストールされます。

## 2. 仮想環境の利用

Poetryは自動的に仮想環境を作成します。以下のコマンドで仮想環境を有効化できます：

```bash
poetry shell
```

あるいは、コマンドを実行する際に`poetry run`を付けることもできます：

```bash
poetry run python -m algo_study.algorithms.sorting.quick_sort
```

## 3. アルゴリズムの実行

### 単一のアルゴリズムを実行

```bash
# クイックソートの例を実行
poetry run python -m algo_study.algorithms.sorting.quick_sort
```

### ベンチマークの実行

```bash
poetry run python examples/sorting_benchmark.py
```

## 4. テストの実行

PyTestを使ってテストを実行するには：

```bash
# すべてのテストを実行
poetry run pytest

# 特定のテストを実行
poetry run pytest tests/algorithms/sorting/test_quick_sort.py
```

## 5. 新しいアルゴリズムの追加

1. 適切なディレクトリに新しいPythonファイルを作成します：
   ```bash
   touch algo_study/algorithms/search/binary_search.py
   ```

2. アルゴリズムを実装します

3. テストを作成します：
   ```bash
   mkdir -p tests/algorithms/search
   touch tests/algorithms/search/test_binary_search.py
   ```

## 6. 依存関係の管理

新しいパッケージを追加するには：

```bash
# 本番環境の依存関係を追加
poetry add numpy

# 開発環境の依存関係を追加
poetry add --dev black
```

## 7. コード品質の維持

コードフォーマットと品質チェックを行うには：

```bash
# Black でフォーマット
poetry run black .

# isort でインポートをソート
poetry run isort .

# flake8 でリンティング
poetry run flake8
```
