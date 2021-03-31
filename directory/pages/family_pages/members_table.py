from directory.database.get import basic_query
import os
from directory.settings import  *
from directory.settings import db_url
from reportlab.lib import colors

def members_table_section(fam_id, db_url=db_url):
    from directory.database.get import basic_query
    sql = basic_query(db_url).sql_dataframe

    table_header = ["Name", "Relationship", "Profession", "Phone", "DOB", "DOM/DOO", "Blood"]
    members_df = sql(f'''SELECT * FROM members WHERE famid = {fam_id};''')
    members_data = []
    members_data.append(table_header)
    for i in range(members_df.shape[0]):
        member_series = members_df.loc[i]
        member_data = [member_series["member_name"], member_series['rltshp'], member_series['prof'],
                        member_series['phone'], member_series['dob'], member_series['dom'], member_series['blood_group']]
        members_data.append(member_data)

    from reportlab.platypus import Table as RLTable
    from reportlab.platypus import TableStyle

    # AUTOMATIC LENGTH CALCULATION SYSTEM>>>
    lengths_col = [max([len(str(members_data[row_idx][col_idx])) for row_idx in range(len(members_data))]) for col_idx in
                    range(len(members_data[0]))]
    pct_len_col = list(map(lambda x: x / sum(lengths_col), lengths_col))
    col_widths = list(map(lambda x: PAGE_FRAME_WIDTH * x, pct_len_col))

    row_height = 16
    members_table = RLTable(members_data, colWidths=col_widths, rowHeights=[row_height for i in range(len(members_data))])

    # setting styles
    members_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.2, 0.2, 0.3)),
                                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                                ("ALIGN", (0,0), (-1, 0), "CENTER"), # align only the header row.. if not end cell shoudl be (-1,-1)
                                ("FONTNAME", (0,0), (-1, 0), "yanone"),  # header font
                                ("FONTSIZE", (0,0), (-1, 0), 9),  # header font size
                                ("FONTNAME", (0, 1), (-1, -1), "oswald_extralight"),  # other row fonts
                                ("FONTSIZE", (0, 1), (-1, -1), 8),  # font size of other rows
                                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                                ("ALIGN", (1, 0), (-1, -1), "CENTER"),  # all columns except name center align
                                ]))

    internal_border_color = colors.white
    start = 1
    # adding horizontal lines as borders
    for i in range(start, len(members_data)):  # 1 because don't want header row to have horizontal line
        table_style = TableStyle([("LINEABOVE", (0, i), (-1, i), 0.1, internal_border_color), ])
        members_table.setStyle(table_style)

    # adding vertical lines as borders
    for i in range(start, len(members_data[0])):  # 1 because don't want header row to have vertial line
        table_style = TableStyle([("LINEBEFORE", (i, 1), (i, -1), 0.1,
                                    internal_border_color), ])  # (i, 1) is neccesory to avoid header vert line
        members_table.setStyle(table_style)

    return members_table