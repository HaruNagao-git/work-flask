from flask_wtf import FlaskForm
from models import Memo, User
from wtforms import PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError


# ==================================================
# Formクラス
# ==================================================
class MemoForm(FlaskForm):
    # タイトル
    title = StringField(
        "タイトル：",
        validators=[
            DataRequired("タイトルは必須入力です"),
            Length(max=10, message="10文字以下で入力してください"),
        ],
    )
    # 内容
    content = TextAreaField(
        "内容：",
    )
    # ボタン
    submit = SubmitField("送信")

    # カスタムバリデータ
    def validate_title(self, title):
        # StringFieldオブジェクトではなく、その中のデータ(文字列)をクエリに渡す必要があるため
        # 以下のようにtitle.dataを使用して、StringFieldから実際の文字列データを取得する
        memo = Memo.query.filter_by(title=title.data).first()
        if memo:
            raise ValidationError(
                f"タイトル '{title.data}' は既に存在します。\
                別のタイトルを入力してください。"
            )


# ログイン用入力クラス
class LoginForm(FlaskForm):
    # ユーザ名
    username = StringField("ユーザ名：", validators=[DataRequired("ユーザ名は必須入力です")])
    # パスワード
    password = PasswordField(
        "パスワード：", validators=[Length(4, 10, "パスワードの長さは4文字以上10文字以内です")]
    )
    # ボタン
    submit = SubmitField("ログイン")

    # カスタムバリデータ
    # パスワードに英数字と記号が含まれているかチェックする
    def validate_password(self, password):
        if not (
            any(c.isalpha() for c in password.data)
            and any(c.isdigit() for c in password.data)
            and any(c in "!@#$%^&*()" for c in password.data)
        ):
            raise ValidationError("パスワードには【英数字と記号：!@#$%^&*()】を含める必要があります")


# サインアップ用入力クラス
class SignUpForm(LoginForm):
    # ボタン
    submit = SubmitField("サインアップ")

    # カスタムバリデータ
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("そのユーザ名は既に使用されています")


# Wiki検索フォーム
class WikiForm(FlaskForm):
    # 検索ワード
    keyword = StringField("検索ワード：", render_kw={"placeholder": "入力してください"})
    # 検索ボタン
    submit = SubmitField("Wiki検索")
