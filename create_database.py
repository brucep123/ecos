from pathlib import Path
import sqlite3

schema_path = Path("database/schema.sql")
database_path = Path("database/ecos.db")

with sqlite3.connect(database_path) as conn:

    with open(schema_path, "r") as schema_file:

        conn.executescript(schema_file.read())

print("Database initialized")