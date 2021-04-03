from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

from directory.settings import PAGE_FRAME_WIDTH, PAGE_FRAME_HEIGHT

title_background = colors.Color(0.1, 0.5, 0.6)
title_text_color = colors.white
TITLE_SECTION_ROW_HEIGHT = PAGE_FRAME_HEIGHT * 0.95

def title_section(title_text):
    text = f'''{title_text}'''
    heading_title_table = Table([[text.upper(),]], colWidths=[PAGE_FRAME_WIDTH], rowHeights=[TITLE_SECTION_ROW_HEIGHT])
    heading_title_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), title_background),
            ("TEXTCOLOR", (0, 0), (-1, -1), title_text_color),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ])
    )
    return heading_title_table