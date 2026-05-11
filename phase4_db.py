import pandas as pd

def main():
    # the general pattern for any database connection:
    # 1. build a connection string
    # 2. create an engine
    # 3. query with pandas or SQL
    # 4. close the connection

    # for aquarius or similar REST-based systems
    # you use requests rather than a direct DB connection
    import requests

    # typical aquarius-style connection pattern
    base_url  = "https://your-aquarius-server.com/AQUARIUS/Publish/v2"
    api_token = "YOUR_API_TOKEN"

    headers = {"Authorization": f"Bearer {api_token}"}

    # get list of locations
    response = requests.get(
        f"{base_url}/GetLocationDescriptionList",
        headers=headers
    )

    # for SQL databases (e.g. PostgreSQL, SQL Server)
    # uv add sqlalchemy psycopg2-binary
    from sqlalchemy import create_engine, text

    # connection string format:
    # "dialect://username:password@host:port/database"
    engine = create_engine(
        "postgresql://username:password@localhost:5432/mydb"
    )

    # query directly into a dataframe — like dbGetQuery() in R
    with engine.connect() as conn:
        df = pd.read_sql(
            text("SELECT * FROM measurements WHERE year = 2022"),
            conn
        )
    print(df.head())

    # write a dataframe back to database — like dbWriteTable() in R
    with engine.connect() as conn:
        df.to_sql("measurements", conn, if_exists="append", index=False)

if __name__ == "__main__":
    main()