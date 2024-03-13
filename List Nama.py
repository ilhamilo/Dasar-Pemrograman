users = {
    'Agung': {'password': '156'},
    'Ozan': {'password': '182'},
    'Safril': {'password': '186'},
    'Destito': {'password': '180'},
    'Salwan': {'password': '159'},
    'Ridho': {'password': '153'},
    'Gatshu': {'password': '181'},
    'Nabil': {'password': '163'},
    'Sagri': {'password': '152'},
    'Atex': {'password': '173'},
    
}

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username in users and users[username]['password'] == password:
        print("Selamat Datang Di Dasar Pemrogaman ") 
else:
        print("Username & Password yang di masukkan salah")