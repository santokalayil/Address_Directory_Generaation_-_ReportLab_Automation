from database.post import post_query
import os
import sys
import pandas as pd


def process():
    print("getting csv files after manual edit")
    manually_edited_csv_files_folder = os.path.join('database', 'csv_after_manual_edit')
    print(f"Checking for the post_processed csv file in the folder '{manually_edited_csv_files_folder}'")

    def are_files_in_folder(folder):
        folder_files = os.listdir(folder)
        needed_files = ['families.csv', 'members.csv']
        if ('families.csv' in folder_files) and ('members.csv' in folder_files):
            print(f"Found files {', '.join(needed_files)}")
            return True
        else:
            print(f"One or more the files in the folder '{folder}' is missing! exiting...")
            sys.exit(1)

    if are_files_in_folder(manually_edited_csv_files_folder):
        print("Continuing to update the sqlite db")

    def delete_records_from_families_sqlite_table(fam_id=6):  # manoj record removal
        table_names = ["families", 'cur_addr', 'nat_addr', 'nat_parish', 'members']

        for table_name in table_names:
            qry = f'''
            DELETE FROM {table_name}
            WHERE famid = {fam_id};
            '''
            sqlite_db_path = os.path.join('database', 'sqlite.db')
            post_query(qry, sqlite_db_path)
        print(f"Removed from all tables fam_id record of id: {fam_id}", end='\r')

    delete_records_from_families_sqlite_table()  # ---- one time removal

    def update_families_sqlite_table(fam_id):
        table_name = "families"
        family = families.loc[families['famid'] == fam_id].reset_index().T.iloc[:,
                 0]  # reset index is done later bcz of problems

        email = family['Email Address']
        where = family['Locality']

        qry = f'''
        UPDATE {table_name}
        SET email = "{email}", "where" = "{where}"
        WHERE famid = {fam_id};
        '''
        sqlite_db_path = os.path.join('database', 'sqlite.db')
        post_query(qry, sqlite_db_path)
        print(f"Updated {table_name} table's fam_ids until number {fam_id}", end='\r')

    def update_cur_addr_sqlite_table(fam_id):
        table_name = "cur_addr"
        family = families.loc[families['famid'] == fam_id].reset_index().T.iloc[:,
                 0]  # reset index is done later bcz of problems

        house_flat_no = family['House Number  / Flat Number']

        # added problem
        house_building_name = family['House Name / Building Name'] #if family['House Name / Building Name'] != '"REVA"' \
            #else (str(family['House Name / Building Name'])).strip('"')

        street = family['Street']
        locality = family["Locality"]
        city = family['City']
        pin = family["Pin Code"]

        qry = f'''
        UPDATE {table_name}
        SET house_flat_no = "{house_flat_no}", house_building_name = "{house_building_name}",
        street = "{street}", locality = "{locality}", city = "{city}", pin = "{pin}"
        WHERE famid = {fam_id};
        '''
        sqlite_db_path = os.path.join('database', 'sqlite.db')
        post_query(qry, sqlite_db_path)
        print(f"Updated {table_name} table's fam_ids until number {fam_id}", end='\r')

    def update_nat_addr_sqlite_table(fam_id):
        table_name = "nat_addr"
        family = families.loc[families['famid'] == fam_id].reset_index().T.iloc[:,0]
        # reset index is done later bcz of problems

        house_name = family['House Name']
        po = family['Post Office']
        place = family["Place"]
        district = family['District']
        state = family["State"]
        pin = family["Pin Code.1"]

        qry = f'''
        UPDATE {table_name}
        SET house_name = "{house_name}", po = "{po}",
        place = "{place}", district = "{district}", state = "{state}", pin = "{pin}"
        WHERE famid = {fam_id};
        '''
        sqlite_db_path = os.path.join('database', 'sqlite.db')
        post_query(qry, sqlite_db_path)
        print(f"Updated {table_name} table's fam_ids until number {fam_id}", end='\r')

    def update_nat_parish_sqlite_table(fam_id):
        table_name = "nat_parish"
        family = families.loc[families['famid'] == fam_id].reset_index().T.iloc[:, 0]
        # reset index is done later bcz of problems

        name = family['Name of Native Parish']
        place = family["Place of Native Parish"]
        diocese = family['Diocese of the Native Parish']

        qry = f'''
        UPDATE {table_name}
        SET name = "{name}", place = "{place}", diocese = "{diocese}"
        WHERE famid = {fam_id};
        '''
        sqlite_db_path = os.path.join('database', 'sqlite.db')
        post_query(qry, sqlite_db_path)
        print(f"Updated {table_name} table's fam_ids until number {fam_id}", end='\r')

    def update_members_sqlite_table(members_table):
        members = members_table
        table_name = 'members'
        for i in range(members.shape[0]):
            famid, member_name = members.iloc[i]['famid'], members.iloc[i]['Name of the Family Member']
            member = members.loc[(members['famid'] == famid) & (members['Name of the Family Member'] == member_name)] \
                         .reset_index().T.iloc[:, 0]

            member_name = member["Name of the Family Member"]
            rltshp = member["Relationship with the Head of the Family"]
            prof = member["Profession"]
            phone = member["Phone Number"]
            dob = member["Date of Birth"]
            dom = member["Date of Marriage / Ordination / Profession"]
            blood_group = member["Blood Group"]

            qry = f''' 
            UPDATE {table_name}
            SET member_name = "{member_name}", rltshp = "{rltshp}", prof = "{prof}",
            phone = "{phone}", dob = "{dob}", dom = "{dom}", blood_group = "{blood_group}"
            WHERE (member_name = "{member_name}") AND (famid = {famid});
            '''
            sqlite_db_path = os.path.join('database', 'sqlite.db')
            post_query(qry, sqlite_db_path)
            print(f"Updated record of member_name '{member_name}' of '{famid}'" + (25 * ' '), end='\r')
        print('Completed updation of members sqlite table..' + (25 * ' '))

    families = pd.read_csv(os.path.join(manually_edited_csv_files_folder, 'families.csv'))
    members = pd.read_csv(os.path.join(manually_edited_csv_files_folder, 'members.csv'))

    def date_preprocess(df, cols):
        """This function converts dob and dom columns in members to proper format and convert to string"""
        # print(df.columns)
        from datetime import datetime as dt
        for col in cols:
            print(f"CHANGING FORMAT IN M/D/Y to D/M/Y for {col}")
            def convert_date_issue(x):
                if x != ' ':
                    try:
                        return str(dt.strptime(x, '%m/%d/%Y').date().strftime('%d/%m/%Y'))
                    except:
                        return ' '
                else:
                    return ' '

            df[col] = df[col].apply(convert_date_issue)
            # df[col] = df[col].apply(lambda x: str(dt.strptime(x, '%m/%d/%Y').date()
            #                                       .strftime('%d/%m/%Y')) if x != ' ' else ' ')
        return df

    # new added...
    name = 'Johny YM'  # 12 Jan 1962 in the format of month-date-year
    members.loc[members.loc[members["Name of the Family Member"] == name].index, 'Date of Birth'] = '1/12/1962'

    members = date_preprocess(members, ['Date of Birth', 'Date of Marriage / Ordination / Profession'])

    def drop_float(number):
        number = str(number)
        delimiter = '.'
        if delimiter in number:
            number = number.split(delimiter)[0]
            return number
        else:
            return number

    members['Phone Number'] = members['Phone Number'].apply(drop_float)  # new added

    # updating all tables in  sqlite database
    def update_all_tables_in_db():
        [update_families_sqlite_table(i) for i in families.FamID.unique()] # FamID instead of famid
        print()
        [update_cur_addr_sqlite_table(i) for i in families.FamID.unique()]
        print()
        [update_nat_addr_sqlite_table(i) for i in families.FamID.unique()]
        print()
        [update_nat_parish_sqlite_table(i) for i in families.FamID.unique()]
        print()
        update_members_sqlite_table(members)
        print("Updating all Tables in  Database Completed! ")

    update_all_tables_in_db()



