# routes/search.py

from flask import Blueprint, render_template, abort, request, redirect
from jinja2 import TemplateNotFound

import requests
import json

search_bp = Blueprint("search_bp", __name__,
                      template_folder='templates')


@search_bp.route('/search')
def search():

    # 關鍵字：標題
    title = request.args.get("title")

    # 關鍵字：集數
    c = request.args.get("c")

    # 關鍵字：語言
    lang = request.args.get("lang")

    # 關鍵字：調性
    to = request.args.get("to")

    # API 串接搜尋
    requestURL = "https://church-music-api.herokuapp.com/api/songs/search?lang=&c=&to=&title=" + title
    r = requests.get(requestURL)
    print("透過API搜尋, URL:", requestURL)

    if not r.status_code == 200:
        result = []
    else:
        result = json.loads(r.text)

    try:
        return render_template("result.html", songs=result, songs_num=len(result), mode="search", c=c, title=title)
    except TemplateNotFound:
        abort(404)
