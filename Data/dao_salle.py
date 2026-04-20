import mysql.connector
import json
from models.salle import Salle

class DataSalle:

    def get_connection(self):
        with open("Data/config.json") as f:
            config = json.load(f)
        return mysql.connector.connect(**config)

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
        values = (salle.code, salle.libelle, salle.type, salle.capacite)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

    def get_salles(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM salle")
        rows = cursor.fetchall()

        salles = []
        for r in rows:
            salles.append(Salle(r[0], r[1], r[2], r[3]))

        conn.close()
        return salles

    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s"
        values = (salle.libelle, salle.type, salle.capacite, salle.code)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM salle WHERE code=%s"
        cursor.execute(query, (code,))
        conn.commit()
        conn.close()

    def get_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM salle WHERE code=%s"
        cursor.execute(query, (code,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Salle(row[0], row[1], row[2], row[3])
        return None

    print("Connexion à la base de données établie")
