from flask import Flask
from flask_migrate import Migrate
# ▼▼▼ リスト 11-3の追加 ▼▼▼
from models import db, User
from flask_login import LoginManager
# ▲▲▲ リスト 11-3の追加 ▲▲▲

# ==================================================
# Flask
# ==================================================
app = Flask(__name__)
# 設定ファイル読み込み
app.config.from_object("config.Config")
# dbとFlaskとの紐づけ
db.init_app(app)
# マイグレーションとの紐づけ（Flaskとdb）
migrate = Migrate(app, db)
# ▼▼▼ リスト 11-3の追加 ▼▼▼
# LoginManagerインスタンス
login_manager = LoginManager()
# LoginManagerとFlaskとの紐づけ
login_manager.init_app(app)
# ▼▼▼ リスト 11-9の追加 ▼▼▼
# ログインが必要なページにアクセスしようとしたときに表示されるメッセージを変更
login_manager.login_message = "認証していません：ログインしてください"
# ▲▲▲ リスト 11-9の追加 ▲▲▲
# 未認証のユーザーがアクセスしようとした際に
# リダイレクトされる関数名を設定する
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# ▲▲▲ リスト 11-3の追加 ▲▲▲

# viewsのインポート
from views import *

# ==================================================
# 実行
# ==================================================
if __name__ == "__main__":
    app.run()