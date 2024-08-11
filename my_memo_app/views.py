from app import app
from flask import redirect, render_template, request, url_for
from models import Memo, db
from werkzeug.exceptions import NotFound


# ==================================================
# ルーティング
# ==================================================
@app.route("/memo/")
def index():
    # メモ全件取得
    memos = Memo.query.all()
    # 画面遷移
    return render_template("index.html", memos=memos)


@app.route("/memo/create", methods=["GET", "POST"])
def create():
    # POST
    if request.method == "POST":
        # データ入力取得
        title = request.form["title"]
        content = request.form["content"]
        # 登録処理
        memo = Memo(title=title, content=content)
        db.session.add(memo)
        db.session.commit()
        # 画面遷移
        return redirect(url_for("index"))
    # GET
    return render_template("create.html")


@app.route("/memo/update/<int:memo_id>", methods=["GET", "POST"])
def update(memo_id):
    # データベースからmemo_idに該当するレコードを探し, 見つからない場合は404エラーを表示
    memo = Memo.query.get_or_404(memo_id)
    # POST
    if request.method == "POST":
        # データ入力取得
        memo.title = request.form["title"]
        memo.content = request.form["content"]
        db.session.commit()
        # 画面遷移
        return redirect(url_for("index"))
    # GET
    return render_template("update.html", memo=memo)


@app.route("/memo/delete/<int:memo_id>")
def delete(memo_id):
    # データベースからmemo_idに該当するレコードを探し, 見つからない場合は404エラーを表示
    memo = Memo.query.get_or_404(memo_id)
    # 削除処理
    db.session.delete(memo)
    db.session.commit()
    # 画面遷移
    return redirect(url_for("index"))


# エラーハンドラー
@app.errorhandler(NotFound)
def show_404_page(error):
    msg = error.description
    print("エラー内容：", msg)
    return render_template("errors/404.html", msg=msg), 404
