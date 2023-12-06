from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# DB ADDRESS CONFIG
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "flask_latihan"

mysql = MySQL(app)

# Session Secret Key
app.secret_key = "INI_RAHASIA"

@app.route("/")
def index():
    # Jika user logged in
    if 'is_logged_in' in session:
        # mysql cursor
        cur = mysql.connection.cursor()

        # Eksekusi query
        cur.execute("SELECT * FROM users")

        # Tampung hasil query
        data = cur.fetchall()

        # Tutup koneksi
        cur.close()

        return render_template('index.html', data=data, username=session['username'])
    else:
        # Jika session tidak ada, alihkan ke halaman login
        return redirect(url_for('login'))

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # Ambil data dari form html
        email = request.form['inpEmail']
        passwd = request.form['inpPass']

        # Mysql Cursor
        cur = mysql.connection.cursor()

        # Eksekusi query 
        cur.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email,passwd))

        # Tampung hasil
        user = cur.fetchone()

        if user:
            # Session Dibuat
            session['is_logged_in'] = True
            session['username'] = user[1]

            # Redirect
            return redirect(url_for('index'))
        else:
            # Jika email atau password salah
            pesanError = "Cek email dan password kamu"
            return render_template("login.html", msg=pesanError)

    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    # Hapus session
    session.pop('is_logged_in', None)
    session.pop('username', None)

    return redirect(url_for('login'))



if __name__ == "__main__":
    app.run(debug=True)