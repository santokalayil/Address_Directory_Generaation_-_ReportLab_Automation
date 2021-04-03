from pandas import to_datetime, merge
from numpy import arange
import os
import pandas as pd
import numpy as np

from directory.settings import db_url
from directory.database.get import basic_query




def generate():
    sql = lambda q: basic_query(db_url).sql_dataframe(q)  # view query function
    df = sql('''select * from members;''')
    df = df[df.prof!="Priest"]
    df = df[(df.dom!=' ') ][['famid','member_name','rltshp','dom']] # & (df.dom.isna())
    df = df[(df.dom!='')]

    df.dom = to_datetime(df.dom).dt.date
    hof = sql('''select famid, member_name as head_of_family from members where rltshp = "Self"''')
    df = merge(left=df, right=hof, how='inner', on='famid') # merge with main df + head of family

    t = pd.DataFrame(df.groupby(['famid','dom'])['member_name'].count())

    # foreseeing possible error of wrongly pairing the couples if same dom for another couple in same family
    if t[t.member_name>2].shape[0] != 0:
        import sys
        print("ISSUE!: More than one pairs with same date of marriage in a family. \nExiting.. Please Correct the Issue First")
        sys.exit(0)

    # finding odd members
    #famids = set([mult_idx[0] for mult_idx in t[t.member_name<2].index])
    # df[df.famid.isin(famids)]

    ann = pd.DataFrame(columns=['famid','couple','dom','head of family'])

    for famid in df.famid.unique():
        fm = df[df.famid==famid]
    #     print(fm)
        for dom in fm.dom.unique():
            filt = (df["dom"]==dom) & (df.famid==famid)
            c = df[filt] # should satisfy both dom and famid
            # get family id of the couple and checking if unique single count
            if len(c.famid.unique()) != 1:
                print("Error\n", (50*"-")+"\n", famid, dom)
            f_id = c.famid.unique()[0] if len(c.famid.unique()) == 1 else "Error"
            dom = c.dom.unique()[0] if len(c.dom.unique()) == 1 else "Error"
            hof = c.head_of_family.unique()[0] if len(c.head_of_family.unique()) == 1 else "Error"
            couple_names = " & ".join(list(df[filt].member_name))
            c_df = pd.DataFrame({'famid':[f_id], 'couple':[couple_names], 'dom':[dom], 'head of family':[hof],})
            ann = ann.append(c_df)
    ann.index = range(1, ann.shape[0]+1)

    # adding month names and dates and ordering according to it
    wa = ann
    wa['month'] = pd.to_datetime(wa.dom).dt.month_name()
    wa['month_order'] = pd.to_datetime(wa.dom).dt.month
    wa['day'] = pd.to_datetime(wa.dom).dt.day
    wa = wa.sort_values(by=['month_order', 'day']).reset_index(drop=True)
    wa['no'] = np.arange(1, len(wa) + 1)
    wa = wa[['no', 'couple','month','day', 'head of family']]
    return wa