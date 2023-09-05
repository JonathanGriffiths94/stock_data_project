from pathlib import Path

if __name__ == "__main__":
    print("Initialising database")
    for sqlfile in sorted(
        list((Path("devops") / "db" / "schema_upgrades").glob("*.sql"))
    ):
        with open(sqlfile, "r") as f:
            print(sqlfile)
            query = f.read()
