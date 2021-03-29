
from reportlab.lib import colors
from directory.settings import *

color_yellow = colors.Color(0.9, 0.9, 0.5)
color_light = colors.Color(0.7, 0.8, 0.9)
color_general = colors.Color(0.2, 0.3, 0.4)
# color_dark = 
color_deep_dark = colors.Color(0.2, 0.2, 0.3)
color_extra_light = colors.Color(0.9, 0.94, 0.98)
# color_extra_light = colors.Color(1, 1, 1)
color_white = colors.Color(1, 1, 1)


from reportlab.platypus import Table as RLTable
from reportlab.platypus import Spacer
from reportlab.platypus import TableStyle

def produce_heading(text):
    heading_title_table = RLTable([[text.upper(),]], colWidths=[PAGE_FRAME_WIDTH])
    heading_title_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), color_general),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.whitesmoke),
        ])
    )
    return [Spacer(width=PAGE_FRAME_WIDTH, height=4, isGlue=True), heading_title_table, Spacer(width=PAGE_FRAME_WIDTH, height=2, isGlue=True)]

def horizontal_row(height=3, width=PAGE_FRAME_WIDTH, color=colors.Color(0.2, 0.3, 0.4)):
    row_table = RLTable([["",]], colWidths=[width], rowHeights=[height])
    row_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), color),
        ])
    )
    return [Spacer(width=PAGE_FRAME_WIDTH, height=4, isGlue=True), row_table, Spacer(width=PAGE_FRAME_WIDTH, height=2, isGlue=True)]

def ribbon(height=10, width=PAGE_FRAME_WIDTH, color=color_light, space_before=0):
    row_table = RLTable([["",]], colWidths=[width], rowHeights=[height])
    row_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), color),
        ])
    )
    return [row_table]

family_title_background = colors.Color(0.5, 0.1, 0.6)
family_title_text_color = colors.white # colors.whitesmoke

FAMILY_TITLE_SECTION_ROW_HEIGHT = PAGE_FRAME_HEIGHT/25

def family_title_section(fam_id, family_head):
    text = f'''{fam_id}. {family_head}'''
    heading_title_table = RLTable([[text.upper(),]], colWidths=[PAGE_FRAME_WIDTH], rowHeights=[FAMILY_TITLE_SECTION_ROW_HEIGHT])
    heading_title_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), family_title_background),
            ("TEXTCOLOR", (0, 0), (-1, -1), family_title_text_color),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ])
    )
    return heading_title_table # Spacer(width=PAGE_FRAME_WIDTH, height=4, isGlue=True), 

pct = 0.35
image_width = 320 * pct
image_height = 249 * pct
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()
styleN = styles['Normal']
# styleN.wordWrap = 'CJK'
styleN.fontName = 'oswald_light'
styleN.fontSize = 8

def address_section():
    address_current = "#29, HSR, Hennur, Bangalore"
    address_native = "kalayil house, chennenkalthadom p o, mannarakulanji"
    parish_native = "St. John Chrysostom Malankara Catholic Church, Mannaralkunlanji"
    diocese_native = "Pathanamthitta"
    new_line = "<br/>"

    address_paragraph = Paragraph(
        f"""Current Address: {address_current}"""+new_line+
        f"""Native Address: {address_native}"""+new_line+
        f"""Native Parish:{parish_native}"""+new_line+
        f"""Native Diocese: {diocese_native}""", 
        styleN
        )
    para_table = RLTable(
        [
            [address_paragraph]
        ],
        colWidths=[PAGE_FRAME_WIDTH-image_width], rowHeights=[image_height]
        )
    para_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.bisque),
            # ("TEXTCOLOR", (0, 0), (-1, -1), family_title_text_color),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0,0), (-1, -1), "oswald_light"), # header font
            ("FONTSIZE", (0,0), (-1, -1), 8),
        ])
    )
    return para_table

import os
from reportlab.platypus import Image
# find image width just above address section function
def photo_section():
    url = os.path.join('photos', '1.jpg')
    img = Image(filename=url, width=image_width, height=image_height, )
    img.hAlign = 'CENTER'
    return img

from reportlab.platypus import Table
def photo_and_address_section():
    section = Table(
        [
            [photo_section(), address_section()]
        ],
        colWidths=[image_width, PAGE_FRAME_WIDTH-image_width],
        # rowHeights=[(PAGE_FRAME_HEIGHT/2) - FAMILY_TITLE_SECTION_ROW_HEIGHT]
    )
    section.setStyle(
        [
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ('BACKGROUND', (0, 0), (0, -1), family_title_background),
        ]
    )
    return section



def members_table_section():
    return Paragraph('Hi')
# box_elements = [

# ]
