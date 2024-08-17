from flask import Blueprint, render_template
from flask_login import login_required
from forms import WikiForm
from wikipediaapi import Wikipedia

# Blueprint
wiki_bp = Blueprint("wiki", __name__, url_prefix="/wiki")

# 日本語版Wikipediaを利用
wiki_ja = Wikipedia("ja")


# ==================================================
# ルーティング
# ==================================================
@wiki_bp.route("/search", methods=["GET", "POST"])
@login_required
def search():
    # Form生成
    form = WikiForm()
    # POST
    if form.validate_on_submit():
        # データ入力取得
        keyword = form.keyword.data
        page = wiki_ja.page(keyword)
        disp_char = 400
        # 検索結果
        if page.exists():
            return render_template(
                "wiki/wiki_search_result.html",
                keyword=keyword,
                summary=page.summary[:disp_char],
                url=page.fullurl,
            )
        else:
            return render_template(
                "wiki/wiki_search_result.html",
                error="指定されたキーワードの結果は見つかりませんでした。",
            )

    # GET
    return render_template("wiki/wiki_search.html", form=form)
