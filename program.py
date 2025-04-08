import mysql.connector
from datetime import datetime

def connect_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zakat_db"
        )
    except mysql.connector.Error as e:
        print(f"Error: Gagal koneksi ke database - {str(e)}")
        exit(1)

def create_beras_table():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS beras (
            id INT AUTO_INCREMENT PRIMARY KEY,
            harga DECIMAL(10,2)
        )
    ''')
    db.commit()

#beras db
def tampilkan_data_beras():
    db = connect_db()
    cursor = db.cursor()
    try:
        print("\n=== Data Beras ===")
        cursor.execute("SELECT * FROM beras")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(f"ID: {row[0]}, Harga: Rp {row[1]:,.2f}")
        else:
            print("Tidak ada data beras.")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        cursor.close()
        db.close()

def tambah_data_beras():
    db = connect_db()
    cursor = db.cursor()
    try:
        print("\n=== Tambah Data Beras ===")
        harga = float(input("Masukkan harga beras per Liter: Rp "))
        
        cursor.execute('''
            INSERT INTO beras (harga)
            VALUES (%s)
        ''', (harga,))
        db.commit()
        print("\nHarga beras berhasil ditambahkan!")
        
    except ValueError:
        print("Error: Harga harus berupa angka!")
    except Exception as e:
        print(f"Error: {str(e)}")



try:
    db = connect_db()
    cursor = db.cursor()
    create_beras_table()
except mysql.connector.Error as e:
    print(f"Database connection failed: {e}")
    exit(1)

try:
    while True:
        print("\n=== Menu ===")
        print("1. Tambah Data Beras")
        print("2. Tampilkan Data Beras")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == '1':
            tambah_data_beras()
        elif pilihan == '2':
            tampilkan_data_beras()
        elif pilihan == '3':
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid!")
finally:
    cursor.close()
    db.close()