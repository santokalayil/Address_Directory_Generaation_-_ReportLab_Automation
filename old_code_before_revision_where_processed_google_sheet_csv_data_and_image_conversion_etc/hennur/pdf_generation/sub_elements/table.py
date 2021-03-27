

def generate_family_table(fam_id):
    from database.get import basic_query
    import os
    sql = basic_query(os.path.join("database", "sqlite.db")).sql_dataframe

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

    members_table = RLTable(members_data, colWidths=col_widths, )

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







# imports
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.pdfbase import pdfmetrics

# constants
from pdf_generation.page_settings import PAGE_FRAME_WIDTH

PAGE_FRAME_SIZE = 324.85039370078744  # this bcz of circular import

# register a new font
pdfmetrics.registerFont(TTFont('merriweather','fonts/merriweather/Merriweather-Black.ttf'))
pdfmetrics.registerFont(TTFont('yanone','fonts/yanone/YanoneKaffeesatz-Light.ttf'))
pdfmetrics.registerFont(TTFont('oswald_regular', 'fonts/oswald/Oswald-Regular.ttf'))
pdfmetrics.registerFont(TTFont('oswald_semibold', 'fonts/oswald/Oswald-SemiBold.ttf'))
pdfmetrics.registerFont(TTFont('oswald_medium', 'fonts/oswald/Oswald-Medium.ttf'))
pdfmetrics.registerFont(TTFont('oswald_light', 'fonts/oswald/Oswald-Light.ttf'))
pdfmetrics.registerFont(TTFont('oswald_extralight', 'fonts/oswald/Oswald-ExtraLight.ttf'))

# styling
from reportlab.platypus import TableStyle
from reportlab.lib import colors

# base table style
def Table(data):

	DEFAULT_COL_WIDTH = PAGE_FRAME_SIZE / 7

	from reportlab.platypus import Table as RLTable

	# AUTOMATIC LENGTH CALCULATION SYSTEM>>>
	lengths_col = [max([len(str(data[row_idx][col_idx])) for row_idx in range(len(data))]) for col_idx in range(len(data[0]))]
	pct_len_col = list(map(lambda x: x / sum(lengths_col) , lengths_col))
	COL_WIDTHS = list(map(lambda x: PAGE_FRAME_WIDTH * x, pct_len_col))

	table = RLTable(data, colWidths=COL_WIDTHS,)
	table_style = TableStyle([
			("BACKGROUND", (0,0), (-1, 0), colors.Color(0.2, 0.2, 0.3)), # bg, startin cell (0,0), ending_cell (6, 0) # ReportLabFidBlue
			("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
			("ALIGN", (0,0), (-1, 0), "CENTER"), # align only the header row.. if not end cell shoudl be (-1,-1)
			("FONTNAME", (0,0), (-1, 0), "yanone"), # header font
			("FONTSIZE", (0,0), (-1, 0), 9), # header font size
			#("BOTTOMPADDING", (0,0), (-1, 0), 12), # last one px 12 px pading is given

			("FONTNAME", (0,1), (-1, -1), "oswald_extralight"), # other row fonts
			("FONTSIZE", (0,1), (-1, -1), 8), # font size of other rows
			("BACKGROUND", (0,1), (-1, -1), colors.beige),

			("ALIGN", (1,0), (-1, -1), "CENTER"), # all columns except name center align

			#("GRID", (0,0), (-1, -1), 0.1, colors.black), # Grid to all columns arnd rows

		])
	table.setStyle(table_style)

	# borders
	# table_style = TableStyle([("BOX", (0,0), (-1, -1), 0.1, colors.black), ]) # box, start ,end, thickness, color
	# table.setStyle(table_style)

			# ("LINEBEFORE", (2,1), (2, -1), 0.1, colors.red),
			# ("LINEABOVE", (0,2), (-1, 2), 0.1, colors.green),

	internal_border_color = colors.white
	start = 1

	# adding horizontal lines as borders
	for i in range(start, len(data)): # 1 because don't want header row to have horizontal line
		table_style = TableStyle([("LINEABOVE", (0,i), (-1, i), 0.1, internal_border_color), ])
		table.setStyle(table_style)

	# adding vertical lines as borders
	for i in range(start, len(data[0])): # 1 because don't want header row to have vertial line
		table_style = TableStyle([("LINEBEFORE", (i,1), (i, -1), 0.1, internal_border_color), ]) # (i, 1) is neccesory to avoid header vert line
		table.setStyle(table_style)

	return table




