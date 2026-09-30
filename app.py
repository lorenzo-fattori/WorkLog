from datetime import date
from pathlib import Path
import sqlite3

from flask import Flask, flash, g, redirect, render_template, request, url_for


BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "worklog.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-secret-key"

MONTH_NAMES = [
    "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno",
    "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre",
]


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_error):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            work_date TEXT NOT NULL,
            hours REAL NOT NULL CHECK(hours > 0 AND hours <= 24),
            UNIQUE(work_date)
        )
        """
    )
    db.commit()


def month_data(year, month):
    db = get_db()
    entries = db.execute(
        """
        SELECT id, work_date, hours
        FROM entries
        WHERE work_date >= ? AND work_date < ?
        ORDER BY work_date DESC
        """,
        (f"{year:04d}-{month:02d}-01", f"{year + (month == 12):04d}-{1 if month == 12 else month + 1:02d}-01"),
    ).fetchall()
    total = sum(entry["hours"] for entry in entries)
    return entries, total


def month_url(year, month):
    return url_for("month", year=year, month=month)


@app.route("/")
def index():
    today = date.today()
    return redirect(month_url(today.year, today.month))


@app.route("/month/<int:year>/<int:month>")
def month(year, month):
    if month < 1 or month > 12:
        return redirect(url_for("index"))

    entries, total = month_data(year, month)
    previous_month = month - 1 or 12
    previous_year = year - (month == 1)
    next_month = month + 1 if month < 12 else 1
    next_year = year + (month == 12)

    db = get_db()
    year_total = db.execute(
        "SELECT COALESCE(SUM(hours), 0) FROM entries WHERE work_date LIKE ?",
        (f"{year:04d}-%",),
    ).fetchone()[0]

    return render_template(
        "month.html",
        entries=entries,
        total=total,
        year_total=year_total,
        year=year,
        month=month,
        month_name=MONTH_NAMES[month - 1],
        today=date.today().isoformat(),
        previous_url=month_url(previous_year, previous_month),
        next_url=month_url(next_year, next_month),
    )


@app.post("/entries")
def add_entry():
    work_date = request.form.get("work_date", "")
    hours_value = request.form.get("hours", "")

    try:
        selected_date = date.fromisoformat(work_date)
        hours = float(hours_value)
        if hours <= 0 or hours > 24:
            raise ValueError
    except (TypeError, ValueError):
        flash("Inserisci una data valida e un numero di ore tra 0,25 e 24.", "error")
        return redirect(request.referrer or url_for("index"))

    db = get_db()
    try:
        db.execute(
            "INSERT INTO entries (work_date, hours) VALUES (?, ?)",
            (selected_date.isoformat(), hours),
        )
        db.commit()
        flash("Giornata aggiunta al registro.", "success")
    except sqlite3.IntegrityError:
        flash("Esiste già una registrazione per questo giorno.", "error")

    return redirect(month_url(selected_date.year, selected_date.month))


@app.post("/entries/<int:entry_id>/delete")
def delete_entry(entry_id):
    db = get_db()
    entry = db.execute("SELECT work_date FROM entries WHERE id = ?", (entry_id,)).fetchone()
    if entry is not None:
        work_date = date.fromisoformat(entry["work_date"])
        db.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
        db.commit()
        flash("Registrazione eliminata.", "success")
        return redirect(month_url(work_date.year, work_date.month))

    flash("Registrazione non trovata.", "error")
    return redirect(url_for("index"))


with app.app_context():
    init_db()


if __name__ == "__main__":
    app.run(debug=True)
