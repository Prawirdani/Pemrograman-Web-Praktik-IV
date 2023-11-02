from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# DB ADDRESS CONFIG
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "flask_latihan"

mysql = MySQL(app)

@app.route("/")
def index():
    # mysql cursor
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM users")

    data = cur.fetchall()

    cur.close()

    print(data[0])

    for row in data:
        print(row)

    return render_template('index.html', data=data)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)