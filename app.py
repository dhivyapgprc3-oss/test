from __future__ import annotations

import os
import sqlite3
from typing import List, Dict

from flask import Flask, render_template, jsonify, g

APP = Flask(__name__)
DB_PATH = "/workspace/app.db"


def get_db_connection() -> sqlite3.Connection:
    if "db_connection" not in g:
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row
        g.db_connection = connection
    return g.db_connection


@APP.teardown_appcontext
def close_db_connection(exception: BaseException | None) -> None:
    connection: sqlite3.Connection | None = g.pop("db_connection", None)
    if connection is not None:
        connection.close()


@APP.route("/")
def index() -> str:
    return render_template("index.html")


@APP.route("/api/table", methods=["GET"])
def get_table_data():
    connection = get_db_connection()
    rows = connection.execute("SELECT col_left, col_right FROM items ORDER BY id ASC;").fetchall()
    data: List[Dict[str, str]] = [
        {"col_left": row["col_left"], "col_right": row["col_right"]} for row in rows
    ]
    return jsonify({"rows": data, "count": len(data)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    APP.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)