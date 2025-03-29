"""
クイックソートアルゴリズムのテスト
"""
import pytest

from algo_study.algorithms.sorting.quick_sort import quick_sort


def test_quick_sort_with_integers():
    """整数配列のソートをテスト"""
    # 準備
    unsorted = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    
    # 実行
    result = quick_sort(unsorted)
    
    # 検証
    assert result == expected


def test_quick_sort_with_strings():
    """文字列配列のソートをテスト"""
    # 準備
    unsorted = ["banana", "apple", "cherry", "date"]
    expected = ["apple", "banana", "cherry", "date"]
    
    # 実行
    result = quick_sort(unsorted)
    
    # 検証
    assert result == expected


def test_quick_sort_with_empty_array():
    """空配列のソートをテスト"""
    # 準備
    unsorted = []
    expected = []
    
    # 実行
    result = quick_sort(unsorted)
    
    # 検証
    assert result == expected


def test_quick_sort_with_single_element():
    """1要素配列のソートをテスト"""
    # 準備
    unsorted = [42]
    expected = [42]
    
    # 実行
    result = quick_sort(unsorted)
    
    # 検証
    assert result == expected


def test_quick_sort_with_duplicate_elements():
    """重複要素を含む配列のソートをテスト"""
    # 準備
    unsorted = [3, 3, 3, 2, 2, 1, 1]
    expected = [1, 1, 2, 2, 3, 3, 3]
    
    # 実行
    result = quick_sort(unsorted)
    
    # 検証
    assert result == expected


def test_quick_sort_with_negative_numbers():
    """負の数を含む配列のソートをテスト"""
    # 準備
    unsorted = [5, -10, 0, 15, -5]
    expected = [-10, -5, 0, 5, 15]
    
    # 実行
    result = quick_sort(unsorted)
    
    # 検証
    assert result == expected
