from directory.database.get import basic_query
import os
# from reportlab.platypus import Paragraph, Spacer
# from reportlab.lib.styles import ParagraphStyle

def family_common_data(fam_id, db_url='sqlite.db'):
    sql = basic_query(db_url).sql_dataframe
    # head of famliy
    head_of_family = sql(f'''SELECT * FROM members where famid={fam_id} AND rltshp="Self"''').loc[0].member_name

    # current_address and email
    print(f"FamID {fam_id} - {head_of_family}")
    print(sql(f'''SELECT * FROM families where famid={fam_id}'''))
    # print(f'''SELECT * FROM families where famid={fam_id}''')
    email = sql(f'''SELECT * FROM families where famid={fam_id}''').loc[0].email.strip()
    email_text = f"Email: {email}" if email else ' '
    # print(f'''SELECT * FROM cur_addr where famid={fam_id}''')
    ca_list = list(
        sql(f'''SELECT * FROM cur_addr where famid={fam_id}''').loc[0, 'house_flat_no':'pin'].to_dict().values())
    ca_list = [i for i in ca_list if (i != '') or (i != '')]
    current_address_text = ', '.join([str(i).strip() for i in ca_list])  # we can change later
    current = f'''Current Address:\n{current_address_text}'''

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

    # para_style = ParagraphStyle(name='Normal', fontName='oswald_light', fontSize=8,
    #                             spaceAfter=0, spaceBefore=0, leading=10)

    current_address = current + '. ' + email_text
    # current_address = Paragraph(current + '. ' + email_text, style=para_style)
    # email = Paragraph(email_text, style=para_style)
    # native_address = Paragraph(native, style=para_style)
    native_address = native
    native_parish = parish_name
    # native_parish = Paragraph(parish_name, style=para_style)
    diocese = diocese
    # diocese = Paragraph(diocese, style=para_style)

    text = {"current_address": current_address,
            "email": email,
            "native_address": native_address,
            "native_parish": native_parish,
            "diocese": diocese,
            }

    dictionary = {'head': head_of_family, 'text': text} # 'family_photo': fm_img, 
    return dictionary