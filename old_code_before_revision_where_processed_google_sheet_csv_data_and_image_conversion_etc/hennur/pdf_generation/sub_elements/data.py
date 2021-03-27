from database.get import basic_query
import os


def family_common_data(fam_id):
    sql = basic_query(os.path.join("database", "sqlite.db")).sql_dataframe
    # head of family
    head_of_family = sql(f'''SELECT * FROM members where famid={fam_id} AND rltshp="Self"''').loc[0].member_name

    # current_address and email
    ca_list = list(
        sql(f'''SELECT * FROM cur_addr where famid={fam_id}''').loc[0, 'house_flat_no':'pin'].to_dict().values())
    current_address = ',\n'.join([str(i).strip() for i in ca_list])  # we can change later
    email = sql(f'''SELECT * FROM families where famid={fam_id}''').loc[0].email
    ca_list = list(
        sql(f'''SELECT * FROM cur_addr where famid={fam_id}''').loc[0, 'house_flat_no':'pin'].to_dict().values())
    ca_list = [i for i in ca_list if (i != '') or (i != '')]
    current_address_text = ', '.join([str(i).strip() for i in ca_list])  # we can change later
    current = f'''Current Address:\n{current_address_text}\nEmail: {email}\n'''

    # native address
    na_series = sql(f'''SELECT * FROM nat_addr where famid={fam_id}''').loc[0, 'house_name':'pin']
    house_name = str(na_series['house_name'])
    po = f'''{str(na_series['po']).strip()} P. O.''' if len(str(na_series['po']).strip()) else ''
    the_rest = ', '.join([str(i).strip() for i in na_series['place':'pin'].values if len(str(i).strip())])
    na_list = [house_name, po, the_rest]
    native_text = ', '.join(na_list)
    native = f'''Native Place Address:\n{native_text}''' if len(native_text.strip()) else ''

    # native parish details
    nat_parish_series = sql(f'''SELECT * FROM nat_parish where famid={fam_id}''').loc[0]
    parish_name = f'''Native Parish: {str(nat_parish_series['name'])}, {str(nat_parish_series['place'])}''' \
        if len(str(nat_parish_series['name']).strip()) else ''
    diocese = f'''Diocese: {str(nat_parish_series['diocese'])}''' if len(
        str(nat_parish_series['diocese']).strip()) else ''
    native_parish_details = f'''{parish_name}\n{diocese}'''

    paragraph = f'''{current}\n{native}\n\n{native_parish_details}'''
    dictionary = {'head': head_of_family, 'paragraph': paragraph}
    return dictionary





# from pdf_generation.sub_elements.data_preprocess import preprocess # change this
#
# preprocess()





# from utilities.match_file import match_photos
# import pandas as pd
#
# import os
#
#
# class Data:
#     def __init__(self, data):
#         self.data = data
#
#     def process_data(self):
#         return self.data


def getFam(famid, merg, mem):
    com = merg[merg.famid == famid].iloc[0]

    # print(com)
    com_head = com['Name of the Family Member']

    # print(com[16:19])

    ca_ls = ', '.join([str(i).strip() for i in com[4:10].values if i not in [' ']])
    na_ls = ', '.join([str(i).strip() for i in com[10:16].values if i not in [' ']])
    em = com['Email Address']

    # print(com.index)
    # dummy
    na_par = ', '.join([str(i).strip() for i in com[16:18].values if i not in [' ']])
    na_dio = com[18].strip()
    # na_dio = na_dio
    img_link = match_photos(famid)

    # from mem table
    member = (mem[mem.famid == famid]).drop(['famid'], axis=1)
    if 'Unnamed: 0' in member.columns:
        member.drop('Unnamed: 0', axis=1, inplace=True)
    data = [list(member.iloc[memb]) for memb in range(member.shape[0])]
    data = data
    return com_head, ca_ls, em, na_ls, na_par, na_dio, data, img_link





