import sqlite3


# ALL DATABASE INSERT COMMANDS Should come here
# dataframe to sql
def df2sql(df, table_name, database_url):
    """Function to insert all the data from input pandas dataframe."""
    conn = sqlite3.connect(database_url)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.commit()


# query to update or insert into database
def post_query(query, database_url):
    db_file = database_url
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()

