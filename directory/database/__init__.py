#!/usr/bin/env python

import sqlite3
import pandas as pd
import os

database_url = os.path.join('database', 'sqlite.db')

# functions

def Q(q, database_url, out=False, description=False):
    db_file = database_url
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(q)
    output = cur.fetchall() if out else None
    conn.commit()
    cur.close()
    if description:
        return output, cur.description
    else:
        return output


def sql(q, database_url):
    """Function to output dataframe from sql query """
    output, cur_description = Q(q, database_url, out=True, description=True)
    # print(cur_description)
    cols = [i[0] for i in cur_description]
    return pd.DataFrame(output, columns=cols)


def df2sql(df, table_name, database_url):
    """Function to insert all the data from input pandas dataframe."""
    conn = sqlite3.connect(database_url)
    df.to_sql(table_name, conn, if_exists='replace', index = False)
    conn.commit()


def dataframe_to_sqlite():  # this is the main function
    # Members Table
    mem = pd.read_csv(os.path.join('csv_files', 'members.csv'), index_col=0).reset_index()
    # mem.columns = ['famid','member_name','rltshp','prof','if_others','phone','dob','dom','blood_group']
    mem.columns = ['famid','member_name','rltshp','prof', 'phone','dob','dom','blood_group']
    mem.phone = mem.phone.apply(lambda x: str(x).split('.')[0])

    tablename = 'members'
    # dropping if existed
    q = f'DROP TABLE IF EXISTS {tablename};'
    Q(q, database_url)

    # creating table
    q = f'''
        CREATE TABLE {tablename} --IF NOT EXISTS 
        (
           id INT PRIMARY KEY   NOT NULL,
           famid          INT    NOT NULL,
           member_name    CHAR(40) NOT NULL,
           rltshp CHAR(20) NOT NULL,
           prof        CHAR(20),
           if_others CHAR(50),
           phone CHAR(10),
           dob DATE,
           dom CHAR(20),
           blood_group Char(8),
           FOREIGN KEY (famid) REFERENCES families(famid)
        );
    '''
    Q(q, database_url)
    df2sql(mem, 'members', database_url)
    q = '''select * from members;'''
    sql(q, database_url).head()

    # Family Table
    # Note that where is Additional columns which is already contained in the current address
    fam = pd.read_csv(os.path.join('csv_files', 'families.csv'))
    cols = list(fam.columns)
    fm_map_cols = dict(
                    famid='famid',
                    timestamp='Timestamp',
                    email='Email Address',
                    # house_flat = 'House Number  / Flat Number',
                    where='Locality',
                    photo='Family Photo'
                   )
    map_dic = {val: key for (key, val) in fm_map_cols.items()}
    fm = fam[fm_map_cols.values()].copy()
    fm.columns = fm.columns.map(map_dic)

    tablename = 'families'
    # dropping if existed
    q = f'DROP TABLE IF EXISTS {tablename};'
    Q(q, database_url)

    # creating table
    q = f'''
        CREATE TABLE {tablename} --IF NOT EXISTS 
        (
           famid INT PRIMARY KEY   NOT NULL,
           timestamp    TIMESTAMP NOT NULL,
           email CHAR(40) NOT NULL,
           locality CHAR({int(fm['where'].str.len().max())}),
           photo CHAR({int(fm.photo.str.len().max())})
        );
    '''
    Q(q, database_url)
    df2sql(fm, tablename, database_url)
    sql('select * from families;', database_url).head()


    # Current Address Table

    cur_addr_map_cols = dict(
        famid='famid',
        house_flat_no='House Number  / Flat Number',
        house_building_name='House Name / Building Name',
        street='Street',
        locality='Locality',
        city='City',
        pin='Pin Code',
                   )
    map_dic = {val:key for (key, val) in cur_addr_map_cols.items()}
    cur = fam[cur_addr_map_cols.values()].copy()
    cur.columns = cur.columns.map(map_dic)
    # cur.reset_index(inplace=True)  # to get family id

    tablename = 'cur_addr'
    # dropping if existed
    q = f'DROP TABLE IF EXISTS {tablename};'
    Q(q, database_url)

    # creating table
    q = f'''
        CREATE TABLE {tablename} --IF NOT EXISTS 
        (
           id INT PRIMARY KEY   NOT NULL,
           famid INT NOT NULL,
           house_flat_no CHAR({int(cur.house_flat_no.str.len().max())}),
           house_building_name CHAR({int(cur.house_building_name.str.len().max())}),
           street CHAR({int(cur.street.str.len().max())}),
           locality CHAR({int(cur.locality.str.len().max())}),
           city CHAR({int(cur.city.str.len().max())}),
           pin CHAR(6),
           FOREIGN KEY (famid) REFERENCES families(famid)
        );
    '''
    Q(q, database_url)
    df2sql(cur, tablename, database_url)
    sql('select * from cur_addr;', database_url).head()

    # Native Address Table

    nat_addr_map_cols = dict(
        famid = 'famid',
        house_name = 'House Name',
        po = 'Post Office',
        place = 'Place',
        district='District',
        state = 'State',
        pin = 'Pin Code.1'
                   )
    map_dic = {val:key for (key, val) in nat_addr_map_cols.items()}
    nat = fam[nat_addr_map_cols.values()].copy()
    nat.columns = nat.columns.map(map_dic)
    nat['pin'] = nat.pin.apply(lambda x: str(x).split('.')[0] if len(str(x)) > 6 else str(x) if len(str(x)) == 6 else (str(x)+'_'))
    # nat.reset_index(inplace=True) # to get familly id

    tablename = 'nat_addr'
    # dropping if existed
    q = f'DROP TABLE IF EXISTS {tablename};'
    Q(q, database_url)

    # creating table
    q = f'''
        CREATE TABLE {tablename} 
        (
           id INT PRIMARY KEY   NOT NULL,
           famid INT NOT NULL,
           house_name CHAR({int(nat.house_name.str.len().max())}),
           po CHAR({int(nat.po.str.len().max())}),
           place CHAR({int(nat.place.str.len().max())}),
           district CHAR({int(nat.district.str.len().max())}),
           state CHAR({int(nat.state.str.len().max())}),
           pin CHAR(6),
           FOREIGN KEY (famid) REFERENCES families(famid)
        );
    '''
    Q(q, database_url)
    df2sql(nat, tablename, database_url)
    sql(f'select * from {tablename};', database_url).head()

    # ## Native Parish Table

    nat_parish_map_cols = dict(
        famid = 'famid',
        name = 'Name of Native Parish',
        place = 'Place of Native Parish',
        diocese='Diocese of the Native Parish'
        )
    map_dic = {val:key for (key, val) in nat_parish_map_cols.items()}
    nat_parish = fam[nat_parish_map_cols.values()].copy()
    nat_parish.columns = nat_parish.columns.map(map_dic)
    # nat_parish.reset_index(inplace=True) # to get familly id

    tablename = 'nat_parish'
    # dropping if existed
    q = f'DROP TABLE IF EXISTS {tablename};'
    Q(q, database_url, False)

    # creating table
    q = f'''
        CREATE TABLE {tablename} --IF NOT EXISTS 
        (
           id INT PRIMARY KEY   NOT NULL,
           famid INT NOT NULL,
           name CHAR({int(nat_parish.name.str.len().max())}),
           place CHAR({int(nat_parish.place.str.len().max())}),
           diocese CHAR({int(nat_parish.diocese.str.len().max())}),
           FOREIGN KEY (famid) REFERENCES families(famid)
        );
    '''
    Q(q, database_url, False)
    df2sql(nat_parish, tablename, database_url)
    sql(f'select * from {tablename};', database_url).head()


    # ## Creating Base View


    Q('''drop view if exists base_view;''', database_url)
    Q('''create view base_view as
            select members.famid, member_name as head_of_family, prof, phone, street, locality, nat_addr.place, photo
            from members 
                left join families on members.famid = families.famid
                left join cur_addr on families.famid = cur_addr.famid
                left join nat_addr on families.famid = nat_addr.famid
                left join nat_parish on families.famid = nat_parish.famid
            where members.rltshp = 'Self'
        ;''', database_url)

    sql('''select * from base_view;''', database_url).to_csv(os.path.join('csv_files', 'base_view.csv'), index=False)
    sql('''select * from base_view;''', database_url)
    print("Data is copied over to sqlite database from preprocessed csv file!")
