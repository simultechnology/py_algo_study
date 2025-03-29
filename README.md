# アルゴリズム学習プロジェクト

Pythonを使用したアルゴリズムとデータ構造の学習用リポジトリです。

## セットアップ方法

1. Poetryをインストールする（まだの場合）：
   ```bash
   pip install poetry
   ```

2. 依存関係をインストールする：
   ```bash
   poetry install
   ```

3. 仮想環境を有効化する：
   ```bash
   poetry shell
   ```

## プロジェクト構造

- `algo_study/`: メインのソースコードディレクトリ
  - `data_structures/`: 様々なデータ構造の実装
  - `algorithms/`: アルゴリズムの実装
  - `utils/`: ユーティリティ関数
- `tests/`: テストコード
- `examples/`: アルゴリズムの使用例

## 実行方法

```bash
# 例：ソートアルゴリズムの実行
poetry run python -m algo_study.algorithms.sorting.quick_sort
```
