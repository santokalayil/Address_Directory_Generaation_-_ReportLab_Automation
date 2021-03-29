import sqlite3
import pandas as pd
import os


class basic_query:

    def __init__(self, db_url):
        self.db_url = db_url

    def query(self, q, out=False, description=False):
        conn = sqlite3.connect(self.db_url)
        cur = conn.cursor()
        cur.execute(q)
        output = cur.fetchall() if out else None
        conn.commit()
        cur.close()
        if description:
            return output, cur.description
        else:
            return output

    def sql_dataframe(self, q):
        """Function to output dataframe from sql query """
        output, cur_description = self.query(q, out=True, description=True)
        # print(cur_description)
        cols = [i[0] for i in cur_description]
        return pd.DataFrame(output, columns=cols)


class family_query(basic_query):

    def __init__(self, fam_id, db_url):
        super().__init__(db_url)
        self.fam_id = fam_id

    @property
    def head(self):
        fam_data = self.sql_dataframe('''SELECT head_of_family from base_view
                                        WHERE famid = {}; '''.format(self.fam_id)).loc[0]
        return fam_data.get('head_of_family')

    @property
    def current_address_and_email(self):
        fam_data = self.sql_dataframe('''SELECT
                      c.house_flat_no, c.house_building_name, c.street, c.locality, c.city, c.pin, f.email
                      FROM families as f left join cur_addr as c on c.famid = f.famid

            WHERE f.famid = {}; '''.format(self.fam_id)).loc[0]
        return fam_data

    @property
    def native_address(self):
        fam_data = self.sql_dataframe('''SELECT 
                      n.house_name, n.po, n.place, n.district, n.state, n.pin
                      FROM families as f 
                      left join nat_addr as n
                          on n.famid = f.famid

            WHERE f.famid = {}; '''.format(self.fam_id)).loc[0]
        return fam_data

    @property
    def native_parish_details(self):
        fam_data = self.sql_dataframe('''SELECT name, place, diocese from nat_parish
                                        WHERE famid = {}; '''.format(self.fam_id)).loc[0]
        return fam_data
