# 商品を購入して、消費税を加えた計算結果を返す関数を記述してください。
# 第1引数に商品の金額、第2引数に消費税（10%）を設定できるようにしてください。

def calculate(item,tax=0.1):
    totall = item + tax*item
    print(f"{totall}円")

calculate(1000)