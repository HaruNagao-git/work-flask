from flask import Flask, render_template

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

# ==================================================
# ルーティング
# ==================================================
# TOPページ
@app.route('/') 
def index():
    return render_template('top.html')

# 一覧
@app.route('/list') 
def item_list():
    return render_template('list.html')

# 詳細
@app.route('/detail/<int:id>')
def item_detail(id):
    return render_template('detail.html', show_id=id)

# render_templateで値を渡す
@app.route("/multiple")
def show_jinja_multiple():
    word1 = "テンプレートエンジン"
    word2 = "神社"
    return render_template('jinja/show1.html', temp= word1, jinja = word2)

# render_templateで値を渡す「辞書型」
@app.route("/dict")
def show_jinja_dict():
    words = {
        'temp' : "てんぷれーとえんじん",
        'jinja' : "ジンジャ"
    }
    return render_template('jinja/show2.html', key = words)

# render_templateで値を渡す「リスト型」
@app.route("/list2")
def show_jinja_list():
    hero_list = ['桃太郎', '金太郎', '浦島タロウ']
    return render_template('jinja/show3.html', users = hero_list)

# ▼▼▼【リスト3.24】▼▼▼
# render_templateで値を渡す「クラス」
class Hero:
    # コンストラクタ
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 表示用関数
    def __str__(self):
        return f'名前：{self.name} 年齢：{self.age}'

@app.route("/class")
def show_jinja_class():
    hana = Hero('花咲かじいさん', 99)
    return render_template('jinja/show4.html', user = hana)
# ▲▲▲【リスト3.24】▲▲▲

# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    app.run()