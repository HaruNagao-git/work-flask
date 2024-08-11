from flask import Flask
from flask_migrate import Migrate
from models import db

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

app.config.from_object("config.Config")  # 設定ファイル読み込み
db.init_app(app)  # dbとFlaskとの紐付け
migrate = Migrate(app, db)  # マイグレーションとの紐付け(Flaskとdb)

from views import *

# ==================================================
# 実行
# ==================================================
if __name__ == "__main__":
    app.run()
