## BAB IV Integrasi Flask dengan Database MySQL

### Langkah Pembuatan database
1. Nyalakan Service Apache dan Mysql pada XAMPP Control Panel.
2. Akses phpmyadmin dengan mengetikkan `localhost/phpmyadmin` pada browser.
3. Buat database baru dengan nama `flask_latihan`
4. Pada database `flask_latihan` masuk ke tab **SQL**, eksekusi query pembuatan tabel users berikut:
    ```sql
    CREATE TABLE users(
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255),    
        password VARCHAR(255),    
        email VARCHAR(255)    
    );
    ```
5. Masukkan 3 contoh data dengan query berikut:
    ```sql
    INSERT INTO users(username, password, email) VALUES
    ("John Doe", "doe123", "doe@gmail.com"),
    ("Lorem Ipsum", "lorem321", "lorem@gmail.com"),
    ("Littlefinger", "thenorth123", "lfinger@gmail.com");
    ```

### Untuk menjalankan projek
1. Clone Repository ini atau download manual dengan format zip.
2. Extract folder BAB IV, kemudian buka vscode pada direktori folder tersebut.
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
7. Install Libray `flask` dan `flask-mysqldb` dengan perintah pada terminal:
    ```shell
    pip install flask flask-mysqldb
    # atau jika gagal
    pip3 install flask flask-mysqldb
    ```
8. Jalankan server dengan menjalankan file `app.py`.
