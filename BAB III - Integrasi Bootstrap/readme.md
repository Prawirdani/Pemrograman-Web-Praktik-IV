## BAB III Integrasi CSS Framework Bootstrap & Templating/Layouting
### Untuk menjalankan projek
1. Clone project ini atau download manual dengan format zip kemudian extract.
2. Buka vscode pada folder BAB III - Bootstrap & Layout
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
7. Install Libray `flask` dengan perintah pada terminal:
    ```shell
    pip install flask
    # atau jika gagal
    pip3 install flask
    ```
8. Jalankan server dengan menjalankan file `app.py`.