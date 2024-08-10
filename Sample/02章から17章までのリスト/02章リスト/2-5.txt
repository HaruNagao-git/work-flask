# 関数outer
def outer(func):
    # 関数内関数inner
    def inner():
        print('===開始===')
        func()
        print('===終了===')
    return inner

# 関数a
def a():
    print('Aです')

# 関数の実行：戻り値は変数testへ
test = outer(a)
# 関数の実行
test()