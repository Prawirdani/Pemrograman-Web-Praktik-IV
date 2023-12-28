## BAB IX Database Migration

### Untuk menjalankan project
1. Clone Repository ini atau download manual dengan format zip.
2. Extract folder BAB IX, kemudian buka vscode pada direktori folder tersebut.
3. Buka terminal vscode.
4. Inisiasi *Virtual Environtment*, dengan perintah:
    ```shell
    virtualenv env
    # atau jika perintah diatas tidak berhasil
    py -m venv env 
    # atau
    python -m venv env
    # atau
    python3 -m venv env
    ```
5. Jika pada direktori projek terdapat folder env, maka python *Virtual Environtment* berhasil di inisiasi.
6. Mengaktifkan *Virtual Environtment*, pada terminal ketikkan perintah:
    ```shell
    env\scripts\activate
    # Jika tidak berhasil, coba gantikan terminal dari powershell menjadi command prompt.
    ```
7. Install Libray `flask`, `python-dotenv`, `flask-sqlalchemy`, `flask-migrate` dan `pymysql`  dengan perintah pada terminal:
    ```shell
    pip install flask python-dotenv flask-sqlalchemy flask-migrate pymysql
    # atau jika gagal
    pip3 install flask python-dotenv flask-sqlalchemy flask-migrate pymysql
    ```
8. Jalankan server dengan menjalankan perintah `flask run` pada terminal

### Untuk Menjalankan Migrasi
1. Pastikan telah membuat database dengan nama sesuai pada variabel `DB_DATABASE` di file environment `.flaskenv`
2. Apply Migrations untuk membuat tabel users dan todos dengan perintah ketikkan perintah `flask db upgrade` pada terminal.