from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

# Инициализация базы
def init_db():
    with sqlite3.connect("places.db") as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS places (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                lat REAL,
                lng REAL,
                discount TEXT,
                category TEXT
            )
        ''')

# Главная: Admin UI
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        name = request.form["name"]
        lat = request.form["lat"]
        lng = request.form["lng"]
        discount = request.form["discount"]
        category = request.form["category"]
        with sqlite3.connect("places.db") as conn:
            conn.execute("INSERT INTO places (name, lat, lng, discount, category) VALUES (?, ?, ?, ?, ?)",
                         (name, lat, lng, discount, category))
        return redirect("/admin")

    with sqlite3.connect("places.db") as conn:
        places = conn.execute("SELECT * FROM places").fetchall()
    return render_template("admin.html", places=places)

# Удаление
@app.route("/delete/<int:id>")
def delete(id):
    with sqlite3.connect("places.db") as conn:
        conn.execute("DELETE FROM places WHERE id = ?", (id,))
    return redirect("/admin")

# API для Mini App
@app.route("/api/places")
def get_places():
    with sqlite3.connect("places.db") as conn:
        places = conn.execute("SELECT name, lat, lng, discount FROM places").fetchall()
    return jsonify([
        {"name": name, "lat": lat, "lng": lng, "discount": discount}
        for name, lat, lng, discount in places
    ])

if __name__ == "__main__":
    init_db()
    app.run(debug=True)