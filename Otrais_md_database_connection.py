import mysql.connector

try:
    # Izveidojiet savienojumu
    connection = mysql.connector.connect(
        host="school",
        user="root",
        password="",
        database="otrais_md_datubāze"
    )
    
    # Pārbaudiet, vai savienojums ir veiksmīgs
    if connection.is_connected():
        print("Savienojums ar MySQL ir veiksmīgs!")
        
except mysql.connector.Error as e:
    print(f"Kļūda pieslēdzoties MySQL: {e}")
finally:
    # Aizveriet savienojumu
    if connection.is_connected():
        connection.close()
        print("Savienojums ir aizvērts.")