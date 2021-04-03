from pandas import to_datetime, merge
from numpy import arange
import os

from directory.settings import db_url
from directory.database.get import basic_query

def generate():
    sql = lambda q: basic_query(db_url).sql_dataframe(q)  # view query function
    df = sql('''select * from members;''')
    df.dob = to_datetime(df.dob).dt.date
    bdf = df[['famid', 'member_name', 'dob']]
    hof = sql('''select famid, member_name as head_of_family from members where rltshp = "Self"''')

    birth = merge(left=bdf, right=hof, how='inner', on='famid')
    birth['Month'] = to_datetime(birth.dob).dt.month_name()
    birth['month_order'] = to_datetime(birth.dob).dt.month
    birth['Day'] = to_datetime(birth.dob).dt.day
    birth = birth.sort_values(by=['month_order', 'Day']).reset_index(drop=True)
    birth['No'] = arange(1, len(birth) + 1)
    bday_df = birth[['No', 'Month', 'Day', 'member_name', 'head_of_family']]\
        .rename(columns={'member_name': 'Member Name', 'head_of_family': 'Head of the Family'})

    return bday_df