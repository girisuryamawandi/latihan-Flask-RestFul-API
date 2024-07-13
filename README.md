# latihan-Flask-RestFul-API
Latihan pembuatan Restful API, menggunakan Flask, data base MySQL dan SQLAlchemy

__ Panduan menjalankan __
1. Buat database MySQL
2. Instal python module yang dengan mengunakan requirements.txt, disarankan menggunakan virtual enviroment
    - make new virtual enviroment
      > python -m venv nama_env 
    - install modul dengan menggunakan pip
      > pip install -r requirements.txt
4. Buat file config.py dengan format data variabel dari template_config.py
5. Isi user, password, database_ip dan database_name berdasarkan database yang telah ada
6. Jalankan Flask server dengan cara
   > python app.py
7. Setelah dijalankan tembak API menggunakan Postman
   - localhost/task
     dapat menggunakan get atau post method
     untuk get hanya masukkan url saja
     > localhost/task/1
     
     untuk post method body bisa diisi 
     > contoh :
     > {"title":"CT",
     > "description":"Contract Terminal",
     > "done": 0
     > }
   - localhost/task/id(angka)
     bisa menggunakan get, put, atau delete method
     contoh:
     untuk put method :
     > localhost/task/1
     dengan body
     > {"title":"CT",
     > "description":"Contract Terminal",
     > "done": 0
     > }
     
     untuk method get dan delete cukup masukann url saja
     > localhost/task/1
