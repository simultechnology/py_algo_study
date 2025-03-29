"""
ソートアルゴリズムのベンチマーク例

様々なソートアルゴリズムのパフォーマンスを比較します。
"""
import random
import time
from typing import List, Callable

import matplotlib.pyplot as plt

from algo_study.algorithms.sorting.quick_sort import quick_sort


def generate_random_array(size: int) -> List[int]:
    """
    指定されたサイズのランダムな整数配列を生成します。
    
    Args:
        size: 配列のサイズ
        
    Returns:
        ランダムな整数の配列
    """
    return [random.randint(0, 1000) for _ in range(size)]


def measure_sort_time(sort_func: Callable, arr: List[int]) -> float:
    """
    ソート関数の実行時間を測定します。
    
    Args:
        sort_func: ソート関数
        arr: ソートする配列
        
    Returns:
        実行時間（秒）
    """
    start_time = time.time()
    sort_func(arr.copy())  # 元の配列を変更しないようにコピーを使用
    end_time = time.time()
    return end_time - start_time


def run_benchmark():
    """
    各サイズの配列でソートアルゴリズムのベンチマークを実行し、結果をプロットします。
    """
    sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]
    algorithms = {
        "Quick Sort": quick_sort,
        # 他のソートアルゴリズムを追加する場合はここに追加
        # "Merge Sort": merge_sort,
        # "Heap Sort": heap_sort,
        # 等々
    }
    
    results = {name: [] for name in algorithms}
    
    for size in sizes:
        print(f"サイズ {size} の配列をベンチマーク中...")
        arr = generate_random_array(size)
        
        for name, func in algorithms.items():
            time_taken = measure_sort_time(func, arr)
            results[name].append(time_taken)
            print(f"  {name}: {time_taken:.6f}秒")
    
    # 結果をプロット
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(sizes, times, marker='o', label=name)
    
    plt.xlabel('配列サイズ')
    plt.ylabel('実行時間（秒）')
    plt.title('ソートアルゴリズムの性能比較')
    plt.legend()
    plt.grid(True)
    plt.savefig('sorting_benchmark.png')
    plt.show()


if __name__ == "__main__":
    run_benchmark()
