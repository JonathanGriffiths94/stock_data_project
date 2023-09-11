import pandas as pd


class MockData:
    def get_db_creation_data():
        return pd.DataFrame(
            data={
                "symbol": ["ADBE", "Vz", "Z"],
                "company": ["Adobe Inc.", "Verision", "Zillow"],
            }
        )
