import sqlite3

DB_FILE = "database.db"
SCHEMA_FILE = "schema.sql"

def init_db():
    with sqlite3.connect(DB_FILE) as con:
        con.execute("PRAGMA foreign_keys = ON")
        with open(SCHEMA_FILE, "r") as f:
            con.executescript(f.read())
    print("Tietokanta luotu ja indeksit lisätty!")

if __name__ == "__main__":
    init_db()