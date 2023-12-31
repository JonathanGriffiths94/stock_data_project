import sqlite3
from pathlib import Path

import sqlalchemy

if __name__ == "__main__":
    print("Initialising database")

    for sqlfile in sorted(
        list((Path("devops") / "db" / "schema_upgrades").glob("*.sql"))
    ):
        with open(sqlfile, "r") as f:
            print(sqlfile)
            query = f.read()

            connection = sqlite3.connect("app.db")
            cursor = connection.cursor()
            cursor.execute(sqlalchemy.text(query))
            connection.commit()
