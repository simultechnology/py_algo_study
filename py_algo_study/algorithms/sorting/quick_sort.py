"""
クイックソートアルゴリズムの実装
"""
from typing import List, TypeVar

T = TypeVar('T', int, float, str)


def quick_sort(arr: List[T]) -> List[T]:
    """
    クイックソートアルゴリズムを使用して配列をソートします。
    
    Args:
        arr: ソートする配列
        
    Returns:
        ソート済みの配列
    
    時間計算量:
        平均: O(n log n)
        最悪: O(n²)
    空間計算量:
        O(log n)
    """
    # 空の配列または1要素の配列はそのまま返す
    if len(arr) <= 1:
        return arr
    
    # ピボットを選択（ここでは配列の最初の要素）
    pivot = arr[0]
    
    # ピボットより小さい要素、等しい要素、大きい要素に分ける
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]
    
    # 再帰的にソートして結合
    return quick_sort(less) + equal + quick_sort(greater)


if __name__ == "__main__":
    # 使用例
    test_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quick_sort(test_array)
    print(f"元の配列: {test_array}")
    print(f"ソート後: {sorted_array}")
    
    # 文字列の配列でも動作する
    str_array = ["banana", "apple", "cherry", "date"]
    sorted_str_array = quick_sort(str_array)
    print(f"元の文字列配列: {str_array}")
    print(f"ソート後: {sorted_str_array}")
