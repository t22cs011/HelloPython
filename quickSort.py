"""
2021/01/25
@Yuya Shimizu

クイックソート
"""

def quick_sort(data):
    
    i = len(data) - 1

    #分割できなくなる(リスト要素が1以下)であれば，そのままデータを返す(並べ替えの必要なし)
    if len(data) <= 1:
        return data

    pivot = data.pop(0)     #リストの先頭をピボットとして取り出す    
    
    #スライス・内包表記を用いない場合
    left = [] 
    right = []
    
    for i in data:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    left = quick_sort(left)       #入力に対する左側リストを形成する
    right = quick_sort(right)   #入力に対する右側リストを形成する
    
    """"
    
    [式 for 変数 in イテラブル if 条件]
    
    式: リストの要素となる値を表す式
    変数: イテラブルなオブジェクト（リストなど）の要素を一つずつ代入する変数
    イテラブル: 繰り返し処理の対象となるシーケンス
    if 条件: 条件を満たす要素のみをリストに追加する
    
    """
    
    # # ピボットより小さいものでリストを作る
    # left = [i for i in data if i <= pivot]
    
    # # ピボットより大きいものでリストを作る
    # right = [i for i in data if i > pivot]

    #########再帰しきった結果のみ，quick_sort関数の出力として返される
    #########それ以外のreturnは上のleft = quick_sort(right), left = quick_sort(right)
    return left + [pivot] + right


if __name__ == '__main__':
    DATA = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

    print(f"{DATA} → {quick_sort(DATA)}")
