## BAB VII Struktur Project Flask REST API

### Untuk menjalankan project
1. Clone Repository ini atau download manual dengan format zip.
2. Extract folder BAB VII, kemudian buka vscode pada direktori folder tersebut.
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
7. Install Libray `flask` dan `python-dotenv` dengan perintah pada terminal:
    ```shell
    pip install flask python-dotenv
    # atau jika gagal
    pip3 install flask python-dotenv
    ```
8. Jalankan server dengan menjalankan perintah `flask run` pada terminal
