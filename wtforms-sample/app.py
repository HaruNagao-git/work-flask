from flask import Flask, render_template, request

# インスタンス生成
app = Flask(__name__)

# ルーティング
from forms import UserInfoForm


# ユーザ情報：入力
@app.route("/", methods=["GET", "POST"])
def show_enter():
    # フォームの作成
    form = UserInfoForm(request.form)
    # POST
    if (
        request.method == "POST"
        and form.validate()  # form.validate==False⇒入力に問題あり
    ):
        return render_template("result.html", form=form)
    # POST以外と「form.validate()がFalse」
    return render_template("enter2.html", form=form)


# 実行
if __name__ == "__main__":
    app.run()
