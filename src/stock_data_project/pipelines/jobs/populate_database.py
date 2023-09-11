import os
import sqlite3

import alpaca_trade_api as tradeapi

if __name__ == "__main__":
    print("Populating database")
    connection = sqlite3.connect("app.db")

    cursor = connection.cursor()

    api = tradeapi.REST(
        key_id=os.environ["ALPACA_API_KEY"],
        secret_key=os.environ["ALPACA_API_SECRET"],
        base_url=os.environ["ALPACA_API_URL"],
    )

    assets = api.list_assets()

    for asset in assets:
        print(asset.name, asset.symbol)

    connection.commit()
