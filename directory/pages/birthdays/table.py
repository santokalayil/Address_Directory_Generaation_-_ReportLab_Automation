from reportlab.lib import colors
from directory.settings import *
# from pdf_generation.pages.birthdays import dataframe
from .dataframe import generate as dataframe
from reportlab.platypus import Table, TableStyle, PageBreak, Paragraph


def generate():
    df = dataframe()
    # page title
    page_title = (" ".join(list("birthdays"))).upper()
    title_col_style = TableStyle(
        [
            # ('GRID', (0, 0), (-1, -1), 0.5, colors.cadetblue),
            ("BACKGROUND", (0, 0), (-1, -1), colors.Color(0.1, 0.5, 0.6)),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
            ("FONT", (0, 0), (-1, -1), 'oswald_semibold', 10),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]
    )
    title_single_col_table = Table([[page_title]],
                                   rowHeights=[18], colWidths=PAGE_FRAME_WIDTH,
                                   style=title_col_style
                                   )

    elements = []
    table_data = [list(df.columns)]
    width_10th = PAGE_FRAME_WIDTH / 10
    table_style = TableStyle(
        [('GRID', (0, 0), (-1, -1), 0.5, colors.cadetblue),  # INNERGRID
         ('BACKGROUND', (0, 0), (-1, 0), colors.darkslategray),  # colors.Color(0.2, 0.2, 0.3),
         ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
         ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
         ("ALIGN", (0, 0), (-1, 0), "CENTER"),  # align only the header row.. if not end cell shoudl be (-1,-1)
         ("FONTNAME", (0, 0), (-1, 0), "yanone"),  # header font
         ("FONTSIZE", (0, 0), (-1, 0), 9),  # header font size
         ("FONTNAME", (0, 1), (-1, -1), "oswald_extralight"),  # other row fonts
         ("FONTSIZE", (0, 1), (-1, -1), 8),  # font size of other rows
         ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
         ("ALIGN", (1, 0), (-1, -1), "CENTER"),  # all columns except name center align
         ]
    )

    rows_per_page = 26
    total_rows = rows_per_page + 1
    row_height = PAGE_FRAME_HEIGHT / total_rows
    row_height = row_height * 0.90  # adjusted row height bcz of grid thickness of 0.5
    for idx in range(len(df)):
        if idx == 0 or idx % rows_per_page != 0:
            table_data.append(df.loc[idx].to_list())
        else:
            # since page already consisted of 27 rows, we are appending table and restarts table creation
            element = Table(data=table_data,
                            colWidths=[width_10th, width_10th * 1.5, width_10th / 2, width_10th * 3.5,
                                       width_10th * 3.5],
                            rowHeights=[row_height for i in range(total_rows)],
                            style=table_style, hAlign=None, vAlign=None)
            page_title_content_table = Table([[title_single_col_table], [element]])
            elements.append(page_title_content_table)
            elements.append(PageBreak())
            table_data = [list(df.columns), df.loc[idx].to_list()]  # adding table headers and the row of idx

    # whatever comes after last multiple of 27 are to be added as a new table
    element = Table(data=table_data,
                    colWidths=[width_10th, width_10th * 1.5, width_10th / 2, width_10th * 3.5,
                               width_10th * 3.5],
                    rowHeights=None, style=table_style, hAlign=None, vAlign=None)
    page_title_content_table = Table([[title_single_col_table], [element]])
    elements.append(page_title_content_table)



    # table_data = [list(df.columns)] + [df.loc[idx].to_list() for idx in range(len(df))]
    # width_10th = PAGE_FRAME_WIDTH / 10
    # table_style = TableStyle(
    #     [('GRID', (0, 0), (-1, -1), 0.5, colors.cadetblue), #INNERGRID
    #      ('BACKGROUND', (0, 0), (-1, 0), colors.darkslategray),  # colors.Color(0.2, 0.2, 0.3),
    #      ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
    #      ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    #      ("ALIGN", (0, 0), (-1, 0), "CENTER"),  # align only the header row.. if not end cell shoudl be (-1,-1)
    #      ("FONTNAME", (0, 0), (-1, 0), "yanone"),  # header font
    #      ("FONTSIZE", (0, 0), (-1, 0), 9),  # header font size
    #      ("FONTNAME", (0, 1), (-1, -1), "oswald_extralight"),  # other row fonts
    #      ("FONTSIZE", (0, 1), (-1, -1), 8),  # font size of other rows
    #      ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    #      ("ALIGN", (1, 0), (-1, -1), "CENTER"),  # all columns except name center align
    #      ]
    # )
    # element = Table(data=table_data,
    #                 colWidths=[width_10th, width_10th*1.5, width_10th/2, width_10th*3.5, width_10th*3.5],
    #                 rowHeights=None, style=table_style, hAlign=None, vAlign=None)
    # start = 1
    # internal_border_color = colors.grey
    # # adding horizontal lines as borders
    # for i in range(start, len(table_data)):  # 1 because don't want header row to have horizontal line
    #     table_style = TableStyle([("LINEABOVE", (0, i), (-1, i), 0.1, internal_border_color), ])
    #     element.setStyle(table_style)
    #
    # # adding vertical lines as borders
    # for i in range(start, len(table_data[0])):  # 1 because don't want header row to have vertial line
    #     table_style = TableStyle([("LINEBEFORE", (i, 1), (i, -1), 0.1,
    #                                internal_border_color), ])  # (i, 1) is neccesory to avoid header vert line
    #     element.setStyle(table_style)
    return elements
