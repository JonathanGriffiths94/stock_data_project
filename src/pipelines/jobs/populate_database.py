import os
import sqlite3

import alpaca_trade_api as tradeapi

connection = sqlite3.connect("app.db")

cursor = connection.cursor()

api = tradeapi.REST(
    os.environ["ALPACA_API_KEY"], os.environ["ALPACA_API_SECRET"], base_url=""
)

assets = api.list_assets()

for asset in assets:
    print(asset.name, asset.symbol)

connection.commit()
