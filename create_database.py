import sqlite3


def main():

    with open(
        "schema.sql",
        "r",
        encoding="utf-8"
    ) as file:

        schema = file.read()

    conn = sqlite3.connect(
        "database/ecos.db"
    )

    conn.executescript(schema)

    conn.commit()

    conn.close()

    print("Database created.")


if __name__ == "__main__":
    main()