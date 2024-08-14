from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

# Flask-SQLAlchemyの作成
db = SQLAlchemy()


# ==================================================
# モデル
# ==================================================
class Memo(db.Model):
    # テーブル名
    __tabelname__ = "memos"
    # id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # タイトル
    title = db.Column(db.String(50), nullable=False)
    # 内容
    content = db.Column(db.Text)


# ユーザ
class User(UserMixin, db.Model):
    # テーブル名
    __tablename__ = "users"
    # id(PK)
    id = db.Column(db.Integer, primary_key=True)
    # ユーザ名
    username = db.Column(db.String(50), unique=True, nullable=False)
    # パスワード
    password = db.Column(db.String(120), nullable=False)

    # パスワードをハッシュ化して設定する
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # 入力したパスワードとハッシュ化されたパスワードの比較
    def check_password(self, password):
        return check_password_hash(self.password, password)
