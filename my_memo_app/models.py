from flask_sqlalchemy import SQLAlchemy

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
