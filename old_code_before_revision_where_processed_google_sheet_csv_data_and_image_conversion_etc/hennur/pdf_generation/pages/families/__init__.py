from pdf_generation.sub_elements.table import generate_family_table
from pdf_generation.sub_elements.family_generic_data import family_common_data
from database.get import basic_query
import os
from reportlab.platypus import PageBegin, FrameBreak, Spacer
from reportlab.lib import colors
from pdf_generation.page_settings import *


def generate():
    sql = basic_query(os.path.join("database", "sqlite.db")).sql_dataframe
    family_ids = sql('''select * from families;''').famid.unique()
    families = [PageBegin()]

    # ORDERING FAMILIES ACCORDING TO HEAD OF FAMILY ALPHABETICALLY
    order_of_families = sql('''select * from members where rltshp = "Self" order by member_name''').famid.to_dict().values()
    order_family_map = {idx: f_id for idx, f_id in enumerate(order_of_families, start=1)}

    for i in range(1, len(order_family_map)+1):
        famid = order_family_map[i]

        # for function
        common_data = family_common_data(famid)
        heading = f'''{i}. {common_data['head']}'''
        print(common_data['head'])
        from reportlab.platypus import Table as RLTable
        from reportlab.platypus import TableStyle
        head_box = RLTable([[heading]], colWidths=[PAGE_FRAME_WIDTH], rowHeights=[PAGE_FRAME_HEIGHT/25])
        head_box_style = TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.Color(0.5, 0.1, 0.6)),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),  # heading text color
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

            ]
        )
        head_box.setStyle(head_box_style)

        families.append(head_box)


        image_col_width = (320*0.35) * 1

        # common_data = family_common_data(famid)
        # from pdf_generation.sub_elements.box import generate_paragraph_flowable

        para_table = RLTable([
            [common_data['text']['current_address']],
             #[common_data['text']['email']],
             [common_data['text']['native_address']],
             [common_data['text']['native_parish']],
             [common_data['text']['diocese']],
              ])
        plain_box = RLTable([[common_data['family_photo'], para_table]],  # , common_data['text']['diocese']
                            colWidths=[image_col_width, PAGE_FRAME_WIDTH-image_col_width],  # [(PAGE_FRAME_WIDTH/2)-0.1, ]
                            rowHeights=[PAGE_FRAME_HEIGHT / 6])
        plain_box_style = TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.white),  # image and para col background
                # ("BACKGROUND", (0, 0), (0, -1), colors.antiquewhite),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.red),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("LEFTPADDING", (0, 0), (0, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (0, -1), "MIDDLE"),  # PHOTO CELL
                ("VALIGN", (1, 0), (1, -1), "TOP"),  # ADDRESS CELL
                ("VALIGN", (0, 1), (1, -1), "TOP"),  # ADDRESS CELL
                ("BACKGROUND", (1, 0), (1, -1), colors.white),  # LEFT PADDING TO ADDRESS CELL

            ]
        )
        plain_box.setStyle(plain_box_style)
        families.append(plain_box)
        families.append(Spacer(1, 6))

        members_table = generate_family_table(famid)
        families.append(members_table)
        families.append(FrameBreak())
    # removing the last element FrameBreak from the list to prevent an additional empty page creation
    families.pop()
    return families
