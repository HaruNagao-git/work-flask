from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from models import User, db

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

app.config.from_object("config.Config")  # 設定ファイル読み込み
db.init_app(app)  # dbとFlaskとの紐付け
migrate = Migrate(app, db)  # マイグレーションとの紐付け(Flaskとdb)

# LoginManagerインスタンス
login_manager = LoginManager()
# LoginManagerとFlaskとの紐付け
login_manager.init_app(app)
# ログインが必要なページにアクセスしようとしたときに表示されるメッセージを変更
login_manager.login_message = "認証していません：ログインしてください"
# 未認証のユーザがアクセスしようとした際にリダイレクトされる関数名を設定する
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from views import *  # viewsから全ての関数をインポート(コードの位置大事！！！)

# ==================================================
# 実行
# ==================================================
if __name__ == "__main__":
    app.run()
